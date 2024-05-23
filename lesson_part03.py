# Материал урока

import pandas as pd
import numpy as np

# набор дат через 1 день
dates = pd.date_range(start='2024-01-25', periods=10, freq='D')

# 10 случайных значений
values = np.random.rand(10)

# dataframe
df = pd.DataFrame({'Date': dates, 'Value': values})
# Дату установим как индекс
df.set_index('Date', inplace=True)

# Установаить интервал Месяц и взать среднее по месяцу
month = df.resample('M').mean()

print(df)
print(month)
