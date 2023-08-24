import logging
import os

MAX_LOG_FILES = 10
LOG_FILE_NAME = 'engine.log'
log_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Output')
log_file = os.path.join(log_folder, LOG_FILE_NAME)

# Create the Output directory if it doesn't exist
if not os.path.exists(log_folder):
	os.makedirs(log_folder)

if os.path.exists(log_file):
	for i in range(MAX_LOG_FILES - 1, 0, -1):  # starts from 9 moving down to 0
		current_file = f'{log_file}.{i}'
		next_file = f'{log_file}.{i + 1}'

		if os.path.exists(current_file):
			if os.path.exists(log_file + '.' + str(MAX_LOG_FILES)):
				os.remove(log_file + '.' + str(MAX_LOG_FILES))  # this will be next_file
			os.rename(current_file, next_file)
	os.rename(log_file, f'{log_file}.1')


# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s\t- %(message)s')

# Create a logger instance
logger = logging.getLogger('engine_logger')

# Create a file handler to write logs to a file
file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s\t- %(message)s')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)  # Set the desired level for file handler

# Create a stream handler to write logs to the console
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(levelname)s\t- %(message)s')
console_handler.setFormatter(console_formatter)
console_handler.setLevel(logging.WARNING)  # Set the desired level for console handler

# Add both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
