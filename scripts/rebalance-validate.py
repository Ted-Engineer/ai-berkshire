#!/usr/bin/env python3
"""
portfolio-rebalance 执行质量验证脚本（harness）
用法: python3 scripts/rebalance-validate.py [stage]
  stage: 0-5 或 "all"（默认all）

检查 .claude/.workflow/ 目录状态 + reports/ 输出，判定执行是否合规。
输出 JSON: {"stage": N, "pass": bool, "violations": [...], "warnings": [...]}
"""
import sys, os, json, glob
from pathlib import Path
from datetime import datetime

def _force_utf8_stdio():
    """Windows GBK 控制台下 verdict 字符串里的 ✅/🔴 会抛 UnicodeEncodeError。"""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass

_force_utf8_stdio()

REPO = Path(__file__).resolve().parent.parent
WF = REPO / ".claude" / ".workflow"
REPORTS = REPO / "reports"
CONFIG = REPO / "config"

def today():
    return datetime.now().strftime("%Y%m%d")

def read_file(p):
    try:
        return Path(p).read_text(encoding="utf-8")
    except:
        return ""

def check_stage_0():
    """预检：环境就绪 + 温度判定完成"""
    v, w = [], []
    # 配置文件存在
    for f in ["portfolio-targets.md", "search-matrix.md"]:
        if not (CONFIG / f).exists():
            v.append(f"config/{f} 不存在")
    # workflow激活
    if not (WF / "active").exists():
        v.append(".claude/.workflow/active 不存在（workflow未激活）")
    # 温度文件（搜索当天或最近）
    temp_files = (glob.glob(str(WF / "market-temperature-*.txt"))
                  + glob.glob(str(WF / "step0-temperatures-*.md")))
    if not temp_files:
        w.append("未找到 market-temperature-*.txt / step0-temperatures-*.md（市场温度未判定？）")
    # candidates.csv存在
    if not (WF / "candidates.csv").exists():
        w.append("candidates.csv 不存在")
    return v, w

def check_stage_1():
    """持仓核实"""
    v, w = [], []
    pl = REPORTS / "portfolio-latest.md"
    if not pl.exists():
        v.append("reports/portfolio-latest.md 不存在")
    return v, w

def check_stage_2():
    """持仓分析：逐只验证4个Agent的产出证据。

    skill-tracker-hook 写入的 .done 文件只含 {skill,args,timestamp}，
    不含 Agent ID，因此证据检查看 reports/ 下的四维产出文件：
    reports/investment-team-batch/<date>/{TICKER}-{business,financial,industry,risk}.md
    或旧版 reports/{TICKER}/0[1-4]-*.md。
    """
    v, w = [], []
    done_files = glob.glob(str(WF / f"investment-team-*-{today()}.done"))
    if not done_files:
        done_files = glob.glob(str(WF / "investment-team-*.done"))
    if not done_files:
        v.append("未找到任何 investment-team-*.done 文件")
        return v, w

    for f in done_files:
        stem_parts = Path(f).stem.split("-")
        ticker = stem_parts[2] if len(stem_parts) > 2 and stem_parts[2] else ""
        if not ticker or not ticker.isascii():
            w.append(f"{Path(f).stem}: .done 文件名中无法解析出 ticker，跳过产出检查")
            continue
        dim_files = (glob.glob(str(REPORTS / "investment-team-batch" / "*" / f"{ticker}-*.md"))
                     + glob.glob(str(REPORTS / ticker / "0[1-4]-*.md")))
        if len(dim_files) < 4:
            v.append(f"{ticker}: 四维产出文件不足4个（找到{len(dim_files)}个，退化违规！）")
    return v, w

