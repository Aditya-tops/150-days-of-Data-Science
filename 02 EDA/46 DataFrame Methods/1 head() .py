import pandas as pd

df1 = pd.read_csv("sales1.csv")
df2 = df1.head(100)

print(df1[200:208])
# print()
# print(df2)
print(df2.to_string())
'''
df[start:end]
df[150:200]
'''


'''
0      166837         Veeru  34in Ultrawide Monitor       NaN
1      166838         Tarun             Samsung m10       NaN
2      166839         Kedar            20in Monitor       NaN
3      166840       Lavanya               iPhone 11       3.0
4      166841          Venu      Macbook Pro Laptop       2.0
..        ...           ...                     ...       ...
595    167403        Balaji      Macbook Pro Laptop       1.0
596    167404       Lavanya         ThinkPad Laptop       1.0
597    167405          Venu           Flatscreen TV       1.0
598    167406        Siddhu             Samsung m20       2.0
599    167407         Tarun      LG Washing Machine       1.0

[600 rows x 4 columns]

   Order ID Customer Name                     Product  Quantity
0    166837         Veeru      34in Ultrawide Monitor       NaN
1    166838         Tarun                 Samsung m10       NaN
2    166839         Kedar                20in Monitor       NaN
3    166840       Lavanya                   iPhone 11       3.0
4    166841          Venu          Macbook Pro Laptop       2.0
5    166842          Venu  Bose SoundSport Headphones       2.0
6    166843        Harsha      27in 4K Gaming Monitor       2.0
7    166844        Harsha                 Samsung m10       1.0
8    166845        Siddhu      34in Ultrawide Monitor       2.0
'''

