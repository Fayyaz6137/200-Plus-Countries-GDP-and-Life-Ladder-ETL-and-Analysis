import pandas as pd


def extract_csv(path: str) -> pd.DataFrame:
    """
    Reads raw CSV data and returns a DataFrame.
    """
    print("Extracting CSV data...")
    df = pd.read_csv(path)
    return df
