# PROTOCOLO DE TRATAMENTO DE PONTOS EM ABERTO

## O que é um ponto em aberto neste sistema

Um ponto em aberto é um aspecto do método que o material original não resolveu completamente,
mas cuja ausência de resolução não impede o uso prático do método no seu escopo consolidado.

Exemplos concretos:
- O material desenvolveu o método para contexto A e explorou extensão para contexto B sem
  consolidar a extensão. O ponto em aberto: extensão para B não está resolvida.
- O material articulou um princípio mas não definiu operacionalmente onde ele começa a se
  aplicar e onde deixa de se aplicar. O ponto em aberto: limites operacionais do princípio.
- O material identificou uma tensão entre dois componentes do método sem definir como resolver
  a tensão em casos de conflito. O ponto em aberto: heurística de resolução da tensão.

## O que NÃO é ponto em aberto

- Erro do formalizador (pular etapa, resumir, deixar de articular) — isso é falha, não ponto
  em aberto
- Ausência de completude por escolha do formalizador — se o material tem informação e o
  formalizador não incluiu, é omissão, não ponto em aberto
- Coisas que o material nunca abordou — não são pontos em aberto. Se a ausência afeta a
  aplicação do método, é ponto cego e segue `protocolo-pontos-cegos.md`. Se não afeta, é
  simplesmente fora de escopo e não entra no documento

O critério de distinção: ponto em aberto é sempre algo que o material abordou, mas que não chegou
à consolidação final. O que o material nunca abordou não é ponto em aberto: ou é ponto cego (se
faz falta na aplicação) ou é fora de escopo (se não faz falta).

## Regra absoluta: NUNCA inventar para preencher

O sistema não fecha pontos em aberto com invenção. Se o material não resolveu, o documento
final declara que não está resolvido. Isso preserva a honestidade epistêmica e a confiabilidade
do documento.

Preencher com invenção é o pior antipadrão possível porque:
1. Contamina o método com conteúdo que não veio do desenvolvimento real
2. Passa por informação verdadeira quando é hipótese do formalizador
3. Corrói a confiança de quem sabia que aquilo não estava resolvido no material
4. Pode induzir aplicação errada em quem tomar a invenção como recomendação validada

## Onde os pontos em aberto aparecem no documento final

Os pontos em aberto identificados devem aparecer em três lugares no documento final:

**Lugar 1 — Dentro das seções onde se manifestam.**
Se o ponto em aberto é sobre extensão para contexto B, ele aparece na seção de Escopo:
"O método como articulado aqui cobre o contexto A. Extensão para contexto B foi explorada
mas não consolidada. Ver seção 'Pontos em Aberto' para detalhes."

**Lugar 2 — Na seção final "Pontos em Aberto".**
Seção específica ao final do documento com lista de todos os pontos em aberto identificados,
cada um descrito com:
- Qual é o aspecto não resolvido
- O que o material chegou a explorar sobre ele (se algo)
- Por que a resolução completa não foi atingida
- Sugestão de como o ponto poderia ser resolvido em desenvolvimento futuro (opcional e sinalizado
  como sugestão, não como resolução)

**Lugar 3 — Nas notas finais sobre evolução futura.**
Aspectos em aberto podem indicar direções naturais de evolução do método. Se apropriado,
mencionar na seção de Notas Finais que a resolução de determinados pontos em aberto seria
o próximo passo natural de desenvolvimento.

## Fórmulas linguísticas honestas para pontos em aberto

Estas fórmulas foram testadas para preservar honestidade sem corroer confiabilidade:

Fórmula 1 — Extensão não consolidada:
"O método na sua forma madura cobre [escopo consolidado]. Extensões para [escopo adicional]
foram exploradas durante o desenvolvimento mas não consolidadas. Aplicadores que precisam
operar em [escopo adicional] devem tratar isso como área de adaptação cuidadosa, aplicando
os princípios articulados e validando resultados empiricamente."

Fórmula 2 — Tensão sem heurística de resolução:
"A tensão entre [componente A] e [componente B] pode aparecer em [contexto específico]. O
método não estabeleceu uma heurística formal de resolução. Observações do desenvolvimento
sugerem que [orientação parcial], mas a resolução completa permanece em aberto."

Fórmula 3 — Princípio sem limites operacionais definidos:
"O princípio [nome do princípio] governa [aspecto]. Onde exatamente começa e onde deixa de
se aplicar não foi definido operacionalmente. Aplicadores devem exercer julgamento em situações
de fronteira, orientados pela função consequencial do princípio."

Fórmula 4 — Pergunta que permanece em aberto:
"A pergunta '[pergunta específica]' permanece em aberto. O método como articulado aqui funciona
sem resolver esta pergunta, mas aplicações em [contexto específico] podem demandar resolução
adicional."

## Diferença entre ponto em aberto legítimo e limitação do formalizador

Se o formalizador não conseguiu extrair algo que estava no material, isso é limitação do
formalizador, não ponto em aberto do método. Fazer essa distinção honestamente é parte da
integridade do processo.

Uma forma de testar: se um formalizador diferente olhasse o mesmo material, ele também encontraria
o mesmo ponto em aberto? Se sim, é ponto em aberto real do método. Se não, é limitação do
formalizador atual e precisa de revisão.

## Nota sobre aspectos em aberto que tornariam o método inaplicável

Se um aspecto em aberto for tão fundamental que sua ausência de resolução tornaria o método
inaplicável no seu próprio escopo consolidado, isso não é ponto em aberto — é indicador de
que o método ainda não maturou o suficiente para formalização. Nesse caso o formalizador deve
declarar honestamente que o método não atingiu maturação suficiente para formalização, ainda
que muitos aspectos tenham sido desenvolvidos.

## Pontos em aberto no modo material pronto

No modo material pronto, ponto em aberto é o que o autor abordou sem concluir: uma etapa anunciada
e não explicada, um critério mencionado sem definição, uma exceção reconhecida sem orientação de
como tratá-la. A regra é a mesma do modo conversa: declarar, nunca completar.
