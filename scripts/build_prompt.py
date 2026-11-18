#!/usr/bin/env python3
"""Gerar o prompt portátil a partir do núcleo e dos módulos editoriais."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import sys
import tempfile


MODULE_PATHS = (
    "references/texto.md",
    "references/visual.md",
    "references/apresentacoes.md",
    "references/interfaces.md",
    "references/dados.md",
    "references/audiovisual.md",
    "references/unicode.md",
)
ORIGIN_HEADING = re.compile(r"^ {0,3}##\s+Origin version check\s*#*\s*$")
LEVEL_TWO_HEADING = re.compile(r"^ {0,3}##(?:\s|$)")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
ATTRIBUTION = re.compile(r"^(?:Autor|Licença):\s*\S")


def strip_skill_metadata(text: str) -> str:
    """Remover frontmatter e version-check, mantendo atribuição e exemplos."""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        end = next((index for index in range(1, len(lines)) if lines[index].strip() == "---"), None)
        if end is None:
            raise ValueError("Frontmatter YAML sem delimitador de fechamento.")
        lines = lines[end + 1:]

    output: list[str] = []
    attributions: list[str] = []
    skipping = False
    fence_character: str | None = None
    fence_length = 0
    for line in lines:
        match = FENCE.match(line)
        outside_fence = fence_character is None
        if outside_fence and ORIGIN_HEADING.match(line):
            skipping = True
            continue
        if outside_fence and skipping and LEVEL_TWO_HEADING.match(line):
            output.extend(attributions)
            if attributions:
                output.append("")
            attributions = []
            skipping = False
        if skipping:
            # As versões antigas colocavam estes créditos dentro da seção técnica.
            if outside_fence and ATTRIBUTION.match(line):
                attributions.append(line)
        else:
            output.append(line)
        if match:
            delimiter, remainder = match.groups()
            if outside_fence:
                fence_character = delimiter[0]
                fence_length = len(delimiter)
            elif delimiter[0] == fence_character and len(delimiter) >= fence_length and not remainder.strip():
                fence_character = None
                fence_length = 0
    output.extend(attributions)
    return "\n".join(output).strip() + "\n"


def render_prompt(root: Path) -> str:
    core = strip_skill_metadata((root / "SKILL.md").read_text(encoding="utf-8"))
    parts = [
        "<!-- Gerado por scripts/build_prompt.py; editar SKILL.md e references/. -->\n",
        core.rstrip(),
        "\n## Uso deste arquivo portátil\n\n"
        "As instruções editoriais e os módulos incluídos estão incorporados abaixo. "
        "Selecionar somente os módulos pertinentes à tarefa e ao material recebido; "
        "não aplicar todos por padrão. Referências a esses módulos apontam para as "
        "seções incorporadas neste arquivo. Scripts e ferramentas continuam opcionais "
        "e só podem ser usados quando estiverem realmente disponíveis.\n",
    ]
    for relative_path in MODULE_PATHS:
        module = root / relative_path
        if module.is_file():
            content = module.read_text(encoding="utf-8").strip()
            parts.append(f"\n---\n\n<!-- Módulo incorporado: {relative_path} -->\n\n{content}\n")
    return "\n".join(parts).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Raiz da skill.")
    parser.add_argument("--check", action="store_true", help="Verificar o arquivo gerado sem gravar.")
    args = parser.parse_args(argv)
    output = args.root / "HUMANIZADOR.md"
    temporary: Path | None = None
    try:
        expected = render_prompt(args.root).encode("utf-8")
        if args.check:
            if not output.is_file() or output.read_bytes() != expected:
                print("HUMANIZADOR.md ausente ou desatualizado; executar scripts/build_prompt.py.", file=sys.stderr)
                return 1
            print("HUMANIZADOR.md está atualizado.")
            return 0
        with tempfile.NamedTemporaryFile(mode="wb", dir=args.root, prefix=".humanizador-", suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(expected)
        os.replace(temporary, output)
        temporary = None
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Falha ao gerar o prompt: {error}", file=sys.stderr)
        return 2
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    print("HUMANIZADOR.md gerado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
