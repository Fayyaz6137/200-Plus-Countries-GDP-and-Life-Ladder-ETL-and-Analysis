import pandas as pd
import requests


def extract_from_api():
    # Years 2020-2025
    start_year = 2020
    end_year = 2025

    print("Extracting API data...")
    # API URL for GDP per capita for all countries
    api_url = (f"http://api.worldbank.org/v2/country/all/indicator/NY.GDP"
               f".PCAP.CD?date={start_year}:{end_year}&format=json&per_page=20000")

    response = requests.get(api_url)
    data = response.json()

    # Extract relevant data
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

    df = pd.DataFrame(records)
    return df
