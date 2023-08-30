import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # select the users with valid emails
    pattern = r'^[a-zA-Z0-9_\-\.]+$'
    valid = users.loc[users['mail'].str.endswith('@leetcode.com') & users['mail'].str[0].str.isalpha() & users['mail'].str.split('@leetcode.com').str[0].str.match(pattern)]
    return valid