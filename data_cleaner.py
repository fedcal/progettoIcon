import pandas as pd
import numpy as np

def dataPreparation():
    #remove
    akas = pd.read_csv('./dataset/akas.csv', sep=",", low_memory=False)
    akas = akas.drop(columns=['attributes','region','language'])
    akas.to_csv('./dataset/akas.csv')

def mainDataCleaner():
   print("ciao")


