import db


if __name__ == '__main__':
    article_list = db.get_all_article()
    for a in article_list:
        print(f"{a['id']}   {a['title']}   {a['create_time']}")