from monitoring.monitoring_consumer.consumer import bus, listen_kill_server
from monitoring import logger


if __name__ == '__main__':
    logger.info('Start consumer...')
    bus.run()
    listen_kill_server()
    logger.info('-' * 50)
    logger.info('END')


