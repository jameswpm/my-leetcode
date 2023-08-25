import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # filter original dataframe checking it it is both low_fats and recyclabe
    rslt_df = products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    # return only the product_id columns 
    return rslt_df[['product_id']]
    