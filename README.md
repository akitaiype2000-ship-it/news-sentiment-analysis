# 📰 News Sentiment Analysis Dashboard

An end-to-end News Sentiment Analysis application built using **Python**, **PostgreSQL**, **Docker**, **Streamlit**, and **Amazon Web Services (AWS)**.

The application collects news articles, performs sentiment analysis, stores the processed data in an Amazon RDS PostgreSQL database, and presents the results through an interactive Streamlit dashboard deployed on Amazon ECS Fargate.

---

## 🚀 Features

- 📰 Fetches the latest news articles
- 😊 Performs sentiment analysis on news headlines and descriptions
- 🗄️ Stores processed data in Amazon RDS PostgreSQL
- 📊 Interactive Streamlit dashboard
- 📈 Visualizes sentiment distribution using charts
- 🐳 Dockerized application
- ☁️ Deployed on Amazon ECS Fargate
- 🔒 Secure cloud deployment using AWS Security Groups

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries
- Streamlit
- Pandas
- SQLAlchemy
- Psycopg2
- TextBlob

### Database
- PostgreSQL (Amazon RDS)

### Cloud Services
- Amazon ECS
- Amazon ECR
- Amazon RDS
- AWS Fargate

### Containerization
- Docker

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
NewsSentimentProject/
│
├── app.py
├── dashboard.py
├── create_table.py
├── insert_data.py
├── view_data.py
├── upload_to_s3.py
├── db_test.py
├── requirements.txt
├── Dockerfile
├── README.md
└── news_sentiment.csv
```

---

## ⚙️ Project Workflow

```
Latest News Articles
          │
          ▼
    Sentiment Analysis
          │
          ▼
 Amazon RDS PostgreSQL
          │
          ▼
      Docker Image
          │
          ▼
      Amazon ECR
          │
          ▼
 Amazon ECS (Fargate)
          │
          ▼
 Streamlit Dashboard
```

---

## 📊 Dashboard

The dashboard provides:

- Latest news articles
- Sentiment labels
- Polarity scores
- Sentiment distribution chart
- Interactive data visualization

---

## 🐳 Docker

### Build Docker Image

```bash
docker build -t news-sentiment .
```

### Run Docker Container

```bash
docker run -p 8501:8501 news-sentiment
```

---

## ☁️ AWS Deployment

The application is deployed using:

- Amazon Elastic Container Registry (ECR)
- Amazon Elastic Container Service (ECS)
- AWS Fargate
- Amazon RDS PostgreSQL
- AWS Security Groups

---

## ▶️ Run Locally

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Launch Dashboard

```bash
streamlit run dashboard.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

## 📸 Screenshots

### Dashboard
<img width="1857" height="821" alt="Screenshot 2026-09-04 121926" src="https://github.com/user-attachments/assets/066712f5-e248-4baa-94f5-cd22ecf5f400" />
> <img width="1901" height="702" alt="Screenshot 2026-09-04 121859" src="https://github.com/user-attachments/assets/acda5467-09ee-49e5-8f38-9592f3839d0f" />
> <img width="1881" height="812" alt="Screenshot 2026-09-04 121838" src="https://github.com/user-attachments/assets/a1300146-d222-4375-9fa2-0a0250a959b5" />


Example:

```
images/dashboard.png
```

---

## 📈 Future Enhancements

- Real-time news updates
- Advanced NLP sentiment models
- User authentication
- Search and filter news articles
- Historical sentiment trends
- Scheduled automated data ingestion
- Interactive analytics dashboard

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Python Programming
- Sentiment Analysis
- PostgreSQL Database
- SQLAlchemy ORM
- Docker Containerization
- Amazon RDS
- Amazon ECR
- Amazon ECS
- AWS Fargate
- Cloud Deployment
- Git & GitHub

---

## 👨‍💻 Author

**Akita**

GitHub: https://github.com/akitaiype2000-ship-it

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
