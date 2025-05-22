import json
import time
import random
from kafka import KafkaProducer

KAFKA_TOPIC_NAME = "sensor-suhu-gudang"
KAFKA_BOOTSTRAP_SERVERS = 'localhost:29092'

GUDANG_IDS = ["G1", "G2", "G3"]

# Inisialisasi producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    gudang_id = random.choice(GUDANG_IDS)
    suhu = random.randint(70, 85)
    
    # Sesekali suhu lebih tinggi
    if random.random() < 0.1:
        suhu = random.randint(81, 90)

    message = {
        "gudang_id": gudang_id,
        "suhu": suhu,
        "timestamp": time.time()
    }
    
    producer.send(KAFKA_TOPIC_NAME, message)
    print(f"Mengirim data suhu: {message}")
    time.sleep(1)
