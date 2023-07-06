import pandas as pd

df = pd.read_clipboard()
print(df)
df.to_csv('./Data/men_season8.csv', index=False)