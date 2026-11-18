# Pesquisa e fundamentos da versão 4.0

Consulta: 12 de novembro de 2026. As recomendações combinam critérios técnicos,
orientações dos próprios mantenedores e decisões editoriais da Humanizador.
A pesquisa não valida a skill como detector de conteúdo gerado por IA.

## Conteúdo

- Como interpretar as fontes
- Acessibilidade e comunicação visual
- Interação, dados e audiovisual
- Unicode e proveniência
- Material enviado pelo autor
- Decisões editoriais adotadas

## Como interpretar as fontes

Uma norma oferece critérios no seu domínio. Um design system descreve escolhas
contextuais. Uma heurística ajuda a revisar, sem provar autoria ou causalidade.
As extensões para outros canais são propostas editoriais e mantêm essa distinção.

## Acessibilidade e comunicação visual

### A11Y1. W3C, WCAG 2.2

https://www.w3.org/TR/WCAG22/

Critérios aplicáveis incluem contraste de texto, cor, teclado, foco, reflow, ampliação
e tamanho de alvos. A skill mantém condições e exceções e exige verificação adequada
antes de uma afirmação de conformidade. Não usa a norma como régua universal de
tamanho de fonte em imagens ou projeções.

### A11Y2. W3C WAI, Easy Checks

https://www.w3.org/WAI/test-evaluate/preliminary/

Uma revisão inicial encontra parte das barreiras e não equivale a avaliação completa.
Aplicação na skill: registrar o que uma captura permite observar e o que exige
implementação, arquivo original ou teste.

### VIS1. Nielsen Norman Group, Visual Hierarchy in UX

https://www.nngroup.com/articles/visual-hierarchy-ux-definition/

A organização visual orienta a ordem de atenção por escala, contraste e agrupamento.
A Humanizador transforma isso em diagnóstico de competição e prioridade. Não adota
limites de cores ou tamanhos como leis gerais.

### VIS2. Nielsen Norman Group, Aesthetic and Minimalist Design

https://www.nngroup.com/articles/aesthetic-minimalist-design/

Informação sem função pode competir com a informação necessária. A redução de ruído
não obriga uma aparência minimalista. Aplicação: preservar conteúdo necessário e
avaliar densidade pela tarefa.

### UI1. GOV.UK Design System, Headings

https://design-system.service.gov.uk/styles/headings/

Orienta consistência de níveis, apresentação e capitalização de frase.
Capitalização de frase em português é um padrão editorial da skill; preservar
marcas, nomes próprios e convenções do autor.

### TYPE1. GOV.UK Design System, Paragraphs

https://design-system.service.gov.uk/styles/paragraphs/

O design system usa tamanhos específicos em seu contexto e registra mudanças para
telas pequenas. Aplicação: não inventar um tamanho único para todas as peças nem
perpetuar números sem conferir o sistema de referência.

### SLIDE1. Microsoft, apresentações acessíveis no PowerPoint

https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities

A documentação cobre títulos, ordem de leitura, fontes, contraste e alternativas
textuais. A recomendação de 18pt ou mais pertence ao contexto de apresentações,
sem substituir a inspeção do destino de uso.

### PT1. Governo brasileiro, Cartilha de Acessibilidade gov.br

https://www.gov.br/gestaodeconteudo/pt-br/manuais-e-tutoriais/diretrizes-para-edicao-de-conteudo/cartilha-de-acessibilidade-gov.br

Integra compreensão textual, tipografia, links, imagens, tabelas e gráficos.
Aplicação: tratar linguagem e apresentação como partes da mesma experiência, com
alternativas adequadas ao conteúdo.

## Interação, dados e audiovisual

### UI2. GOV.UK Design System, Error message

https://design-system.service.gov.uk/components/error-message/

Mensagens devem explicar o problema e a recuperação. Repetir a mesma mensagem no
campo e no resumo pode ser funcional. A skill distingue essa consistência da
redundância promocional e evita inventar recursos do serviço.

