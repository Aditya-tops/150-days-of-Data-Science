import pandas as pd

df = pd.read_csv("sales4.csv")
a = pd.unique(df.Product_Name)
print(a)
print(len(a))      # data frame have 20 products
'''
['27in FHD Monitor' 'iPhone 11' 'Bose SoundSport Headphones'
 'Apple iPad 10.2-inch' 'Google Phone' 'Samsung Galaxy S9 Plus'
 '20in Monitor' 'LG Washing Machine' 'iPhone 7s' 'Samsung Galaxy S20'
 'LG ThinQ Refrigerator ' 'Apple Airpods Headphones' 'iPhone 8'
 'Macbook Pro Laptop' 'LG Mobile' 'ThinkPad Laptop' 'Flatscreen TV'
 '34in Ultrawide Monitor' 'iPhone 9' '27in 4K Gaming Monitor']
'''