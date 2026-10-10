#!/usr/bin/env python3
"""Function removing all duplicate rows"""


def remove_duplicates(df):
    """
    Removes duplicate rows from a DataFrame.
    df: pandas DataFrame that may contain duplicate rows
    Returns a DataFrame with duplicates removed, keeping the first occurrence.
    """
    df = df.copy()
    df = df.drop_duplicates()
    return df
