import logging
from monitoring import bus, listen_kill_server
from monitoring import Config


if __name__ == '__main__':
    print('Start consumer....')
    print(f'Config : USER: {Config.USER} \n'
                    f'PASS: {Config.PASS} \n'
                    f'PORT: {Config.PORT} \n'
                    f'HOST: {Config.HOST} \n'
                    f'NAME: {Config.NAME} \n'
                    f'KAFKA_IP: {Config.KAFKA_IP} \n'
                    f'TOPIC : {Config.TOPIC} \n'
                    f'GROUP_ID : {Config.GROUP_ID}')
    logging.info('Start consumer...')
    bus.run()
    listen_kill_server()
    logging.info('-' * 50)
    logging.info('END')


