import pandas as pd


def convert_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert numeric columns stored as strings with comma decimals
    into float values.
    """

    df = df.copy()

    for col in df.columns:

        if col == "date":
            continue

        if df[col].dtype == "object":

            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", ".", regex=False)
            )

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    return df


def convert_date(df):

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    return df