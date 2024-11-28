from neo4j import GraphDatabase

def init_neo4j():
    neo4j_driver = GraphDatabase.driver(
    "bolt://neo4j:7678",
    auth=("neo4j", "password")
    )
    return neo4j_driver

