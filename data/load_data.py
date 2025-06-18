# data/load_data.py
import pandas as pd
import requests

def load_tiingo_data():
    API_KEY = 'YOUR_TIINGO_API_KEY_HERE'
    url = "https://api.tiingo.com/tiingo/daily/spy/prices"
    params = {
        'startDate': '2023-01-01',
        'endDate': '2025-12-31',
        'resampleFreq': 'daily',
        'columns': 'adjClose'
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {API_KEY}'
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df[['adjClose']].rename(columns={'adjClose': 'adj_close'}).dropna()
    return df
