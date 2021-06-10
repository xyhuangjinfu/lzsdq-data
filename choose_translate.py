import re


# fp = open("assets/origin.txt", encoding="utf-8")
# article = fp.read();
# fp.close()
# paragraphs = article.split("\n")
# for p in paragraphs:
#     sentences = p.split(".")
#     for s in sentences:
#         s = s.strip()
#         if s != "":
#             s += "."
#             print(s)
#     print("\n")


def translate_compare():
    origin_format_list = split_article("\n", ".", read_content("origin.txt"))
    baidu_format_list = split_article("\n", "。", read_content("baidu.txt"))
    youdao_format_list = split_article("\n", "。", read_content("youdao.txt"))

    assert len(origin_format_list) == len(baidu_format_list)
    assert len(origin_format_list) == len(youdao_format_list)

    compare_list = []
    for idx in range(0, len(origin_format_list)):
        if origin_format_list[idx] == "\n":
            compare_list.append("\n")
            continue
        compare_list.append(origin_format_list[idx])
        compare_list.append("\n")
        compare_list.append(baidu_format_list[idx])
        compare_list.append("\n")
        compare_list.append(youdao_format_list[idx])

    fp = open("assets/translate/compare.txt", "w", encoding="utf-8")
    fp.seek(0)
    fp.truncate()
    fp.write("".join(compare_list))
    fp.close()


def read_content(file_name):
    fp = open(f"assets/translate/{file_name}", encoding="utf-8")
    content = fp.read();
    fp.close()
    return content


def split_article(paragraph_separator, sentence_separator, article):
    format_list = []
    reg_sentence = f".+?\{sentence_separator}"
    pattern_sentence = re.compile(reg_sentence)
    paragraphs = article.split(paragraph_separator)
    for p in paragraphs:
        p = p.strip()
        sentences = re.findall(pattern_sentence, p)
        for s in sentences:
            s = s.strip()
            format_list.append(s)
            format_list.append("\n")
        format_list.append("\n")
    # 移除最后段落的换行
    format_list.pop()
    format_list.pop()
    return format_list


def format_article():
    origin_format_list = split_article("\n", ".", read_content("origin.txt"))
    fp = open("assets/translate/compare.txt", "w", encoding="utf-8")
    fp.seek(0)
    fp.truncate()
    fp.write("".join(origin_format_list))
    fp.close()


if __name__ == '__main__':
    format_article()
