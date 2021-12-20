import logging
import os, sys
sys.path.append(os.getcwd())
from threading import Event
import logging

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from monitoring.config import Config


try:
    engine = create_engine(f'postgresql://{Config.USER}:{Config.PASS}@{Config.HOST}:{int(Config.PORT)}/{Config.NAME}')
    session_db = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base = declarative_base()
    Base.query = session_db.query_property()
    INTERRUPT_EVENT = Event()
except Exception as e:
    logging.exception(e)
    print(f'Config : USER: {Config.USER} \n'
          f'PASS: {Config.PASS} \n'
          f'PORT: {Config.PORT} \n'
          f'HOST: {Config.HOST} \n'
          f'NAME: {Config.NAME} \n'
          f'KAFKA_IP: {Config.KAFKA_IP} \n'
          f'TOPIC : {Config.TOPIC} \n'
          f'GROUP_ID : {Config.GROUP_ID}')



