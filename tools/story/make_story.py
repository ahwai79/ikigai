"""Build the three IG Story frames (1080x1920) for 2026-12."""
from pathlib import Path

P = Path(__file__).parent
SHAPE = (P / "shape2.txt").read_text(encoding="utf-8")


def mark(fill, cls="", extra=""):
    if cls != "deco":
        return ""
    return f'<svg class="deco" viewBox="0 0 247 207" aria-hidden="true"><path fill="{fill}" d="{SHAPE}"/></svg>'


HEAD = """<!doctype html><html lang="zh-Hant-HK"><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>
.board{width:1080px;height:1920px;padding:220px 96px 250px;display:flex;flex-direction:column}
.tag{font-size:28px;border-radius:999px;padding:8px 24px;align-self:flex-start}
.tag svg{width:36px;height:36px}
.page{font-size:24px;letter-spacing:2px}
.top{display:flex;justify-content:space-between;align-items:center}
.src{font-size:20px;line-height:1.55}
%s
</style></head><body>"""

# Frame 1: hook
f1 = HEAD % """
.board{background:var(--green);color:var(--white)}
.deco{right:-280px;bottom:200px;width:860px;height:720px;opacity:.14}
.tag{border:2px solid rgba(255,255,255,.55)}
.page{color:var(--sage)}
h1{margin:120px 0 0;font-size:118px;font-weight:900;line-height:1.12}
.n{margin-top:40px;font-size:300px;font-weight:800;line-height:.9;color:var(--sage);letter-spacing:-10px}
.cap{margin-top:28px;font-size:44px;font-weight:700;line-height:1.4}
.chip{margin-top:56px;align-self:flex-start;background:var(--white);color:var(--green);border-radius:24px;padding:26px 34px;display:flex;align-items:baseline;gap:18px}
.chip b{font-size:72px;font-weight:800}
.chip span{font-size:34px;font-weight:700}
.next{margin-top:auto;font-size:34px;font-weight:700;color:var(--sage)}
.src{margin-top:24px;color:rgba(255,255,255,.7)}
""" + f"""<div class="board">{mark('#d4e0d9','deco')}
<div class="top"><div class="tag">{mark('#fbf9f9')}職場Ikigai｜阿維</div><div class="page">1 / 3</div></div>
<h1>明年人工<br>加幾多？</h1>
<div class="n num">1.44%</div>
<div class="cap">僱主估 2027 年平均加人工</div>
<div class="chip"><span>今年通脹預測</span><b class="num">約 1.9%</b></div>
<div class="next">人工追唔追得上物價？→</div>
<div class="src">資料來源：Jobsdb《2027 招聘、薪酬及福利調查報告》（2026年10月）；政府經濟顧問辦公室（2026年11月）</div>
</div></body></html>"""

# Frame 2: poll (leave space for IG poll sticker)
f2 = HEAD % """
.board{background:var(--sand);color:var(--black)}
.tag{border:2px solid var(--green);color:var(--green)}
.page{color:var(--green)}
.lead{margin-top:110px;font-size:40px;font-weight:700;color:var(--green);line-height:1.45}
.stat{margin-top:36px;display:flex;gap:24px}
.stat div{flex:1;background:var(--white);border-radius:24px;padding:30px 30px 28px}
.stat b{display:block;font-size:92px;font-weight:800;line-height:1;color:var(--green)}
.stat span{display:block;margin-top:12px;font-size:30px;line-height:1.4;color:var(--ink-soft)}
.note{margin-top:28px;font-size:32px;line-height:1.55;color:var(--ink-soft)}
h1{margin:90px 0 0;font-size:96px;font-weight:900;line-height:1.2;color:var(--navy)}
.space{flex:1}
.src{color:var(--muted)}
""" + f"""<div class="board">
<div class="top"><div class="tag">{mark('#05414c')}職場Ikigai｜阿維</div><div class="page">2 / 3</div></div>
<div class="lead">加薪預算，唔係平均分</div>
<div class="stat"><div><b class="num">11%</b><span>員工攞到最高評級</span></div><div><b class="num">22%</b><span>佢哋分到嘅加薪預算</span></div></div>
<div class="note">表現一般嘅大多數，加幅通常低過「平均」。</div>
<h1>你今年<br>有冇加人工？</h1>
<div class="space"></div>
<div class="src">資料來源：WTW 薪酬預算規劃調查（2026年7月）</div>
</div></body></html>"""

# Frame 3: CTA
f3 = HEAD % """
.board{background:var(--navy);color:var(--white)}
.deco{left:-320px;top:300px;width:860px;height:720px;opacity:.12}
.tag{border:2px solid rgba(255,255,255,.55)}
.page{color:var(--sage)}
h1{margin:150px 0 0;font-size:100px;font-weight:900;line-height:1.22}
.sub{margin-top:40px;font-size:40px;line-height:1.6;color:var(--sage)}
.cta{margin-top:auto;background:var(--sage);color:var(--green);border-radius:32px;padding:52px 56px;display:flex;flex-direction:column;gap:14px}
.cta span{font-size:40px;font-weight:700;line-height:1.4}
.cta b{font-size:96px;font-weight:900;line-height:1.15}
.link{margin-top:32px;font-size:30px;color:var(--sage);line-height:1.5}
""" + f"""<div class="board">{mark('#d4e0d9','deco')}
<div class="top"><div class="tag">{mark('#fbf9f9')}職場Ikigai｜阿維</div><div class="page">3 / 3</div></div>
<h1>收入<br>跟唔跟得上<br>你嘅成長？</h1>
<div class="sub">做咗幾年，想知仲有咩路可以行？</div>
<div class="cta"><span>想了解保險行業嘅發展前景</span><b>DM 我「加薪」</b></div>
<div class="link">睇完整分析：ahwai79.github.io/ikigai</div>
</div></body></html>"""

for name, html in (("story1.html", f1), ("story2.html", f2), ("story3.html", f3)):
    (P / name).write_text(html, encoding="utf-8")
print("built")
