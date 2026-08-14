import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_size=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up.')