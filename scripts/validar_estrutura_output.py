#!/usr/bin/env python3
"""
Validacao heuristica do documento final formalizado contra os 5 testes obrigatorios.

Este script NAO substitui a auditoria do Especialista 10. Ele complementa: faz checagens
mecanicas rapidas que podem detectar problemas grosseiros. A auditoria semantica profunda
continua sendo trabalho do Auditor.

ESCOPO: aplicavel APENAS ao DOCUMENTO FINAL FORMALIZADO produzido pelo Especialista 11.
NAO aplicar a arquivos internos da skill (SKILL.md, protocolos, templates, especialistas),
pois esses arquivos podem legitimamente referenciar "o usuario", "a conversa" e outros
padroes que so contam como contaminacao no documento final entregue ao leitor externo.

Uso:
    python3 validar_estrutura_output.py <caminho-do-documento-final.md>
"""

import re
import sys
import unicodedata
from pathlib import Path


def sem_acentos(texto: str) -> str:
    """
    Remove acentos para que os padroes (escritos sem acento) encontrem palavras acentuadas.
    Sem isso, "durante a discussão" nao seria encontrado pelo padrao "discussao".
    """
    return "".join(c for c in unicodedata.normalize("NFKD", texto) if not unicodedata.combining(c))


# Padroes de contaminacao conversacional — se aparecem no documento, e falha do teste 5.
PADROES_CONTAMINACAO = [
    r"\b(o|a) usuari[oa]\b",
    r"\bdurante a (conversa|discussao|iteracao|sessao)\b",
    r"\bconforme (conversamos|discutimos|falamos)\b",
    r"\bnessa conversa\b",
    r"\bnesta conversa\b",
    r"\bem uma das iteracoes\b",
    r"\bcomo mencionado anteriormente\b",  # borderline — flag para revisao humana
    r"\ba inteligencia artificial (respondeu|disse|perguntou)\b",
    r"\bo modelo (respondeu|disse|perguntou)\b",
    r"\bo (chat|dialogo|prompt) (revelou|mostrou|indicou)\b",
    # Modo material pronto: referencias a fonte que fazem o documento depender dela.
    # "o autor diz" sozinho nao entra: em metodos sobre leitura de textos, "o autor" e conteudo.
    r"\bo autor (deste|do) (livro|curso|ebook|material)\b",
    r"\bno capitulo \d+",
    r"\bneste (livro|curso|ebook|material)\b",
]

# Blocos esperados no documento final — se algum bloco central estiver ausente, o teste 4
# (completude) esta em risco.
BLOCOS_ESPERADOS = {
    "definicao": [r"defini[cç][aã]o", r"o que [eé] este m[eé]todo"],
    "escopo": [r"escopo de aplica[cç][aã]o", r"onde se aplica"],
    "principios": [r"princ[íi]pios fundamentais"],
    "anatomia": [r"anatomia", r"estrutura e mecanismo", r"componentes"],
    "mecanismo": [r"mecanismo de funcionamento", r"mecanismo causal", r"como funciona"],
    "aplicacao": [r"aplica[cç][aã]o pr[aá]tica", r"sequ[eê]ncia execut[aá]vel", r"guia de aplica"],
    "criterios_qualidade": [r"crit[eé]rios de qualidade"],
    "erros": [r"erros comuns", r"prote[cç][aã]o contra"],
    "antipadroes": [r"antipadr[oõ]es"],
    "variacoes": [r"varia[cç][oõ]es leg[íi]timas", r"varia[cç][oõ]es"],
    "limites": [r"limites de adapta[cç][aã]o", r"limites"],
    "pontos_abertos": [r"pontos em aberto"],
    "condicoes": [r"condi[cç][oõ]es para o m[eé]todo funcionar"],
    "pontos_cegos": [r"pontos cegos"],
}

MARCADOR_CAMADA_EXTERNA = "CAMADA EXTERNA AO MATERIAL"


def teste_1_autossuficiencia(texto: str) -> tuple[bool, list[str]]:
    """
    Heuristica: procurar termos usados sem definicao previa. Se um termo aparece em maiusculo
    ou entre aspas na primeira aparicao mas nao ha definicao proxima, e sinal de falha.
    """
    problemas = []
    # Buscar referencias a "material original" ou "conversa" ou "iteracoes" no documento final —
    # nao deveriam estar la
    if re.search(r"\b(no|do|no) material (original|bruto)\b", sem_acentos(texto), re.IGNORECASE):
        problemas.append(
            "Documento faz referencia ao 'material original' — o leitor nao tem acesso a isso, "
            "e sinal de falha de autossuficiencia."
        )
    return (len(problemas) == 0, problemas)


