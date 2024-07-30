import logging
from logging.handlers import RotatingFileHandler
import os

class Logger:

    @staticmethod
    def get_logger(name: str, log_file: str = 'app.log', level: int = logging.DEBUG) -> logging.Logger:
        """
        Creates a logger instance.

        :param name: Name of the logger (usually __name__).
        :param log_file: Path to the log file.
        :param level: Logging level (e.g., logging.DEBUG, logging.INFO).
        :return: Configured logger instance.
        """
        # Create a logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        
        # Create a file handler
        if not logger.handlers:
            log_file_directory = os.path.dirname(log_file)
            if log_file_directory:
                # Ensure the directory exists
                os.makedirs(os.path.dirname(log_file), exist_ok=True)

            file_handler = RotatingFileHandler(log_file, maxBytes=10**6, backupCount=5)
            file_handler.setLevel(level)

            # Create a console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)

            # Create a formatter and set it for the handlers
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add the handlers to the logger
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
