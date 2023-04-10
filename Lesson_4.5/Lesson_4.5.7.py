from zipfile import ZipFile
import os.path


file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']


with ZipFile('files.zip', mode='a') as zip_file:
    for name in file_names:
        size = os.path.getsize(name)
        if size <= 100:
            zip_file.write(name)
