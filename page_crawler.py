import os.path
import urllib.parse
import urllib.request

import cache_util
import pageparser.howstuffworks_parser as howstuffworks_parser
import pageparser.livescience_parser as livescience_parser
import root_dir_util


def get_article(url):
    """
    根据url获取文章内容，url可能有后续url，需要各网站独立处理
    :param url:
    :return:
    """
    if howstuffworks_parser.is_my_domain(url):
        return howstuffworks_parser.get_article_by_url(url)
    if livescience_parser.is_my_domain(url):
        return livescience_parser.get_article_by_url(url)


def get_page(url):
    """
    提取链接对应的网页内容
    :param url:
    :return:
    """
    cache_name = url.replace("//", "-").replace(":", "-").replace("/", "-")
    cache_path = os.path.join(root_dir_util.get_root_dir(), "cache", cache_name)

    cache_content = cache_util.read(cache_path)
    if cache_content:
        return cache_content

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)

    if resp.getcode() != 200:
        return None

    resp = resp.read()
    resp = resp.decode("utf-8")

    cache_util.write(cache_path, resp)

    return resp


if __name__ == '__main__':
    # url = "https://science.howstuffworks.com/magnets-and-magnetism-kids.htm"
    url = "https://science.howstuffworks.com/magnet.htm"
    # h = HowStuffWorks()
    # h.get_article(url)
    # text = '<a href="https://science.howstuffworks.com/magnet.htm">Magnets</a> lalalalalala <a href="https://science.howstuffworks.com/hello.htm">hello</a>'
    # remove_link(text)

    # article = get_article(url)
    # print(article["title"])
    # paragraphs = article["paragraphs"]
    # for p in paragraphs:
    #     print(p)

    print(get_page(url))
