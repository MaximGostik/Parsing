import time

import openpyxl as op
from insert_db import date_db_name, date_db_file
from datetime import datetime
import os


def date_from_xlsx(filename, file):

     wb = op.open(filename, read_only=True)   #с помощью библиотеки "openpyxl" открываем файл
     sheet = wb.active           # активируем первый лист
     row_count = sheet.max_row      # определяем количество рядов

     for r in range(1, sheet.max_row+1):   # циклом перебираем все ряды, после их значения (по одному ряду)
          # передаем в функцию "date_db_name"
          name = sheet[r][0].value
          bd_1 = sheet[r][1].value
          bd = datetime.strptime(bd_1, "%d.%m.%Y")
          sex = sheet[r][2].value

          date_db_name(name, bd, sex, file) # добавляем сведения в таблицу "users"

     wb._archive.close() # файл закрываем
     return row_count  # возвращаем значения о количестве рядов файла


def parser(path):

     dir_list = os.listdir(path) #считываем наименования всех файлов из папки
     files_name = [name for name in dir_list if name.endswith(".xlsx")] # с помощью цикла перебираем
     # все файлы и добавляем в список наименования заканчивающиеся ".xlsx"

     for file in files_name: # циклом перебираем наименования файлов
          row_count = date_from_xlsx(path+'\\'+file, file) # в функцию помещаем имя файла "xlsx"
          date_db_file(file, datetime.now(), row_count) # в функцию помещаем сведения о наименовании
          # файла, дате и времени загрузки, количестве записей
          os.remove(path+'\\'+file) # удаляем считанный файл


if __name__ == "__main__":

     path = "C:\\Users\\maxim\\Date" # путь к папке, где помещены файлы

     while True:
          parser(path)
          time.sleep(20)





