# TEMPLATE DE ENTREGA FINAL AO USUÁRIO

Quando o Especialista 11 concluir e todos os 11 passos estiverem completos, a skill entrega
ao usuário no formato abaixo. Este template é usado após a conclusão do fluxo, na mensagem
final da execução.

```
🎉 DISSECAÇÃO COMPLETA — DOCUMENTO FORMALIZADO PRONTO

📦 O QUE VOCÊ RECEBE:

1. DOCUMENTO FORMALIZADO COMPLETO
[Se o usuário pediu output em arquivo: entregar o arquivo .md em /mnt/user-data/outputs/
 usando present_files.
 Se pediu output no chat: entregar o documento completo aqui na mensagem.]

2. RESUMO EXECUTIVO
- Método extraído: [nome preciso do método]
- Domínio: [área de conhecimento onde se insere]
- Modo de material: [modo conversa / modo material pronto]
- Componentes principais: [lista curta dos elementos anatômicos centrais]
- Aplicabilidade imediata: [contextos onde pode ser aplicado agora com base no documento]
- Volume do documento final: [aproximadamente X palavras / N seções]

3. PONTOS EM ABERTO SINALIZADOS
[Lista honesta dos aspectos que o material original não resolveu completamente. Cada um com:
 - Qual é o aspecto não resolvido
 - Onde no documento está sinalizado
 - Se aplicável, sugestão de resolução futura]

[Se não houver pontos em aberto significativos, escrever:
 "Não foram identificados pontos em aberto de escopo significativo. O método foi formalizado
  na sua forma consolidada sem necessidade de sinalizações honestas de incompletude."]

4. PONTOS CEGOS SINALIZADOS
[Lista das ausências que o material nunca abordou e que afetam a aplicação, do mais grave para
 o menos grave, cada uma com a pergunta que a resolve. Se não houver, escrever: "Não foram
 identificados pontos cegos relevantes."]

5. SUGESTÕES DE USO

Para aplicar imediatamente:
- Leitura sequencial do documento para primeira apropriação do método
- Depois, consulta direcionada aos blocos específicos durante aplicação real
- Bloco 3 (Aplicação Prática) é o mais consultado durante uso ativo
- Bloco 4 (Proteção Contra Aplicação Errada) é o mais consultado quando aparecerem dificuldades

Para compartilhar com outras pessoas:
- O documento é autossuficiente — quem receber não precisa ter contexto do material original
- Se houver terminologia específica do seu contexto que apareça no documento, considere
  incluir explicações contextuais na apresentação
- Colaboradores que vão aplicar devem estudar especialmente os pré-requisitos e os princípios
  fundamentais antes de tentar a sequência executável

Para evoluir o método no futuro:
- Os pontos em aberto sinalizados são as direções naturais de próxima evolução
- As perguntas dos pontos cegos indicam o que levar para uma nova conversa: respondidas, elas
  podem ser incorporadas numa nova dissecação
- Aplicações reais que forcem adaptação além dos limites articulados vão gerar aprendizado
- Documente casos de aplicação para futura re-formalização quando volume de aprendizado
  justificar

✅ Alguma seção do documento que gostaria de aprofundar ou ajustar?
```

## Comportamento em ambiente Claude Code

Se estiver no Claude Code, e o usuário pediu output em arquivo, o Especialista 11 escreve
o arquivo em /mnt/user-data/outputs/ (ou pasta apropriada do projeto atual) e usa present_files
para o usuário acessar. Se o material original tinha um nome ou tema identificável, sugerir
nome do arquivo baseado nisso (exemplo: metodo-[nome-conciso].md).

## Comportamento em ambiente Claude.ai

Se estiver no Claude.ai, e o usuário pediu output em arquivo, entregar o documento como
artifact Markdown. Se pediu no chat, entregar diretamente na mensagem final. A mensagem final
pode ser longa — respeitar a densidade necessária, não comprimir o documento apenas para
economizar espaço na mensagem.

## Comportamento após entrega

A pergunta final "alguma seção que gostaria de aprofundar ou ajustar?" é convite genuíno.
Se o usuário responder pedindo ajuste, retornar ao especialista responsável pela seção em
questão (não refazer o pipeline inteiro). Ajustes localizados podem envolver:
- Aprofundamento de um princípio específico → retornar ao Especialista 6
- Detalhamento de um passo do guia de aplicação → retornar ao Especialista 8
- Adição de erro/antipadrão específico que faltou → retornar ao Especialista 9
- Revisão de fluidez do documento como um todo → retornar ao Especialista 11 com instrução
  específica

Se o usuário disser que está satisfeito, encerrar naturalmente sem forçar continuidade.
