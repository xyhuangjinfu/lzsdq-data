import os.path


def read(cache_path):
    if os.path.exists(cache_path):
        fp = open(cache_path, "r", encoding="utf-8")
        content = fp.read()
        fp.close()
        return content
    else:
        return None


def write(cache_path, content):
    fp = open(cache_path, "w+", encoding="utf-8")
    fp.seek(0)
    fp.truncate()
    fp.write(content)
    fp.close()
