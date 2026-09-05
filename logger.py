import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path('logs')
LOG_FILE = LOG_DIR / 'automation.log'

LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger('automation-tool-55')
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

handler = RotatingFileHandler(
    LOG_FILE, 
    maxBytes=1024 * 1024 * 5, 
    backupCount=3
)
handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console_handler)

def get_logger():
    return logger