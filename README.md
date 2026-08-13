# Humanizador Universal 3.1.0

Autor: André Almeida  
Licença: MIT

O **Humanizador Universal** é uma especificação de comportamento editorial para modelos de linguagem e agentes de IA. Ele foi desenhado para remover sinais comuns de texto com cara de IA em **português brasileiro**, sem inventar fatos, sem alterar o sentido original e sem transformar a voz do autor em uma voz genérica de consultoria.

Desde a versão 3.0.0, deixou de ser uma skill acoplada a uma plataforma específica e passou a funcionar como um **prompt universal portátil**. Isso significa que o Humanizador pode ser usado em qualquer LLM, agente, aplicação de chat, orquestrador, automação ou API que aceite instruções em linguagem natural. A versão 3.1.0 manteve essa arquitetura e acrescentou conteúdo editorial novo (ver Changelog).

> Humanizar não é inventar. O Humanizador melhora ritmo, clareza, naturalidade e especificidade, mas não cria números, fontes, casos, experiências pessoais, resultados ou opiniões que não estejam no texto original.

## O que mudou nesta versão

A versão anterior foi escrita no formato de skill com metadados e campos associados a ambientes específicos, como compatibilidade declarada e ferramentas permitidas. A nova versão foi reorganizada para ser independente de plataforma.

| Área | Antes | Agora |
|---|---|---|
| Dependência de plataforma | Estrutura orientada a skill com metadados de compatibilidade. | Prompt universal em Markdown, copiável para qualquer LLM ou agente. |
| Ferramentas | Havia lista de ferramentas permitidas, mesmo que a skill não dependesse delas. | Não há dependência de ferramentas externas. |
| Uso em APIs | Não havia orientação detalhada para chamadas por API. | Há modelos de uso manual, por agente e por API. |
| Documentação | Documentação empacotada em arquivos PDF/DOCX derivados da versão antiga. | Documentação consolidada no README e instrução universal em `HUMANIZADOR.md`. |
| Portabilidade | Focada em ambientes específicos. | Compatível com ChatGPT, Claude, Gemini, OpenRouter, agentes customizados, n8n, LangChain, CrewAI, AutoGen, scripts próprios e qualquer sistema que aceite prompt textual. |

## Arquivos do repositório

| Arquivo | Finalidade |
|---|---|
| `HUMANIZADOR.md` | Prompt universal principal. É o arquivo recomendado para copiar como system prompt, developer prompt, custom instruction ou instrução permanente de agente. |
| `SKILL.md` | Cópia do prompt universal mantida para compatibilidade com fluxos que procuram automaticamente um arquivo chamado `SKILL.md`. |
| `README.md` | Documentação detalhada para humanos, com explicação de funcionamento, parâmetros, exemplos e boas práticas. |

## Como funciona

O Humanizador transforma o modelo em um editor. Ao receber um texto, o agente deve ler o conteúdo inteiro, identificar sinais de artificialidade, classificar o gênero textual, escolher um perfil de edição, decidir a intensidade da intervenção, reescrever apenas o necessário e apontar riscos factuais quando houver lacunas.

O objetivo não é deixar o texto informal a qualquer custo. Em documentação técnica, por exemplo, humanizar significa remover ambiguidade, floreio e marketing. Em um post de LinkedIn, pode significar reduzir jargão, quebrar simetria artificial e trazer uma opinião mais nítida. Em uma proposta comercial, significa tornar a mensagem mais clara, controlando promessas e evitando adjetivos vazios.

## Perfis de edição

| Perfil | Quando usar | Prioridade editorial |
|---|---|---|
| `linkedin` | Posts, carrosséis, legendas, artigos curtos e conteúdo de opinião. | Naturalidade, opinião, concretude, menos jargão e menos tom de guru. |
| `email-executivo` | E-mails para clientes, parceiros, diretoria, fornecedores ou times internos. | Clareza, firmeza, cordialidade real, intenção explícita e menos rodeio. |
| `documentacao` | README, manuais, políticas, especificações, fluxos e instruções. | Precisão, sequência lógica, consistência terminológica e instrução acionável. |
| `proposta-comercial` | Propostas, escopos, ofertas, decks e descrições de solução. | Clareza de problema, entrega, limite, benefício e promessa controlada. |
| `academico` | Artigos, ensaios, relatórios técnico-acadêmicos e justificativas metodológicas. | Rigor, sobriedade, coesão, precisão conceitual e cuidado argumentativo. |
| `jornalistico` | Notícias, notas, resumos factuais, releases e textos informativos. | Fato, fonte, atribuição, verificabilidade e ausência de perfume promocional. |

Se o usuário não informar um perfil, use `auto`. Nesse caso, o modelo deve inferir o gênero a partir do texto e do pedido.

## Modos de intensidade

