import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    table = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    return table[table['customerId'].isnull()][['name']].rename(columns={'name': 'Customers'})
