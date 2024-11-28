import uuid
from datetime import datetime


class PhoneRepository:
    def __init__(self, driver):
        self.driver = driver

    def create_phone_interaction(self, interaction_data):
        with self.driver.session() as session:
            query = """
            MERGE (sender:Device {sender_id: $sender_id, 
                                name: $sender_name,
                                brand: $sender_brand,
                                model: $sender_model ,
                                os: $sender_os,
                                latitude: $sender_latitude,
                                longitude: $sender_longitude,
                                altitude_meters: $sender_altitude_meters,
                                accuracy_meters: $sender_accuracy_meters
                                })
            MERGE (receiver:Device {receiver_id: $receiver_id
                                name: $receiver_name,
                                brand: $receiver_brand,
                                model: $receiver_model ,
                                os: $receiver_os,
                                latitude: $receiver_latitude,
                                longitude: $receiver_longitude,
                                altitude_meters: $receiver_altitude_meters,
                                accuracy_meters: $receiver_accuracy_meters
                                })
            CREATE (sender)-[i:INTERACTION{
                       from_device: $from_device,
                       to_device: $to_device,
                       method: $method,
                       bluetooth_version: $bluetooth_version,
                       signal_strength_dbm: $signal_strength_dbm,
                       distance_meters: $distance_meters,
                       duration_seconds: $duration_seconds,
                       timestamp: $timestamp
            }
            ]->(receiver)
            """
            result = session.run(query, {
                'sender_id': interaction_data['devices'][0]['id'],
                'sender_name': interaction_data['devices'][0]['name'],
                'sender_brand': interaction_data['devices'][0]['brand'],
                'sender_model': interaction_data['devices'][0]['model'],
                'sender_os': interaction_data['devices'][0]['os'],
                'sender_latitude': interaction_data['devices'][0]['latitude'],
                'sender_longitude': interaction_data['devices'][0]['longitude'],
                'sender_altitude_meters': interaction_data['devices'][0]['altitude_meters'],
                'sender_accuracy_meters': interaction_data['devices'][0]['accuracy_meters'],
                'receiver_id': interaction_data['devices'][1]['id'],
                'receiver_name': interaction_data['devices'][1]['name'],
                'receiver_brand': interaction_data['devices'][1]['brand'],
                'receiver_model': interaction_data['devices'][1]['model'],
                'receiver_os': interaction_data['devices'][1]['os'],
                'receiver_latitude': interaction_data['devices'][1]['latitude'],
                'receiver_longitude': interaction_data['devices'][1]['longitude'],
                'receiver_altitude_meters': interaction_data['devices'][1]['altitude_meters'],
                'receiver_accuracy_meters': interaction_data['devices'][1]['accuracy_meters'],
                'interaction_id': str(uuid.uuid4()),
                'from_device': interaction_data['interaction']['from_device'],
                'to_device': interaction_data['interaction']['to_device'],
                'method': interaction_data['interaction']['method'],
                'bluetooth_version': interaction_data['interaction']['bluetooth_version'],
                'signal_strength_dbm': interaction_data['interaction']['signal_strength_dbm'],
                'distance_meters': interaction_data['interaction']['distance_meters'],
                'duration_seconds': interaction_data['interaction']['duration_seconds'],
                'timestamp': datetime.strptime(interaction_data['interaction']['timestamp'], '%d/%m/%Y, %H:%M:%S')
            })

            return result.single()['interaction_id']