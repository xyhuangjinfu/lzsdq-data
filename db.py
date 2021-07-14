import datetime
import os

import mysql.connector


def get_all_article():
    db_connection = None
    db_cursor = None
    article_list = []
    try:
        db_connection = _open_db_connection()
        db_cursor = db_connection.cursor()

        sql_str = "SELECT id, title, create_time FROM article ORDER BY create_time DESC LIMIT 10000;"
        db_cursor.execute(sql_str)

        for (article_id, article_title, create_time) in db_cursor:
            article = {"id": article_id, "title": article_title, "create_time": create_time}
            article_list.append(article)

    except mysql.connector.Error as error:
        if db_connection:
            db_connection.rollback()
    finally:
        _close_db_cursor(db_cursor)
        _close_db_connection(db_connection)
        return article_list


def add_article(title, ordered_paragraphs):
    db_connection = None
    db_cursor = None
    success = False
    try:
        db_connection = _open_db_connection()
        db_cursor = db_connection.cursor()

        sql_article = "INSERT INTO `lzsdq`.`article` (title, summary, create_time) VALUES (%s, %s, %s)"
        val_article = (title, ordered_paragraphs[0], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        db_cursor.execute(sql_article, val_article)
        article_id = db_cursor.lastrowid

        sql_paragraph = "INSERT INTO `lzsdq`.`paragraph` (article_id, sequence, content) VALUES (%s, %s, %s)"
        for sequence in range(1, len(ordered_paragraphs) + 1):
            val_paragraph = (article_id, sequence, ordered_paragraphs[sequence - 1])
            db_cursor.execute(sql_paragraph, val_paragraph)

        db_connection.commit()
        success = True
    except mysql.connector.Error as error:
        success = False
        if db_connection:
            db_connection.rollback()
    finally:
        _close_db_cursor(db_cursor)
        _close_db_connection(db_connection)
        return success


def _open_db_connection():
    db_connection = mysql.connector.connect(
        host=os.environ["MYSQL_HOST"],
        port=os.environ["MYSQL_PORT"],
        database=os.environ["MYSQL_SCHEMA"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PWD"]
    )
    db_connection.autocommit = False
    return db_connection


def _close_db_connection(db_connection):
    if db_connection.is_connected():
        db_connection.close()


def _close_db_cursor(db_cursor):
    if db_cursor:
        db_cursor.close()


if __name__ == '__main__':
    pass
