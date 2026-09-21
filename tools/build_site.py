#!/usr/bin/env python3
"""build_site.py — 将 notes/ 下的论文笔记 Markdown 生成为 docs/decoupling/fr3d.html 阅读网页。

用法: python3 tools/build_site.py
依赖: pip3 install markdown
"""
import re
import html
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "notes" / "FR3D_论文阅读笔记.md"
OUT = ROOT / "docs" / "decoupling" / "fr3d.html"
UPDATED = "2026-09-15"

STATS_HTML = '''
<div class="stats">
  <div class="stat"><div class="stat-num">0.178</div><div class="stat-label">KITTI 深度 AbsR ↓<br>t+2.0s · zero-shot 最优</div></div>
  <div class="stat"><div class="stat-num">0.229</div><div class="stat-label">nuScenes 深度 AbsR ↓<br>t+2.5s · zero-shot 最优</div></div>
  <div class="stat"><div class="stat-num">0.403</div><div class="stat-label">KITTI 位姿 ATE ↓<br>t+2.0s（基线 0.626）</div></div>
  <div class="stat"><div class="stat-num">≤1.64%</div><div class="stat-label">静态区域深度漂移 @1s<br>解耦有效性的直接证据</div></div>
</div>'''


def build():
    body = markdown.markdown(
        NOTES.read_text(encoding="utf-8"),
        extensions=["tables", "fenced_code", "sane_lists"],
    )
    # notes/ 中的相对路径 ../docs/images/ 改写为网页相对路径 ../images/
    body = body.replace("../docs/images/", "../images/")
    # “图 + 斜体图注”段落 → 居中 <figure>
    fig_pattern = re.compile(
        r"<p>\s*<img([^>]*?)\s*/>\s*(?:<br\s*/?>\s*)?<em>(.*?)</em>\s*</p>", re.S
    )

    def to_figure(m):
        fig = f'<figure><img{m.group(1)}>'
        if m.group(2):
            fig += f"<figcaption>{m.group(2)}</figcaption>"
        return fig + "</figure>"

    body, n_figs = fig_pattern.subn(to_figure, body)
    body = body.replace("<!--STAT-CARDS-->", STATS_HTML)

    # 目录锚点
    counter: dict = {}
    toc = '<nav class="toc"><div class="toc-title">📑 目录</div><ul>'
    for lvl, content in re.findall(r"<h([23])>(.*?)</h\1>", body, flags=re.S):
        plain = re.sub(r"<[^>]+>", "", content).strip()
        slug = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", plain).strip("-").lower()
        counter[slug] = counter.get(slug, 0) + 1
        if counter[slug] > 1:
            slug = f"{slug}-{counter[slug]}"
        lvl = int(lvl)
        toc += f'<li class="lv{lvl}"><a href="#{slug}">{html.escape(plain)}</a></li>'
        body = body.replace(
            f"<h{lvl}>{content}</h{lvl}>", f'<h{lvl} id="{slug}">{content}</h{lvl}>', 1
        )
    toc += "</ul></nav>"

    page = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FR3D 论文阅读笔记 · 自动驾驶世界模型中的解耦</title>
