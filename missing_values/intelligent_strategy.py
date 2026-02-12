import pandas as pd

def handle_missing_intelligent(df):
    for column in df.columns:

        # NUMERIC COLUMNS
        if pd.api.types.is_numeric_dtype(df[column]):
            skewness = df[column].skew()

            # Heuristic: if distribution is skewed, use median
            if abs(skewness) > 1:
                df[column] = df[column].fillna(df[column].median())
            else:
                df[column] = df[column].fillna(df[column].mean())

        # CATEGORICAL COLUMNS
        else:
            df[column] = df[column].fillna("unknown")

    return df
