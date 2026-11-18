# Unicode, auditoria e preservação

Esta seção substitui a remoção automática ampla da versão 3.2.0. Fontes UNI1, UNI2 e
UNI3 em references/fontes.md. Caracteres invisíveis não demonstram autoria por IA
nem intenção de rastreamento.

## Primeiro identificar a função

Joiners, controles bidirecionais, seletores de variação e tags podem ter uso legítimo.
Preservar idiomas, emojis compostos, bandeiras por sequência de tags, variantes
ideográficas e matemáticas, identificadores e exemplos sobre o próprio Unicode.
Não converter letras gregas ou cirílicas apenas por parecerem latinas.

Espaços sem quebra podem manter número e unidade juntos. Soft hyphen pode controlar
hifenização. Um BOM inicial pode ter função de codificação. A origem e o destino
importam. Não aplicar "remover sempre" a classes inteiras.

Em código, URLs, chaves, fórmulas, assinaturas, citações e registros literais, preservar
o original. Tratar o dado técnico fora da revisão estilística e só alterar com escopo
explícito e verificação adequada.

## Auditoria exata opcional

Usar scripts/audit_unicode.py quando houver Python e acesso ao texto original:

    python scripts/audit_unicode.py --input texto.txt

O script apenas lê e emite JSON com contagens dos caracteres monitorados. Não limpa,
não classifica autoria, não confirma malícia e não substitui avaliação linguística.
O inventário não é uma análise completa de todos os mecanismos Unicode. Não inclui
trechos do usuário por padrão.

Sem executar o auditor ou outra medição adequada, não declarar contagem exata nem
"arquivo livre de caracteres invisíveis". A visão de um screenshot ou OCR não garante
os code points do arquivo original.

## Decidir e relatar

Uma remoção ou normalização requer contexto suficiente de que o caractere é resíduo
e não tem função no trecho. Em dúvida, preservar. Quando o pedido exigir limpeza,
isolar as mudanças autorizadas, manter original recuperável e comparar resultado.

Nos formatos completo, diagnostico, comparativo ou plano-de-edicao, informar tipo,
contagem medida, decisão e eventual incerteza. No formato somente-versao, respeitar
a saída sem comentários e não fazer mudança ambígua; nenhuma obrigação de diagnóstico
se sobrepõe a esse formato. Solicitar esclarecimento apenas se indispensável.

Não chamar uma recomendação de limpeza de sanitização executada. Não apresentar
remoção de caracteres como remoção de marca d'água estatística. Não oferecer
"indetectabilidade" como resultado editorial.
