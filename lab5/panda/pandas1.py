import pandas as pd
#
# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
# df = pd.read_csv(csv_path)
# print(df.head())

# del df
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df = pd.read_excel(xlsx_path)
# print(df)
#
# #  column as a dataframe
# x = df[['Length']]
# print(x)
#
# del x
# #  column as a series
# x = df['Length']
# print(x)
#
# print("\n\n")
# y = df[['Artist', 'Length', 'Genre']]
# print(y)


print(df.iloc[0, 0])
print(df.loc[1, 'Artist'])
print(df.iloc[0:2, 0:3])
print(df.loc[0:2, 'Artist':'Released'])