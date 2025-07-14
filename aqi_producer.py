from kafka import KafkaProducer
import requests
import json
import time

API_KEY = "your_api_key"

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

CITIES = {
    "Delhi": {"lat": 28.6139, "lon": 77.2090},
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "London": {"lat": 51.5074, "lon": -0.1278},
}
# Add more cities if required

while True:
    for city, coords in CITIES.items():
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={coords['lat']}&lon={coords['lon']}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            data["city"] = city
            print(f"Sending data: {data}")
            producer.send('air_quality', value=data)
    time.sleep(300)  # 5 minutes

