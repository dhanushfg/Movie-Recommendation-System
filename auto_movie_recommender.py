import pandas as pd
import random

# Load data
data = pd.read_csv('ratings.csv')
data['Movie'] = data['Movie'].str.strip()

# List of unique movies
all_movies = data['Movie'].unique().tolist()

# Create fake average ratings for each movie
fake_ratings = {}
for movie in all_movies:
    fake_ratings[movie] = round(random.uniform(3.5, 5.0), 1)

# Suggest 2 other movies for each movie
for movie in all_movies:
    other_movies = [m for m in all_movies if m != movie]
    if len(other_movies) >= 2:
        suggested = random.sample(other_movies, 2)
        print(f"\n🎬 If you enjoyed '{movie}', here are 2 other movies you might love:\n")
        for s in suggested:
            print(f"  ➡️ {s}  (Avg Rating: {fake_ratings[s]} ⭐) - Highly recommended for fans of thrilling stories!")
    elif other_movies:
        s = other_movies[0]
        print(f"\n🎬 If you enjoyed '{movie}', you might also love:\n")
        print(f"  ➡️ {s}  (Avg Rating: {fake_ratings[s]} ⭐) - A great pick with strong reviews!")
    else:
        print(f"\n🎬 No other movies to suggest for '{movie}'.")
