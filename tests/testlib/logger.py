import logging
import logging.config

logging.config.fileConfig("logging_config.ini")  # для простоты используем тот же конфиг
logger = logging.getLogger()
