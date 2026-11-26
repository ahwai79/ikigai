"""Insert illustrations into the Story frames (run after make_story.py / weekly frames are written)."""
from pathlib import Path
import illus as I

def put(fn, items):
    p = Path(fn); s = p.read_text(encoding="utf-8")
    s = s.replace("</div></body></html>", "".join(items) + "</div></body></html>", 1)
    p.write_text(s, encoding="utf-8")

# 職場Ikigai
put("story1.html", [
    I.payslip("left:600px;top:270px;width:360px"),
    I.sparkle("left:930px;top:760px;width:64px", I.S),
    I.sparkle("left:880px;top:840px;width:34px", I.S),
    I.price_tag("left:720px;top:1060px;width:270px"),
])
put("story2.html", [
    I.arrow_doodle("left:700px;top:930px;width:250px", I.G),
    I.coins("left:790px;top:1420px;width:200px"),
    I.sparkle("left:740px;top:1420px;width:44px", I.G),
])
put("story3.html", [
    I.chat_bubble("left:650px;top:330px;width:330px", "加薪", I.S, I.G),
    I.phone("left:810px;top:840px;width:170px"),
    I.sparkle("left:600px;top:300px;width:46px", I.S),
])
# 金融週報
put("w1.html", [
    I.storm("left:640px;top:300px;width:360px"),
    I.line_down("left:760px;top:1080px;width:220px", I.S),
])
put("w2.html", [
    I.bars_up("left:96px;top:1470px;width:250px", I.G),
    I.arrow_doodle("left:760px;top:1010px;width:230px", I.G),
    I.anchor("left:830px;top:1460px;width:130px", I.G),
])
put("w3.html", [
    I.calendar("left:700px;top:330px;width:270px"),
    I.sparkle("left:640px;top:310px;width:46px", I.S),
    I.sparkle("left:960px;top:640px;width:30px", I.S),
])
print("ok")
