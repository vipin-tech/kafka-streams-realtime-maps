from pykafka import KafkaClient
import json
from datetime import datetime
import uuid, time

def get_kafka_client():
    return KafkaClient(hosts='localhost:9092')

def generate_uuid():
    return uuid.uuid4()

def get_bus_coordinates():
    inp_data = open('../data/busdata_2.json')
    coordinates = json.load(inp_data)['features'][0]['geometry']['coordinates']

    return coordinates

def get_checkpoint(coordinates):
    i = 0
    while i<len(coordinates):
        data = dict()
        data['busline'] = '39a'
        data['key'] = data['busline'] + '_' + str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['latitude'] = coordinates[i][1]
        data['longitude'] = coordinates[i][0]
        message = json.dumps(data)

        producer.produce(message.encode('ascii'))
        time.sleep(1)

        if i == len(coordinates)-1:
            i = 0
        else:
            i+=1

kafka_client = get_kafka_client()

topic = kafka_client.topics['busdata']
producer = topic.get_sync_producer()

coordinates = get_bus_coordinates()

get_checkpoint(coordinates)
