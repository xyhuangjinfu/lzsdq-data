import os.path

import page_crawler
import translate_youdao


def create(url):
    article_en = page_crawler.get_article(url)

    paragraphs_en = article_en["paragraphs"]
    paragraphs_zh = []
    for p_en in paragraphs_en:
        sentences_zh = []
        for s_en in p_en:
            s_zh = translate_youdao.en2zh(s_en)
            sentences_zh.append(s_zh)
        paragraphs_zh.append(sentences_zh)

    article_zh = {}
    article_zh["title"] = translate_youdao.en2zh(article_en["title"])
    article_zh["paragraphs"] = paragraphs_zh

    return write_contrast(article_en, article_zh)


def write_contrast(article_en, article_zh):
    dir_path = os.path.join("output", "article_contrast")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    out_file_path = os.path.join(dir_path, f"{article_zh['title']}.txt")

    fp = open(out_file_path, "w+", encoding="utf-8")
    fp.seek(0)
    fp.truncate()

    fp.write(article_en["title"])
    fp.write("\n")
    fp.write(article_zh["title"])
    fp.write("\n")
    fp.write("\n")

    for p_idx in range(0, len(article_en["paragraphs"])):
        for s_idx in range(0, len(article_en["paragraphs"][p_idx])):
            fp.write(article_en["paragraphs"][p_idx][s_idx])
            fp.write("\n")
            fp.write(article_zh["paragraphs"][p_idx][s_idx])
            fp.write("\n")
        fp.write("\n")

    fp.close()

    return out_file_path


if __name__ == '__main__':
    out_path = create("https://science.howstuffworks.com/magnets-and-magnetism-kids.htm")
    print(f"对比成功：{out_path}")
