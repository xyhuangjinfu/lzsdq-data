
import re

fp = open("tutorial/pages/www.kepuchina.cn.html", encoding="utf-8")
content = fp.read()
fp.close()

pattern_href = re.compile("href=\"(.+?)\"")
urls = re.findall(pattern_href, content)
x = []
for u in urls:
    if not u.startswith("http"):
        continue
    if u.endswith("css") or u.endswith("js"):
        continue
    x.append(u)
for i in x:
    print(i)