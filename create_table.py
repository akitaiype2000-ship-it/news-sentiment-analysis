import psycopg2

conn = psycopg2.connect(
    host="news-sentiment-db.cj0mi2u8yzvv.ap-south-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="NewsProject123!",
    port=5432
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS news (
    id SERIAL PRIMARY KEY,
    title TEXT,
    source TEXT,
    author TEXT,
    published TIMESTAMP,
    description TEXT,
    url TEXT,
    sentiment VARCHAR(20),
    polarity FLOAT
);
""")

conn.commit()

print("Table created successfully!")

cursor.close()
conn.close()