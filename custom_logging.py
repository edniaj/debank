import logging
from logging.handlers import RotatingFileHandler

def setup_logging(info_log_filename, error_log_filename):

    '''
    0. Rotating file handler 
    1. Set up handler
    2. Set up logger
    3. Add handler into the logger
    '''
    
    # Set level and format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    
    # Create loggers and assign handlers
    handler_info = RotatingFileHandler(info_log_filename, maxBytes=10000, backupCount=1)
    handler_info.setFormatter(formatter)
    handler_info.setLevel(logging.INFO)
    logger_info = logging.getLogger('info_logger')
    logger_info.setLevel(logging.INFO)
    logger_info.addHandler(handler_info)


    handler_error = RotatingFileHandler(error_log_filename, maxBytes=10000, backupCount=1)
    handler_error.setFormatter(formatter)
    handler_error.setLevel(logging.ERROR)
    logger_error = logging.getLogger('error_logger')
    logger_error.setLevel(logging.ERROR)
    logger_error.addHandler(handler_error)

    return logger_info, logger_error
