import sqlite3
import pandas as pd


def save_data_sqllite3(df, path):
    print('Saving Integrated Dataset into sqllite3')
    conn = sqlite3.connect(path)
    df.to_sql("GDP_and_Life_Ladder", conn, if_exists="replace", index=False)
    conn.close()
    print('Saved')


def return_data_sqllite3(path):
    print('Returning Integrated Dataset')
    conn = sqlite3.connect(path)
    df = pd.read_sql("SELECT * FROM GDP_and_Life_Ladder", conn)
    return df
