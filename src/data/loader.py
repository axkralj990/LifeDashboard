import pandas as pd
from src.config.mapping import TransactionsMapping

def create_year_column(df: pd.DataFrame) -> pd.DataFrame:
    df[TransactionsMapping.YEAR['object']] = df[TransactionsMapping.DATE['file']].dt.year.astype(str)
    return df

def create_month_column(df: pd.DataFrame) -> pd.DataFrame:
    df[TransactionsMapping.MONTH['object']] = df[TransactionsMapping.DATE['file']].dt.month.astype(str)
    return df

def create_year_month_column(df: pd.DataFrame) -> pd.DataFrame:
    # df[TransactionsMapping.YEAR_MONTH['object']] = df[TransactionsMapping.DATE['file']].dt.to_period('M')
    df[TransactionsMapping.YEAR_MONTH['object']] = df[TransactionsMapping.DATE['object']].dt.strftime('%Y-%m')
    return df

def load_transaction_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(
        path,
        dtype={
            TransactionsMapping.AMOUNT['file']: float,
            TransactionsMapping.CATEGORY_1['file']: str,
            TransactionsMapping.CATEGORY_2['file']: str,
            TransactionsMapping.DATE['file']: str,
        },
        parse_dates=[TransactionsMapping.DATE['file']],
    )
    
    data = data.rename(columns={
        TransactionsMapping.AMOUNT['file']: TransactionsMapping.AMOUNT['object'],
        TransactionsMapping.CATEGORY_1['file']: TransactionsMapping.CATEGORY_1['object'],
        TransactionsMapping.CATEGORY_2['file']: TransactionsMapping.CATEGORY_2['object'],
        TransactionsMapping.DATE['file']: TransactionsMapping.DATE['object']})
    
    return (data.
            pipe(create_year_column).
            pipe(create_month_column).
            pipe(create_year_month_column))