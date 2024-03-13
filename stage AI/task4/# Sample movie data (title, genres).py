# Sample movie data (ID, Title, Genres)
movies = [
    (1, "Toy Story", ["Animation", "Children", "Comedy"]),
    (2, "Jumanji", ["Adventure", "Children", "Fantasy"]),
    (3, "Jurassic Park", ["Action", "Adventure", "Sci-Fi"]),
    (4, "Forrest Gump", ["Comedy", "Drama", "Romance"]),
    (5, "Matrix", ["Action", "Sci-Fi"]),
    (6, "Titanic", ["Drama", "Romance"]),
    (7, "Shrek", ["Animation", "Adventure", "Comedy"])
]

# Function to recommend movies based on user preferences
def recommend_movies(user_preferences, movies, top_n=3):
    movie_scores = {}  # Dictionary to store movie scores

    for movie_id, title, genres in movies:
        score = 0
        for preference in user_preferences:
            if preference in genres:
                score += 1  # Increment score for each matching genre
        movie_scores[title] = score

    # Sort movies by score in descending order
    sorted_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)

    # Return top N recommended movies
    return [movie[0] for movie in sorted_movies[:top_n]]

# Example user preferences
user_preferences = ["Adventure", "Sci-Fi", "Action"]

# Recommend movies based on user preferences
recommended_movies = recommend_movies(user_preferences, movies)
print("Recommended movies for you:")
for movie in recommended_movies:
    print("-", movie)
