import boto3

# Create S3 client
s3 = boto3.client("s3")

# Your bucket name
bucket_name = "akita-news-sentiment-2026-1234-141485589054-ap-south-1-an"

# Upload sample.json
s3.upload_file("sample.json", bucket_name, "sample.json")

print("✅ File uploaded successfully!")