import pandas as pd
import random
import openpyxl
from openpyxl import load_workbook
import xlwings as xw
from openpyxl.styles import Alignment

# 1 задача
recipes = pd.read_csv('recipes_sample.csv', delimiter=',')
recipes = recipes.drop(columns = ['n_steps', 'contributor_id'])
reviews = pd.read_csv('reviews_sample.csv', delimiter=',')
#print(recipes)
#print(reviews)


# 2 задача
srez1 = random.sample(list(recipes.index), int(0.05 * len(recipes)))
data1 = []
[data1.append(recipes.iloc[i]) for i in sorted(srez1)]
short_recipes = pd.DataFrame(data1)

srez2 = random.sample(list(reviews.index), int(0.05 * len(reviews)))
data2 = []
[data2.append(reviews.iloc[i]) for i in sorted(srez2)]
short_reviews = pd.DataFrame(data2)

with pd.ExcelWriter('recipes.xlsx') as writer:
    short_recipes.to_excel(writer, sheet_name='Рецепты')
    short_reviews.to_excel(writer, sheet_name='Отзывы')


# 3 задача
Sheet0 = xw.Book('recipes.xlsx').sheets['Рецепты']
Sheet0.range('J1').value = 'seconds_assign'
Sheet0.range('J2').options(transpose=True).value = (short_recipes.minutes * 60).values
Sheet0.range('H2').options(transpose=True).value = (short_recipes.minutes*60).values


# 4 задача
Sheet0.range('I1').value = 'seconds_formula'
Sheet0.range('I2:I1501').value = "=D2*60"


# 5 задача
sheet = load_workbook(filename="recipes.xlsx")
sheet1 = sheet.get_sheet_by_name('Рецепты')
xw.Range('I1:L1').columns[0].column_width = 30
xw.Range('I1:L1').columns[1].column_width = 30
for letter in Sheet0.range('I1:L1'):
    col = sheet1.column_dimensions[f'{letter}']
    col.alignment = Alignment(horizontal="center")
Sheet0.range('I1:L1').api.Font.Bold = True


# 6 задача
for i in range(2,1502):
    if int(Sheet0.range((i, 4)).value) < 5:
        Sheet0.range((i, 4)).color = (25, 200, 20)
    elif 5 <= int(Sheet0.range((i, 4)).value) <= 10:
        Sheet0.range((i, 4)).color = (255, 226, 83)
    else:
        Sheet0.range((i, 4)).color = (240, 30, 30)


# 7 задача
Sheet0.range('J1').value = 'n_reviews'
Sheet0.range('J1').api.Font.Bold = True
xw.Range('J1').columns[0].column_width = 30
Sheet0.range('J1').api.HorizontalAlignment = -4108
