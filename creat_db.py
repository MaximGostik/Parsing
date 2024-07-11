# создаем две таблицы ('users', 'files') в базе данных "sakila"

import pymysql


try:
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3307,
        user='root',
        password='3934302Mvdnvg',
        database='world',
        cursorclass=pymysql.cursors.DictCursor)

    print("successfully connected...")

    try:
        with connection.cursor() as cursor:
            create_table1_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
                    " name varchar(64), date_birth DATE," \
                    " sex varchar(32), file_name varchar(64), PRIMARY KEY (id));"
            cursor.execute(create_table1_query)
            # создаем таблицу "users" для внесения сведений о гражданах (ФИО, дата рождения, пол, имя файла)

            create_table2_query = "CREATE TABLE `files`(id int AUTO_INCREMENT," \
                    " name varchar(64), time_load DATETIME," \
                    " count int, PRIMARY KEY (id));"
            cursor.execute(create_table2_query)
            # создаем таблицу "files" для внесения сведений о файлах .xlsx (Имя файла, дату и время загрузки, количество записей)

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)



