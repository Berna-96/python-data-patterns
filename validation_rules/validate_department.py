import pandas as pd

def validate_department(df, config):
    allowed = config["department"]["allowed"]

    invalid_mask = ~df["department"].str.lower().isin(allowed)
    invalid_mask = invalid_mask.fillna(False)

    df.loc[invalid_mask, "department"] = pd.NA
    return df


