import csv

def get_num_and_letter(s):
    s = s.split('-')
    return int(s[0]), s[1]


with open('student_counts.csv', 'r', encoding='utf-8') as my_file:
    rows = csv.reader(my_file, delimiter=',')
    content = [row for row in rows]

first = [content[0][0]] + sorted(content[0][1:], key=get_num_and_letter)

res = [','.join(first)]

for i in range(1, len(content)):
    tmp = content[i][0]
    for j in range(1, len(content[i])):
        indx = content[0].index(first[j])
        tmp += ',' + content[i][indx]
    res.append(tmp)

with open('sorted_student_counts.csv', 'w', encoding='utf-8') as output_file:
    for x in res:
        print(x, file=output_file)
