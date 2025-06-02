import os
import pandas as pd
from pymongo import MongoClient
 
# Read Mongo credentials from environment (set in .env via docker-compose)
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME", "root")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "password")
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_DB   = os.getenv("MONGO_DB", "healthcare_dataset")
 
# Connect to MongoDB
uri = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:27017/"
client = MongoClient(uri)
db = client[MONGO_DB]
collection = db["patients"]
 
# Read the CSV
file_path = "/app/data/healthcare_dataset-20250506.csv"
df = pd.read_csv(file_path, sep=";")
 
# Normalize column names for Mongo
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
 
# 1) Check for nulls
null_counts = df.isnull().sum()
print("Null counts per column:")
print(null_counts)
 
# 2) Parse date columns (convert "DD/MM/YYYY" → ISO format)
df["date_of_admission"] = pd.to_datetime(
    df["date_of_admission"], dayfirst=True, errors="coerce"
)
df["discharge_date"] = pd.to_datetime(
    df["discharge_date"], dayfirst=True, errors="coerce"
)
 
# 3) (Optional) Fill any remaining nulls in string columns with empty string
#    and in numeric/date columns as you see fit.
df.fillna("", inplace=True)
 
# Convert to list of dicts and insert
documents = df.to_dict(orient="records")
collection.insert_many(documents)
 
print(f"{len(documents)} documents inserted into MongoDB.")