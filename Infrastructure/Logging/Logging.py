import logging
from datetime import datetime
import os

#def main():    
# Define the log directory

# Set the base directory to the current file location
base_dir = os.path.dirname(os.path.abspath(__file__))  #Logging.py path
log_dir = os.path.join(base_dir, "logs")  # Replace with your desired path
os.makedirs(log_dir, exist_ok=True)  # Ensure the directory exists

logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level. Debug is the minimum level of log messagesthat will be recorded
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
    filename=os.path.join(log_dir, f"SeveralAITechniques_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"),  # Optional: Log to a file
    filemode='a'  # Optional: Add new log messages to the end of the file without overwriting its contents.
)

def debug(message):
    logging.debug(message)

def info(message):
    logging.info(message)

def warning(message):
    logging.warning(message)

def error(message):
    logging.error(message)

def critical(message):
    logging.critical(message)

#main()
