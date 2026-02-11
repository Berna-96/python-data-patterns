import pandas as pd

def validate_salary(df, config):
    min_salary = config["salary"]["min"]
    max_salary = config["salary"]["max"]

    invalid_mask = (df["salary"] < min_salary) | (df["salary"] > max_salary)

    df.loc[invalid_mask, "salary"] = pd.NA
    return df

