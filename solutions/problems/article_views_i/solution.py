import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # select lines where author_id that are equal to viewer_id using query
    author_view_own = views.query("author_id == viewer_id")
    # select the id and order the table
    return author_view_own[['author_id']].rename(columns={'author_id': 'id'}).sort_values(by=['id']).drop_duplicates(['id'])