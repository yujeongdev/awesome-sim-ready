#!/usr/bin/env python3
"""Lightweight validation for the awesome-sim-ready repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "docs/asset-qa-checklist.md",
    "docs/reading-path.md",
]

README_REQUIRED_TEXT = [
    "Awesome Sim-Ready 3D Asset Generation",
    "Aim of the Project",
    "What is a Sim-Ready Asset",
    "Legend",
    "Must Read First",
    "End-to-End Sim-Ready Asset Generation",
    "Articulated Object Generation and Reconstruction",
    "Physics, Materials, and Dynamics Grounding",
    "Datasets and Benchmarks",
    "Evaluating Sim-Ready Assets",
    "Thanks",
]

FORBIDDEN_README_TEXT = [
    "Related Awesome Lists",
    "Toolchains and Simulator Formats",
]


def strip_fenced_code(text: str) -> str:
    output: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            output.append(line)
    return "\n".join(output)


def slugify_heading(heading: str) -> str:
    """Approximate GitHub's Markdown heading anchor generation for this repo."""
    heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
    heading = re.sub(r"[`*_~]", "", heading)
    heading = re.sub(r"[^a-z0-9가-힣 _-]", "", heading)
    heading = re.sub(r"\s+", "-", heading)
    return heading.strip("-")


def anchors_for(path: Path) -> set[str]:
    text = strip_fenced_code(path.read_text(encoding="utf-8"))
    anchors = set(re.findall(r"<a\s+id=[\"']([^\"']+)[\"']", text))
    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            anchor = slugify_heading(match.group(2))
            if anchor:
                anchors.add(anchor)
    return anchors


def iter_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )


def check_required_files(errors: list[str]) -> None:
    for rel_path in REQUIRED_FILES:
        path = ROOT / rel_path
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty required file: {rel_path}")


def check_readme(errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for text in README_REQUIRED_TEXT:
        if text not in readme:
            errors.append(f"README missing required text: {text}")
    for text in FORBIDDEN_README_TEXT:
        if text in readme:
            errors.append(f"README contains removed broad section: {text}")
    if readme.count("*Why engineers care:*") < 15:
        errors.append("README should include at least 15 resources with 'Why engineers care' notes")
    for tag in ["[G]", "[A]", "[P]", "[F]", "[V]"]:
        if tag not in readme:
            errors.append(f"README missing capability tag: {tag}")


def check_internal_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    anchor_cache: dict[Path, set[str]] = {}
    for path in iter_markdown_files():
        text = strip_fenced_code(path.read_text(encoding="utf-8"))
        for match in link_pattern.finditer(text):
            url = match.group(1)
            if "://" in url or url.startswith("mailto:"):
                continue
            target, _, fragment = url.partition("#")
            target_path = path if not target else path.parent / target
            if target and not target_path.exists():
                errors.append(f"{path.relative_to(ROOT)} links to missing file: {url}")
                continue
            if fragment:
                resolved_target_path = target_path.resolve()
                if resolved_target_path not in anchor_cache:
                    anchor_cache[resolved_target_path] = anchors_for(resolved_target_path)
                if fragment not in anchor_cache[resolved_target_path]:
                    errors.append(
                        f"{path.relative_to(ROOT)} links to missing anchor #{fragment} in "
                        f"{resolved_target_path.relative_to(ROOT)}"
                    )


def check_trailing_whitespace(errors: list[str]) -> None:
    for path in iter_markdown_files() + sorted((ROOT / ".github").rglob("*.yml")):
        for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"{path.relative_to(ROOT)}:{idx}: trailing whitespace")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_readme(errors)
    check_internal_markdown_links(errors)
    check_trailing_whitespace(errors)
    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
