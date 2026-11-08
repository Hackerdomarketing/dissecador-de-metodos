# PROTOCOLO DE FLUXO DE ORQUESTRAÇÃO DOS 11 PASSOS

Este documento define a sequência exata, as validações entre passos, e as regras de acionamento
dos especialistas. É o coração operacional da skill dissecador-de-metodos.

## Sequência obrigatória

A ordem dos 11 passos é inviolável. Pular passos destrói o sistema porque cada especialista
depende de inputs específicos produzidos pelos anteriores. A tabela abaixo mostra as dependências.

| Passo | Especialista | Recebe input de | Produz output para |
|-------|--------------|-----------------|--------------------|
| 1 | Leitor Imersivo | Material bruto do usuário | 2, 3, 4, 5 |
| 2 | Identificador do Objeto Central | 1 + material bruto | Todos os posteriores |
| 3 | Cartógrafo de Evolução | 2 + material bruto | 4, 6 a 11 |
| 4 | Caçador de Pontos de Virada | 3 + material bruto | 6, 7, 11 |
| 5 | Lexicógrafo Técnico | 3, 4 + material bruto | 6, 7, 8, 9, 11 |
| 6 | Arquiteto de Definição e Princípios | 2, 3, 4, 5 | 7, 8, 9, 10, 11 |
| 7 | Anatomista de Estrutura e Mecanismo | 2, 3, 4, 5, 6 | 8, 9, 10, 11 |
| 8 | Engenheiro de Aplicação | 3, 4, 5, 6, 7 | 9, 10, 11 |
| 9 | Catalogador de Erros e Variações | 3, 5, 6, 7, 8 | 10, 11 |
| 10 | Auditor de Integridade | 1 a 9 + material bruto | Loop de correção se necessário, varredura de pontos cegos → 11 |
| 11 | Redator-Chefe Final | 1 a 10 (corrigidos) | Documento final ao usuário |

## Modos de material

O modo é escolhido na ativação e informado a cada especialista junto com seus inputs.

- **Modo conversa**: os 11 especialistas operam como descrito em seus arquivos, incluindo a
  reconstrução da evolução (Especialista 3) e dos pontos de virada (Especialista 4). As correções e
  rejeições presentes no material são tratadas como pistas de critérios de qualidade
  (Especialistas 1 e 2), e o motivo de cada versão abandonada segue do Especialista 3 para os
  Especialistas 6 e 9.
- **Modo material pronto**: os Especialistas 1 a 4 seguem as seções "Modo material pronto" de seus
  arquivos. O Especialista 3 entrega um mapa de dependências em vez de um mapa de evolução, e o
  Especialista 4 entrega ideias-chave em vez de pontos de virada. Os Especialistas 5 a 11 operam
  igual. A tabela de dependências acima continua valendo: muda o conteúdo entregue, não quem
  entrega para quem.

## Validações internas entre cada passo

Antes de prosseguir do passo N para o passo N+1, o orquestrador valida internamente:

1. O output do passo N tem profundidade real ou está superficial?
2. O output do passo N respeita o foco em conteúdo conceitual, sem descrever dinâmica conversacional?
3. O output do passo N é fiel ao material original, sem invenções?
4. O output do passo N é autossuficiente — não exige ler a conversa para entender?
5. O próximo especialista terá todos os inputs que precisa?

Se qualquer verificação falhar, reaciona o especialista com instrução específica de correção
antes de prosseguir.

## Checkpoint obrigatório após passo 2

Após o Especialista 2 (Identificador do Objeto Central) concluir sua entrega, o orquestrador
deve interromper o fluxo e pedir confirmação explícita do usuário. Ver `protocolo-checkpoint-passo-2.md`
para o protocolo detalhado. Este checkpoint é inviolável. Erro na identificação do objeto
central propaga para todos os passos posteriores e arruína o documento final.

## Loop de correção após passo 10

Se o Auditor (Especialista 10) identificar lacunas, contaminações ou problemas de integridade,
o orquestrador retorna ao especialista correspondente com instrução específica de correção
antes de acionar o Especialista 11. O ciclo é:

Auditor identifica problema → orquestrador reaciona especialista N → especialista N produz
correção → auditor valida → se aprovado, prossegue para 11; se ainda tem problema, repete.

Antes de reacionar um especialista, aplicar a regra dos três destinos: só volta para correção o
que pode ser corrigido com base no material. Se a correção exigiria informação ausente do material,
ela não volta: vira ponto em aberto (se o material tocou no assunto) ou ponto cego (se nunca
tocou). Pedir a um especialista para "desenvolver mais" sem base no material é pedir invenção.

Máximo de 3 iterações por especialista. Após isso, o problema recebe o destino correspondente
(ponto em aberto ou ponto cego) e é declarado honestamente no documento final.

## Comportamento em Modo A (Claude Code com Task tool)

Em cada passo, o orquestrador dispara um subagent via Task tool com:
- Instrução clara de identidade (referência ao arquivo `agents/especialista-NN-slug.md`)
- Inputs necessários (outputs dos especialistas anteriores)
- Material bruto original (referência ou conteúdo dependendo do tamanho)
- Solicitação explícita do output no formato exato do especialista

O subagent opera em contexto isolado. Retorna output estruturado. Orquestrador coleta e
prossegue.

## Comportamento em Modo B (Claude.ai sem Task tool)

Em cada passo, o orquestrador:
1. Declara explicitamente ao usuário qual passo está iniciando
2. Carrega mentalmente o arquivo `references/especialista-NN-slug.md`
3. Assume a identidade do especialista
4. Produz o output no formato exato do especialista, integralmente
5. Encerra explicitamente o papel do especialista antes de prosseguir
6. Aguarda "ok" ou "continuar" do usuário (opcional em passos regulares, obrigatório no
   checkpoint do passo 2)

Preserva os outputs anteriores no histórico da conversa, referenciando-os pelo nome do
especialista quando o próximo precisar consultar.

## Comportamento em materiais grandes no Modo B

Se o material bruto for maior que 60 mil tokens estimados, o orquestrador deve avisar o
usuário antes do passo 1:

"O material que você forneceu tem aproximadamente [X] mil tokens. No ambiente atual (Claude.ai
sem subagents), materiais deste tamanho têm risco alto de estourar o contexto antes de completar
os 11 passos. Recomendações:

Opção 1: continuar sequencialmente ciente de que talvez precise dividir a execução em várias
conversas. Cada passo entrega output que pode ser colado em nova conversa para retomar.

Opção 2: se você tem acesso ao Claude Code, migrar para lá — a skill roda cada especialista
em subagent com contexto próprio e materiais até 200 mil tokens são processados sem problema.

Opção 3: dividir o material em blocos menores e processar cada bloco separadamente, integrando
os documentos finais depois.

Qual você prefere?"

## Regras absolutas do orquestrador
(Herdadas do system prompt original do coordenador)

1. Nunca executar o trabalho de um especialista diretamente. Sempre acionar o arquivo.
2. Nunca pular passos.
3. Sempre exigir confirmação do usuário no checkpoint do passo 2.
4. Sempre validar output de cada especialista antes de prosseguir.
5. Nunca permitir contaminação conversacional no documento final.
6. Sempre preservar profundidade. Resumir é perder.
7. Nunca inventar para preencher lacunas. Aplicar os três destinos: completar com base no
   material, marcar como ponto em aberto ou registrar como ponto cego. Toda dedução recebe a
   marca [INFERIDO].
8. Sempre formalizar apenas a versão mais madura do conhecimento.
9. Sempre operar com explicitude total — sem abreviações não explicadas.
10. A conversa (material bruto) é veículo, não objeto. Extrair o conhecimento, nunca descrever
    como a conversa fluiu.
