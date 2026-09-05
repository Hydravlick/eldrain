"""Shared document semantics and strict YAML loading for vault tools."""
from __future__ import annotations

import json
from pathlib import Path

import yaml


MODEL = json.loads((Path(__file__).resolve().parents[1] / ".agents/policies/document-model.json").read_text(encoding="utf-8"))
GAMEPLAY_ROOTS = frozenset(MODEL["gameplay_roots"])
ACTIVE = MODEL["active_status"]


class MetadataError(ValueError):
    pass


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise MetadataError("YAML keys must be strings")
        if key in result:
            raise MetadataError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_yaml(text: str) -> dict:
    try:
        data = yaml.load(text, Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        raise MetadataError(str(exc)) from exc
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise MetadataError("expected a YAML mapping")
    return data


def frontmatter_text(path: Path) -> str | None:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    if not lines or lines[0] != "---":
        return None
    for end in range(1, len(lines)):
        if lines[end] == "---":
            return "\n".join(lines[1:end])
    raise MetadataError("unclosed frontmatter")


def parse_frontmatter(path: Path) -> dict:
    text = frontmatter_text(path)
    return load_yaml(text) if text is not None else {}


def is_gameplay(path: Path, root: Path) -> bool:
    return path.relative_to(root).parts[0] in GAMEPLAY_ROOTS


def route_metadata(data: dict) -> list[str]:
    problems = []
    for key in MODEL["route_fields"]:
        value = data.get(key)
        if key == "index_order":
            if type(value) is not int:
                problems.append("index_order must be an integer")
        elif not isinstance(value, str) or not value.strip() or "\n" in value:
            problems.append(f"{key} must be nonempty single-line text")
    return problems
