#!/usr/bin/env python3
"""職場Ikigai（招募轉介紹月報）：發佈同存檔。

用法（喺 repo 根目錄）：
    python3 tools/publish.py YYYY-MM

先將今期放喺 issues/YYYY-MM.html，預覽圖放喺 issues/og/YYYY-MM.png，再跑上面指令。佢會：
1. 將今期複製做首頁 index.html（固定網址 https://ahwai79.github.io/ikigai/），
   預覽圖複製做 og.png，WhatsApp 預覽改用固定網址同固定圖。
2. 每期存檔頁（issues/YYYY-MM.html）保留自己嘅網址同圖，舊期加「存檔」提示。
3. 重做往期目錄 issues/index.html（新到舊）。
重複跑都安全。只想重做目錄：python3 tools/publish.py --index
"""
import html
import re
import shutil
import sys
from pathlib import Path

BASE = "https://ahwai79.github.io/ikigai/"
IBASE = BASE + "issues/"
ROOT = Path(__file__).resolve().parent.parent
CAREER = ROOT / "issues"
OG = CAREER / "og"

ARCH_RE = re.compile(r'  <!-- archive-banner -->\n  <div class="arch">.*?</div>\n', re.S)
ARCH_CSS = ('<style id="archive-css">.arch{background:#f4efe7;color:#161616;border:1px solid #dfe6e2;'
            'border-radius:12px;padding:10px 14px;font-size:14px;line-height:1.6}'
            '.arch a{color:#05414c;font-weight:700}</style>')
ARCH_CSS_RE = re.compile(r'<style id="archive-css">.*?</style>\n?', re.S)


def stems():
    return sorted(f.stem for f in CAREER.glob("????-??.html")) if CAREER.exists() else []


def meta(page: str):
    m = re.search(r'<div class="issue">([^<]*)</div>', page)
    t = re.search(r"<h1[^>]*>(.*?)</h1>", page, re.S)
    return (m.group(1).strip() if m else ""), (re.sub(r"<[^>]+>", "", t.group(1)).strip() if t else "")


def set_og(page: str, url: str, img: str) -> str:
    page = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', page, count=1)
    return re.sub(r'<meta property="og:image" content="[^"]*">', f'<meta property="og:image" content="{img}">', page, count=1)


def stamp(stem: str, latest: str):
    path = CAREER / f"{stem}.html"
    page = ARCH_CSS_RE.sub("", ARCH_RE.sub("", path.read_text(encoding="utf-8")))
    page = set_og(page, f"{IBASE}{stem}.html", f"{IBASE}og/{stem}.png")
    if stem != latest:
        issue, _ = meta(page)
        page = page.replace("</head>", ARCH_CSS + "\n</head>", 1)
        banner = ('  <!-- archive-banner -->\n'
                  f'  <div class="arch">存檔頁｜{html.escape(issue)}。數字只反映當時情況。'
                  f'<a href="{BASE}">看最新一期 →</a>　<a href="{IBASE}">往期目錄</a></div>\n')
        page = page.replace('<div class="wrap">\n', '<div class="wrap">\n' + banner, 1)
    path.write_text(page, encoding="utf-8")


def thumb(stem: str) -> bool:
    src, dst = OG / f"{stem}.png", OG / f"{stem}-s.jpg"
    if not src.exists():
        return False
    if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
        from PIL import Image
        im = Image.open(src).convert("RGB")
        im.thumbnail((600, 315))
        im.save(dst, "JPEG", quality=82, optimize=True)
    return True


def build_index():
    all_stems = stems()
    latest = all_stems[-1] if all_stems else None
    cards = []
    for stem in reversed(all_stems):
        issue, title = meta((CAREER / f"{stem}.html").read_text(encoding="utf-8"))
        href = BASE if stem == latest else f"{stem}.html"
        img = (f'<img src="og/{stem}-s.jpg" alt="" loading="lazy" width="600" height="315">'
               if thumb(stem) else '<div class="noimg"></div>')
        tag = '<span class="new">最新</span>' if stem == latest else ""
        cards.append(f'    <a class="card" href="{href}">{img}<div class="body"><div class="meta">{tag}'
                     f'{html.escape(issue)}</div><div class="t">{html.escape(title)}</div></div></a>')
    page = f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="職場Ikigai 往期目錄：每月一個職場數字。">
<meta property="og:type" content="website">
<meta property="og:title" content="職場Ikigai｜往期目錄">
<meta property="og:description" content="每月一個職場數字，之前每一期都可以重溫。">
<meta property="og:url" content="{IBASE}">
<meta property="og:image" content="{BASE}og.png">
<title>職場Ikigai｜往期目錄</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&display=swap">
<style>
body{{margin:0;background:#fbf9f9;color:#161616;font-family:"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;line-height:1.7}}
.wrap{{max-width:660px;margin:0 auto;padding:24px 16px 44px;display:flex;flex-direction:column;gap:16px}}
h1{{margin:0;font-size:28px;font-weight:900}}
.lead{{margin:0;color:#566468}}
.card{{display:block;background:#fff;border:1px solid #dfe6e2;border-radius:16px;overflow:hidden;color:inherit;text-decoration:none}}
.card img,.noimg{{display:block;width:100%;height:auto;aspect-ratio:1200/630;background:#05414c}}
.body{{padding:12px 16px 14px}}
.meta{{font-size:13px;color:#566468;display:flex;gap:8px;align-items:center}}
.new{{flex:none;white-space:nowrap;background:#05414c;color:#ffffff;border-radius:999px;padding:0 10px;font-size:12px;font-weight:700}}
.t{{font-size:18px;font-weight:700;margin-top:2px}}
.card:focus-visible{{outline:3px solid #e6b65a;outline-offset:2px}}
a.back{{color:#05414c;font-weight:700}}
</style>
</head>
<body>
<div class="wrap">
  <h1>職場Ikigai｜往期目錄</h1>
  <p class="lead">每月一個職場數字，陪你想清楚下一步。</p>
{chr(10).join(cards)}
  <a class="back" href="{BASE}">← 看最新一期</a>
</div>
</body>
</html>
"""
    (CAREER / "index.html").write_text(page, encoding="utf-8")


def publish(stem: str):
    src = CAREER / f"{stem}.html"
    if not src.exists():
        sys.exit(f"搵唔到 issues/{stem}.html")
    latest = stems()[-1]
    for s in stems():
        stamp(s, latest)
    page = ARCH_CSS_RE.sub("", ARCH_RE.sub("", (CAREER / f"{latest}.html").read_text(encoding="utf-8")))
    (ROOT / "index.html").write_text(set_og(page, BASE, f"{BASE}og.png"), encoding="utf-8")
    if (OG / f"{latest}.png").exists():
        shutil.copyfile(OG / f"{latest}.png", ROOT / "og.png")
    build_index()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--index":
        build_index()
    else:
        publish(sys.argv[1])
    print("done")
