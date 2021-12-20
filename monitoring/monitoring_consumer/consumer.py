from monitoring import INTERRUPT_EVENT
from monitoring.models import MonitoringPrice, session_db
from datetime import datetime
import json
import signal
import logging
from monitoring.flask_kafka_source import FlaskKafka
from monitoring.config import Config


bus = FlaskKafka(INTERRUPT_EVENT,
                 bootstrap_servers=Config.KAFKA_IP,
                 group_id=Config.GROUP_ID
                 )


@bus.handle(Config.TOPIC)
def test_topic_handler(msg) -> None:
    """Слушатель для записи в базу"""
    try:
        data = json.loads(msg.value)
        logging.info(f'Accepted data : {data}')
        print(f'Accepted data from {data["shop_name"]}: {data}')
        data['created'] = datetime.now()
        data['last_updated'] = datetime.now()

        mp = MonitoringPrice(**data)
        mp.save()
        print(f'Count from db shop: {data["shop_name"]}-{mp.get_today_data_count(shop_name=data["shop_name"])}')
    except Exception as e:
        logging.exception(e)
    finally:
        session_db.close()


def listen_kill_server():
    """"""
    signal.signal(signal.SIGTERM, bus.interrupted_process)
    signal.signal(signal.SIGINT, bus.interrupted_process)
    signal.signal(signal.SIGQUIT, bus.interrupted_process)
    signal.signal(signal.SIGHUP, bus.interrupted_process)
