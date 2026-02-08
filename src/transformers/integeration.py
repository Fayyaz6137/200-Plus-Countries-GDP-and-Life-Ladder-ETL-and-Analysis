import pandas as pd


def integrate_datasets(df_csv, df_api):
    print('Integrating processed CSV and API datasets')
    df = pd.concat([df_csv, df_api], ignore_index=True)
    df = fill_life_ladder(df)

    return df


def fill_life_ladder(df):
    print('Filling life-ladder in integrated dataset')
    df['Life Ladder'] = df.groupby('Country name')['Life Ladder'].transform(lambda x: x.interpolate())

    return df
