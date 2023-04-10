from zipfile import ZipFile


with ZipFile('desktop.zip', 'r') as zip_file:
    info = zip_file.infolist()

print(*[x[0] + [' ' + x[1], ''][x[1] == '0 MB'] for x in [(str('  ' * x.filename.rstrip('/').count('/')) + x.filename.rstrip('/').split('/')[-1], str(x.file_size) + ' B' if 0 < x.file_size < 1024 else (str(round(x.file_size / 1024)) + ' KB' if 1024 < x.file_size < 1048576 else str(round(x.file_size / 1048576)) + ' MB')) for x in info]], sep='\n')
