# Dissecador de Métodos

Skill para o Claude que orquestra 11 especialistas master-level em sequência rigorosa para
extrair o método, framework ou sistema de conhecimento que emergiu em um material bruto
iterativo (conversa, transcrição, sessão de estudo, brainstorm, pesquisa), e formalizá-lo
em um documento autossuficiente, profundo e imediatamente aplicável por qualquer pessoa que
nunca tenha visto o material original.

## O que esta skill faz

Recebe um material bruto onde conhecimento foi sendo desenvolvido ao longo de iterações e
entrega um documento formalizado completo que:

- Define o método com precisão operacional (não descrição genérica)
- Articula seus princípios fundamentais com análise consequencial
- Descreve sua anatomia completa e o mecanismo causal de funcionamento
- Fornece um guia executável passo a passo com critérios de qualidade e checkpoints
- Cataloga erros comuns, antipadrões e variações legítimas
- Preserva pontos em aberto com honestidade epistêmica

O documento existe como se tivesse sido escrito por um especialista que domina o assunto,
não como análise de uma conversa.

## Como ativar

Apenas por comando explícito. Diga uma dessas frases (ou similares) na sua mensagem para o
Claude, junto do material que deseja dissecar:

- "use o dissecador-de-metodos"
- "aciona o dissecador-de-metodos"
- "roda o dissecador-de-metodos"
- "disseca com o dissecador-de-metodos"

A skill não ativa por triggers implícitos como "extrai o método dessa conversa" ou "formaliza
isso aqui". Isso é intencional — evita ativações não desejadas do pipeline completo dos 11
passos quando você quer apenas uma extração leve.

## Instalação

### Claude Code (Modo A — recomendado)

Copie a pasta `dissecador-de-metodos/` para uma dessas localizações:

**Instalação pessoal** (disponível em todos os projetos):
```bash
mkdir -p ~/.claude/skills/
cp -r dissecador-de-metodos ~/.claude/skills/
```

**Instalação específica de projeto**:
```bash
mkdir -p .claude/skills/
cp -r dissecador-de-metodos .claude/skills/
```

Verifique a instalação:
```bash
claude /skills
# Deve mostrar 'dissecador-de-metodos' na lista
```

### Claude.ai (Modo B)

Empacote a pasta como arquivo `.zip` (a pasta `dissecador-de-metodos/` deve estar na raiz
do zip, contendo o `SKILL.md` diretamente):

```bash
cd /caminho/pai/da/pasta
zip -r dissecador-de-metodos.zip dissecador-de-metodos/
```

Depois no Claude.ai:
1. Abrir Settings → Customize → Skills (ou Settings → Capabilities → Skills)
2. Clicar em "+" → "Create skill" → "Upload"
3. Fazer upload do arquivo `dissecador-de-metodos.zip`
4. Ativar o toggle da skill

Nota importante sobre limites no Claude.ai: materiais brutos acima de 60 mil tokens têm risco
crescente de estourar contexto no Modo B (Claude.ai sem subagents). A skill vai avisar você
quando detectar essa situação e oferecer alternativas.

## Como usar depois de instalada

1. Cole o material bruto na conversa (ou anexe como arquivo)
2. Diga: "use o dissecador-de-metodos"
3. A skill vai apresentar a análise inicial do material e perguntar o formato de output
4. Você confirma "iniciar" e a skill começa a rodar
5. Após o Passo 2 (identificação do objeto central), a skill vai pausar e pedir sua confirmação
6. Você confirma que o objeto central foi identificado corretamente
7. A skill continua os passos 3 a 11 automaticamente (no Modo A) ou pedindo "ok" a cada passo
   (no Modo B)
8. No final, você recebe o documento formalizado no formato que pediu

## Arquitetura da skill

- `SKILL.md` — orquestrador master, contém as regras absolutas e o fluxo de execução
- `agents/` — 11 arquivos de especialistas para uso via Task tool no Claude Code
- `references/` — mesmos 11 arquivos para leitura sequencial no Claude.ai, mais 4 protocolos
  operacionais (fluxo, checkpoint, cinco testes, tratamento de pontos em aberto)
- `assets/` — templates de saída (documento formalizado e entrega final)
- `scripts/` — utilitários Python (estimador de volume, detector de ambiente, validador
  heurístico)

## Compatibilidade

- Claude Code (versão 2.1.86+): funciona plenamente em Modo A com subagents paralelos via Task
  tool
- Claude.ai (Pro, Max, Team, Enterprise): funciona em Modo B sequencial, com aviso automático
  para materiais grandes
- Claude Desktop: funciona conforme o ambiente subjacente
- Free tier do Claude.ai: skills customizadas requerem plano pago; verificar disponibilidade
  atual da funcionalidade

## Limitações conhecidas

1. No Claude.ai (Modo B), materiais acima de 100 mil tokens tem risco alto de estourar
   contexto antes de completar os 11 passos. A skill avisa e oferece alternativas.
2. O sistema depende do material bruto ter maturado suficientemente para permitir formalização.
   Se o material não desenvolveu um objeto central identificável, o Especialista 2 vai reportar
   isso honestamente e a skill vai parar em vez de forçar formalização de conteúdo imaturo.
3. Aspectos que o material não resolveu permanecem em aberto no documento final — a skill nunca
   inventa para preencher lacunas.

## Créditos

Construída com a metodologia da skill-forge (Rafa Marks) a partir do system prompt do
"Diretor Editorial Master de Formalização de Conhecimento Emergente" e dos 11 arquivos de
especialistas do sistema Dissecador de Métodos original.
