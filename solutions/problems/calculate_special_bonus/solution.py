import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    #insert new columns
    employees['bonus'] = 0
    # select users with bonus and update the column accordingly
    employees.loc[(employees['employee_id'] % 2 != 0) & (employees['name'].str[0] != 'M'), 'bonus'] = (employees['salary'])
    return employees[['employee_id', 'bonus']].sort_values(by=['employee_id'])