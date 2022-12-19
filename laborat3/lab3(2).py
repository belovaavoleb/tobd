import json
import re
import pandas
import pickle
import os


f = open("contributors_sample.json", mode='r', encoding = 'utf-8')
data = json.load(f)


# 2.1 задача
#job_titles = {}
#for inf in data:
#    for job in inf['jobs']:
#        if job not in job_titles:
#            job_titles[job] = list()
#            job_titles[job].append(inf['username'])
#        else:
#            job_titles[job].append(inf['username'])
#print(job_titles)


# 2.2 задача (с использованием 2.1)
#with open('job_people.pickle', 'wb') as f_pckl:
#    pickle.dump(job_titles, f_pckl)
#with open('job_people.json', mode='w', encoding='utf-8') as f_json:
#    json.dump(job_titles, f_json, indent='\t')
#f_pckl.close()
#f_json.close()
#
#size_pckl = os.path.getsize(filename="job_people.pickle")
#size_json = os.path.getsize(filename="job_people.json")
#print(f'Размер файла job_people.pickle: {size_pckl} байт, {size_pckl/1024} КБ.')
#print(f'Размер файла job_people.json: {size_json} байт, {size_json/1024} КБ.')
#print(f'Объем файла JSON больше на {size_json/1024 - size_pckl/1024} КБ.')


# 2.3 задача
#with open('job_people.pickle', 'rb') as f_pckl:
#    data1 = pickle.load(f_pckl)
#print(data1)

