import pandas as pd
import re

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # select patients with Type I Diabetes
    diabetes = patients.loc[patients['conditions'].str.split().apply(lambda x: any(part.startswith('DIAB1') for part in x))]
    return diabetes