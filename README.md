# Humanizador 2.6.2

Skill para remoção de sinais de texto gerado por IA em português brasileiro. Reescreve conteúdo para soar mais natural, humano e específico, sem inventar fatos.

## O que faz

Remove padrões comuns de escrita com cara de IA:

- Linguagem inflada e grandeza artificial
- Abstrações vazias e jargão corporativo
- Gerúndio ornamental e conectivos mecânicos
- Prosa fragmentada e listas secas
- Intensificadores gastos e adjetivos-curinga
- Hedging excessivo e voz passiva desnecessária
- Falta de voz autoral

## Perfis de edição

| Perfil | Quando usar |
|--------|------------|
| LinkedIn | Post, carrossel, artigo curto de opinião |
| E-mail executivo | E-mail para cliente, parceiro, diretoria |
| Documentação | Manual, README, política interna, especificação |
| Proposta comercial | Proposta, deck comercial, oferta de serviço |
| Acadêmico | Artigo, ensaio, relatório técnico-acadêmico |
| Jornalístico | Notícia, nota, resumo factual, release |

## Modos de intensidade

- **Leve**: texto já bom, só precisa perder marcas óbvias
- **Padrão**: maioria dos casos
- **Forte**: texto genérico, promocional ou claramente sintético
- **Seguro factual**: precisão importa mais que estilo

## Regra central

Humanizar não é inventar. Nunca inventa nomes, cargos, empresas, números, estudos, datas, estatísticas ou citações. Quando falta substância, diz que falta substância.

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `SKILL.md` | Skill principal (compatível com Manus, Claude Code, OpenCode) |
| `SKILL.yaml` | Mesmo conteúdo em formato YAML |
| `documentacao_humanizador_2.6.2.pdf` | Documentação completa em PDF |
| `documentacao_humanizador_2.6.2.docx` | Documentação completa em Word |
| `manifest.txt` | Lista de arquivos do pacote |

## Como usar

### No Manus

Copie o `SKILL.md` para a pasta de skills do Manus (`/home/ubuntu/skills/humanizador/SKILL.md`).

### No Claude Code / OpenCode

Copie o `SKILL.yaml` para o diretório de skills do seu ambiente.

### Uso direto

Cole o conteúdo do `SKILL.md` como system prompt em qualquer LLM e envie o texto que deseja humanizar.

## Créditos

Este projeto partiu do trabalho do [Humanizer](https://github.com/blader/humanizer) por [@blader](https://github.com/blader). A versão original serviu como base e foi expandida com perfis de edição para português brasileiro, novos padrões de detecção e modos de intensidade.

## Licença

MIT

## Autor

André Almeida
