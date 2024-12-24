import re
import csv

#task 1

f1 = 'task1-en.txt'
with open(f1, 'r', encoding='utf-8') as file:
    s = file.read()

num_plus_char = re.findall(r'[a-zA-Z|0-9]+', s)
num_lower_than_ten = re.findall(r'[\d]|[-][\d+]', s)

#print(num_plus_char)


#task 2

f2 = 'task2.html'
with open(f2, 'r', encoding='utf-8') as file:
    s = file.read()

png_links = re.findall(r'[/]\S+[.]png', s)

#print(png_links)


#task 3

f3 = 'task3.txt'
with open(f3, 'r', encoding='utf-8') as file:
    s = file.read()

list_id = re.findall(r' [0-9]+ ', s)
surnames = re.findall(r' [A-Z][a-z]+ ', s)
email = re.findall(r'\S+@\S+[\.]\w+', s)
reg_date = re.findall(r' \d{4}-\d{2}-\d{2} ', s)
link = re.findall(r' http\S+[^@][\.]\S+ ', s)

data = ['ID  Surname  email  date of registration  link']
for i in range(len(list_id)):
    data += [list_id[i] + surnames[i] + email[i] + reg_date[i] + link[i]]

with open('output.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\n')
    csvwriter.writerow(data)


#add_task
f_add = 'task_add.txt'
with open(f_add, 'r', encoding='utf-8') as file:
    s = file.read()

dates = re.findall(r' (\d{2}[-/.]\d{2}[-/.]\d{4})|(\d{4}[-/.]\d{2}[-/.]\d{2})', s)
emails = re.findall(r' \w+@\w+[\.][a-z]+', s)
links = re.findall(r' http\S+[^@][\.]\w+', s)
#print(links)