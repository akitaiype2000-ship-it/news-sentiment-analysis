import requests
from textblob import TextBlob
import psycopg2

# ---------- News API ----------
api_key = "ba901fc4867d4cc3b1dcfc0f87949b3e"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)
data = response.json()

# ---------- PostgreSQL Connection ----------
conn = psycopg2.connect(
    host="news-sentiment-db.cj0mi2u8yzvv.ap-south-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="NewsProject123!",
    port=5432
)

cursor = conn.cursor()

# ---------- Insert Data ----------
for article in data["articles"]:

    title = article["title"]
    source = article["source"]["name"]
    author = article["author"]
    description = article["description"]
    published = article["publishedAt"]
    news_url = article["url"]

    polarity = TextBlob(title).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    cursor.execute("""
        INSERT INTO news
        (title, source, author, published, description, url, sentiment, polarity)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        title,
        source,
        author,
        published,
        description,
        news_url,
        sentiment,
        polarity
    ))

conn.commit()

print("✅ Data inserted successfully!")

cursor.close()
conn.close()