from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if len(args) == 0:
            zip_file.extractall()
        else:
            for file in args:
                zip_file.extract(file)
