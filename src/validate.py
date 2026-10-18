def validate_data(df):
    print("validate started")
    if df.empty:
        raise ValueError("DataFrame is empty.")

    return True