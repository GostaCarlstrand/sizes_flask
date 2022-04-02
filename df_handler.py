import pandas as pd


def get_person_df(gender):
    df = pd.read_csv(f'./org_csv/{gender}.csv')
    return df.head(50)

