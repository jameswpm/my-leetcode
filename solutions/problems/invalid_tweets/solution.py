import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # select the ids of tweets with invalid content
    invalid = tweets.loc[tweets['content'].str.len() > 15]
    return invalid[['tweet_id']]