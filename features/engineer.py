# features/engineer.py
def create_features(df):
    for lag in range(1, 6):
        df[f'lag_{lag}'] = df['adj_close'].shift(lag)
    df['rolling_mean_5'] = df['adj_close'].rolling(5).mean()
    df['rolling_std_5'] = df['adj_close'].rolling(5).std()
    df['day_of_week'] = df.index.dayofweek
    df.dropna(inplace=True)
    return df
