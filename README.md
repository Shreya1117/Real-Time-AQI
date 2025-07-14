# Real-Time-AQI
A real-time system that streams air quality data from multiple cities using the OpenWeatherMap API and Kafka, stores it in HDFS, and analyzes it using Apache Spark.


This project collects, stores, analyzes, and visualizes real-time air quality data from multiple global cities using:

- OpenWeatherMap API  
- Apache Kafka  
- Apache Spark  
- Hadoop HDFS  
- Matplotlib (for visualization)

---

## 📦 Features

- Collects real-time AQI data for multiple cities.
- Streams data using Kafka.
- Stores air quality data in HDFS.
- Performs analysis using PySpark (e.g., average pollutant levels).
- Visualizes air quality statistics using Matplotlib.

---

## 🛠️ System Architecture
OpenWeatherMap API --> Kafka Producer --> Kafka Broker --> Kafka Consumer --> HDFS --> Spark Job --> Matplotlib


---

## 🔧 Setup Instructions

### 1. Clone & Start Hadoop, Spark, and Kafka Cluster

Use the excellent [hadoop-docker-compose](https://github.com/dhzdhd/hadoop-docker-compose) setup:

```bash
git clone https://github.com/dhzdhd/hadoop-docker-compose.git
cd hadoop-docker-compose
docker-compose up -d

### 2. Access the Spark Container

docker exec -it spark-master bash

Install required Python libraries inside the container (if not already):

pip install pandas matplotlib seaborn kafka-python requests

---

## 📁 Project Structure

air_quality_project/
├── producer.py             # Fetches AQI data from API and sends to Kafka
├── consumer.py             # Reads Kafka data and writes to HDFS
├── air_quality_stream.py   # Spark job to clean, analyze, and visualize data
└── README.md               # Project instructions
---

## 🌐 OpenWeatherMap API Setup

    Go to OpenWeatherMap and sign up.

    Get your API key.

    Replace the placeholder in producer.py:

API_KEY = "your_api_key_here"

---

## 🚀 How to Run the Project

    ⚠️ Run each script in a separate terminal or background session inside the spark-master container.

### 1. Start the Kafka Producer

python producer.py

This fetches data from the OpenWeatherMap API for selected cities every 5 minutes and sends it to Kafka topic air_quality.
### 2. Start the Kafka Consumer

python consumer.py

This reads from the Kafka topic and stores JSON data in HDFS at /user/lab_project/air_quality.json.
### 3. Run the Spark Job for Analysis & Visualization

python air_quality_stream.py

This reads data from HDFS, performs analysis using Spark, and visualizes pollutant levels using Matplotlib.

---

📚 Dependencies

    Python 3.10+

    Apache Kafka

    Apache Spark with PySpark

    Hadoop HDFS

    pandas, matplotlib, seaborn, kafka-python, requests



