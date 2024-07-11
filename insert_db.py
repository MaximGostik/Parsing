# функция date_db_name вносит строку ФИО, год рождения, пол в таблицу "users"
# функция date_db_file вносит строку Имя файла, дату и время загрузки, количество записей в таблицу "files"

import pymysql


def date_db_name(name, db, sex, file_name):

    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3307,
            user='root',
            password='3934302Mvdnvg',
            database='world',
            cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO `users` (name, date_birth, sex, file_name) VALUES (%s, %s, %s, %s)"
                cursor.execute(insert_query, (name, db, sex, file_name))
                connection.commit()
                print(f"Добавлен в таблицу 'users' - {name}, {db}, {sex}, {file_name}")
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...(date_db_name)")
        print(ex)


def date_db_file(file_name, time_load, count):

    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3307,
            user='root',
            password='3934302Mvdnvg',
            database='world',
            cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO `files` (name, time_load, count) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (file_name, time_load, count))
                connection.commit()
                # print(f"Добавлен в таблицу 'files' - {file_name}, {time_load}, {count}")
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...(date_db_file)")
        print(ex)

