import re
import urllib.parse
import urllib.request


class HowStuffWorks:
    domain = "howstuffworks.com"

    def get_article(self, url):
        page_content = get_page(url)
        title = self._get_title(page_content)
        paragraphs = self._get_paragraphs(page_content)
        return {"title": title, "paragraphs": paragraphs}

    def _get_title(self, page_content):
        pattern_title = re.compile('<h1.*?>([\s\S]+?)</h1>')
        title_list = re.findall(pattern_title, page_content)
        for t in title_list:
            if t != "${t.title}":
                return t.strip()

    def _get_paragraphs(self, page_content):
        pattern_paragraph = re.compile('<p>([\s\S]+?)</p>')
        paragraph_list = re.findall(pattern_paragraph, page_content)
        p_list = []
        for p in paragraph_list:
            p_list.append(remove_link(p))
        return p_list


def get_article(url):
    """
    根据url获取文章内容，url可能有后续url，需要各网站独立处理
    :param url:
    :return:
    """
    if HowStuffWorks.domain in url:
        return HowStuffWorks().get_article(url)


def get_page(url):
    """
    提取链接对应的网页内容
    :param url:
    :return:
    """
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    resp = resp.read()
    resp = resp.decode("utf-8")
    return resp


def remove_link(content_contain_link):
    """
    从超链接中提取文字内容
    :param content_contain_link:
    :return:
    """
    pattern_link = re.compile('<a.*?>(.+?)</a>')

    def _link_content(matched):
        return matched.group(1)

    content_no_link = re.sub(pattern_link, _link_content, content_contain_link)
    return content_no_link


if __name__ == '__main__':
    url = "https://science.howstuffworks.com/magnets-and-magnetism-kids.htm"
    # h = HowStuffWorks()
    # h.get_article(url)
    # text = '<a href="https://science.howstuffworks.com/magnet.htm">Magnets</a> lalalalalala <a href="https://science.howstuffworks.com/hello.htm">hello</a>'
    # remove_link(text)

    article = get_article(url)
    print(article["title"])
    paragraphs = article["paragraphs"]
    for p in paragraphs:
        print(p)