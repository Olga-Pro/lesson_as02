# Материал урока

import pandas as pd

# словарь
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)

# создание категорий
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')


print(df['department'].cat.categories)
print(df['gender'].cat.categories)

# числовой код категорий
print(df['gender'].cat.codes)

# добавить категорию
df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

# удалить категорию
df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)

print(df)