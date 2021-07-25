import re
import urllib.parse
import urllib.request


def en2zh(content):
    url = "http://m.youdao.com/translate"
    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://m.youdao.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36 Edg/92.0.902.55",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "http://m.youdao.com/translate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    }
    data = {
        "inputtext": content,
        "type": "EN2ZH_CN",
    }
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, urllib.parse.urlencode(data).encode('utf-8'))
    resp = resp.read()
    resp = resp.decode("utf-8")
    pattern_result = re.compile('<ul id="translateResult">\s*<li>(.+)</li>\s*</ul>')
    result_list = re.findall(pattern_result, resp)
    return result_list[0]
