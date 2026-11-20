import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='application.log',
    filemode='a'
)

logging.info("Application started")
logging.warning("Warning message")
logging.error("Error message")
