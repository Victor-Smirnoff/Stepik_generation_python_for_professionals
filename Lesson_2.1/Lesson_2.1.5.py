from string import ascii_lowercase, ascii_uppercase, ascii_letters

def convert(string):
    count_upper = 0
    count_lower = 0
    for i in string:
        if i in ascii_letters and i in ascii_uppercase:
            count_upper += 1
        elif i in ascii_letters and i in ascii_lowercase:
            count_lower += 1
    if count_lower >= count_upper:
        return string.lower()
    return string.upper()
