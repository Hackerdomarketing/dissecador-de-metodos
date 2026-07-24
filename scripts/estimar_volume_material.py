#!/usr/bin/env python3
"""
Estima o volume aproximado em tokens de um material bruto para a skill dissecador-de-metodos.
Ajuda o orquestrador a decidir se precisa avisar o usuário sobre risco de estouro de contexto
no Modo B (Claude.ai sequencial).

Uso:
    python3 estimar_volume_material.py <caminho-do-arquivo>
    ou
    echo "conteudo" | python3 estimar_volume_material.py -

Classificação por volume:
    - Pequeno: até 20.000 tokens (roda em qualquer ambiente)
    - Medio: 20.000 a 60.000 tokens (roda em qualquer ambiente com folga)
    - Medio-alto: 60.000 a 100.000 tokens (avisar usuario em Modo B)
    - Grande: 100.000 a 200.000 tokens (recomendar Modo A / Claude Code)
    - Muito grande: acima de 200.000 tokens (dividir material)
"""

import sys


def estimar_tokens(texto: str) -> int:
    """
    Estimativa conservadora baseada em observação: portugues costuma ficar em torno
    de 3.5 caracteres por token para texto denso. Para materiais com muito codigo,
    tabelas ou terminologia tecnica, pode subir para 4-4.5 caracteres por token.
    Uso 3.5 como estimativa conservadora (chega mais alto que a realidade, evita
    subestimar o volume).
    """
    return len(texto) // 3


def classificar_volume(tokens: int) -> tuple[str, str]:
    """
    Retorna tupla (categoria, recomendacao_para_usuario).
    """
    if tokens < 20_000:
        return (
            "pequeno",
            "Roda confortavelmente em qualquer ambiente. Prosseguir normalmente.",
        )
    if tokens < 60_000:
        return (
            "medio",
            "Roda em qualquer ambiente com folga. Prosseguir normalmente.",
        )
    if tokens < 100_000:
        return (
            "medio-alto",
            "No Modo B (Claude.ai sem subagents), ha risco moderado de estourar "
            "contexto perto do final. No Modo A (Claude Code com Task tool), roda "
            "confortavelmente. Avisar o usuario se estiver em Modo B.",
        )
    if tokens < 200_000:
        return (
            "grande",
            "No Modo B, alto risco de estourar contexto antes do passo 11. Recomendar "
            "migrar para Modo A (Claude Code) OU dividir material em blocos menores. "
            "Prosseguir no Modo B apenas com aviso claro e plano de retomada.",
        )
    return (
        "muito-grande",
        "Volume excede o limite de contexto de 200 mil tokens da maior parte dos "
        "planos. Dividir material em blocos menores e processar cada bloco separadamente, "
        "integrando os documentos finais depois.",
    )


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 estimar_volume_material.py <caminho-do-arquivo | ->", file=sys.stderr)
        sys.exit(1)

    caminho = sys.argv[1]

    if caminho == "-":
        texto = sys.stdin.read()
    else:
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                texto = f.read()
        except FileNotFoundError:
            print(f"Arquivo nao encontrado: {caminho}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}", file=sys.stderr)
            sys.exit(1)

    tokens = estimar_tokens(texto)
    categoria, recomendacao = classificar_volume(tokens)

    print(f"Volume estimado: {tokens:,} tokens")
    print(f"Categoria: {categoria}")
    print(f"Recomendacao: {recomendacao}")


if __name__ == "__main__":
    main()
