import re
import urllib.request

import db


# def parse_


def parse_chazidian(url):
    """
    https://www.chazidian.com
    :param url:
    :return:
    """
    resp = urllib.request.urlopen(url)
    html = resp.read().decode("utf-8")
    reg_ignore = re.compile("\r|\n|\t")
    html = re.sub(reg_ignore, "", html)

    reg_title = re.compile("""<span id="print_title">(.+?)</span>""")
    data = re.findall(reg_title, html)
    title = data[0]

    reg_paragraphs_div = re.compile("""<div id="print_content">(.+?)</div>""")
    data = re.findall(reg_paragraphs_div, html)
    paragraphs_div = data[0]

    reg_paragraph = re.compile("""<p>(.+?)</p>""")
    data = re.findall(reg_paragraph, paragraphs_div)
    paragraphs = data

    return {"title": title, "paragraphs": paragraphs}


if __name__ == '__main__':
    url = "https://www.chazidian.com/kepu_9329/"
    article = parse_chazidian(url)

    print(article["title"])
    print(article["paragraphs"])

    success = db.add_article(article["title"], article["paragraphs"])
    print(f"success {success}")
