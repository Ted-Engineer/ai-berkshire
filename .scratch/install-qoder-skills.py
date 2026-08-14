#!/usr/bin/env python3
"""把 ai-berkshire 项目里的全部 skill 安装到 Qoder (~/.qoder/skills)。

安装来源（三类）：
1. skills/<dir>/SKILL.md   —— 目录型 skill，整目录复制（含 agents/、scripts/ 等配套）
2. skills/<name>.md        —— 单文件投研 skill（Claude command 格式，无 frontmatter），
                              生成 ~/.qoder/skills/<name>/SKILL.md，补上标准 YAML frontmatter
3. codex-skills/investment-memo-craft —— Codex-only 手写包（无同名 skills/ 源），整目录复制
"""

import os
import re
import shutil
import sys
from pathlib import Path

REPO = Path("/Users/liuyucheng/IdeaProjects/ai-berkshire")
QODER_SKILLS = Path.home() / ".qoder" / "skills"

installed, skipped, errors = [], [], []


def first_h1(text: str) -> str:
    for line in text.splitlines():
        m = re.match(r"^#\s+(.+)$", line)
        if m:
            return m.group(1).strip()
    return ""


def ensure_frontmatter(skill_md: Path, name: str) -> None:
    """确保 SKILL.md 有合法的 name/description frontmatter，没有则补上。"""
    content = skill_md.read_text(encoding="utf-8")
    if content.startswith("---\n") and "\n---\n" in content[4:]:
        head = content[: content.index("\n---\n", 4)]
        if re.search(r"^name:\s*\S+", head, re.M) and re.search(r"^description:\s*\S+", head, re.M):
            return
    title = first_h1(content) or name
    fm = f"---\nname: {name}\ndescription: \"AI Berkshire skill: {title}.\"\n---\n\n"
    skill_md.write_text(fm + content, encoding="utf-8")


def install_dir_skill(src: Path, name: str) -> None:
    dst = QODER_SKILLS / name
    if dst.is_symlink():
        target = os.path.realpath(dst)
        if os.path.realpath(src) == target:
            # 已通过符号链接安装且指向正确源，仅需确保 frontmatter 合法
            skill_md = dst / "SKILL.md"
            if skill_md.exists():
                ensure_frontmatter(skill_md, name)
                skipped.append(name)
                return
        dst.unlink()
    elif dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    ensure_frontmatter(dst / "SKILL.md", name)
    installed.append(name)


def install_standalone(md: Path) -> None:
    name = md.stem
    body = md.read_text(encoding="utf-8")
    title = first_h1(body) or name
    dst_dir = QODER_SKILLS / name
    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    dst_dir.mkdir(parents=True)
    fm = f"---\nname: {name}\ndescription: \"AI Berkshire skill: {title}. Source: skills/{md.name}.\"\n---\n\n"
    (dst_dir / "SKILL.md").write_text(fm + body, encoding="utf-8")
    installed.append(name)


def main() -> int:
    if not QODER_SKILLS.exists():
        errors.append(f"Qoder skills 目录不存在: {QODER_SKILLS}")
        return 1

    # 1. 目录型 skill：skills/<dir>/SKILL.md
    for d in sorted((REPO / "skills").iterdir()):
        if d.is_dir() and (d / "SKILL.md").exists():
            try:
                install_dir_skill(d, d.name)
            except Exception as e:  # noqa: BLE001
                errors.append(f"{d.name}: {e}")
        elif d.is_dir():
            errors.append(f"目录型 skill 缺少 SKILL.md: skills/{d.name}")

    # 2. 单文件投研 skill：skills/<name>.md
    for md in sorted((REPO / "skills").glob("*.md")):
        try:
            install_standalone(md)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{md.stem}: {e}")

    # 3. Codex-only 手写包（无同名 skills/ 源）
    memo = REPO / "codex-skills" / "investment-memo-craft"
    if (memo / "SKILL.md").exists():
        try:
            install_dir_skill(memo, "investment-memo-craft")
        except Exception as e:  # noqa: BLE001
            errors.append(f"investment-memo-craft: {e}")
    else:
        errors.append("缺少 codex-skills/investment-memo-craft/SKILL.md")

    print(f"安装成功: {len(installed)} 个")
    for n in installed:
        print(f"  ✓ {n}")
    if skipped:
        print(f"已是最新（符号链接指向正确源）: {len(skipped)} 个")
        for n in skipped:
            print(f"  ↺ {n}")
    if errors:
        print(f"错误: {len(errors)} 个", file=sys.stderr)
        for e in errors:
            print(f"  ✗ {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
