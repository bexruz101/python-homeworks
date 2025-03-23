import requests
import random


API_KEY = "7212cf109775d84ae6fac56ca800c710"
BASE_URL = "https://api.themoviedb.org/3"


def get_genres():
    """Fetch available genres from TMDb API"""
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(url, params=params).json()

    genres = {
        genre["name"].lower(): genre["id"] for genre in response.get("genres", [])
    }
    return genres


def get_movies_by_genre(genre_id):
    """Fetch movies from a specific genre"""
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "with_genres": genre_id,
    }
    response = requests.get(url, params=params).json()
    return response.get("results", [])


def recommend_movie(genre_name):
    """Recommend a random movie from the chosen genre"""
    genres = get_genres()

    if genre_name.lower() not in genres:
        print("Invalid genre. Please try again.")
        return

    genre_id = genres[genre_name.lower()]
    movies = get_movies_by_genre(genre_id)

    if not movies:
        print("No movies found for this genre.")
        return

    movie = random.choice(movies)

    print("\n🎬 **Movie Recommendation** 🎬")
    print(f"Title: {movie['title']}")
    print(f"Overview: {movie['overview']}")
    print(f"Release Date: {movie['release_date']}")
    print(f"Rating: {movie['vote_average']} ⭐")


# User input for genre
user_genre = input("Enter a movie genre (e.g., Action, Comedy, Horror): ")
recommend_movie(user_genre)
