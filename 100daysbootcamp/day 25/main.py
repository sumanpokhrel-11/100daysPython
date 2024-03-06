import pandas as pd
data = pd.read_csv('100daysbootcamp\day 25\squirrel_data.csv')
gray_squirrel = len(data[data['Primary Fur Color']=='Gray'])
black_squirrel = len(data[data['Primary Fur Color']=='Black'])
cinnamon_squirrel = len(data[data['Primary Fur Color']=='Cinnamon'])

print(gray_squirrel)

dict_squirrel = {
    'color' :['gray', 'black', 'cinnamon'],
    'count' : [gray_squirrel, black_squirrel, cinnamon_squirrel]
}

df = pd.DataFrame(dict_squirrel)
df.to_csv('100daysbootcamp/day 25/color_squirrel.csv')
data = pd.read_csv('100daysbootcamp/day 25/color_squirrel.csv')
print(data)