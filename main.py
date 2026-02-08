from src.utils.config import DATA_PATH, DB_PATH
from src.extractors import csv_reader, api_reader
from src.transformers import csv_transformer, api_data_transformer, integeration
from src.loaders.sqlite3_loder import save_data_sqllite3,return_data_sqllite3


def main():
    print("Starting ETL pipeline...")

    df_csv_raw = csv_reader.extract_csv(DATA_PATH)
    print(df_csv_raw)

    df_csv_transformed = csv_transformer.transform_data(df_csv_raw)
    print(df_csv_transformed)

    df_api_raw = api_reader.extract_from_api()
    print(df_api_raw)

    df_api_transformed = api_data_transformer.transform_data(df_api_raw)
    df_api_transformed = df_api_transformed[df_api_transformed["Country name"].isin(df_csv_transformed["Country name"])]
    print(df_api_transformed)

    final_dataset = integeration.integrate_datasets(df_csv_transformed, df_api_transformed)
    print(final_dataset)

    save_data_sqllite3(final_dataset, DB_PATH)

if __name__ == "__main__":
    main()
