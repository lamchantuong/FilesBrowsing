import time
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

while True:
    time.sleep(10)
    logger.info("hello")
