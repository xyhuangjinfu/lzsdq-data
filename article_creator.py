import argparse
import os.path
import re

import page_crawler
import translate_youdao


def create(url, translate):
    print("------------------------------------------------------------------------------------------------")
    print(f"工作链接: {url}   翻译：{translate}")
    article_en = page_crawler.get_article(url)
    if article_en:
        print("原文获取成功")
    else:
        print("原文获取失败")
        return

    if not translate:
        print("不翻译，退出")
        return

    paragraphs_en = article_en["paragraphs"]
    paragraphs_zh = []
    for p_en in paragraphs_en:
        sentences_zh = []
        for s_en in p_en:
            s_zh = translate_youdao.en2zh(s_en)
            sentences_zh.append(s_zh)
        paragraphs_zh.append(sentences_zh)

    article_zh = {"title": translate_youdao.en2zh(article_en["title"]),
                  "paragraphs": paragraphs_zh}
    print("翻译获取成功")

    contrast_path = write_contrast(article_en, article_zh)
    zh_path = write_zh(article_zh)
    print(f"中英对比文件：{contrast_path}")
    print(f"中文翻译文件：{zh_path}")

    return contrast_path, zh_path


def write_zh(article_zh):
    dir_path = os.path.join("output", "article_zh")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_name = article_zh['title']
    invalid_char_pattern = "[?？:：\s]"
    file_name = re.sub(invalid_char_pattern, "_", file_name)
    out_file_path = os.path.join(dir_path, f"{file_name}.txt")

    fp = open(out_file_path, "w+", encoding="utf-8")
    fp.seek(0)
    fp.truncate()

    fp.write(article_zh["title"])
    fp.write("\n")
    fp.write("\n")

    for p_idx in range(0, len(article_zh["paragraphs"])):
        for s_idx in range(0, len(article_zh["paragraphs"][p_idx])):
            fp.write(article_zh["paragraphs"][p_idx][s_idx])
            fp.write("\n")
        fp.write("\n")

    fp.close()

    return out_file_path


def write_contrast(article_en, article_zh):
    dir_path = os.path.join("output", "article_contrast")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_name = article_zh['title']
    invalid_char_pattern = "[?？:：\s]"
    file_name = re.sub(invalid_char_pattern, "_", file_name)
    out_file_path = os.path.join(dir_path, f"{file_name}.txt")

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


def get_cli_args():
    parser = argparse.ArgumentParser(description='文章翻译对比工具')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', dest='download', action='store_true', default='False', help='only download')
    group.add_argument('-t', dest='translate', action='store_true', default='False', help='download and translate')

    parser.add_argument('url', default='', type=str, help='网页链接')

    return parser.parse_args()


if __name__ == '__main__':
    args = get_cli_args()
    is_translate = (str(args.translate) == str(True))
    create(args.url, is_translate)
