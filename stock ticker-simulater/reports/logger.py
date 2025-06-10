import logging
import os


def setup_logger(name, log_file="simulator.log", level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)
    handler = logging.FileHandler(os.path.join("logs", log_file))
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger