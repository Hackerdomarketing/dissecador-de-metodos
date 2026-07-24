# PROTOCOLO DOS CINCO TESTES OBRIGATÓRIOS DE INTEGRIDADE

Este documento consolida os cinco testes que o Especialista 10 (Auditor) aplica ao conjunto
integrado de outputs dos especialistas 1 a 9 antes de liberar para o Redator-Chefe Final. Também
é o critério final de qualidade do documento entregue ao usuário. Se o documento final não
passar nos 5 testes, o sistema falhou.

## Teste 1 — Autossuficiência

Pergunta central: alguém que nunca viu o material original consegue entender completamente
o método a partir do documento?

Sinais de falha:
- Referências a contextos que existiam no material bruto mas não no documento
- Pressuposição de conhecimento que não foi articulado no documento
- Frases que fariam sentido a quem leu o material bruto mas não a quem só lê o documento
- Termos usados sem definição prévia
- Menções vagas do tipo "como foi discutido anteriormente" sem que o documento traga a
  discussão

Procedimento de aplicação: simular mentalmente um leitor totalmente virgem do material bruto
e ler o documento do início ao fim. Marcar cada ponto onde esse leitor imaginário sentiria
falta de contexto ou entenderia mal por falta de definição.

## Teste 2 — Aplicabilidade

Pergunta central: alguém com os pré-requisitos articulados no documento consegue aplicar o
método com base apenas no documento?

Sinais de falha:
- Passos que assumem conhecimento procedimental não explicitado
- Critérios de qualidade ausentes onde decisões de qualidade são necessárias
- Indicadores de progresso que faltam
- Decisões implícitas no método que não foram articuladas como decisões
- Guia de aplicação que é lista de passos, não guia executável (falta articulação sobre como
  executar bem cada passo)

Procedimento de aplicação: simular mentalmente a aplicação do método por alguém qualificado
pelos pré-requisitos. Identificar cada ponto onde o aplicador precisaria "adivinhar" o que
fazer porque o documento não articulou.

## Teste 3 — Fidelidade

Pergunta central: o documento corresponde ao que foi efetivamente desenvolvido no material
original, sem invenção, distorção ou inferência sem base?

Sinais de falha:
- Afirmações que não têm sustentação no material bruto
- Princípios "acrescentados" pela lógica interna do formalizador em vez de extraídos do material
- Estruturas mais organizadas do que o material original produziu (invenção de ordem que não
  havia)
- Componentes ou mecanismos inventados para completar uma anatomia esteticamente coerente
- Erros e antipadrões inventados por analogia sem base no método específico

Procedimento de aplicação: para cada afirmação central do documento, buscar no material bruto
a passagem que a sustenta. Se não encontrar, a afirmação é candidata a violação de fidelidade.
Duas ressalvas: (1) formulação nova de conteúdo real do material NÃO é violação, é integração
editorial legítima; (2) explicitação de implícito claramente presente no material NÃO é violação,
é formalização legítima.

## Teste 4 — Completude

Pergunta central: o documento cobre tudo que precisa cobrir para que o método seja compreendido
e aplicável?

Sinais de falha:
- Definição do método sem escopo articulado
- Princípios sem análise consequencial
- Anatomia sem mecanismo causal
- Aplicação sem critérios de qualidade
- Ausência de proteção contra erros comuns onde erros são previsíveis
- Ausência de tratamento de variações onde adaptação a contextos diferentes é esperada
- Aspectos em aberto do material que foram simplesmente omitidos em vez de sinalizados
  honestamente

Procedimento de aplicação: verificar se cada bloco esperado do documento final está presente
com profundidade adequada. Fundamentos (definição + escopo + princípios), Estrutura (anatomia
+ mecanismo), Aplicação (pré-requisitos + passos + critérios + checkpoints), Proteção (erros
+ antipadrões + confusões), Adaptação (variações + limites), Encerramento (pontos em aberto).

## Teste 5 — Ausência de contaminação conversacional

Pergunta central: o documento existe como se tivesse sido escrito por um especialista que
domina o método, ou trai que foi extraído de uma conversa?

Sinais de falha:
- Frases como "durante a discussão", "conforme conversamos", "o usuário perguntou"
- Descrição de dinâmica conversacional em vez de conhecimento
- Meta-comentários sobre como o método foi desenvolvido em vez do método em si
- Estrutura do documento espelhando a estrutura cronológica da conversa em vez da hierarquia
  conceitual do conteúdo
- Referência a "iterações" ou "refinamentos sucessivos" quando o que importa é o estado final
  maduro

Procedimento de aplicação: leitura sistemática buscando qualquer traço da origem conversacional
do material. Zero tolerância. Uma única frase contaminada é suficiente para reprovar o teste.

## Aplicação combinada dos 5 testes

Um documento só é aprovado quando passa em todos os 5 testes simultaneamente. Falhar em qualquer
um exige retorno ao especialista responsável para correção antes de prosseguir.

## Tratamento de "pontos em aberto"

Pontos em aberto identificados durante a auditoria não são falhas nos testes se forem preservados
honestamente no documento final na seção específica. Falha ocorre quando um ponto em aberto
foi disfarçado como conclusão ou preenchido com invenção. Ver `protocolo-tratamento-pontos-abertos.md`.

## Nota sobre severidade dos testes

Os 5 testes têm severidade equivalente. Não há hierarquia. Um documento que passa em 4 e
falha em 1 é reprovado com a mesma severidade que um que falha em 3. Autossuficiência é tão
importante quanto ausência de contaminação. Aplicabilidade é tão importante quanto fidelidade.
