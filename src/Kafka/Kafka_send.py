#from email.contentmanager import get_non_text_content

from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['alma-gncon:9092'],  # Replace with your Kafka broker addresses
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
print(">>>>>>")
producer.send('quickstart-events', {'key': 'Esta es una prueba'})
producer.flush()
print("Message published")