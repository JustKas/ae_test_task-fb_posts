"""
Logger for POS Onboarding UI tests.
Use 'log' object for logging, e.g. log.info("Message").
"""
import os
import logging
from logging import handlers
from datetime import datetime

from project_constants import project_path


folder = "logs"
log_path = ""
log_name = "fb.log"

date_format = "%m-%d-%Y_%H_%M_%S"
name_format = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] - %(message)s"

# create folder if not exists
if not os.path.exists(log_path):
    log_path = os.path.join(project_path, folder)
    if not os.path.exists(log_path):
        os.makedirs(log_path)

file_name = os.path.join(log_path, log_name)

# Create logger
log = logging.getLogger('fb_logger')
log.setLevel(logging.DEBUG)

fmt = logging.Formatter(name_format, date_format)
console_handler = logging.StreamHandler()
file_handler = handlers.RotatingFileHandler(filename=datetime.now().strftime(file_name.format(date_format)),
                                            maxBytes=(1048576*5),
                                            backupCount=7)
console_handler.setFormatter(fmt)
file_handler.setFormatter(fmt)

log.addHandler(console_handler)
log.addHandler(file_handler)
