# 🏥 Healthcare ETL Pipeline with MongoDB

This project sets up an ETL pipeline that ingests CSV healthcare data into MongoDB using Python, Docker, and Jupyter Notebooks. It includes real-time file monitoring, data cleaning, insertion into MongoDB, and data exploration using Jupyter.

---

## 📁 Project Structure

```
.
├── data/                    # Folder for input CSV files
├── etl/
│   └── etl.py     # ETL script that watches and ingests CSV
├── notebooks/
│      
├── .env                    # MongoDB credentials
├── docker-compose.yml      # Docker services: MongoDB, Jupyter, etc.
├ 
└── README.md               # Project documentation
```

---

## ⚙️ Technologies Used

- Python 3.11
- Docker & Docker Compose
- MongoDB + Mongo Express
- Jupyter Notebook (scipy-notebook)
- Python Libraries:
  - `pandas`
  - `pymongo`
  - `watchdog`
  - `python-dotenv`

---

## 🚀 Getting Started



### 1. Configure Environment Variables

Create a `.env` file:

```
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=password
MONGO_HOST=mongo
```

### 2. Start the Services

```bash
docker-compose up -d
```

- MongoDB: `localhost:27017`
- Mongo Express: [http://localhost:8082](http://localhost:8082)
- Jupyter Notebook: [http://localhost:9988](http://localhost:9988)

---

## 🧪 Running the ETL Script


It will:
- Watch the `/data` folder
- Load new CSV files
- Clean the data
- Insert into MongoDB `patients` collection

---

## 📊 Exploring the Data

Open `notebooks/analysis.ipynb` in Jupyter and explore:

- Patients admitted after Jan 1, 2023
- Patients older than 50
- Patients named “Thomas”
- Patient counts per condition
- Patients taking specific medications (e.g., Lipitor)

---

## 🧱 Proposed MongoDB Schema

Example document:

```json
{
  "name": "Alice Johnson",
  "age": 67,
  "date_of_admission": ISODate("2023-03-21T00:00:00Z"),
  "discharge_date": ISODate("2023-03-28T00:00:00Z"),
  "medical_condition": "Diabetes",
  "medications": ["Metformin", "Lipitor"]
}
```

- Embedded medications list for simplicity
- Single collection: no need for references

---



## 👩‍💻 Author

Created with ❤️ by **Wiem Ben Ameur**
