import datetime

import mysql.connector


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
        host="106.14.140.35",
        port="3306",
        database="lzsdq",
        user="hjf",
        password="654321"
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
