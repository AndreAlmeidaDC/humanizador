# Humanizador Universal 4.0.0

Autor: André Almeida. Licença: MIT.

O Humanizador orienta a revisão de comunicação em português brasileiro. A versão 4.0
amplia o trabalho editorial para peças visuais, apresentações, interfaces, conversas,
dados e audiovisual, preservando a proposta original de melhorar a expressão sem
inventar fatos ou substituir a identidade do autor.

"Humanizar" significa tornar a comunicação compreensível, adequada ao contexto e
coerente com sua intenção. A skill não identifica autoria por IA, não certifica
acessibilidade e não promete passar por detectores.

## O que muda na 4.0

- Núcleo comum com módulos selecionados pelo material recebido.
- Revisão de hierarquia, densidade, legibilidade, redundância e identidade visual.
- Progressão narrativa em apresentações e carrosséis.
- Microcopy, estados de interface e conversas com recuperação e controle.
- Integridade de dados em gráficos e dashboards.
- Roteiros, narração, relação entre canais, legendas e transcrições fiéis.
- Separação explícita entre observado, medido, informado, não verificado e proposto.
- Auditor Unicode executável, somente leitura, em lugar da promessa de limpeza
  automática ampla.
- Oferta de atualização explícita quando uma versão nova é encontrada, respeitando
  autorização já dada e sem autoatualização silenciosa.

A mudança é major porque amplia os gatilhos, reorganiza o pacote e altera a regra de
Unicode. Os perfis, modos e quatro formatos anteriores continuam aceitos; entram
material, ação e plano-de-edicao.

## Como usar

Em um chat sem acesso a arquivos, copiar HUMANIZADOR.md como instrução e enviar o
material em mensagem separada. Esse arquivo inclui os módulos editoriais e mantém
seleção por tarefa. Imagens, áudio e vídeo só podem ser inspecionados se o modelo e o
ambiente tiverem suporte real à mídia.

Em um ambiente de skills, instalar o pacote completo. SKILL.md é o núcleo e os
arquivos de references são lidos sob demanda. Não é necessário instalar dependências
para usar as instruções editoriais.

Exemplos:

- "Use Humanizador para revisar este post com minha voz, somente-versao."
- "Analise este carrossel para leitura no celular e proponha as correções por página."
- "Revise esta landing page preservando identidade, conteúdo e funcionalidades."
- "Reorganize este gráfico sem mudar dados, unidades, escala ou conclusão."
- "Adapte o roteiro para narração; ainda não há áudio para avaliar."
- "Confira esta legenda com o vídeo e preserve o que as pessoas disseram."

## Parâmetros

- material: auto, texto, visual, apresentacao, interface, conversa, dados, audiovisual.
- acao: auto, diagnosticar, revisar, criar, orientar.
- perfil: auto, linkedin, email-executivo, documentacao, proposta-comercial, academico,
  jornalistico.
- modo: leve, padrao, forte, seguro-factual.
- formato: completo, somente-versao, diagnostico, comparativo, plano-de-edicao.
- Contexto opcional: público, objetivo, canal, voz, identidade, restrições e destino.

É possível enviar apenas o material e o pedido. O agente deve inferir escolhas
reversíveis e perguntar somente quando uma lacuna realmente impedir o trabalho.

## O que pode ser entregue

A entrega acompanha as capacidades reais do ambiente. Com texto, a skill pode orientar
reescrita direta. Com captura, pode analisar o visível e produzir direção de edição.
Com um arquivo editável e ferramenta compatível, pode orientar alterações e a
verificação do resultado. A instrução sozinha não edita um vídeo, mede CSS ou
renderiza uma apresentação.

O resultado deve distinguir revisão executada de recomendação. Não declarar foco,
teclado, cálculo, voz, timecode ou contraste aprovado sem a inspeção correspondente.

## Regras que evitam correção cega

Repetição pode ajudar: rótulos, unidades, navegação e mensagens de erro consistentes
orientam a pessoa. O problema é a repetição sem função que ocupa espaço e compete com
informação necessária. Três itens, uma cor forte ou um gradiente não provam autoria.

