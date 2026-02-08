import pandas as pd


def transform_data(df):
    print('Transforming raw CSV data')
    df = fill_null_values(df)
    df = fill_missing_years(df)
    df = data_formatter(df)

    return df


def fill_null_values(df):
    print('Filling Null Values')
    df.isnull().sum()
    df['Log GDP per capita'] = df['Log GDP per capita'].fillna(df['Log GDP per capita'].median())

    return df


def data_formatter(df):
    print('Formatting Data')
    df = df.drop_duplicates()
    df['Country name'] = df['Country name'].str.strip()
    df['Country name'] = df['Country name'].str.title()
    df["year"] = df["year"].astype(int)
    df = df[['Country name', 'year', 'Life Ladder', 'Log GDP per capita']]

    return df


def fill_missing_years(df):
    print('Filling Mising Year\'s Data')
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
