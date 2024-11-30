from datetime import datetime
import uuid

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
                        MERGE (receiver:Device {receiver_id: $receiver_id,
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
                        RETURN i.interaction_id as interaction_id
                        """

            fields = ['id', 'name', 'brand', 'model', 'os', 'latitude', 'longitude', 'altitude_meters', 'accuracy_meters' ]
            dct_values = {}
            for i, field in enumerate (fields):
                if i < 5:
                    dct_values[f'sender_{field}'] = interaction_data['devices'][0][field]
                else:
                    dct_values[f'sender_{field}'] = interaction_data['devices'][0]['location'][field]
            for i, field in enumerate(fields):
                if i < 5:
                    dct_values[f'receiver_{field}'] = interaction_data['devices'][1][field]
                else:
                    dct_values[f'receiver_{field}'] = interaction_data['devices'][1]['location'][field]
            dct_values['interaction_id'] = str(uuid.uuid4())
            dct_values['from_device'] = interaction_data['interaction']['from_device']
            dct_values['to_device'] = interaction_data['interaction']['to_device']
            dct_values['method'] = interaction_data['interaction']['method']
            dct_values['bluetooth_version'] = interaction_data['interaction']['bluetooth_version']
            dct_values['signal_strength_dbm'] = interaction_data['interaction']['signal_strength_dbm']
            dct_values['distance_meters'] = interaction_data['interaction']['distance_meters']
            dct_values['duration_seconds'] = interaction_data['interaction']['duration_seconds']
            dct_values['timestamp'] = datetime.strptime(interaction_data['interaction']['timestamp'], '%Y-%m-%dT%H:%M:%S')

            result = session.run(query, dct_values)
            return result.single()['interaction_id']