import pandas as pd
import numpy as np

def main():
    #lettura dati da csv
    credits_csv=pd.read_csv("./dataset/credits.csv", sep=",")
    links_csv = pd.read_csv("./dataset/links.csv", sep=",")
    links_csv = pd.read_csv("./dataset/links_small.csv", sep=",")
    keywords_csv=pd.read_csv("./dataset/keywords.csv", sep=",")
    movies_metadata= pd.read_csv("./dataset/movies_metadata.csv", sep=",", low_memory=False)
    ratings=pd.read_csv("./dataset/ratings.csv", sep=",")
    ratings_small=pd.read_csv("./dataset/ratings_small.csv.csv",sep=",")

    #elimino le colonne da movies_metadata che non mi interessano
    movies_metadata_clean = movies_metadata.drop(columns=['belongs_to_collection', 'budget', 'homepage', 'imdb_id', 'poster_path', 'revenue', 'status', 'video'])
    movies_metadata_clean.to_csv('./dataset/movies_metadata_clean.csv', index=False)

    """#elimino le righe dal file keywords con campo vuoto
    keywords_csv_clean = keywords_csv
    rowindex = 0
    for row in keywords_csv_clean['keywords']:
        if row is not None and row == '[]':
            keywords_csv_clean.drop(rowindex, axis=0, inplace=True)
        rowindex += 1
    keywords_csv_clean.to_csv("./dataset/keywords_clean.csv")"""