from dotenv import load_dotenv
import os


load_dotenv()


class Config:
    USER = os.getenv('DB_USER')
    PASS = os.getenv('DB_PASS')
    PORT = os.getenv('DB_PORT')
    HOST = os.getenv('DB_HOST')
    NAME = os.getenv('DB_NAME')
    KAFKA_IP = os.getenv('IP')
    TOPIC = os.getenv('TOPIC')
    GROUP_ID = os.getenv('GROUP_ID')
