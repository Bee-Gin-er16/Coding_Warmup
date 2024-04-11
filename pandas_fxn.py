import pandas as pd

#OP1
# df = pd.read_csv('./Automobile_data.csv')
# print(df.head(5))
# print(df.tail(5))

#OP2
# df = pd.read_csv('./Automobile_data.csv', na_values={
# 'price':["?","n.a"],
# 'stroke':["?","n.a"],
# 'horsepower':["?","n.a"],
# 'peak-rpm':["?","n.a"],
# 'average-mileage':["?","n.a"]})
# print(df)

#OP3
# df = pd.read_csv('./Automobile_data.csv')
# df = df [['company','price']][df.price==df['price'].max()]
# print(df)

#OP4
df = pd.read_csv('./Automobile_data.csv')
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
print(toyotaDf)

#OP5
print(df['company'].value_counts())

#OUTDATED FEATURES
#OP6
# df = pd.read_csv('./Automobile_data.csv')
# car_Manufacturers = df.groupby('company')
# priceDf = car_Manufacturers['company','price'].max()
# print(priceDf)

#OP7
# car_Manufacturers = df.groupby('company')
# mileageDf = car_Manufacturers['company','average-mileage'].mean()
# print(mileageDf)

#OP8

#OP9

#OP10