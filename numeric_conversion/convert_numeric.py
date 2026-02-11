import pandas as pd

def convert_numeric(df):
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
    return df

