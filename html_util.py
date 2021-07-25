import re


def remove_i(content_contain_tag):
    return remove_double_tag(content_contain_tag, "i")


def remove_a(content_contain_tag):
    return remove_double_tag(content_contain_tag, "a")


def remove_double_tag(content_contain_tag, tag):
    """
    移除内容里面的双标签
    :param content_contain_link:
    :return:
    """
    pattern_link = re.compile(f'<{tag}.*?>(.+?)</{tag}>')

    def _tag_content(matched):
        return matched.group(1)

    content_no_tag = re.sub(pattern_link, _tag_content, content_contain_tag)
    return content_no_tag
