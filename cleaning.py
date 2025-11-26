#%%importing all the libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# %% reading the csv 
df= pd.read_excel('player_records.xlsx')
print(df)
# %% as the colums could not be read in the excel,therefore w have defined them 
df.columns = [
    "Player", "Span", "Mat", "Inns", "NO", "Runs", "HS", "Ave", 
    "BF", "SR", "100", "50", "0", "4s", "6s"
]
df.head()
# %%getting the usual info 
print('description of the data:')
df.describe()


# %%checking  values
print('null values:')
df.isnull().sum()


# %%
print('shape')
df.shape
print('info')
df.info()
# %% changing the hs column 
df['HS']=df['HS'].str.replace("*","",regex=False)
df["HS"]=pd.to_numeric(df["HS"],errors="coerce")


# %%
df.isnull().sum()

# %%
df.info()
# %%
df['Player']=df['Player'].fillna(df["Player"].mode()[0])
# %%
df['Span']=df['Span'].fillna(df["Span"].mode()[0])
# %%
df['Mat']=df["Mat"].fillna(0).astype(int)
# %%
df['Inns']=df["Inns"].fillna(0).astype(int)
# %%
df['NO']=df["NO"].fillna(0).astype(int)
# %%
df['Runs']=df["Runs"].fillna(0).astype(int)
# %%
df['HS']=df['HS'].fillna(df["HS"].median())
# %%
df['Ave']=df["Ave"].fillna(df["Ave"].mean())
# %%
df['BF']=df["BF"].fillna(df["BF"].median())
# %%
df['SR']=df["SR"].fillna(df['SR'].mean())
# %%
df['100']=df["100"].fillna(0).astype(int)
# %%
df['50']=df["50"].fillna(0).astype(int)
# %%
df['0']=df["0"].fillna(0).astype(int)
# %%
df['4s']=df["4s"].fillna(0).astype(int)
# %%
df['6s']=df["6s"].fillna(0).astype(int)
# %%
df.isnull().sum()

# %%saving data
df.to_excel("cricket_cleaned_data.xlsx", index=False)


# %%