### HAI1. Amershi et al., Guidelines for Human-AI Interaction, CHI 2019

https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf

As diretrizes abordam capacidades compreensíveis, contexto social, correção e
controle. A aplicação editorial evita falsa confirmação, intimidade imposta e
representação estereotipada. Essa extensão não é um teste completo de vieses.

### DATA1. Government Analysis Function, Data visualisation: charts

https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/

Orienta escolha, formatação, fonte e acesso aos dados. As recomendações de escala
dependem do gráfico. A skill exige preservar relações e distingue revisão visual
de validação dos números.

### DATA2. Government Analysis Function, Testing dashboards for design and accessibility

https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-testing-dashboards-for-design-and-accessibility/

Aborda contexto, definições, período, atualização, hierarquia, qualidade e testes.
A organização por tarefa na Humanizador é aplicação editorial dessas orientações.

### AV1. W3C WAI, Captions/Subtitles

https://www.w3.org/WAI/media/av/captions/

Legendas representam fala e sons necessários à compreensão, sincronizados com a
mídia. Legendas automáticas precisam de revisão. A skill exige mídia para confirmar
tempos e não chama uma adaptação de fala de transcrição fiel.

### AV2. W3C WAI, Transcribing Audio to Text

https://www.w3.org/WAI/media/av/transcribing/

Orienta fidelidade, identificação de falantes e sons, literalidade e tratamento de
trechos incompreensíveis. A skill separa correção de transcrição de reescrita autoral.

## Unicode e proveniência

### UNI1. Unicode Consortium, Variation Sequences FAQ

https://www.unicode.org/faq/vs.html

Seletores têm usos padronizados além de emojis, incluindo variantes ideográficas e
matemáticas. Isso fundamenta retirar a instrução antiga de apagar esses caracteres
fora de emojis.

### UNI2. Unicode Consortium, Emoji and Pictographs FAQ

https://www.unicode.org/faq/emoji_dingbats.html

Documenta apresentação, modificadores, junção e sequências de tags. Esses mecanismos
podem ter uso legítimo e devem ser preservados conforme o contexto.

### UNI3. Unicode Consortium, UTS #51 Unicode Emoji

https://www.unicode.org/reports/tr51/

Define sequências e apresentação de emojis, incluindo tags. A auditoria da skill
faz inventário de code points; não tenta validar todas as sequências do padrão.

### PROV1. C2PA, Content Credentials Explainer, versão fixada 2.2

https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html

Origem e histórico são diferentes de veracidade factual. A documentação também
considera proveniência incompleta ou removida. A versão fixada fundamenta esses
conceitos; não é apresentada como a edição mais recente.

## Material enviado pelo autor

O pedido incluiu nove capturas de um carrossel de Tuti Nicola (@tutinicola), com
páginas 1 a 7 de um conjunto de oito; duas páginas estavam repetidas nos uploads.
Os temas visíveis incluíram letras pequenas, excesso de informação, repetição,
tríades, títulos e frases genéricas. Não houve URL da publicação no pedido.

Esse material motivou a ampliação de escopo. Não foi usado como prova de autoria de
IA, nem seus screenshots foram incorporados ou redistribuídos. Regras como testar
legibilidade no destino, preservar repetição funcional e não deduzir o CSS de uma
captura são adaptações críticas ao contexto apresentado.

## Decisões editoriais adotadas

- Usar módulos para que a revisão de um e-mail não carregue um checklist de vídeo.
- Manter voz e identidade como critérios positivos, sem inserir defeitos artificiais.
- Tratar títulos, tríades e padrões visuais por função, frequência e consequência.
- Preservar o contrato factual em exemplos e nas próprias reescritas da skill.
- Condicionar execução e verificação às capacidades reais do ambiente.
- Substituir remoção automática de classes Unicode por auditoria e decisão contextual.

Não houve estudo de usuários que comprovasse o efeito dessas regras neste pacote.
Testes automatizados verificam helpers e consistência; casos comportamentais
verificam exemplos de uso e precisam continuar evoluindo com evidências reais.
