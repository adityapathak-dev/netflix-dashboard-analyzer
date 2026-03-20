import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")

df = df.rename(columns={"listed_in": "genre"})

before_2000 = 0
after_2000 = 0

for year in df["release_year"]:
    if year < 2000:
        before_2000 += 1
    else:
        after_2000 += 1

labels = ["Before 2000", "After 2000"]
values = [before_2000, after_2000]

year_counts = df["release_year"].value_counts().sort_index()

country_series = df["country"].str.split(", ").explode()
top_countries = country_series.value_counts().head(10)

rating_counts = df["rating"].value_counts()

genre_series = df["genre"].str.split(", ").explode()
top_genres = genre_series.value_counts().head(10)

fig, axes = plt.subplots(3, 2, figsize=(15, 12))

fig.suptitle("Netflix Content Analysis Dashboard", fontsize=18)

sns.barplot(x=labels, y=values, ax=axes[0][0])
axes[0][0].set_title(" Before vs After 2000")
axes[0][0].set_ylabel("movies and shows ")

sns.countplot(x="type", data=df, ax=axes[0][1])
axes[0][1].set_title("Movies vs TV Shows")
axes[0][1].set_xlabel("")

sns.lineplot(x=year_counts.index, y=year_counts.values, ax=axes[1][0])
axes[1][0].set_title("Content Growth by Year")
axes[1][0].set_xlabel("Year")
axes[1][0].set_ylabel("Titles")

sns.barplot(x=top_countries.values, y=top_countries.index, ax=axes[1][1])
axes[1][1].set_title("Top 10 Countries")

sns.barplot(x=rating_counts.index, y=rating_counts.values, ax=axes[2][0])
axes[2][0].set_title("Ratings Distribution")
axes[2][0].tick_params(axis="x", rotation=45)

sns.barplot(x=top_genres.values, y=top_genres.index, ax=axes[2][1])
axes[2][1].set_title("Top 10 Genres")
axes[2][1].set_ylabel("Genre")
plt.tight_layout()
plt.savefig("netflix_dashboard.png")
plt.show()
