import pandas as pd


def get_person_dict(gender):
    df = pd.read_csv(f'./org_csv/{gender}.csv')
    df = df.head(5)
    df_list = []

    df = df.reset_index()  # make sure indexes pair with number of rows
    for index, row in df.iterrows():
        df_dict = {
            'chest_c': row['chestcircumference'] / 10,
            'waist_c': row['waistcircumference'] / 10,
            'Gender': row['Gender'],
            'HeightCm': row['Heightin'] * 2.54,
            'WeightKg': row['Weightlbs'] * 0.45359237
        }
        df_list.append(df_dict)
    return df_list


