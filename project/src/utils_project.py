"""
Utility functions for Stage 3 Project
"""

import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Simple reusable function to clean column names:
    - strip spaces
    - make lowercase
    - replace spaces with underscores
    """
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
    )
    return df
