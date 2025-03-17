import logging
import os

class SimpleFileLogger:
    def __init__(self, log_file='app.log', log_level=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.log_file = log_file

        # Create a file handler
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(log_level)

        # Create a logging format
        formatter = logging.Formatter('%(message)s')
        file_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)

