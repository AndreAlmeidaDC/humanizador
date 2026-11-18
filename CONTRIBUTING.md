# Contribuição

Mudanças neste pacote alteram o comportamento de agentes. Preservar clareza,
fidelidade, identidade e consentimento, com complexidade proporcional à tarefa.

## Onde editar

- SKILL.md: contrato comum, roteamento, entrada e saída.
- references: regras detalhadas por material e fontes verificáveis.
- scripts: operações determinísticas opcionais.
- tests: preservação de conteúdo e comportamento dos helpers.
- README.md, metadata.json e CHANGELOG.md: escopo, versão e mudanças.
- agents/openai.yaml: apresentação e acionamento no ambiente de skills.

SKILL.md e as referências são as fontes editoriais. HUMANIZADOR.md é gerado e
não deve ser editado à mão.

## Gerar e validar

    python scripts/build_prompt.py
    python scripts/validate_skill.py
    python -m unittest discover -s tests -v
    python scripts/build_prompt.py --check

O gerador remove o frontmatter e a seção Origin version check, preserva o conteúdo
editorial e incorpora os módulos fixos na ordem definida no script. O validador
detecta divergência de versões, arquivos ausentes e desatualização do bundle.

## Revisar comportamento

Manter o núcleo abaixo de 500 linhas e carregar módulos sob demanda. Não criar uma
lista universal de estilos proibidos. Cada recomendação deve ter contexto, efeito
e limite, especialmente quando vier de uma norma ou design system.

Conferir exemplos contra a entrada. Uma frase mais específica não pode ganhar fatos
que o original não tinha. Preservar código, falas e dados. Informar capacidade
necessária para editar ou verificar o material.

Ao avaliar em outro agente, fornecer a skill e o pedido original sem o resultado
esperado. Consultar references/cenarios.md apenas para preparar e julgar o teste.

## Publicar

Explicar por que a mudança foi necessária, o comportamento resultante e os testes
executados. Registrar mudanças de gatilhos, dependências e consentimento. Não usar
um resultado de validação estrutural como prova de acessibilidade ou qualidade
em todos os modelos.

Preservar a oferta de atualização e a regra de não substituir arquivos sem
autorização. Um pedido explícito de atualizar já satisfaz a autorização para esse
escopo e não exige confirmação repetida.
