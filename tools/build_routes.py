from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

try:
    from tools.document_model import ACTIVE, MetadataError, parse_frontmatter, route_metadata
except ModuleNotFoundError:
    from document_model import ACTIVE, MetadataError, parse_frontmatter, route_metadata


DOMAINS = {
    "01_Core_Vision": ("Ядро и видение", "Когда вопрос касается обещания игры, core loop или материальной грамматики."),
    "02_World_Lore": ("Мир и лор", "Когда нужны законы мира, метафизика, культуры или причинность."),
    "03_Factions_Societies": ("Фракции и институты", "Когда вопрос касается Очагов, доверия, контрактов или социальных ролей."),
    "04_Player_Entities": ("Пешка и идентичность", "Когда меняются жизнь Пешки, теги, body, profile или recovery."),
    "05_Combat_Survival": ("Бой и выживание", "Когда вопрос меняет оружие, угрозу, урон, скрытность или counterplay."),
    "06_Economy_Loot": ("Экономика и возврат", "Когда вопрос касается ценности, лута, обмена, extraction или стабилизации."),
    "07_Gear_Inventory": ("Снаряжение и инвентарь", "Когда вопрос касается loadout, предметов, Термоса, контейнеров или крафта."),
    "08_World_Generation": ("Генерация и аномалия", "Когда вопрос касается мира, маршрутов, сервера, входа, выхода или POI."),
}


@dataclass(frozen=True)
class Route:
    path: Path
    group: str
    order: int
    summary: str
    read_when: str


def routes_for(root: Path, domain: str) -> list[Route]:
    routes: list[Route] = []
    base = root / domain
    if not base.exists():
        return routes
    for path in base.rglob("*.md"):
        if path.name == "00_Routes.md":
            continue
        data = parse_frontmatter(path)
        if data.get("status") != ACTIVE or data.get("index_route") != "owner":
            continue
        errors = route_metadata(data)
        if errors:
            raise MetadataError(f"{path.relative_to(root)}: {'; '.join(errors)}")
        order = data["index_order"]
        routes.append(Route(path, str(data["index_group"]), order, str(data["index_summary"]), str(data["read_when"])))
    return sorted(routes, key=lambda route: (route.order, route.group, route.path.as_posix()))


def render_domain(root: Path, domain: str) -> str:
    title = DOMAINS[domain][0]
    lines = [
        "---", "type: index", "system: navigation", "status: active", "generated: true", "---", "",
        f"# {title}: маршруты", "",
        "> Эта страница строится `python tools/build_routes.py --write`. Не редактируйте блоки маршрутов вручную.", "",
    ]
    routes = routes_for(root, domain)
    current_group: str | None = None
    for route in routes:
        if route.group != current_group:
            current_group = route.group
            lines.extend([f"## {current_group.replace('_', ' ')}", ""])
        relative = route.path.relative_to(root).with_suffix("").as_posix()
        lines.append(f"- [[{relative}]] — {route.summary} **Читать когда:** {route.read_when}")
    if not routes:
        lines.extend(["## Нет маршрутов", "", "Нет страниц с `index_route: owner`."])
    return "\n".join(lines) + "\n"


def render_root(root: Path) -> str:
    lines = [
        "---", "type: index", "system: navigation", "status: active", "generated: true", "---", "",
        "# Элдрейн — маршрутизатор канона", "",
        "**Локальная правка (Bounded):** маршрут → owner → необходимые прямые зависимости. Для правки конкретного правила или страницы не нужно читать весь vault.", "",
        "**Синтез и архитектура (Synthesis / architecture):** для Feature design, межсистемной архитектуры, причинного исследования, карты зависимостей, рефакторинга ownership или корпуса и разделения Lore ↔ Gameplay можно сначала изучить несколько доменов по задаче. Такой обзор не ограничен прямыми зависимостями и предшествует решениям о владении правилами.", "",
        "## Домены", "",
    ]
    for domain, (title, read_when) in DOMAINS.items():
        if routes_for(root, domain):
            lines.append(f"- [[{domain}/00_Routes|{title}]] — {read_when}")
    lines.extend(["", "## Текущая работа", "", "- [[09_Project_Management/Architecture_MVP|Архитектура MVP]] — когда меняются границы активных систем.", "- [[09_Project_Management/TODO|Открытая работа]] — когда нужна текущая задача или acceptance evidence.", "- [[09_Project_Management/Risk_Register|Реестр рисков]] — когда решение зависит от активного риска."])
    return "\n".join(lines) + "\n"


def build(root: Path) -> None:
    root = root.resolve()
    rendered = {}
    for domain in DOMAINS:
        if (root / domain).exists():
            rendered[root / domain / "00_Routes.md"] = render_domain(root, domain)
    rendered[root / "00_Index.md"] = render_root(root)
    for path, text in rendered.items():
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")


def check(root: Path) -> list[Path]:
    root = root.resolve()
    stale: list[Path] = []
    for domain in DOMAINS:
        path = root / domain / "00_Routes.md"
        if (root / domain).exists() and (not path.exists() or path.read_text(encoding="utf-8") != render_domain(root, domain)):
            stale.append(path)
    root_index = root / "00_Index.md"
    if not root_index.exists() or root_index.read_text(encoding="utf-8") != render_root(root):
        stale.append(root_index)
    return stale


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    try:
        if args.write:
            build(args.root)
            return 0
        stale = check(args.root)
    except MetadataError as exc:
        print(f"INVALID_ROUTE_METADATA: {exc}")
        return 1
    for path in stale:
        print(path)
    return 1 if stale else 0


if __name__ == "__main__":
    raise SystemExit(main())
