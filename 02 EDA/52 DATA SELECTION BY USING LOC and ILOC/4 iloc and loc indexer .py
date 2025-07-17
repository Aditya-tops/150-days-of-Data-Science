# go adn pgm 1,2
# selecting single col
import pandas as pd
df = pd.read_csv("sales2.csv")
print(df.iloc[0])
print(df.iloc[2])
print(df.iloc[-1])