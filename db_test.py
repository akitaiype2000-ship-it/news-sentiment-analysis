import psycopg2

try:
    conn = psycopg2.connect(
        host="news-sentiment-db.cj0mi2u8yzvv.ap-south-1.rds.amazonaws.com",
        database="postgres",
        user="postgres",
        password="NewsProject123!",
        port=5432
    )

    print("Connected Successfully!")

    conn.close()

except Exception as e:
    print(e)