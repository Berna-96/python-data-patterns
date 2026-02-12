import pandas as pd
from logging.file_logger import write_log

def handle_missing_intelligent(df):
    for column in df.columns:

        if pd.api.types.is_numeric_dtype(df[column]):
            skewness = df[column].skew()

            if abs(skewness) > 1:
                write_log("INFO", f"Column {column} → skewed distribution → median applied")
                df[column] = df[column].fillna(df[column].median())
            else:
                write_log("INFO", f"Column {column} → symmetric distribution → mean applied")
                df[column] = df[column].fillna(df[column].mean())

        else:
            write_log("INFO", f"Column {column} → categorical → filled with 'unknown'")
            df[column] = df[column].fillna("unknown")

    return df
