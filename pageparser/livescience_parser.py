from bs4 import BeautifulSoup
from bs4 import Tag

import page_crawler
import sentence_spliter


def is_my_domain(url):
    domain = "livescience.com"
    return domain in url


def get_article_by_url(url):
    return get_article(page_crawler.get_page(url))


def get_article(page_html):
    title = None
    paragraphs = []

    soup = BeautifulSoup(page_html, 'html.parser')

    h1_tag_list = soup.findAll("h1")
    for h1_tag in h1_tag_list:
        title = h1_tag.get_text()

    div_article_body = None
    div_list = soup.findAll("div")
    for div in div_list:
        if "id" in div.attrs and "article-body" == div.attrs["id"]:
            div_article_body = div
    for child_tag in div_article_body:
        if type(child_tag) is Tag and child_tag.name == "p":
            paragraph = child_tag.get_text()
            if paragraph:
                sentence = sentence_spliter.split(paragraph)
                if sentence and len(sentence) > 0:
                    paragraphs.append(sentence)

    return {"title": title, "paragraphs": paragraphs}


if __name__ == '__main__':
    url = "https://www.livescience.com/can-we-stop-earth-from-heating-up"
    a = get_article(page_crawler.get_page(url))

    print(a["title"])
    for p in a["paragraphs"]:
        for s in p:
            print(s, end="\n")
        print()
