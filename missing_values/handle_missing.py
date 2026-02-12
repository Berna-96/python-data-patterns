import pandas as pd

def handle_missing(df, strategy="mean", fill_value=None):
    """
    Generic missing value handler.

    Parameters:
        df (DataFrame): input dataframe
        strategy (str): mean | median | constant | drop
        fill_value: used only for constant strategy
    """

    if strategy == "mean":
        return df.fillna(df.mean(numeric_only=True))

    elif strategy == "median":
        return df.fillna(df.median(numeric_only=True))

    elif strategy == "constant":
        if fill_value is None:
            raise ValueError("fill_value must be provided for constant strategy")
        return df.fillna(fill_value)

    elif strategy == "drop":
        return df.dropna()

    else:
        raise ValueError(f"Unknown strategy: {strategy}")

