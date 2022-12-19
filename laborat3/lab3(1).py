import json
import re
import pandas

f = open("contributors_sample.json", mode='r', encoding = 'utf-8')
data = json.load(f)

# 1.1 задача
#print(data[:3])


# 1.2 задача
#domains = set()
#for i in data:
#    regex = re.findall(r'@.+', i['mail'])
#    domains.add(str(*regex)[1:])
#print(domains)


# 1.3 задача
#def find_info(username, data):
#    flag = 0
#    for inf in data:
#        if inf['username'] == username:
#            print(inf)
#            flag = 1
#            break
#    if flag == 0:
#        raise ValueError("Не найден человек с заданным `username`, повторите ввод")
#
#
#username = input('Введите имя человека для поиска информации: ')
#find_info(username, data)


# 1.4 задача
#gender = {'M': 0, 'F':0}
#for inf in data:
#    gender[inf['sex']] += 1
#print(gender)


# 1.5 задача
#data1 = []
#for inf in data:
#    new_data = []
#    new_data.append(inf['id'])
#    new_data.append(inf['username'])
#    new_data.append(inf['sex'])
#    data1.append(new_data)
#
#contributors = pandas.DataFrame(data1, columns = ['id', 'username', 'sex'])
#print(contributors)


# 1.6 задача (с использованием 1.5)
#recipes = pandas.read_csv('recipes_sample.csv', delimiter = ',')
#new = pandas.merge(recipes, contributors, how = 'left')
#print(new)
#print(f'Информация в JSON файле отсутсвует для {len(new) - new.username.count()} человек')
