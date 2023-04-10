from zipfile import ZipFile


with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

k = 100
res = None

for i in range(len(info)):
    if info[i].is_dir() == False:
        before = info[i].file_size
        after = info[i].compress_size
        tmp = (after / before) * 100
        if tmp < k:
            k = tmp
            res = info[i].filename

print(res.split('/')[-1])
