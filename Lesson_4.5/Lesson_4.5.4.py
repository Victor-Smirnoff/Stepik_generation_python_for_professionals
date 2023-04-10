from zipfile import ZipFile
from datetime import datetime

date_fix = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

print(*sorted([info[i].filename.split('/')[-1] for i in range(len(info)) if info[i].is_dir() == False and datetime(*info[i].date_time) > date_fix]), sep='\n')
