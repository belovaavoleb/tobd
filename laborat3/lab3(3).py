from bs4 import BeautifulSoup
import json
import sys
import pandas as pd
import numpy as np


# 3.1 задача
#with open('steps_sample.xml') as f_xml:
#    soup = BeautifulSoup(f_xml, 'html.parser')
#
#dct = {}
#for i in soup.find_all('recipe'):
#    dct[i.id.string] = []
#    z = 1
#    for j in i.steps('step'):
#        x = f'Turn{z}: ' + j.string
#        dct[i.id.string].append(x)
#        if z == 2:
#            break
#        z += 1
#
#with open('steps_sample.json', mode='w', encoding='utf-8') as f_jsn:
#    json.dump(dct, f_jsn, indent='\t')

# 3.2 задача
#with open('steps_sample.xml') as f_xml:
#    soup = BeautifulSoup(f_xml, 'html.parser')
#dct2 = {}
#
#for i in soup.find_all('recipe'):
#    n = len(i.find_all('step'))
#    if not(n in dct2):
#        dct2[n] = []
#        dct2[n].append(i.id.string)
#    else:
#        dct2[n].append(i.id.string)
#print(dct2)


# 3.3 задача
#with open('steps_sample.xml') as f_xml:
#    soup = BeautifulSoup(f_xml, 'html.parser')
#s = []
#for i in soup.find_all('recipe'):
#    for j in i.steps('step'):
#        if 'minutes' in j.string or 'hours' in j.string:
#            s.append(i.id.string)
#            break
#print(s)


# 3.4 задача (+ 3.2 задача)
#recipes = pd.read_csv('recipes_sample.csv', delimiter=',')
#recipes.n_steps = recipes.n_steps.fillna(0)
#for i in range(len(recipes)):
#    if recipes.loc[i, 'n_steps'] == 0:
#        for j in dct2:
#            if str(recipes.loc[i, 'id']) in dct2[j]:
#                recipes.loc[i, 'n_steps'] = j
#                break
#print(recipes)
