def transform_data(df):
    print("transform_started")
    df = df.copy()
    df.columns = df.columns.str.lower().str.strip()

    return df