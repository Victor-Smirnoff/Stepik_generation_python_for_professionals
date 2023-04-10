from zipfile import ZipFile
from datetime import datetime


with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

lst_names = sorted([info[i].filename.split('/')[-1] for i in range(len(info)) if info[i].is_dir() == False])

for i in range(len(lst_names)):
    for j in range(len(info)):
        if info[j].is_dir() == False and info[j].filename.split('/')[-1] == lst_names[i]:
            print(info[j].filename.split('/')[-1])
            print(f'  Дата модификации файла: {datetime(*info[j].date_time)}')
            print(f'  Объем исходного файла: {info[j].file_size} байт(а)')
            print(f'  Объем сжатого файла: {info[j].compress_size} байт(а)')
            print()
