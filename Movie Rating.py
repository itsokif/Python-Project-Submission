import requests
import pandas as pd

def fetch_movie_details(movie_id, api_key):
    """Fetch detailed information for a single movie using its IMDb ID."""
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={movie_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_movies_based_on_genre(search_term, genre, api_key):
    """Fetch movies based on a search term and filter them by genre."""
    search_url = f"http://www.omdbapi.com/?apikey={api_key}&s={search_term}&type=movie"
    search_response = requests.get(search_url)
    movies_in_genre = []
    
    if search_response.status_code == 200:
        search_data = search_response.json()
        if search_data['Response'] == 'True':
            for movie in search_data.get('Search', []):
                movie_details = fetch_movie_details(movie['imdbID'], api_key)
                if movie_details and 'Genre' in movie_details and genre.lower() in movie_details['Genre'].lower():
                    movies_in_genre.append({
                        'Title': movie_details['Title'],
                        'Year': movie_details['Year'],
                        'Genre': movie_details['Genre']
                    })
        else:
            print(search_data['Error'])
    else:
        print(f"Error searching movies: HTTP {search_response.status_code}")
    
    return movies_in_genre

def save_movies_to_csv(movies, genre):
    """Save the list of filtered movies to a CSV file."""
    df = pd.DataFrame(movies)
    filename = f"{genre}_movies.csv"
    df.to_csv(filename, index=False)
    print(f"Saved {len(movies)} movies to {filename}")

def main():
    api_key = "4cfde676"  # Replace with your actual API key
    genre = input("Enter the movie genre you are interested in: ").lower().strip()
    print(f"Fetching movies that match genre: {genre}")
    movies = fetch_movies_based_on_genre("movie", genre, api_key)
    if movies:
        save_movies_to_csv(movies, genre)
        print("Movies fetched and filtered successfully.")
        try:
            df = pd.read_csv(f"{genre}_movies.csv")
            print("Here are some movies we found:")
            print(df.head())
        except pd.errors.EmptyDataError:
            print("No data available to display.")
    else:
        print("No movies found for the specified genre. Please try a different search.")

if __name__ == "__main__":
    main()
