from kafka import KafkaConsumer
import json
import os
import uuid

consumer = KafkaConsumer(
    'air_quality',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

hdfs_path = '/user/lab_project/'  # HDFS target folder

for message in consumer:
    data = message.value
    filename = f"/tmp/air_quality_{uuid.uuid4()}.json"
    
    with open(filename, 'w') as f:
        f.write(json.dumps(data) + "\n")
    
    os.system(f"hdfs dfs -put {filename} {hdfs_path}")
    os.remove(filename)