def check_stage_3():
    """候选扫描：数量+搜索次数+来源覆盖"""
    v, w = [], []
    # candidates数量
    csv_path = WF / "candidates.csv"
    if csv_path.exists():
        lines = csv_path.read_text().strip().split("\n")
        count = len(lines) - 1  # 减去header
        if count < 300:
            w.append(f"candidates.csv 仅{count}只（目标≥300）")
    else:
        v.append("candidates.csv 不存在")
    
    # 搜索次数
    log_path = WF / "search-log.txt"
    if log_path.exists():
        lines = log_path.read_text().strip().split("\n")
        count = len([l for l in lines if l.strip()])
        if count < 120:
            w.append(f"search-log.txt 仅{count}次搜索（目标≥120）")
    else:
        v.append("search-log.txt 不存在")
    
    # 搜索工具 used 标记（search-tracker-hook 写入的任意 *.used）
    if not glob.glob(str(WF / "*.used")):
        w.append("未找到搜索工具 *.used 标记")
    
    # 来源H和I的.done
    h_done = glob.glob(str(WF / "*爆发*")) + glob.glob(str(WF / "*sourceH*"))
    i_done = glob.glob(str(WF / "*修复*")) + glob.glob(str(WF / "*sourceI*"))
    if not h_done:
        w.append("未找到来源H（爆发股猎手）执行标记")
    if not i_done:
        w.append("未找到来源I（估值修复猎手）执行标记")
    return v, w

def check_stage_4():
    """冒泡排序：终选评分须统一来自 /investment-team 框架并标注来源"""
    v, w = [], []
    reports = sorted(glob.glob(str(REPORTS / "portfolio-action-*.md")))
    if not reports:
        return v, w  # stage 5 会报缺失
    content = read_file(reports[-1])
    if "investment-team" not in content:
        w.append("最终报告未标注评分来源'基于/investment-team'（冒泡排序终选须统一使用四大师框架评分）")
    return v, w

def check_stage_5():
    """最终报告验证"""
    v, w = [], []
    # 找当天的action报告
    reports = glob.glob(str(REPORTS / f"portfolio-action-{today()}*.md"))
    if not reports:
        reports = glob.glob(str(REPORTS / "portfolio-action-*.md"))
    if not reports:
        v.append("未找到 portfolio-action-*.md 报告")
        return v, w
    
    content = read_file(sorted(reports)[-1])  # 取最新
    
    # 必须包含的段落
    required = ["行业分布对比", "执行清单", "执行顺序", "预期回报", "风险管理", "推荐验证矩阵"]
    for section in required:
        if section not in content:
            v.append(f"报告缺少'{section}'段落")
    
    # 集中度检查
    if "集中度" not in content and "top" not in content.lower():
        w.append("报告未包含集中度检查")
    
    # 校验行
    if "校验" not in content and "100.0%" not in content:
        w.append("报告未包含分布合计校验行")
    
    # recommended-buys.txt
    rb = WF / "recommended-buys.txt"
    if not rb.exists():
        w.append("recommended-buys.txt 不存在")
    
    return v, w

STAGES = {
    0: ("预检：环境+温度", check_stage_0),
    1: ("持仓核实", check_stage_1),
    2: ("持仓分析（4Agent反退化）", check_stage_2),
    3: ("候选扫描（数量+搜索+来源）", check_stage_3),
    4: ("冒泡排序", check_stage_4),
    5: ("最终报告", check_stage_5),
}

def main():
    stage_arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    
    results = []
    if stage_arg == "all":
        stages_to_run = range(6)
    else:
        stages_to_run = [int(stage_arg)]
    
    total_v, total_w = [], []
    for s in stages_to_run:
        name, func = STAGES[s]
        v, w = func()
        total_v.extend([f"[Stage {s}] {x}" for x in v])
        total_w.extend([f"[Stage {s}] {x}" for x in w])
        results.append({"stage": s, "name": name, "violations": len(v), "warnings": len(w)})
    
    output = {
        "timestamp": datetime.now().isoformat(),
        "pass": len(total_v) == 0,
        "summary": results,
        "violations": total_v,
        "warnings": total_w,
        "verdict": "✅ PASS" if not total_v else f"🔴 BLOCK ({len(total_v)} violations)"
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    
    if total_v:
        sys.exit(1)

if __name__ == "__main__":
    main()
