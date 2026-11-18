#!/usr/bin/env python3
"""Validar estrutura e consistência da skill sem alterar arquivos ou usar rede."""

from __future__ import annotations

import argparse
from datetime import datetime
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse


BASE_FILES = {
    "SKILL.md", "HUMANIZADOR.md", "README.md", "CHANGELOG.md", "metadata.json",
    "references/version-check.md", "scripts/audit_unicode.py",
    "scripts/build_prompt.py", "scripts/validate_skill.py", "tests/test_tools.py",
    "agents/openai.yaml",
}
SEMVER = re.compile(r"\d+\.\d+\.\d+")


def parse_frontmatter(text: str) -> dict[str, str]:
    """Ler os dois campos escalares da skill; aceitar texto simples ou em bloco."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md deve começar com frontmatter YAML delimitado por ---.")
    end = next((index for index in range(1, len(lines)) if lines[index].strip() == "---"), None)
    if end is None:
        raise ValueError("Frontmatter YAML sem delimitador de fechamento.")
    fields: dict[str, str] = {}
    index = 1
    while index < end:
        line = lines[index]
        index += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([A-Za-z_][\w-]*):[ \t]*(.*)", line)
        if not match:
            raise ValueError("Frontmatter deve conter apenas campos escalares name e description.")
        key, value = match.groups()
        if key in fields:
            raise ValueError(f"Campo duplicado no frontmatter: {key}.")
        if value in {"|", "|-", "|+", ">", ">-", ">+"}:
            block = []
            while index < end and (not lines[index].strip() or lines[index][:1].isspace()):
                block.append(lines[index].strip())
                index += 1
            value = " ".join(block).strip()
        elif value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError as error:
                raise ValueError(f"Aspas ou escapes inválidos no campo {key}.") from error
            if not isinstance(value, str):
                raise ValueError(f"O campo {key} deve ser texto.")
        elif value.startswith("'"):
            if not re.fullmatch(r"'(?:[^']|'')*'", value):
                raise ValueError(f"Aspas inválidas no campo {key}.")
            value = value[1:-1].replace("''", "'")
        elif value.startswith(("[", "{", "&", "*", "!")):
            raise ValueError(f"Usar texto escalar simples no campo {key}.")
        elif value.lower() in {"null", "true", "false", "~"} or re.fullmatch(r"[-+]?\d+(?:\.\d+)?", value):
            raise ValueError(f"O campo {key} deve ser texto, não um valor YAML tipado.")
        fields[key] = value.strip()
    return fields


def title_version(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            match = re.search(r"(?<![\d.])(\d+\.\d+\.\d+)\s*#*\s*$", line)
            return match.group(1) if match else None
    return None


def validate_skill(root: Path) -> list[str]:
    errors: list[str] = []

    def read_text(relative_path: str) -> str | None:
        try:
            return (root / relative_path).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"Não foi possível ler {relative_path} como UTF-8 ({type(error).__name__}).")
            return None

    skill = read_text("SKILL.md")
    if skill is not None:
        if len(skill.splitlines()) >= 500:
            errors.append(f"SKILL.md deve ter menos de 500 linhas; possui {len(skill.splitlines())}.")
        try:
            frontmatter = parse_frontmatter(skill)
            if set(frontmatter) != {"name", "description"}:
                errors.append("Frontmatter deve conter exatamente name e description, sem campos extras.")
            if frontmatter.get("name") != "humanizador":
                errors.append("Frontmatter name deve ser humanizador.")
            if not frontmatter.get("description"):
                errors.append("Frontmatter description deve ser texto não vazio.")
        except ValueError as error:
            errors.append(str(error))

    metadata_text = read_text("metadata.json")
    metadata = None
    if metadata_text is not None:
        try:
            metadata = json.loads(metadata_text)
            if not isinstance(metadata, dict):
                errors.append("metadata.json deve conter um objeto JSON.")
                metadata = None
        except json.JSONDecodeError:
            errors.append("metadata.json contém JSON inválido.")

    declared_files: set[str] = set()
    content_version = None
    if metadata is not None:
        if metadata.get("name") != "humanizador":
            errors.append("metadata.json name deve ser humanizador.")
        try:
            date_version = metadata.get("version", "")
            if not isinstance(date_version, str) or not re.fullmatch(r"\d{4}\.\d{2}\.\d{2}", date_version):
                raise ValueError
            datetime.strptime(date_version, "%Y.%m.%d")
        except ValueError:
            errors.append("metadata.json version deve ser uma data válida em YYYY.MM.DD.")
        content_version = metadata.get("content_version")
        if not isinstance(content_version, str) or not SEMVER.fullmatch(content_version):
            errors.append("metadata.json content_version deve seguir MAJOR.MINOR.PATCH.")
            content_version = None
        origin = metadata.get("origin_url")
        try:
            origin_valid = isinstance(origin, str) and urlparse(origin).scheme == "https" and bool(urlparse(origin).netloc)
        except ValueError:
            origin_valid = False
        if not origin_valid:
            errors.append("metadata.json origin_url deve ser uma URL HTTPS absoluta.")
        branch = metadata.get("default_branch")
        if not isinstance(branch, str) or not branch.strip():
            errors.append("metadata.json default_branch deve ser texto não vazio.")
        policy = metadata.get("update_policy")
        if not isinstance(policy, dict):
            errors.append("metadata.json update_policy deve ser um objeto.")
        else:
            if policy.get("requires_user_consent") is not True:
                errors.append("update_policy.requires_user_consent deve ser true.")
            if policy.get("silent_self_update_allowed") is not False:
                errors.append("update_policy.silent_self_update_allowed deve ser false.")
        required = metadata.get("required_files")
        if not isinstance(required, list) or not required:
            errors.append("metadata.json required_files deve ser uma lista não vazia.")
        else:
            for relative_path in required:
                if not isinstance(relative_path, str) or not relative_path or Path(relative_path).is_absolute() or ".." in Path(relative_path).parts:
                    errors.append("required_files contém um caminho inválido; usar arquivos relativos à skill.")
                    continue
                if relative_path in declared_files:
                    errors.append(f"Arquivo repetido em required_files: {relative_path}.")
                declared_files.add(relative_path)
                if not (root / relative_path).is_file():
                    errors.append(f"Arquivo obrigatório ausente: {relative_path}.")

    mandatory_files = set(BASE_FILES)
    builder = None
    builder_path = root / "scripts/build_prompt.py"
    if builder_path.is_file():
        try:
            # Evitar criação de __pycache__ durante uma validação somente leitura.
            previous_setting = sys.dont_write_bytecode
            sys.dont_write_bytecode = True
            try:
                spec = importlib.util.spec_from_file_location("humanizador_prompt_builder", builder_path)
                builder = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(builder)
            finally:
                sys.dont_write_bytecode = previous_setting
            mandatory_files.update(builder.MODULE_PATHS)
        except (OSError, ImportError, SyntaxError, AttributeError) as error:
            errors.append(f"Não foi possível carregar build_prompt.py ({type(error).__name__}).")
            builder = None
    for relative_path in sorted(mandatory_files):
        if not (root / relative_path).is_file() and relative_path not in declared_files:
            errors.append(f"Arquivo essencial ausente: {relative_path}.")
    if metadata is not None:
        undeclared = mandatory_files - declared_files
        if undeclared:
            errors.append("required_files não declara arquivos essenciais: " + ", ".join(sorted(undeclared)) + ".")

    readme = read_text("README.md")
    changelog = read_text("CHANGELOG.md")
    if content_version is not None:
        for filename, text in (("SKILL.md", skill), ("README.md", readme)):
            if text is not None and title_version(text) != content_version:
                errors.append(f"O título de {filename} deve declarar a content_version {content_version}.")
        if changelog is not None and not re.search(r"(?<![\d.])" + re.escape(content_version) + r"(?![\d.])", changelog):
            errors.append(f"CHANGELOG.md não menciona a versão {content_version}.")
    if builder is not None and skill is not None:
        try:
            expected = builder.render_prompt(root).encode("utf-8")
            if (root / "HUMANIZADOR.md").read_bytes() != expected:
                errors.append("HUMANIZADOR.md está desatualizado; executar scripts/build_prompt.py.")
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f"Não foi possível verificar HUMANIZADOR.md ({type(error).__name__}).")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Raiz da skill.")
    args = parser.parse_args(argv)
    errors = validate_skill(args.root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("Validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
