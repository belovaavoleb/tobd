import pandas as pd
import random
from bs4 import BeautifulSoup
import sys
import re


recipes = pd.read_csv('recipes_sample.csv', delimiter=',')

# 1 задание
#id_sample = random.sample(list(recipes.values), 5)
#max_len1 = max(max([len(str(i[1])) for i in id_sample]), len('id'))
#max_len2 = max(max([len(str(i[2])) for i in id_sample]), len('minutes'))
#print(f"|{'id':^{max_len1}}|{'minutes':^{max_len2}}|")
#print(f"|{'-'*int(max_len1 + max_len2 + 1)}|")
#for i in id_sample:
#    print(f"|{i[1]:^{max_len1}}|{i[2]:^{max_len2}}|")



# 2 и 3 задание
#with open('steps_sample.xml') as f_xml:
#    soup = BeautifulSoup(f_xml, 'html.parser')
#samples_dct = {}
#for recipe in soup.find_all('recipe'):
#    samples_dct[recipe.id.string] = list()
#    for step in recipe.find_all('step'):
#        samples_dct[recipe.id.string].append(step.string)
#
#
#
# def show_info(name, steps, minutes, author_id):
#     steps_str = f''
#     counter = 1
#     for i in steps:
#         steps_str += f'{counter}. {i.capitalize()}\n'
#         counter += 1
#     s = f'"{name.title()}"\n\n' + steps_str + f'----------\nАвтор: {author_id}\nСреднее время приготовления: {minutes} минут\n'
#     return (s)
#
# id_search = int(input("Введите номер (id) искомого рецепта: "))
# recipe_search = recipes[recipes.id == id_search]
# flag = 0
# try:
#     ind = int(recipe_search.index[0])
# except IndexError:
#     print(f"Рецепта с введенным id ({id_search}) не существует. Введите id существующего рецепта, например: 170895")
#     flag = 1
# if flag == 0:
#     print()
#     print(show_info(recipe_search.name[ind], samples_dct[str(recipe_search.id[ind])], recipe_search.minutes[ind], recipe_search.contributor_id[ind]))




#3 задание
#r = re.compile(r"(\d+ (hour|hours|minute|minutes)\b)")
#res = []
#for i in samples_dct['25082']:
#    if r.findall(i):
#        res.append(r.findall(i))
#print(res)



#4 задание
#r1 = re.compile(r"^this[\w\d\s]*, {0,1}but")
#counter = 0
#examples = []
#for i in recipes.description.values:
#    res = r1.match(str(i))
#    if res:
#        counter += 1
#        examples.append(i)
#print(f"Всего {counter} описаний, подходящих под заданный шаблон.")
#print()
#counter_1 = 1
#for i in random.sample(examples, 3):
#    print(f"Пример {counter_1}:")
#    print(i, end=f"\n{'-'*127}\n")
#    counter_1 += 1



#5 задание
# r2 = re.compile(r"\d / \d")
# ind_1 = 0
# print("Изначальные шаги рецепта: ")
# for i in samples_dct['72367']:
#     res = r2.search(i)
#     print(i)
#     if res:
#         a = res.group()[0]
#         b = res.group()[-1]
#         samples_dct['72367'][ind_1] = re.sub(r"\d / \d",f"{a}/{b}", i)
#     ind_1 += 1
# print(samples_dct['72367'])



