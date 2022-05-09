import pandas as pd



if __name__ == '__main__':
    #calcolo i voti medi per ogni film
    movies = pd.read_csv('./dataset/movies.csv', sep=",", low_memory=False)
    ratings= pd.read_csv('./dataset/ratings.csv', sep=",", low_memory=False)


    merge_movies_ratings=pd.merge(movies,ratings,on=["movieId"],how="outer")
    number_of_votes=merge_movies_ratings.groupby(['movieId'])['movieId'].count()
    average_ratings=merge_movies_ratings.groupby('movieId').mean('rating')

    df_ratings = average_ratings.join(number_of_votes,lsuffix='_caller', rsuffix='_other')
    merge_movies_ratings = merge_movies_ratings.join(df_ratings,lsuffix='_caller', rsuffix='_other')
    mostRatedMovies = merge_movies_ratings.where("count >= 50")
    print(mostRatedMovies)

