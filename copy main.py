import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3



df = pd.read_csv('data/raw/world-happiness-report.csv')

df.isnull().sum()
df['Log GDP per capita'] = df['Log GDP per capita'].fillna(df['Log GDP per capita'].median()) # Data Quality Assesment Dimension 1

df = df.drop_duplicates()

df['Country name'] = df['Country name'].str.strip()

df['Country name'] = df['Country name'].str.title()

df["year"] = df["year"].astype(int)

def fill_missing_years(df):
    # Find the range of years
    df['year'] = df['year'].astype(int)

    # Get full range of years in dataset
    year_min = df['year'].min()
    year_max = df['year'].max()

    # Get list of countries
    countries = df['Country name'].unique()

    # Create full grid
    full_grid = pd.MultiIndex.from_product(
        [countries, range(year_min, year_max + 1)],
        names=['Country name', 'year']
    ).to_frame(index=False)

    # Left merge ensures all countries x years exist
    df_full = full_grid.merge(df, on=['Country name', 'year'], how='left')

    # Sort by country and year
    df_full = df_full.sort_values(['Country name', 'year'])

    # Numeric columns to fill
    numeric_cols = ['Life Ladder', 'Log GDP per capita', 'Social support',
                    'Healthy life expectancy at birth', 'Freedom to make life choices',
                    'Generosity', 'Perceptions of corruption']

    # Interpolate missing values
    df_full[numeric_cols] = df_full.groupby('Country name')[numeric_cols].transform(lambda g: g.interpolate())

    # Forward/backward fill if first/last years were missing
    df_full[numeric_cols] = df_full.groupby('Country name')[numeric_cols].transform(lambda g: g.ffill().bfill())
    return df_full


df=fill_missing_years(df)

df = df[['Country name', 'year', 'Life Ladder', 'Log GDP per capita']]


# API


start_year = 2020
end_year = 2025

# API URL for GDP per capita for all countries
api_url = (f"http://api.worldbank.org/v2/country/all/indicator/NY.GDP"
           f".PCAP.CD?date={start_year}:{end_year}&format=json&per_page=20000")

response = requests.get(api_url)
data = response.json()

# Extract relevant daata
records = []
for entry in data[1]:  # data[0] has metadata
    country = entry['country']['value']
    year = int(entry['date'])
    gdp_per_capita = entry['value']  # Can be None
    records.append({
        'Country name': country,
        'year': year,
        'GDP per capita': gdp_per_capita
    })

df_api = pd.DataFrame(records)

# df_api

df_api.isnull().sum()

df_api ['GDP per capita'] = df_api ['GDP per capita'].fillna(df_api ['GDP per capita'].median()) # Data Quality Assesment

df_api.isnull().sum()

df_api = df_api[df_api["Country name"].isin(df["Country name"])]

df_api['Log GDP per capita'] = np.log(df_api['GDP per capita'])


df_api = df_api[['Country name', 'year', 'Log GDP per capita']]

df_api.head()

# Integration


df_merged = pd.concat([df, df_api], ignore_index=True)
# Sorting
df_merged = df_merged.sort_values(['Country name', 'year']).reset_index(drop=True)

df_merged.head(200)

df_merged.isnull().sum()

df_merged['Life Ladder'] = df_merged.groupby('Country name')['Life Ladder'].transform(lambda x: x.interpolate())

df_merged.isnull().sum()
# %%
df_merged.head(20)

sns.scatterplot(x='Log GDP per capita', y='Life Ladder', data=df)
sns.regplot(x='Log GDP per capita', y='Life Ladder', data=df, scatter=False, color='red')
plt.show()

df["Life Ladder"].hist(bins=20)
plt.title("Distribution of Life Ladder")
plt.show()

df["Log GDP per capita"].hist(bins=20)
plt.title("Log GDP Distribution")
plt.show()

df.groupby("Country name")["Life Ladder"].mean().sort_values(ascending=False).head(10)

country = "Italy"
df[df["Country name"] == country].plot(x="year", y="Life Ladder", title=f"{country} Life Ladder Trend")
plt.show()

country = "Italy"
df[df["Country name"] == country].plot(x="year", y="Log GDP per capita", title=f"{country} Log GDP")
plt.show()

df_merged.isna().mean()*100

conn = sqlite3.connect("WHR.db")
df_merged.to_sql("World_Happiness_Report", conn, if_exists="replace", index=False)
conn.close()

data_NoSQL = df_merged.to_dict(orient="records")
print(data_NoSQL)

# from pymongo import MongoClient
#
# client = MongoClient("mongodb://localhost:27017/")
# db = client["restaurant_db"]
# collection = db["menu"]
# collection.insert_many(data_NoSQL)