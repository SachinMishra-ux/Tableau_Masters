import pandas as pd
import random
import numpy as np

# -------------------------
# 1. MESSY MOVIES CSV FILE
# -------------------------

rows = 40   # number of rows

movie_ids = list(range(1001, 1001 + rows))
titles = [f"Movie {i}" for i in movie_ids]
years = [random.choice(range(2000, 2025)) for _ in movie_ids]
genres = [random.choice(["Action", "Comedy", "Drama", "Sci-Fi", "Horror"]) for _ in movie_ids]
domestic = [round(random.uniform(1e6, 150e6), 2) for _ in movie_ids]
international = [round(random.uniform(1e6, 200e6), 2) for _ in movie_ids]
prod_companies = [random.choice([
    "StudioA|USA|Founded 1995",
    "StudioB|UK|Founded 1984",
    "StudioC|Canada|Founded 2001",
    "StudioD|India|Founded 1998"
]) for _ in movie_ids]

df_movies = pd.DataFrame({
    "Movie_ID": movie_ids,
    "Title": titles,
    "Release_Year": years,
    "Genre": genres,
    "Domestic_BoxOffice": domestic,
    "International_BoxOffice": international,
    "Production_Company": prod_companies
})

# Introduce messiness
df_movies.loc[5, "Title"] = None                         # Missing title
df_movies.loc[8, "Genre"] = ""                           # Empty string
df_movies.loc[12, "Production_Company"] = "Merged Cell"  # Bad formatting
df_movies.loc[15, "Release_Year"] = "20O4"               # Letter O instead of zero
df_movies.loc[18, "Domestic_BoxOffice"] = "N/A"          # Wrong data type
df_movies.loc[22, "International_BoxOffice"] = np.nan    # Missing number
df_movies.loc[25, "Title"] = "Movie, Part 1"             # Comma issues

df_movies.to_csv("messy_movies.csv", index=False)


# -------------------------
# 2. MESSY RATINGS CSV FILE
# -------------------------

critic_score = [round(random.uniform(40, 100), 2) for _ in movie_ids]
audience_score = [round(random.uniform(40, 100), 2) for _ in movie_ids]
critic_reviews = [random.randint(5, 200) for _ in movie_ids]
audience_reviews = [random.randint(20, 1000) for _ in movie_ids]

df_ratings = pd.DataFrame({
    "Movie_ID": movie_ids,
    "Critic_Score": critic_score,
    "Audience_Score": audience_score,
    "Num_Critic_Reviews": critic_reviews,
    "Num_Audience_Reviews": audience_reviews
})

# Messiness
df_ratings.loc[3, "Critic_Score"] = "??"
df_ratings.loc[7, "Audience_Score"] = None
df_ratings.loc[10, "Num_Critic_Reviews"] = "undefined"
df_ratings.loc[15, "Num_Audience_Reviews"] = ""

df_ratings.to_csv("messy_ratings.csv", index=False)


# ----------------------------------------
# 3. MESSY SOCIAL MENTIONS EXCEL FILE
# ----------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

rows_mentions = []
for movie_id in movie_ids[:30]:   # only 30 movies × 6 months
    for m in months:
        rows_mentions.append({
            "Movie_ID": movie_id,
            "Month": m,
            "Twitter_Mentions": random.randint(100, 10000),
            "Instagram_Mentions": random.randint(50, 8000),
            "Facebook_Mentions": random.randint(10, 4000)
        })

df_mentions = pd.DataFrame(rows_mentions)

# Add issues
df_mentions.loc[4, "Month"] = "Merged Cell"
df_mentions.loc[9, "Twitter_Mentions"] = None
df_mentions.loc[12, "Instagram_Mentions"] = "NaN"
df_mentions.loc[20, "Facebook_Mentions"] = "----"

df_mentions.to_excel("messy_mentions.xlsx", index=False)

print("MESSY FILES CREATED SUCCESSFULLY!")
print("- messy_movies.csv")
print("- messy_ratings.csv")
print("- messy_mentions.xlsx")
