import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # select customers id that already order something
    ordered = orders['customerId']
    # filter customers by id that are not in the ordered series
    # the tilde (~) means not
    return customers.loc[~customers['id'].isin(ordered)][['name']].rename(columns={'name': 'Customers'})