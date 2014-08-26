import logging
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

logger.debug("This is debug message")
logger.debug("This is info messag")
logger.debug("This is warning message")

