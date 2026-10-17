def validate_data(df):
    
    if df.empty:
        raise ValueError("DataFrame is empty.")

    return True