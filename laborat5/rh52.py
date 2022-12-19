import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns


recipes = pd.read_csv('recipes_sample.csv', delimiter = ',')
reviews = pd.read_csv('reviews_sample.csv', delimiter = ',')



# 5 задание
# short = recipes[recipes.minutes < 5]
# medium = recipes[(recipes.minutes < 50) & (recipes.minutes >= 5)]
# long = recipes[recipes.minutes >= 50]
# recipes_groups = [short, medium, long]
# lengths = []
# steps = []
# for group in recipes_groups:
#    lengths.append(len(group))
#    steps.append(group.n_steps.mean())
#
# data = pd.DataFrame(data = [[lengths[0], steps[0]], [lengths[1], steps[1]], [lengths[2], steps[2]]], index=['short', 'medium', 'long'], columns=['length', 'average steps'])
# print(data)
#
# fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize = (10,6))
# data.plot(ax=ax1, y='average steps', xlabel = '', kind = 'bar')
# data.plot(ax=ax2, y='length', ylabel = '', kind = 'pie')
# plt.show()



# 6 задание
# reviews_2008 = reviews[reviews.date.str[:4]=='2008']
# reviews_2009 = reviews[reviews.date.str[:4]=='2009']
# fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,6))
# fig.suptitle("Rating histogram in 2008 and 2009")
# reviews_2008.rating.plot.hist(color='olive', ax=ax1)
# reviews_2009.rating.plot.hist(color='orange', ax=ax2)
# ax1.legend()
# ax2.legend()
# plt.show()



# 7 задание
# def duration_status(minutes):
#    if minutes < 5:
#        return "short"
#    elif 5 <= minutes < 50:
#        return "medium"
#    else:
#        return "long"
# recipes['duration'] = recipes['minutes'].map(duration_status)
# print(recipes)
# sns.scatterplot(data=recipes, x='n_steps', y='n_ingredients', hue='duration').set(title='The scatter plot n_steps and n_ingredients')
# plt.show()



# 8 задание
all_data = pd.merge(recipes, reviews, left_on='id', right_on='recipe_id')
print(all_data)
corr_matrix = all_data[['minutes', 'n_steps', 'n_ingredients', 'rating']].corr()
sns.heatmap(data=corr_matrix, cmap='YlOrRd', annot=True).set(title='Корреляционная матрица числовых столбцов таблиц recipes и reviews')
plt.show()