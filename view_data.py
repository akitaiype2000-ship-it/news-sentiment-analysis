import psycopg2

conn = psycopg2.connect(
    host="news-sentiment-db.cj0mi2u8yzvv.ap-south-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="NewsProject123!",
    port=5432
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM news;")

rows = cursor.fetchall()

print("\n===== NEWS DATA =====\n")

for row in rows:
    print(row)
    print("-" * 80)

cursor.close()
conn.close()