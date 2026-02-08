import pandas as pd
import numpy as np

def transform_data(df):
    print('Transforming raw API data')
    df = fill_null_values(df)
    df = data_formatter(df)

    return df


def fill_null_values(df):
    print('Filling Null Values')
    df.isnull().sum()
    df ['GDP per capita'] = df ['GDP per capita'].fillna(df ['GDP per capita'].median()) # Data Quality Assesment

    return df


def data_formatter(df):
    print('Formatting Data')
    # Calculate Log GDP per capita
    df['Log GDP per capita'] = np.log(df['GDP per capita'])

    # Drop original GDP per capita if not needed
    df = df[['Country name', 'year', 'Log GDP per capita']]

    return df



