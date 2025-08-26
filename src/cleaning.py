import pandas as pd
import numpy as np

def fill_missing_median(df, columns=None):
    """
    Fill missing values in numeric columns with the column median.
    """
    df_copy = df.copy()
    numeric_cols = df_copy.select_dtypes(include=[np.number]).columns
    if columns is None:
        columns = numeric_cols
    for col in columns:
        if col in df_copy.columns:
            median_val = df_copy[col].median(skipna=True)
            df_copy[col] = df_copy[col].fillna(median_val)
    return df_copy

def drop_missing(df, col_threshold=0.5, row_threshold=None):
    """
    Drop columns (and optionally rows) with too many missing values.
    """
    df_copy = df.copy()
    
    # Drop columns
    col_missing = df_copy.isna().mean()
    cols_to_drop = col_missing[col_missing >= col_threshold].index
    df_copy = df_copy.drop(columns=cols_to_drop)
    
    # Drop rows
    if row_threshold is not None:
        row_missing = df_copy.isna().mean(axis=1)
        df_copy = df_copy[row_missing < row_threshold]
    
    return df_copy

def normalize_data(df, columns=None):
    """
    Min-Max normalize numeric columns to range [0,1].
    """
    df_copy = df.copy()
    numeric_cols = df_copy.select_dtypes(include=[np.number]).columns
    if columns is None:
        columns = numeric_cols
    for col in columns:
        if col in df_copy.columns:
            col_min = df_copy[col].min()
            col_max = df_copy[col].max()
            if col_min != col_max:  # avoid division by zero
                df_copy[col] = (df_copy[col] - col_min) / (col_max - col_min)
    return df_copy