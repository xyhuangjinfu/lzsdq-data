import os.path
import urllib.request

import db
import root_dir_util


def create_sitemap():
    article_list = db.get_all_article()

    sitemap_path = os.path.join(root_dir_util.get_root_dir(), "output", "sitemap.xml")
    fp = open(sitemap_path, "w+", encoding="utf-8")
    fp.seek(0)
    fp.truncate()

    fp.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    fp.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for article in article_list:
        fp.write('  <url>\n')
        fp.write(f'    <loc>https://www.lzsdq.cn/article/{article["id"]}</loc>\n')
        fp.write(f'    <lastmod>{_get_date(article["create_time"])}</lastmod>\n')
        fp.write('  </url>\n')

    fp.write('</urlset>\n')
    fp.close()
    return sitemap_path


def upload_sitemap(sitemap_path):
    fp = open(sitemap_path, "r", encoding="utf-8")
    content = fp.read()
    fp.close()

    url = "https://www.lzsdq.cn/sitemap.xml"
    req = urllib.request.Request(url, method="PUT")
    resp = urllib.request.urlopen(req, data=bytes(content, encoding="utf-8"))
    status_code = resp.getcode()
    return status_code == 204


def main():
    sitemap_path = create_sitemap()
    print(f"sitemap 创建成功：{sitemap_path}")
    upload_success = upload_sitemap(sitemap_path)
    print(f"上传 sitemap ：{upload_success}")


def _get_date(datetime_obj):
    date_str = datetime_obj.strftime("%Y-%m-%d")
    return date_str


if __name__ == '__main__':
    main()
