# PROTOCOLO DE PONTOS CEGOS

## O que é um ponto cego neste sistema

Um ponto cego é uma ausência que o material nunca abordou, mas que afeta a aplicação do método. Ninguém falou daquilo, e justamente por isso quem aplicar o método vai tropeçar ali.

Exemplo: uma receita que nunca menciona a temperatura do forno. O material está completo em tudo o que discutiu, mas quem seguir a receita vai precisar de uma informação que nunca apareceu.

## O que diferencia ponto cego dos outros três casos

| Caso | O que é | Onde vai |
|---|---|---|
| Ponto em aberto | Algo que o material abordou, mas não concluiu | Seção de pontos em aberto (`protocolo-tratamento-pontos-abertos.md`) |
| Condição de funcionamento | Algo presente, mas oculto: o método depende dele sem mencioná-lo | Seção de condições para o método funcionar (Especialistas 6, 7 e 8) |
| Ponto cego | Algo ausente: o material nunca abordou, e a ausência afeta a aplicação | Camada externa, no final do documento (este protocolo) |
| Fora de escopo | Algo ausente que não afeta a aplicação | Não entra no documento |

Teste rápido: se o material tocou no assunto, não é ponto cego. Se o método depende daquilo e o material só não disse, é condição de funcionamento. Se nunca apareceu e vai fazer falta, é ponto cego.

## Por que esta seção existe e por que fica separada

O documento final é autossuficiente: vai ser aplicado longe do material que o originou. As ausências que nunca foram discutidas viajam junto, invisíveis, e aparecem como erro na hora da aplicação.

Uma ausência só fica visível por comparação: para dizer que falta a temperatura do forno, é preciso saber que receitas de bolo precisam dela. Esse conhecimento vem de fora do material. Por isso esta é a **única parte do sistema em que conhecimento externo ao material é permitido**, e apenas para apontar ausências, nunca para preenchê-las. A separação por um marcador visível garante que o leitor nunca confunda o que veio do material com o que veio de fora.

## Quem faz e quando

- **Especialistas 6, 8 e 9** registram candidatas a ponto cego durante o próprio trabalho: o Especialista 6, quando o material não discute onde o método deixa de valer; o Especialista 8, quando a verificação de executabilidade encontra uma lacuna que o material nunca tocou; o Especialista 9, quando conhece um erro típico de métodos parecidos que o material não aborda.
- **Especialista 10** consolida as candidatas e executa a varredura completa depois dos 5 testes obrigatórios (Etapa 8.2 do arquivo dele).
- **Especialista 11** escreve a camada externa no final do documento, depois das notas finais.

## As três lentes da varredura

Aplique as três, nesta ordem:

1. **Simulação de aplicação**: percorra cada passo do método como alguém que vai aplicá-lo amanhã sem nenhum contexto. Anote onde essa pessoa travaria: uma decisão sem critério para decidir, um passo sem indicação de como saber se foi bem feito, um recurso ou conhecimento que o método exige mas não menciona.
2. **Cenários de falha**: pergunte o que acontece quando as coisas não saem como o método espera. O método diz o que fazer nesses casos? Indica como perceber que algo deu errado e como corrigir?
3. **Comparação com o domínio**: pergunte o que métodos da mesma área costumam tratar e este não trata.

## Formato de cada ponto cego

- **O que falta**: a ausência, descrita de forma específica.
- **Onde pesa**: em qual passo, princípio ou componente do método a falta aparece.
- **Por que deveria estar ali**: o padrão de comparação que revela a ausência, ou seja, o conhecimento externo que mostra que essa peça é necessária.
- **O que acontece se continuar faltando**: a consequência prática para quem aplicar o método.
- **Gravidade**: impede a aplicação, compromete o resultado, ou depende do contexto de quem aplica.
- **Pergunta que resolve**: a pergunta que precisa ser respondida para preencher a lacuna.

## Regras

- **Aponte e pergunte, nunca resolva.** Não preencha o ponto cego com uma resposta, nem sugira qual seria a resposta. Preencher seria inventar uma parte do método.
- **Nada desta seção volta para o corpo do documento.** O método formalizado continua contendo apenas o que veio do material.
- **Inclua apenas ausências que afetam a aplicação.** Teste: se essa falta continuar, alguém aplicando o método vai travar, errar ou aplicar fora das condições em que ele funciona? Se a resposta for não, a ausência não entra.
- **Ausência não é discordância.** Se você discorda de algo que o método afirma, isso não é ponto cego. Esta seção trata apenas do que não está lá, nunca do que está lá e parece errado.
- **O que surgiu no material, mesmo sem conclusão, vai para os pontos em aberto**, e não para cá.
- **Condições de funcionamento vão para a seção de condições**, e não para cá.
- **Escreva cada item como ausência no método** ("o método não define o que fazer quando..."), nunca como ausência na conversa ("a conversa não discutiu...") ou na fonte ("o autor não explica..."). Vale igual nos dois modos de material.
- **Ordene do mais grave para o menos grave.**
- **Se não houver pontos cegos relevantes, declare isso explicitamente.** Nunca fabrique pontos cegos para preencher a seção.

## Marcador da camada externa

Antes da seção de pontos cegos, o documento final traz este marcador, exatamente como está:

```
════════════════════════════════════════
CAMADA EXTERNA AO MATERIAL
Tudo abaixo desta linha não faz parte do método extraído. É um alerta produzido por comparação com conhecimento externo, e não conteúdo do método.
════════════════════════════════════════
```

## Exemplo de um item

- **O que falta**: o método não define o que fazer quando o contato não responde à primeira mensagem.
- **Onde pesa**: passo de abordagem inicial.
- **Por que deveria estar ali**: em prospecção por mensagem direta, a ausência de resposta à primeira mensagem é o cenário mais comum, e não uma exceção.
- **O que acontece se continuar faltando**: quem aplica desiste cedo demais, ou insiste de um jeito que queima o contato.
- **Gravidade**: compromete o resultado.
- **Pergunta que resolve**: quantas tentativas fazer, com qual intervalo, e o que muda em cada uma?

## Antipadrões

- **Ponto cego genérico**: "o método não trata de mentalidade" ou "o método não considera todos os públicos". Não aponta um passo onde a pessoa vai travar; falha no teste de relevância.
- **Discordância disfarçada**: "o método deveria usar outra abordagem". Isso é opinião sobre o que está lá, não ausência.
- **Resposta embutida**: "o método não define o intervalo entre tentativas; o ideal seria três dias". A segunda metade é invenção.
- **Preenchimento para cumprir tabela**: listar ausências irrelevantes porque a seção "precisa ter itens".
- **Vazamento para o corpo**: incorporar um ponto cego ao guia de aplicação como se fosse parte do método.
