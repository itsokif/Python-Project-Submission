Movie Suggestion App
This Python script interacts with the OMDB API to fetch and filter movies based on user-specified genres. It allows users to input a genre, retrieves movies matching that genre from the API, and saves the filtered data to a CSV file. The script utilizes the requests library for API calls and pandas for data manipulation.

Setup
Prerequisites:
![pandas](https://github.com/itsokif/Python-Project-Submission/assets/174767063/ccb15c96-88cc-498e-bfdc-c203c97fde90)

Python 3.x installed on your system.
Install necessary libraries:
bash
Copy code
pip install requests pandas
Obtain an API Key:

Obtain an API key from OMDB API.
Replace "4cfde676" in the script with your actual OMDB API key.
Run the Script:

Execute the script movie_suggestion.py using Python:
bash
Copy code
python movie_suggestion.py
Usage
Enter Genre:

![1st](https://github.com/itsokif/Python-Project-Submission/assets/174767063/b53b852e-2453-4a9e-b70b-9d36b4ad8378)

Upon running the script, enter a movie genre when prompted (e.g., action, comedy, drama).
Fetching Movies:

![2nd](https://github.com/itsokif/Python-Project-Submission/assets/174767063/0445d2a4-04e5-4baf-8431-455102579748)


The script will fetch movies from OMDB API based on the entered genre.
It will filter and save the retrieved movies to a CSV file {genre}_movies.csv.
Displaying Results:

If movies are found and saved successfully, it will display the top movies found.
If no movies are found for the specified genre, it will notify the user to try a different search.
Error Handling:

The script includes basic error handling for HTTP request failures and empty data scenarios.