| Modo | Quando usar | Grau de intervenção |
|---|---|---|
| `leve` | O texto já está bom e só precisa perder marcas óbvias de IA. | Ajustes pontuais em frases, conectivos, adjetivos e ritmo. |
| `padrao` | A maioria dos casos. | Reorganização moderada, corte de gordura, redução de abstrações e melhoria de transições. |
| `forte` | Texto genérico, promocional, engessado ou claramente sintético. | Reestruturação de parágrafos, abertura, ritmo, listas e formulações vagas. |
| `seguro-factual` | Conteúdo sensível, técnico, jornalístico, regulatório, jurídico ou reputacional. | Intervenção cautelosa, com foco em precisão e sinalização de lacunas. |

## Formatos de saída

| Formato | Quando usar | Resultado |
|---|---|---|
| `completo` | Padrão recomendado. | Diagnóstico, perfil/modo, versão revisada, riscos restantes e mudanças feitas. |
| `somente-versao` | Quando o usuário quer apenas o texto final. | Entrega apenas a versão revisada. |
| `diagnostico` | Quando o usuário quer entender os problemas antes de reescrever. | Entrega apenas a análise crítica. |
| `comparativo` | Quando o usuário quer revisar mudanças trecho a trecho. | Entrega tabela com original, problema e sugestão. |

## Instalação e uso manual

Não há instalação obrigatória. O uso básico é copiar o conteúdo de `HUMANIZADOR.md` e colar como instrução no ambiente escolhido.

### Uso em ChatGPT, Claude, Gemini ou outro chat

Abra uma conversa nova, cole o conteúdo de `HUMANIZADOR.md` como primeira mensagem e, em seguida, envie o texto a revisar. Se o produto permitir criar instruções personalizadas, GPTs, projetos ou agentes, salve o conteúdo de `HUMANIZADOR.md` como instrução permanente.

Modelo de chamada recomendado:

```text
Perfil: auto
Modo: padrão
Formato: completo
Restrições: preservar termos técnicos; não aumentar muito o texto

TEXTO A HUMANIZAR:
[cole aqui o texto]
```

Para uma resposta direta:

```text
Humanize o texto abaixo em modo forte e entregue somente a versão final.

TEXTO:
[cole aqui o texto]
```

## Uso em agentes

Em agentes autônomos, use `HUMANIZADOR.md` como instrução de papel, system prompt, developer prompt ou policy local. O agente não precisa de ferramentas para executar a edição. Se o agente tiver ferramentas de leitura e escrita, elas podem ser usadas apenas para abrir arquivos e salvar resultados; a lógica editorial não depende delas.

Estrutura recomendada para agentes:

```text
[INSTRUÇÃO PERMANENTE DO AGENTE]
Cole aqui o conteúdo de HUMANIZADOR.md.

[TAREFA DO USUÁRIO]
Humanize o texto abaixo usando perfil documentação, modo seguro-factual e formato comparativo.

[TEXTO]
...
```

Quando o agente atuar em arquivos longos, preserve a integridade do conteúdo. Ele deve ler o documento inteiro, identificar seções que exigem estilos diferentes e aplicar o perfil dominante sem misturar gêneros indevidamente.

## Uso por API

Em APIs que aceitam mensagens separadas, envie o conteúdo de `HUMANIZADOR.md` como mensagem de sistema ou instrução equivalente. Em seguida, envie o texto do usuário em outra mensagem. O exemplo abaixo é conceitual e pode ser adaptado a qualquer SDK.

```json
{
  "messages": [
    {
      "role": "system",
      "content": "[conteúdo integral de HUMANIZADOR.md]"
    },
    {
      "role": "user",
      "content": "Perfil: linkedin\nModo: forte\nFormato: completo\n\nTEXTO A HUMANIZAR:\n..."
    }
  ]
}
```

Quando o provedor usar nomes diferentes, aplique a equivalência abaixo.

| Conceito | Nome comum em plataformas |
|---|---|
| Instrução permanente | system prompt, developer message, custom instruction, agent instruction, role prompt, policy prompt |
| Texto a editar | user message, input, task, conversation turn, payload |
| Restrições | additional instructions, constraints, metadata, style guide |
| Saída estruturada | response format, JSON schema, markdown output, template |

## Uso em automações

O Humanizador pode ser usado em automações de conteúdo, revisão editorial, CRM, atendimento, documentação e redes sociais. Em ferramentas como n8n, Zapier, Make ou scripts próprios, a prática recomendada é manter `HUMANIZADOR.md` como variável de configuração ou arquivo de referência e concatenar a tarefa específica a cada execução.

Exemplo de template de automação:

```text
[SYSTEM]
{conteudo_do_arquivo_HUMANIZADOR.md}

[USER]
Perfil: {perfil}
Modo: {modo}
Formato: {formato}
Restrições: {restricoes}

TEXTO A HUMANIZAR:
{texto_original}
```

## Boas práticas

O Humanizador funciona melhor quando recebe contexto suficiente. Sempre que possível, informe o canal, o público, o objetivo do texto, o grau de formalidade desejado e qualquer termo que deve ser preservado. Para textos autorais, envie uma amostra da voz do autor. Isso reduz o risco de o modelo transformar o texto em uma voz genérica.

Para conteúdos sensíveis, use `modo: seguro-factual`. Esse modo dá prioridade à precisão e à sinalização de lacunas. Se o texto afirmar resultados sem evidência, o Humanizador deve apontar o risco em vez de suavizar a frase e fazê-la parecer mais confiável do que é.

