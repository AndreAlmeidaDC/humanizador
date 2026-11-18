# Interfaces, microcopy e conversas

Aplicar a landing pages, telas de produto, formulários, onboarding, mensagens de erro,
atendimento e agentes conversacionais. Bases em UI1, UI2, HAI1 e A11Y1 de
references/fontes.md.

## Ação e estado

Identificar a tarefa da pessoa e a informação necessária para decidir. Escrever
botões, links e rótulos que expressem a ação real. Conferir consistência entre
promessa, botão, destino e resultado. Não inventar funcionalidade, prazo, suporte,
garantia ou confirmação para melhorar a mensagem.

Distinguir estados de carregamento, ausência de dados, erro, conclusão e ação ainda
não executada. Se algo foi somente preparado, não dizer enviado, salvo ou resolvido.
Não culpar a pessoa por falha de serviço.

Explicar o erro específico e o próximo passo disponível. Preservar entradas válidas
e orientar recuperação quando o sistema permitir. Evitar "Ops!" e humor em situações
frustrantes se substituírem explicação útil.

## Repetição funcional

Manter o mesmo termo para o mesmo objeto ou comando. Repetir mensagem de erro junto
ao campo e no resumo quando esse padrão ajudar; não reescrever cada ocorrência para
parecer variada. Preservar rótulos, unidades, estados e navegação consistentes.

Em landing pages, detectar se título, cards e seções repetem a mesma promessa sem
oferecer explicação, evidência ou condição. Reorganizar o percurso em torno da decisão
real. Não fabricar prova social, contadores, urgência ou casos para preencher um template.

## Conversa e voz

Responder à necessidade antes de ornamentar. Fazer perguntas específicas quando
necessárias, aproveitar o contexto já fornecido e permitir correção sem recomeçar.
Evitar saudação longa, resumo ritual, elogio automático e oferta genérica ao final
de toda resposta.

Preservar cordialidade e adequar o tom à situação. Não simular experiência pessoal,
emoção ou intimidade. Não inserir gírias, hesitações e erros para fingir espontaneidade.
Não esconder que há automação quando essa informação for relevante para a interação.

Manter controle e recuperação: deixar compreensível o que pode ser feito, como revisar
um erro e quando é preciso outro recurso. Não prometer transferência humana ou
acompanhamento que o serviço não oferece. Para mensagens a terceiros, preparar o
conteúdo; envio depende da autorização e das capacidades do ambiente.

## Uso e acessibilidade

Separar revisão visual da inspeção de comportamento. Com implementação disponível,
verificar navegação por teclado, foco visível, rótulos, hierarquia semântica, zoom,
responsividade e alternativas textuais no escopo da tarefa. Com screenshot, apontar
apenas o visível e registrar os testes pendentes.

WCAG 2.2 AA inclui alvos de 24 por 24 CSS px com exceções, redimensionamento de texto
até 200% e reflow equivalente a 320 CSS px em conteúdo vertical, também com exceções.
Aplicar o critério pertinente e seu método; não converter todo controle em falha só
por sua dimensão aparente numa imagem.

## Exemplo didático

Contexto fornecido: um upload de PDF falhou porque o arquivo tem 18 MB e o limite é 10 MB.
Mensagem possível: "O arquivo tem 18 MB. Envie um PDF de até 10 MB."
Não acrescentar "compacte aqui" se não existir essa opção. Aqui, frases curtas ajudam
a executar a tarefa e não são um defeito de estilo.