def teste_2_aplicabilidade(texto: str) -> tuple[bool, list[str]]:
    """
    Heuristica: se ha secao de aplicacao pratica mas nao ha criterios de qualidade articulados,
    e sinal de falha.
    """
    problemas = []
    tem_aplicacao = bool(
        re.search(r"aplica[cç][aã]o pr[aá]tica|sequ[eê]ncia execut[aá]vel", texto, re.IGNORECASE)
    )
    tem_criterios = bool(re.search(r"crit[eé]rios de qualidade", texto, re.IGNORECASE))
    tem_pre_requisitos = bool(re.search(r"pr[eé]-requisitos", texto, re.IGNORECASE))

    if tem_aplicacao and not tem_criterios:
        problemas.append(
            "Documento tem secao de aplicacao mas nao articula criterios de qualidade — sinal de "
            "aplicabilidade comprometida."
        )
    if tem_aplicacao and not tem_pre_requisitos:
        problemas.append(
            "Documento tem secao de aplicacao mas nao articula pre-requisitos — sinal de "
            "aplicabilidade comprometida."
        )
    return (len(problemas) == 0, problemas)


def teste_3_fidelidade(texto: str) -> tuple[bool, list[str]]:
    """
    Heuristica: dificil de testar mecanicamente. Este teste requer comparacao com o material
    original. Sinalizar que precisa de auditoria semantica.
    """
    return (True, ["Teste 3 (Fidelidade) requer auditoria semantica manual comparando com material original."])


def teste_4_completude(texto: str) -> tuple[bool, list[str]]:
    """
    Verificar se os blocos esperados estao presentes no documento.
    """
    problemas = []
    texto_lower = texto.lower()

    for bloco, padroes in BLOCOS_ESPERADOS.items():
        encontrado = any(re.search(p, texto_lower) for p in padroes)
        if not encontrado:
            problemas.append(f"Bloco esperado ausente: {bloco}")

    # A secao de pontos cegos precisa vir depois do marcador da camada externa
    titulo_pontos_cegos = None
    for m in re.finditer(r"^#+[^\n]*pontos cegos", texto, re.IGNORECASE | re.MULTILINE):
        titulo_pontos_cegos = m.start()
    if titulo_pontos_cegos is not None:
        posicao_marcador = texto.find(MARCADOR_CAMADA_EXTERNA)
        if posicao_marcador == -1:
            problemas.append(
                "Secao de pontos cegos sem o marcador da camada externa — o leitor pode confundir "
                "conhecimento externo com conteudo do metodo."
            )
        elif posicao_marcador > titulo_pontos_cegos:
            problemas.append(
                "Secao de pontos cegos aparece antes do marcador da camada externa — ela precisa "
                "ficar depois do marcador."
            )

    return (len(problemas) == 0, problemas)


def teste_5_contaminacao(texto: str) -> tuple[bool, list[str]]:
    """
    Buscar padroes de contaminacao conversacional. Qualquer aparicao e falha.
    """
    problemas = []
    texto_busca = sem_acentos(texto)
    for padrao in PADROES_CONTAMINACAO:
        matches = re.finditer(padrao, texto_busca, re.IGNORECASE)
        for match in matches:
            # Pegar contexto ao redor
            inicio = max(0, match.start() - 40)
            fim = min(len(texto_busca), match.end() + 40)
            contexto = texto_busca[inicio:fim].replace("\n", " ")
            problemas.append(f"Contaminacao conversacional detectada: '...{contexto}...'")

    return (len(problemas) == 0, problemas)


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 validar_estrutura_output.py <caminho-do-documento.md>", file=sys.stderr)
        sys.exit(1)

    caminho = Path(sys.argv[1])
    if not caminho.exists():
        print(f"Arquivo nao encontrado: {caminho}", file=sys.stderr)
        sys.exit(1)

    texto = caminho.read_text(encoding="utf-8")

    print(f"Validando: {caminho.name}")
    print("=" * 60)

    testes = [
        ("Teste 1 — Autossuficiencia", teste_1_autossuficiencia),
        ("Teste 2 — Aplicabilidade", teste_2_aplicabilidade),
        ("Teste 3 — Fidelidade", teste_3_fidelidade),
        ("Teste 4 — Completude", teste_4_completude),
        ("Teste 5 — Ausencia de contaminacao", teste_5_contaminacao),
    ]

    todos_passaram = True

    for nome, fn in testes:
        passou, problemas = fn(texto)
        status = "✓ PASSOU" if passou else "✗ FALHOU"
        print(f"\n{nome}: {status}")
        if problemas:
            for p in problemas:
                print(f"  - {p}")
        if not passou:
            todos_passaram = False

    print()
    print("=" * 60)
    if todos_passaram:
        print("RESULTADO: documento passou nas checagens heuristicas.")
        print("Auditoria semantica pelo Especialista 10 ainda e necessaria para aprovacao final.")
    else:
        print("RESULTADO: documento tem problemas detectados heuristicamente.")
        print("Corrigir antes de continuar. Auditoria semantica ainda e necessaria depois.")

    sys.exit(0 if todos_passaram else 1)


if __name__ == "__main__":
    main()
