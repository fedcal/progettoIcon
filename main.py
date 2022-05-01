import pandas as pd
import numpy as np


if __name__ == '__main__':
    movies_metadata= pd.read_csv("./dataset/movies_metadata.csv", sep=",", low_memory=False)
    print(movies_metadata.columns)







