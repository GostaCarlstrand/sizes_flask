import pandas as pd


def get_person_dict(gender):
    df = pd.read_csv(f'./org_csv/{gender}.csv')
    #df = df.head(10)   Used to create smaller df
    df_list = []

    df = df.reset_index()
    for index, row in df.iterrows():
        df_dict = {
            'chest_c': row['chestcircumference'] / 10,
            'waist_c': row['waistcircumference'] / 10,
            'gender': row['Gender'],
            'height': round(row['Heightin'] * 2.54, 2),
            'weight': round(row['Weightlbs'] * 0.45359237, 2)
        }
        df_list.append(df_dict)
    return df_list




def convert_to_df():
    from mongo_access import get_persons
    data = get_persons('Male')
    df = pd.DataFrame(data)
    new_df = df[['weight', 'size']].copy()
    print(new_df.head(15))
