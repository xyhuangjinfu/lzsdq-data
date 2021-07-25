import re


def split(paragraph):
    """
    把段落切割成句子
    :param paragraph:
    :return:
    """
    sentence_list = []
    # pattern持续更新
    pattern_sentence_separator = re.compile("(?<!Dr|No)\.|\?|!")

    offset = 0
    while offset < len(paragraph):
        match_sentence = pattern_sentence_separator.search(paragraph, offset)
        next_offset = match_sentence.span()[1]
        sentence = paragraph[offset:next_offset].strip()
        sentence_list.append(sentence)
        offset = next_offset

    return sentence_list


if __name__ == '__main__':
    # p = "fake Dr. Xxx. fake No. one. fake, f1. fake, f2? fake, f3!"
    p = "fake hello. fake Dr. Xxx. fake No. one. fake world. fake, question? fake, sigh!"
    sl = split(p)
    for s in sl:
        print(s)
