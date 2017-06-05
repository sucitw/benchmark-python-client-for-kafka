from kafka import KafkaConsumer, KafkaProducer
from settings import BOOTSTRAP_SERVERS, TOPICS, MSG

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
producer.send(TOPICS, MSG.encode('utf-8'))