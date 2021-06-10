import db


def parse_txt(txt_path):
    fp = open(txt_path, encoding="utf-8")
    content = fp.read()
    fp.close()
    lines = content.split("\n")

    return {"title": lines[0], "paragraphs": lines[1:]}


if __name__ == '__main__':
    txt_path = "assets/article.txt"
    article = parse_txt(txt_path)

    print(article["title"])
    print(article["paragraphs"])

    success = db.add_article(article["title"], article["paragraphs"])
    print(f"success {success}")
