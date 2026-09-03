# News Sentiment Analysis Project

## Overview

This project is a Python-based News Sentiment Analysis application that fetches the latest news using the NewsAPI, analyzes the sentiment of news headlines using TextBlob, stores the results in an AWS RDS PostgreSQL database, uploads the generated CSV file to Amazon S3, and visualizes the sentiment distribution using Matplotlib.

---

## Features

- Fetches live news from NewsAPI
- Performs sentiment analysis using TextBlob
- Classifies news as Positive, Negative, or Neutral
- Stores news data in PostgreSQL (AWS RDS)
- Exports results to a CSV file
- Uploads CSV file to Amazon S3
- Displays sentiment analysis using a bar chart

---

## Technologies Used

- Python
- NewsAPI
- TextBlob
- Pandas
- Matplotlib
- PostgreSQL
- AWS RDS
- AWS S3
- Boto3
- Psycopg2

---

## Project Structure

```
NewsSentimentProject/
│
├── app.py
├── create_table.py
├── db_test.py
├── insert_data.py
├── view_data.py
├── upload_to_s3.py
├── s3test.py
├── test.py
├── news_data.json
├── news_sentiment.csv
├── graph.png
└── sample.json
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/NewsSentimentProject.git
```

Go to the project folder:

```bash
cd NewsSentimentProject
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Required Libraries

```
requests
textblob
pandas
matplotlib
psycopg2-binary
boto3
```

---

## How to Run

### 1. Test Database Connection

```bash
python db_test.py
```

### 2. Create Database Table

```bash
python create_table.py
```

### 3. Fetch News and Insert into Database

```bash
python insert_data.py
```

### 4. View Stored Data

```bash
python view_data.py
```

### 5. Upload CSV to Amazon S3

```bash
python upload_to_s3.py
```

---

## Output

- Latest news fetched from NewsAPI
- Sentiment analysis results
- CSV file containing analyzed news
- Sentiment distribution graph
- Data stored in AWS PostgreSQL
- CSV uploaded to Amazon S3

---

## Future Improvements

- Build a Flask/FastAPI web application
- Add a dashboard for visualization
- Schedule automatic news updates
- Deploy the project to AWS

---

## Author

**Akita**