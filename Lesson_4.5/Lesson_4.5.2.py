from zipfile import ZipFile


with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

before = 0
aftrer = 0

for i in range(len(info)):
    before += info[i].file_size
    aftrer += info[i].compress_size

print(f'Объем исходных файлов: {before} байт(а)')
print(f'Объем сжатых файлов: {aftrer} байт(а)')
