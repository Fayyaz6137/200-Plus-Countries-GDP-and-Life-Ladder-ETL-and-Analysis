# 🌍 GDP & Life Ladder ETL Pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline that integrates GDP data and Life Ladder data into a structured SQLite database.

---

## 📌 Project Overview

This project implements a modular ETL architecture using Python.

The pipeline:

1. Extracts GDP data from a CSV file
2. Extracts Life Ladder data from an API
3. Transforms and cleans both datasets
4. Integrates the datasets
5. Loads the final dataset into a SQLite database

---
## Visualizations
<img width="493" height="385" alt="Picture1" src="https://github.com/user-attachments/assets/0e9979a5-8802-4657-a2cd-09e67e02e627" />

The project includes:
- GDP vs Life Ladder regression plot
- Historical trend comparison
- Country-level happiness distribution


## See Power BI Dashboard
📌 Interactive dashboard available here:  
👉 **[Dashboard Link](https://app.powerbi.com/view?r=eyJrIjoiNmFkN2MyNmUtYmQyYi00ZTRhLTg4NTQtODlmMzM1YTM1NmUzIiwidCI6IjMyYjI3ZjU0LTA5ZmItNDhhZi05YzE3LTBmOThhNWQ1OThiZiIsImMiOjh9)**

---

## 🏗️ Architecture
```bash
Extract → Transform → Integrate → Load → SQLite
```
---


## Data Dictionary
| Column Name           | Data Type | Description                                                                                                                                                   | Example       |
| --------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------- |
| `Country name`        | String    | Name of the country for which the data is recorded.                                                                                                           | `Italia`      |
| `year`                | Integer   | Year in which the data was observed.                                                                                                                          | `2025`        |
| `Life Ladder`         | Float     | Numeric indicator representing a country-level Happiness Score.                                                                                               | `2.375`       |
| `Log GDP per capita`  | Float     | Numeric indicator representing a Logged Value of GDP Per Capita.                                                                                              | `7.697`       |

---

## 📂 Project Structure
```bash
gdp-life-ladder-etl/
│
├── main.py
├── Dockerfile
├── docker-compose.yml
├── notebooks/
│      ├── analysis Jupytor file
├── data/
│      ├── raw/ csv file
│      ├── processed/ sqllite3 db file
└── src/
│      ├── extractors/ 
│      │      ├── api_reader.py
│      │      ├── csv_reader.py
│      ├── transformers/ 
│      │      ├── api_data_transformer.py
│      │      ├── csv_data_transformer.py
│      │      ├── integration.py
│      ├── loaders/
│      │      ├── sqlite3_loader.py
│      └── utils/
│            ├── config.py
├── README.md.txt
├── PowerBI Dashboard Link.txt
└── requirements.txt
```

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Requests
- SQLite3
- Docker
- Docker Compose

---

## 🚀 How to Run

### Run Locally

```bash
pip install -r requirements.txt

python main.py
```
---

## 🐳 Run with Docker
```bash
docker compose up --build
```
The SQLite database file will be created inside the data/processed folder.

---

## 🔍 ETL Steps
1️⃣ Extract

* CSV Reader
* API Reader

2️⃣ Transform

* Data Cleaning
* Type Casting
* Filtering common countries

3️⃣ Integration

Merging datasets on country name

4️⃣ Load

Save final dataset into SQLite database

---

## 📊 Output

* Integrated dataset stored in SQLite database
* Cleaned and merged GDP + Life Ladder data

---

## 🎯 Key Learning Outcomes

* Modular ETL design
* Data integration from multiple sources
* SQLite database loading
* Dockerizing data pipelines
* Clean project structuring

---

## 📌 Future Improvements

* Add logging instead of print statements
* Add exception handling
* Add unit tests
* Add scheduling (Airflow / Cron)
* Containerize with PostgreSQL instead of SQLite