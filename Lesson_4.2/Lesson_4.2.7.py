with open('data.csv', 'r', encoding='UTF-8') as my_file:
    content = [line.strip().split(',') for line in my_file.readlines()][1:]

content = [line[2] for line in content]
content = [content[i].split('@') for i in range(len(content))]
content = [line[1] for line in content]
lst_count = [content.count(address) for address in list(set(content))]
lst_tuples = sorted(zip(lst_count, list(set(content))))
res = [lst_tuples[i][1] + ',' + str(lst_tuples[i][0]) for i in range(len(lst_tuples))]
res_0 = ['domain,count']
result = res_0 + res

with open('domain_usage.csv', 'w', encoding='UTF-8') as my_file_output:
    for x in result:
        print(x, file=my_file_output)
