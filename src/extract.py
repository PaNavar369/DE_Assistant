import pandas as pd


def extract_data(file_path):
    print(file_path)
    df = pd.read_csv(file_path)
    print(df.head())
    return df