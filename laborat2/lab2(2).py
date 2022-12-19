import pandas as pd
import openpyxl

#все вместе !
# 2.1
print(pd.read_csv('recipes_sample.csv')["submitted"] == pd.to_datetime(pd.read_csv('recipes_sample.csv')["submitted"], format='%Y-%m-%d'))


# 2.2
recipes = pd.read_csv("recipes_sample.csv")
recipes["submitted"]=pd.to_datetime(recipes["submitted"], format='%Y-%m-%d')
print(recipes.loc[recipes.submitted.dt.year>=2010])


# 3.1
recipes["description_length"]=recipes["description"].str.len()
print(recipes)


# 3.2
recipes["name_word_count"]=recipes["description"].str.replace(" ", "").str.len()
print(recipes)


# 4.1
a = pd.DataFrame({'contributor_id': recipes['contributor_id']})
a['count'] = 1
a = a.groupby('contributor_id').sum()
a = a['count'].sort_values(ascending=False)
print(a)
print("участник", a.index[0], "добавил  максимальное кол-в рецептов:", a.iloc[0])


# 4.2
review = pd.read_csv("reviews_sample.csv")
b = pd.merge(recipes, review, left_on = 'id', right_on = 'recipe_id')
b.drop("recipe_id", axis = 1, inplace = True)
print(b.groupby('id').mean()['rating'])


# 4.3
recipes['year'] = recipes['submitted'].dt.year
print(recipes.groupby(['year']).count()['name'])


# 5.1
c_new = pd.merge(recipes, review, left_on = 'id', right_on = 'recipe_id')
c_new.drop(columns=['Unnamed: 0', 'minutes', 'contributor_id', 'submitted', 'n_steps', 'description', 'n_ingredients',
'description_length', 'name_word_count', 'recipe_id', 'date', 'review'], inplace=True)
print(c_new)


# 5.2
review_count = review.groupby('recipe_id').review.count()

с2 = pd.merge(recipes, review, how = 'left', left_on = 'id', right_on = 'recipe_id')
с2.drop(columns = ['Unnamed: 0', 'minutes', 'contributor_id', 'submitted', 'n_steps', 'description', 'n_ingredients', 'description_length', 'name_word_count', 'recipe_id', 'date', 'review', 'user_id', 'rating'], inplace=True)
с2.rename(columns = {'id':'recipe_id'}, inplace = True)
с2.drop_duplicates(keep = 'first', inplace = True)

c3 = pd.DataFrame({'recipe_id': review_count.keys(), 'review_count': review_count.values})

c4 = pd.merge(с2, c3, how='left')
print(c4)



# 6.1
print(recipes.sort_values(by='name_word_count', ascending=False).to_csv('sorted_recipes.csv'))


# 6.2
with pd.ExcelWriter("new_tables_results.xlsx") as writer:
    c_new.to_excel(writer, sheet_name = 'Рецепты с оценками')
    c4.to_excel(writer, sheet_name = 'Количество отзывов по рецептам')