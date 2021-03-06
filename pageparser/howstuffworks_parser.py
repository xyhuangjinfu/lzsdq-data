from bs4 import BeautifulSoup
from bs4 import Tag

import page_crawler
import sentence_spliter


def is_my_domain(url):
    domain = "howstuffworks.com"
    return domain in url


def get_article_by_url(url):
    return get_article(page_crawler.get_page(url))


def get_article(page_html):
    title = None
    paragraphs = []

    soup = BeautifulSoup(page_html, 'html.parser')

    h1_list = soup.findAll("h1")
    for h1 in h1_list:
        title = h1.get_text().strip()

    div_list = soup.findAll("div")

    page_body_div_list = []
    for div in div_list:
        attrs = div.attrs
        if "class" in attrs:
            if "page-body" in attrs["class"]:
                page_body_div_list.append(div)

    for div in page_body_div_list:
        for child in div.children:
            if type(child) is Tag:
                if child.name == "p":
                    paragraph = child.get_text()
                    _add_paragraph(paragraphs, paragraph)
                    continue
                if child.name == "div":
                    if "class" in child.attrs and "list" in child.attrs["class"]:
                        for ul in child.children:
                            for li in ul.children:
                                paragraph = li.get_text()
                                _add_paragraph(paragraphs, paragraph)
                        continue
                    if "class" in child.attrs and "blockquote" in child.attrs["class"]:
                        paragraph = child.get_text()
                        _add_paragraph(paragraphs, paragraph)
                        continue

    return {"title": title, "paragraphs": paragraphs}


def _add_paragraph(paragraphs, paragraph):
    if paragraph:
        sentences = sentence_spliter.split(paragraph)
        if sentences and len(sentences) > 0:
            paragraphs.append(sentences)


if __name__ == '__main__':
    # url = "https://science.howstuffworks.com/magnets-and-magnetism-kids.htm"
    url = "https://science.howstuffworks.com/magnet.htm"
    a = get_article(page_crawler.get_page(url))

    for p in a["paragraphs"]:
        for s in p:
            print(s, end="\n")
        print()
