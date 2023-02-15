import os
import random

from imdb import Cinemagoer

os.environ["LANG"] = "ru_RU"

ia = Cinemagoer()


def get_random_movie():
    movies = ia.get_top250_movies()
    movie = movies[random.randint(1, 250)]
    return ia.get_movie(movie.movieID)


def get_film(movie_id):
    return ia.get_movie(movie_id)


if __name__ == "__main__":
    movie = get_random_movie()
    movie_detail = ia.get_movie(movie.movieID)
    print(dict(movie_detail))
