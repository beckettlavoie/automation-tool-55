import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def debug(self, msg):
        self.logger.debug(msg)

logger = Logger()