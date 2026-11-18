#!/usr/bin/env python3
"""Inventário Unicode somente leitura, sem limpeza ou inferência de autoria."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys
import unicodedata


SCHEMA_VERSION = "1.0"
TOOL_VERSION = "4.0.0"

# A presença de um destes caracteres pede contexto; não significa erro.
SINGLE_CATEGORIES = {
    0x00A0: "spacing",
    0x00AD: "soft_hyphen",
    0x061C: "bidirectional_control",
    0x180E: "script_formatting",
    0x2009: "spacing",
    0x200A: "spacing",
    0x200B: "zero_width_space",
    0x200C: "join_control",
    0x200D: "join_control",
    0x200E: "bidirectional_control",
    0x200F: "bidirectional_control",
    0x2028: "line_or_paragraph_separator",
    0x2029: "line_or_paragraph_separator",
    0x202F: "spacing",
    0x2060: "word_joiner",
    0xFEFF: "bom_or_zero_width_no_break_space",
}

CATEGORY_NOTES = {
    "spacing": "Pode preservar uma composição tipográfica intencional.",
    "soft_hyphen": "Pode indicar uma oportunidade legítima de hifenização.",
    "bidirectional_control": "Pode ser necessário em conteúdo bidirecional.",
    "script_formatting": "Pode ter função na escrita do idioma original.",
    "zero_width_space": "Pode marcar uma oportunidade de quebra de palavra.",
    "join_control": "Pode compor emojis ou alterar a escrita de um idioma.",
    "line_or_paragraph_separator": "Pode representar uma separação estrutural legítima.",
    "word_joiner": "Pode impedir uma quebra de linha de forma intencional.",
    "bom_or_zero_width_no_break_space": "Pode ser BOM inicial; o contexto define o tratamento.",
    "variation_selector": "Há usos legítimos em emojis, matemática e outras escritas.",
    "unicode_tag": "Há sequências de tags legítimas, como bandeiras de subdivisões.",
}


def category_for(codepoint: int) -> str | None:
    """Classificar apenas os intervalos cobertos, sem decidir se são indevidos."""
    if codepoint in SINGLE_CATEGORIES:
        return SINGLE_CATEGORIES[codepoint]
    if 0x202A <= codepoint <= 0x202E or 0x2066 <= codepoint <= 0x2069:
        return "bidirectional_control"
    if 0xFE00 <= codepoint <= 0xFE0F or 0xE0100 <= codepoint <= 0xE01EF:
        return "variation_selector"
    if 0xE0000 <= codepoint <= 0xE007F:
        return "unicode_tag"
    return None


def audit_text(text: str) -> dict:
    """Contar code points, sem normalizar, modificar ou reproduzir o texto."""
    counts = Counter(ord(character) for character in text)
    findings = []
    for codepoint, count in sorted(counts.items()):
        category = category_for(codepoint)
        if category is None:
            continue
        findings.append({
            "codepoint": f"U+{codepoint:04X}",
            "name": unicodedata.name(chr(codepoint), "UNASSIGNED OR RESERVED"),
            "category": category,
            "count": count,
            "action": "review",
            "context_note": CATEGORY_NOTES[category],
        })
    return {
        "schema_version": SCHEMA_VERSION,
        "tool_version": TOOL_VERSION,
        "unicode_database_version": unicodedata.unidata_version,
        "mode": "read-only-inventory",
        "total_codepoints": len(text),
        "total_flagged_codepoints": sum(item["count"] for item in findings),
        "distinct_flagged_codepoints": len(findings),
        "findings": findings,
        "limitations": [
            "O inventário cobre os caracteres e intervalos definidos no script; não é uma auditoria completa de Unicode.",
            "Um achado exige revisão de contexto e não prova erro, rastreamento ou autoria por IA.",
            "Nenhum caractere é removido, convertido ou normalizado; não há detecção de homóglifos.",
            "Code points não equivalem necessariamente a letras visíveis ou emojis completos.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="Arquivo UTF-8; se omitido, ler stdin.")
    args = parser.parse_args(argv)
    try:
        raw = args.input.read_bytes() if args.input else sys.stdin.buffer.read()
    except OSError as error:
        print(f"Erro ao ler a entrada: {error.strerror or type(error).__name__}.", file=sys.stderr)
        return 2
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        print(
            f"Entrada inválida: esperado UTF-8; byte inválido na posição {error.start}. "
            "Nenhum conteúdo foi alterado.",
            file=sys.stderr,
        )
        return 2
    json.dump(audit_text(text), sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
