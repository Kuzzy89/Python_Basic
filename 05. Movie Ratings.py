import sys
number_of_movies = int(input())

sum_ratings = 0
low_rating = sys.maxsize
max_rating = -sys.maxsize
low_movie_name = ""
max_movie_name = ""

for count in range(number_of_movies):
    name_of_movie = input()
    rating = float(input())

    sum_ratings += rating

    if rating > max_rating:
        max_rating = rating
        max_movie_name = name_of_movie

    if rating < low_rating:
        low_rating = rating
        low_movie_name = name_of_movie

aver = float(sum_ratings / number_of_movies)
print(f"{max_movie_name} is with highest rating: {max_rating:.1f}")
print(f"{low_movie_name} is with lowest rating: {low_rating:.1f}")
print(f"Average rating: {aver:.1f}")