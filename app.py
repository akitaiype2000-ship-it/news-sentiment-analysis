import json
import boto3

import requests
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
api_key = "ba901fc4867d4cc3b1dcfc0f87949b3e"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)

data = response.json()
# Save raw JSON locally
with open("news_data.json", "w") as file:
    json.dump(data, file, indent=4)
s3 = boto3.client("s3")

bucket_name = "akita-news-sentiment-2026-1234-141485589054-ap-south-1-an"

s3.upload_file(
    "news_data.json",
    bucket_name,
    "news_data.json"
)

print("✅ Raw News JSON uploaded to Amazon S3")
# print(data)
# print(data["articles"][0])
# print(data["articles"][0]["title"])
# print(data["articles"][0]["source"]["name"])
# for article in data["articles"]:
#     print(article["title"])
pos=0
neg=0
neut=0
news_data=[]
for article in data["articles"]:

    title = article["title"]
    source = article["source"]["name"]
    author = article["author"]
    description = article["description"]
    published = article["publishedAt"]
    article_url = article["url"]

    # Sentiment Analysis
    blob = TextBlob(title)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
        pos += 1
    elif polarity < 0:
        sentiment = "Negative"
        neg += 1
    else:
        sentiment = "Neutral"
        neut += 1

    # Print article details
    print("Title:", title)
    print("Source:", source)
    print("Author:", author)
    print("Published:", published)
    print("Description:", description)
    print("URL:", article_url)
    print("Sentiment:", sentiment)
    print("Polarity:", polarity)
    print("-" * 80)

    # Save article data
    news_data.append({
        "Title": title,
        "Source": source,
        "Author": author,
        "Published": published,
        "Description": description,
        "URL": article_url,
        "Sentiment": sentiment,
        "Polarity": polarity
    })

# Print Summary
print("\n========== SUMMARY ==========")
print("Total Articles:", len(data["articles"]))
print("Positive:", pos)
print("Negative:", neg)
print("Neutral:", neut)

# Create DataFrame
df = pd.DataFrame(news_data)

# Save to CSV
df.to_csv("news_sentiment.csv", index=False)

print("\n✅ CSV file 'news_sentiment.csv' created successfully!")

labels=['Positive','Negative','Neutral']
values=[pos,neg,neut]

print(values)

plt.figure(figsize=(6,4))
plt.bar(labels, values)
plt.title("News Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Articles")
plt.tight_layout()
plt.savefig("graph.png")
plt.show()

print("Graph displayed")