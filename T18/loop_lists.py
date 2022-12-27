# Creating list of favorite movies
favorite_movies = ["The Godfather", "La Haine", "Cidade de Deus", "Blood in Blood Out", "Pumping Iron"]

# Looping through the list using enumerate wit the start argument set to 1 (opposed to the default 0)
for position, movie in enumerate(favorite_movies, start = 1):
    print(f"Movie {position}: {movie}")