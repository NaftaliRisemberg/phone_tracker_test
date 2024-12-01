
class GetPhoneRepository:
    def __init__(self, driver):
        self.driver = driver

    def find_bluetooth_connections(self):
        with self.driver.session() as session:
            query = """
                MATCH (sender:Device)-[i:INTERACTION]->(receiver:Device)
                WHERE i.method = 'Bluetooth'
                RETURN sender.sender_id AS sender_id, receiver.receiver_id AS receiver_id, i.duration_seconds AS duration_seconds
            """
            result = session.run(query)
            connections = []
            for record in result:
                connections.append({
                    'sender_id': record['sender_id'],
                    'receiver_id': record['receiver_id'],
                    'duration_seconds': record['duration_seconds']
                })

            return connections

    def find_stronger_interaction(self):
        with self.driver.session() as session:
            query = """
                    MATCH (s:Device)-[i:INTERACTION]->(r:Device) 
                    WHERE i.signal_strength_dbm > -60 
                    RETURN s.sender_id, r.receiver_id
            """
            result = session.run(query)
            connections = []
            for record in result:
                connections.append({
                    'sender_id': record['sender_id'],
                    'receiver_id': record['receiver_id'],
                })

            return connections