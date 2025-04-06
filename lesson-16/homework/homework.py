import pandas as pd
import sqlite3

# === Part 1: Reading Files ===

# 1. chinook.db - Read customers table
conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("\nCustomers Table (First 10 Rows):")
print(customers_df.head(10))
conn.close()

# 2. iris.json
iris_df = pd.read_json('iris.json')
print("\nIris Dataset Shape:", iris_df.shape)
print("Iris Dataset Columns:", iris_df.columns)

# 3. titanic.xlsx
titanic_df = pd.read_excel('titanic.xlsx')
print("\nTitanic Dataset (First 5 Rows):")
print(titanic_df.head())


# 5. movie.csv
movie_df = pd.read_csv('movie.csv')
print("\nRandom 10 Movies:")
print(movie_df.sample(10))


# === Part 2: Exploring DataFrames ===

# 1. iris.json - rename to lowercase, select sepal_length and sepal_width
iris_df.columns = iris_df.columns.str.lower()
sepal_df = iris_df[['sepallength', 'sepalwidth']]
print("\nSelected Sepal Columns:")
print(sepal_df.head())

# 2. titanic.xlsx - filter age > 30, count gender
above_30 = titanic_df[titanic_df['Age'] > 30]
gender_counts = above_30['Sex'].value_counts()
print("\nPassengers Age > 30 - Gender Counts:")
print(gender_counts)



# 4. movie.csv - duration > 120, sort by director_facebook_likes
long_movies = movie_df[movie_df['duration'] > 120]
sorted_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print("\nMovies > 120 min sorted by director_facebook_likes:")
print(sorted_movies.head())


# === Part 3: Challenges and Explorations ===

# iris.json - mean, median, std
print("\nIris Dataset Statistics:")
print("Mean:\n", iris_df.mean(numeric_only=True))
print("Median:\n", iris_df.median(numeric_only=True))
print("Std:\n", iris_df.std(numeric_only=True))

# titanic.xlsx - age stats
age_min = titanic_df['Age'].min()
age_max = titanic_df['Age'].max()
age_sum = titanic_df['Age'].sum()
print("\nTitanic Age Stats:")
print(f"Min: {age_min}, Max: {age_max}, Sum: {age_sum}")

# movie.csv - top director by likes, 5 longest movies
top_director = movie_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
print("\nDirector with Highest Total Facebook Likes:", top_director)

longest_movies = movie_df.nlargest(5, 'duration')[['movie_title', 'director_name']]
print("Top 5 Longest Movies:")
print(longest_movies)