Uma captura reduzida não revela o tamanho original de uma fonte. Um dashboard denso
pode ser apropriado à tarefa. Uma legenda registra a fala e não deve receber uma nova
opinião para soar mais natural. Exemplos editoriais precisam preservar o que já
estava na entrada.

## Arquivos

- SKILL.md: instruções centrais e roteamento.
- HUMANIZADOR.md: versão portátil gerada, com os módulos incorporados.
- references/texto.md: perfis, voz, padrões e exemplos com preservação factual.
- references/visual.md: peças visuais e direção de arte.
- references/apresentacoes.md: slides, decks e carrosséis.
- references/interfaces.md: interfaces, microcopy e conversas.
- references/dados.md: gráficos, infográficos quantitativos e dashboards.
- references/audiovisual.md: roteiro, mídia, legendas e transcrições.
- references/unicode.md: limites e procedimento de auditoria.
- references/fontes.md: pesquisa, URLs, escopo e decisões editoriais.
- references/cenarios.md: casos de aceitação comportamental.
- references/version-check.md: verificação e atualização com consentimento.
- scripts/audit_unicode.py: inventário de caracteres, sem modificar a entrada.
- scripts/build_prompt.py: geração e conferência da versão portátil.
- scripts/validate_skill.py: validação estrutural e de consistência.
- tests/test_tools.py: testes dos helpers.
- metadata.json: versão e política operacional.

## Unicode

O auditor requer Python 3.10 ou superior e usa apenas a biblioteca padrão:

    python scripts/audit_unicode.py --input texto.txt

A saída JSON traz contagens por code point e observações de revisão. O arquivo
original permanece intacto. Um caractere listado pode ser necessário a um idioma,
emoji, fórmula ou identificador. A ferramenta não detecta autoria, não procura
mensagens ocultas completas e não remove marcas estatísticas.

Sem executar uma medição, o agente não deve inventar contagens. No formato
somente-versao, não anexar diagnósticos opcionais nem alterar caracteres ambíguos.

## Verificação de versão com consentimento

Quando encontrar uma versão mais nova, a skill deve resumir as mudanças e oferecer
explicitamente a atualização. Avisar da diferença sem oferecer não basta.
Uma autorização de atualização já presente na conversa é suficiente; não perguntar
novamente. Depois de uma recusa, não insistir na mesma sessão.

A leitura pública e a comparação são informativas. Atualizar arquivos exige
autorização; descartar alterações locais requer decisão específica. Depois de
salvar, verificar conteúdo e versão. O protocolo detalhado está em
references/version-check.md.

## Desenvolvimento e validação

Editar o núcleo e os módulos, nunca a versão portátil à mão. Gerar e conferir:

    python scripts/build_prompt.py
    python scripts/validate_skill.py
    python -m unittest discover -s tests -v
    python scripts/build_prompt.py --check

Os testes verificam código e empacotamento. Não demonstram por si sós qualidade
editorial, acessibilidade ou comportamento de todo modelo. Usar também os cenários
em references/cenarios.md com tarefas reais e preservar a separação entre insumo e
critério de avaliação.

## Pesquisa e créditos

A ampliação usa orientações de W3C/WAI, Unicode Consortium, GOV.UK, Government Analysis
Function, Microsoft e Nielsen Norman Group. O registro em references/fontes.md
distingue critérios técnicos de escolhas editoriais e contextualiza as fontes.

O material de referência enviado pelo autor incluiu capturas de um carrossel de
Tuti Nicola (@tutinicola) sobre padrões de comunicação. As imagens não são
redistribuídas neste pacote. As recomendações foram formuladas para esta skill e
conferidas com fontes primárias, sem tratar o carrossel como prova científica.

O projeto partiu do Humanizer de @blader:
https://github.com/blader/humanizer

Origem mantida por André Almeida:
https://github.com/AndreAlmeidaDC/humanizador

## Histórico

Consultar CHANGELOG.md. A versão 3.0 tornou o prompt portátil; a 3.1 aprofundou os
padrões de estrutura; a 3.2 acrescentou dois-pontos e Unicode; a 4.0 amplia os meios,
corrige exemplos e torna os limites operacionais explícitos.
