import pandas as pd

def validate_age(df, config):
    min_age = config["age"]["min"]
    max_age = config["age"]["max"]

    invalid_mask = (df["age"] < min_age) | (df["age"] > max_age)

    df.loc[invalid_mask, "age"] = pd.NA
    return df

