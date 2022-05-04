import pandas as pd
import numpy as np


if __name__ == '__main__':
    movies_metadata_clean = pd.read_csv("./dataset/movies_metadata_clean.csv", sep=",", low_memory=False)
    column_generes=movies_metadata_clean['genres'].tolist()

    print(column_generes[0])
    #dictionary=pd.DataFrame.from_records(column_generes[0])


    df2=movies_metadata_clean.explode('genres').reset_index(drop=True)
    df3=pd.DataFrame.from_records(df2['genres'].values)
    df2=df2.join(df3).drop(columns=['genres'])
    index=0
    print(df2.loc[1])

    """result = []
    for idx, row in movies_metadata_clean.iterrows():
        for dct in row['genres']:
            dct['name'] = row['name']
            result.append(dct)
    result = pd.DataFrame(result)
    result['rank'] = result['rank'].astype(np.int32)
    result['price'] = result['price'].str.replace('$', '')
    result['price'] = result['price'].astype('float')
    print(result)"""
    """for row in column_generes:
        dict= pd.json_normalize(row)
        print(dict)"""
