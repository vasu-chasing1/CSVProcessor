import csv
import logging
import os
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def write_csv(file_path, data):
    """
    Write list of dictionaries to a CSV file.

    Args:
        file_path (str): Path to output CSV file
        data (list): List of dictionaries to write to CSV
    """
    if not data:
        logging.warning("No data to write.")
        return False
    if  os.path.exists(file_path):
        answer = input(f"File {file_path} already exists. Do you want to overwrite it? (y/n): ")
        if answer.lower() != 'y':
            logging.info("Write operation cancelled.")
            return False
    try:
        with open(file_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"Data successfully written to {file_path}")
        return True
    except Exception as e:
        logging.error(f"Error writing to file: {e}")
        return False
    




