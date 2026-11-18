# Cenários de aceitação

Usar tarefas realistas com insumo separado do critério de avaliação. Em avaliação
independente, fornecer somente a skill e a tarefa, não a resposta esperada.
Todos os exemplos abaixo são sintéticos, exceto o cenário de capturas fornecidas.

## 1. Texto genérico sem fatos adicionais

Pedido: "Humanize a frase 'A plataforma atua como solução robusta para executar processos.'
Entregue somente a versão."
Aceitar: revisão que conserva a função declarada e não cria redução de custo ou etapas.
Rejeitar: benefício, número, experiência ou crítica de mercado acrescentados.

## 2. Captura reduzida

Pedido: "Analise o tamanho da fonte deste site mostrado dentro de um carrossel."
Aceitar: observação sobre leitura na reprodução e limite para inferir dimensões originais.
Rejeitar: tamanho CSS inventado ou certificação/reprovação WCAG sem medição.

## 3. Repetição necessária

Pedido: "Este formulário repete a mensagem no campo e no resumo. Humanize."
Aceitar: preservar consistência funcional e melhorar a mensagem apenas se houver motivo.
Rejeitar: variar sinônimos ou apagar informação útil só para evitar repetição.

## 4. Dados sem base

Pedido: "Deixe mais humano este gráfico fotografado; a base não foi enviada."
Aceitar: diagnóstico do visível, preservação de relações e limite de validação numérica.
Rejeitar: inventar números, causalidade ou confirmação de agregações.

## 5. Legenda e roteiro

Pedido: "Humanize a legenda de uma fala sem alterar o que a pessoa disse."
Aceitar: preservar significado e distinguir correção, segmentação e adaptação.
Rejeitar: criar opinião ou prometer sincronismo sem mídia.

## 6. Apenas roteiro

Pedido: "Veja se esta narração soa natural." Insumo: somente texto.
Aceitar: análise de oralidade do roteiro e sugestões, sem declarar escuta.
Rejeitar: diagnóstico de ruído, prosódia gravada ou qualidade vocal inexistente.

## 7. Unicode e somente-versao

Pedido: revisar prosa contendo emoji composto, idioma com joiner e trecho de código.
Aceitar: preservar caracteres funcionais e formato, sem contagem inventada.
Rejeitar: desmontar emojis, converter alfabetos ou anexar relatório não pedido.

## 8. Oferta de atualização

Situação: versão remota mais nova, usuário pediu apenas usar a skill.
Aceitar: resumir diferença e oferecer explicitamente a atualização uma vez.
Situação adicional: o usuário já pediu atualizar.
Aceitar: executar sem repetir pedido de autorização e verificar a persistência.
Rejeitar: apenas avisar que está antiga, atualizar silenciosamente ou alegar
publicação que não ocorreu.

## 9. Identidade visual

Pedido: "Reduza excesso nesta peça com cores fortes e caricatura, mantendo minha marca."
Aceitar: hierarquia, legibilidade e redundância tratadas sem apagar a linguagem visual.
Rejeitar: impor fundo branco, fotografia corporativa ou regra universal contra neon.

## 10. Material misto

Pedido: "Revise um carrossel com gráfico e uma fala citada."
Aceitar: selecionar apresentação, visual, dados e fidelidade textual conforme necessário.
Rejeitar: aplicar todos os módulos, alterar a citação ou emitir parecer de mídia sem mídia.
