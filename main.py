from waggle.plugin import Plugin
import logging
from random import random

logging.basicConfig(level=logging.INFO)

with Plugin() as plugin:
    logging.info("subscribing...")
    plugin.subscribe("soil_moist")
    logging.info("waiting...")

    while True:
        msg = plugin.get()
        logging.info(f"Another plugin published soil_moist value {msg.value}")