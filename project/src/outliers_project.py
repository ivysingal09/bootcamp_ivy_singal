import pandas as pd

def remove_outliers(df, column, method="zscore", threshold=3):
    """
    Remove outliers from a dataframe column.
    
    Args:
        df (pd.DataFrame): input dataframe
        column (str): column to check for outliers
        method (str): "zscore" or "iqr"
        threshold (float): z-score cutoff or IQR multiplier

    Returns:
        pd.DataFrame: cleaned dataframe
    """
    if column not in df.columns:
        raise ValueError(f"Column {column} not found in dataframe")

    if method == "zscore":
        mean, std = df[column].mean(), df[column].std()
        mask = (df[column] - mean).abs() <= threshold * std
    elif method == "iqr":
        q1, q3 = df[column].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
        mask = df[column].between(lower, upper)
    else:
        raise ValueError("method must be 'zscore' or 'iqr'")

    return df[mask].copy()