<style>
  :root {{
    --accent: #1a6d5b; --accent-light: #e6f2ef; --text: #2b2f33;
    --muted: #6b7280; --border: #e5e7eb; --bg: #f7f8f9; --card: #ffffff;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB",
      "Microsoft YaHei", "Segoe UI", Roboto, sans-serif;
    line-height: 1.85; font-size: 16px;
  }}
  header {{
    background: linear-gradient(135deg, #0f3d33 0%, #1a6d5b 60%, #2a9d8f 100%);
    color: #fff; padding: 44px 20px 36px; text-align: center;
  }}
  header h1 {{ margin: 0 0 10px; font-size: 30px; letter-spacing: 1px; }}
  header p {{ margin: 4px 0; opacity: .92; font-size: 15px; }}
  header a {{ color: #ffe9a8; text-decoration: none; border-bottom: 1px dashed rgba(255,233,168,.6); }}
  .wrap {{ display: flex; max-width: 1180px; margin: 28px auto; gap: 24px; padding: 0 16px; align-items: flex-start; }}
  nav.toc {{
    flex: 0 0 268px; position: sticky; top: 20px; background: var(--card);
    border: 1px solid var(--border); border-radius: 12px; padding: 18px 20px; max-height: calc(100vh - 60px); overflow-y: auto;
  }}
  .toc-title {{ font-weight: 700; margin-bottom: 10px; color: var(--accent); }}
  nav.toc ul {{ list-style: none; margin: 0; padding: 0; }}
  nav.toc li {{ margin: 4px 0; }}
  nav.toc li.lv3 {{ padding-left: 16px; }}
  nav.toc a {{ color: var(--text); text-decoration: none; font-size: 13.5px; display: block; border-radius: 6px; padding: 3px 8px; }}
  nav.toc a:hover {{ background: var(--accent-light); color: var(--accent); }}
  main {{
    flex: 1; min-width: 0; background: var(--card); border: 1px solid var(--border);
    border-radius: 12px; padding: 40px 48px 56px;
  }}
  h2 {{
    color: var(--accent); font-size: 22px; margin-top: 2.2em; padding-bottom: 8px;
    border-bottom: 2px solid var(--accent-light);
  }}
  h3 {{ font-size: 18px; margin-top: 1.8em; }}
  blockquote {{
    margin: 1.2em 0; padding: 14px 20px; background: var(--accent-light);
    border-left: 4px solid var(--accent); border-radius: 0 8px 8px 0; color: #14524a;
  }}
  blockquote p {{ margin: 6px 0; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1.2em 0; font-size: 14.5px; }}
  th {{ background: var(--accent-light); color: #14524a; }}
  th, td {{ border: 1px solid var(--border); padding: 9px 12px; text-align: left; vertical-align: top; }}
  tr:nth-child(even) td {{ background: #fafbfc; }}
  code {{
    background: #eef1f3; border-radius: 4px; padding: 2px 6px;
    font-family: "SF Mono", Menlo, Consolas, monospace; font-size: .9em;
  }}
  pre code {{ display: block; padding: 14px; overflow-x: auto; }}
  hr {{ border: none; border-top: 1px solid var(--border); margin: 2em 0; }}
  figure {{
    margin: 26px auto; text-align: center; max-width: 92%;
    background: #fbfcfd; border: 1px solid var(--border); border-radius: 12px; padding: 18px 18px 14px;
  }}
  figure img {{
    display: block; margin: 0 auto; max-width: 100%; height: auto; border-radius: 8px;
  }}
  figcaption {{
    font-size: 13.5px; color: var(--muted); text-align: center; margin-top: 12px; line-height: 1.75;
  }}
  .stats {{
    display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; align-items: stretch; margin: 26px 0 8px;
  }}
  .stat {{
    flex: 1 1 210px; max-width: 260px; text-align: center; padding: 20px 14px 16px;
    background: linear-gradient(180deg, #f2faf7 0%, #ffffff 100%);
    border: 1px solid #d3e8e1; border-radius: 14px;
  }}
  .stat-num {{ font-size: 30px; font-weight: 800; color: var(--accent); letter-spacing: .5px; }}
  .stat-label {{ font-size: 12.5px; color: var(--muted); margin-top: 8px; line-height: 1.65; }}
  .back-top {{ text-align: center; margin-top: 40px; }}
  .back-top a {{
    display: inline-block; padding: 8px 22px; border-radius: 999px; text-decoration: none;
    background: var(--accent); color: #fff; font-size: 14px;
  }}
  footer {{ text-align: center; color: var(--muted); font-size: 13px; padding: 26px 0 40px; }}
  @media (max-width: 900px) {{
    .wrap {{ flex-direction: column; }}
    nav.toc {{ position: static; max-height: none; flex: none; width: 100%; }}
    main {{ padding: 24px 20px 40px; }}
  }}
</style>
</head>
<body>
<header>
  <h1>FR3D 论文阅读笔记</h1>
  <p>Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion</p>
  <p>主题：自动驾驶世界模型中的「解耦」— Ego-Motion 与 World-Motion 的分离</p>
  <p>📖 论文原文：<a href="https://arxiv.org/html/2606.18250v1" target="_blank">arXiv:2606.18250</a> ｜ 📁 <a href="https://github.com/LOIIIIIII/paper-reading" target="_blank">GitHub 仓库</a></p>
</header>
<div style="max-width:1180px;margin:14px auto 0;padding:0 16px;font-size:14px"><a style="color:#1a6d5b;text-decoration:none" href="index.html">← 解耦方向</a> · <a style="color:#1a6d5b;text-decoration:none" href="../index.html">研究方向首页</a></div>
<div class="wrap">
{toc}
<main>
{body}
<div class="back-top"><a href="#">↑ 回到顶部</a></div>
</main>
</div>
<footer>FR3D Paper Reading Notes · 更新于 {UPDATED} · 由 LiMin xue 整理</footer>
</body>
</html>"""

    OUT.write_text(page + "\n", encoding="utf-8")
    n_stats = page.count('class="stat"')
    print(f"OK: {OUT} | figures={page.count('<figure>')} stats={n_stats} imgs={page.count('<img')}")


if __name__ == "__main__":
    build()
