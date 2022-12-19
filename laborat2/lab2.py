import pandas as pd
import numpy as np

file = pd.read_csv('recipes_sample.csv', delimiter=',', names=['name','id','minutes','contributor_id','submitted','n_steps','description','n_ingredients'])
# 1.1 задача
#df = pd.DataFrame(pd.read_csv('recipes_sample.csv'))
#df = pd.DataFrame(pd.read_csv('reviews_sample.csv'))
#print(df)


# 1.2 задача
#print(pd.DataFrame(pd.read_csv('recipes_sample.csv')).info())


# 1.3 задача
#print(pd.read_csv('recipes_sample.csv').isnull().sum())
#print(pd.read_csv('recipes_sample.csv').isnull().sum().sum())
#print(f"Доля строк: {np.count_nonzero(pd.read_csv('recipes_sample.csv').isnull())/pd.read_csv('recipes_sample.csv').shape[0]}\n")
#print()
#print(pd.read_csv('reviews_sample.csv').isnull().sum())
#print(f"Доля строк: {np.count_nonzero(pd.read_csv('reviews_sample.csv').isnull())/pd.read_csv('reviews_sample.csv').shape[0]}")


# 1.4 задача
#print("подсчет для обзоров", pd.read_csv('reviews_sample.csv').select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).mean())
#print("подсчет для рецептов", pd.read_csv('recipes_sample.csv').select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).mean())


# 1.5 задача
#print(pd.read_csv('recipes_sample.csv')['name'].sample(n=10))


# 1.6 задача
#print(pd.read_csv('reviews_sample.csv').reset_index (drop = True))


# 1.7 задача
#file_n = pd.read_csv('recipes_sample.csv')[(pd.read_csv('recipes_sample.csv').minutes<=20) & (pd.read_csv('recipes_sample.csv').n_ingredients<=5)]
#print(file_n)

