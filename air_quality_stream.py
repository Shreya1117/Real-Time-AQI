from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode
import matplotlib.pyplot as plt

# Initialize Spark session
spark = SparkSession.builder \
    .appName("AirQualityAnalysis") \
    .getOrCreate()

# Disable Arrow (avoid Py4J error)
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "false")

# Read all JSON files from HDFS
hdfs_input_path = "hdfs://master:9000/user/lab_project/"
df = spark.read.json(hdfs_input_path)

# Flatten nested structure
exploded = df.select(
    col("city"),
    col("coord.lat").alias("latitude"),
    col("coord.lon").alias("longitude"),
    explode("list").alias("reading")
)

flat_df = exploded.select(
    "city", "latitude", "longitude",
    col("reading.main.aqi").alias("aqi"),
    col("reading.components.*"),
    col("reading.dt").alias("timestamp")
)

# Show cleaned data
flat_df.show(truncate=False)

# Descriptive statistics
print("=== Descriptive Statistics ===")
flat_df.describe(["co", "no2", "o3", "so2", "pm2_5", "pm10", "nh3"]).show()

# Average AQI and PM2.5 per city
print("=== Average AQI and PM2.5 by City ===")
avg_df = flat_df.groupBy("city") \
    .avg("aqi", "pm2_5") \
    .withColumnRenamed("avg(aqi)", "avg_aqi") \
    .withColumnRenamed("avg(pm2_5)", "avg_pm2_5")

avg_df.show()

# Visualization
pdf_plot = avg_df.toPandas()
plt.figure(figsize=(8, 6))
plt.bar(pdf_plot["city"], pdf_plot["avg_pm2_5"], color="salmon")
plt.title("Average PM2.5 Levels by City")
plt.ylabel("PM2.5 (µg/m³)")
plt.xlabel("City")
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

# Stop Spark
spark.stop()