## Exemplos

### Exemplo para LinkedIn

Entrada:

```text
Perfil: linkedin
Modo: forte
Formato: completo

TEXTO A HUMANIZAR:
Em um cenário cada vez mais dinâmico, a inteligência artificial vem se consolidando como uma aliada estratégica na transformação dos negócios.
```

Saída esperada:

```text
Diagnóstico breve:
O texto usa abertura genérica, linguagem inflada e abstrações comuns em conteúdo corporativo sobre IA.

Perfil e modo usados:
LinkedIn, modo forte.

Versão revisada:
Muita empresa fala de IA como estratégia. Na prática, boa parte ainda usa IA para remendar processo ruim com interface bonita.

Riscos restantes:
A versão revisada tem tom opinativo. Se a intenção for institucional, o tom deve ser suavizado.

O que foi mudado:
Reduzi abstrações, removi o enquadramento genérico e troquei a frase promocional por uma observação mais concreta.
```

### Exemplo para documentação

Entrada:

```text
Perfil: documentacao
Modo: padrão
Formato: somente-versao

TEXTO A HUMANIZAR:
A plataforma atua como uma solução robusta que viabiliza a operacionalização dos processos, promovendo maior eficiência para os usuários.
```

Saída esperada:

```text
A plataforma ajuda os usuários a executar processos com menos etapas manuais.
```

A saída acima remove pose, nominalização e adjetivo vago. Se o texto original não explicar quais processos são executados nem como a eficiência melhora, o Humanizador não deve inventar esse detalhe.

## Limitações

O Humanizador não verifica fatos fora do texto original, a menos que seja combinado com ferramentas de pesquisa ou checagem externa. Ele também não deve prometer originalidade, indetectabilidade por classificadores de IA ou bypass de sistemas de detecção. A finalidade correta é editorial: melhorar clareza, naturalidade e adequação ao contexto.

## Compatibilidade

O Humanizador é compatível com qualquer ambiente que aceite instruções em linguagem natural. Isso inclui chats de LLM, APIs, agentes autônomos, workflows de automação, assistentes internos, sistemas de atendimento, editores com IA e pipelines de conteúdo.

| Ambiente | Como usar |
|---|---|
| ChatGPT, Claude, Gemini e similares | Cole `HUMANIZADOR.md` como instrução ou primeira mensagem. |
| Agentes customizados | Use `HUMANIZADOR.md` como prompt de sistema ou instrução permanente. |
| APIs | Envie `HUMANIZADOR.md` como mensagem de sistema e o texto como mensagem de usuário. |
| Automação | Salve `HUMANIZADOR.md` como variável ou arquivo e concatene com o texto de entrada. |
| Repositórios de prompts | Publique `HUMANIZADOR.md` como prompt principal e preserve este README como documentação. |

## Verificação de versão com consentimento

Esta skill foi padronizada para operar como uma skill atualizável com consentimento humano. No início de um uso relevante, quando houver internet e ferramentas Git ou HTTP disponíveis, o agente deve consultar o repositório de origem, ler o `README.md` e o `CHANGELOG.md` quando existirem, comparar a cópia local com a versão upstream e resumir as novidades encontradas.

Essa checagem não autoriza autoatualização silenciosa. A regra é: **verificar, explicar e perguntar**. O agente deve informar o que mudou, dizer se a mudança impacta a tarefa atual e pedir autorização explícita antes de atualizar qualquer arquivo local da skill. O protocolo completo está em [`references/version-check.md`](references/version-check.md).

## Histórico de alterações

| Data | Versão | Alteração | Motivo |
|---|---|---|---|
| 2026-08-05 | 3.1.0 | Seção dedicada ao paralelismo negativo ("não é X, é Y") como principal marca estrutural de texto de IA, com detecção por frequência e orientação de reescrita; novas entradas na biblioteca de padrões (transição-isca, regra de três mecânica); `HUMANIZADOR.md` passou a ser gerado a partir do `SKILL.md` em vez de mantido à mão. | Fechar a lacuna do padrão estrutural mais comum não coberto pela versão anterior, e eliminar divergência entre os dois arquivos de conteúdo. |
| 2026-05-26 | 3.0.0 | Transformação da skill em prompt universal portátil; remoção de campos específicos de plataforma; criação de documentação detalhada no README; criação de `HUMANIZADOR.md`; manutenção de `SKILL.md` como cópia compatível. | Permitir uso em qualquer agente ou LLM, conforme solicitação do autor. |

## Créditos

Este projeto partiu do trabalho do Humanizer, publicado por [@blader][1]. A versão atual foi mantida no repositório `AndreAlmeidaDC/humanizador` e expandida com perfis de edição para português brasileiro, novos padrões de detecção, modos de intensidade e uma estrutura universal para uso em agentes e LLMs.[2]

## Referências

[1]: https://github.com/blader/humanizer "Humanizer — repositório original de referência"
[2]: https://github.com/AndreAlmeidaDC/humanizador "Humanizador — repositório mantido por André Almeida"

## Licença

MIT
