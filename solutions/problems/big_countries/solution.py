import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # filter original dataframe by the limits in the problem statment
    rslt_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    # return only the selected columns 
    return rslt_df[['name', 'population', 'area']]