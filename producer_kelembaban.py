import json
import time
import random
from kafka import KafkaProducer

KAFKA_TOPIC_NAME = "sensor-kelembaban-gudang"
KAFKA_BOOTSTRAP_SERVERS = 'localhost:29092'

GUDANG_IDS = ["G1", "G2", "G3"]

# Inisialisasi producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    gudang_id = random.choice(GUDANG_IDS)
    kelembaban = random.randint(60, 75)
    
    # Sesekali kelembaban lebih tinggi
    if random.random() < 0.1:
        kelembaban = random.randint(71, 85)

    data = {
        "gudang_id": gudang_id,
        "kelembaban": kelembaban,
        "timestamp": time.time()
    }
    
    producer.send(KAFKA_TOPIC_NAME, data)
    print(f"Mengirim data kelembaban: {data}")
    time.sleep(1)
