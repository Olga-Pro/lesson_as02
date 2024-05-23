# Материал урока

import pandas as pd
import numpy as np

# набор дат через 1 день
dates = pd.date_range(start='2024-01-31', periods=10, freq='D')

# 10 случайных значений
values = np.random.rand(10)

# dataframe
df = pd.DataFrame({'Date': dates, 'Value': values})
df.set_index('Date', )