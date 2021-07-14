import db


def create_sitemap():
    article_list = db.get_all_article()

    fp = open("./assets/sitemap.xml", "w+", encoding="utf-8")
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


def _get_date(datetime_obj):
    date_str = datetime_obj.strftime("%Y-%m-%d")
    return date_str


if __name__ == '__main__':
    create_sitemap()
