import pandas as pd
import numpy as np

def main():
    #lettura dati da csv
    credits_csv=pd.read_csv("./dataset/credits.csv", sep=",")
    links_csv = pd.read_csv("./dataset/links.csv", sep=",")
    links_csv = pd.read_csv("./dataset/links_small.csv", sep=",")
    keywords_csv=pd.read_csv("./dataset/keywords.csv", sep=",")
    movies_metadata= pd.read_csv("./dataset/movies_metadata.csv", sep=",", low_memory=False)

    #elimino le colonne da movies_metadata che non mi interessano
    movies_metadata_clean = movies_metadata.drop(columns=['belongs_to_collection', 'budget', 'homepage', 'imdb_id', 'poster_path', 'production_companies','production_countries', 'revenue', 'status', 'video'])
    movies_metadata_clean.to_csv('./dataset/movies_metadata_clean.csv', index=True)