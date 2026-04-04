from .csv_reader import read_csv
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def merge_csv(file_paths):
    """
    Merge multiple CSV files into a single list of dictionaries.

    Args:
        file_paths (list): List of CSV file paths

    Returns:
        list: Merged list of dictionaries from all CSV files
    """
    merged_data = []
    for i, file_path in enumerate(file_paths):
        data = read_csv(file_path)
        if data:
            merged_data.extend(data)
        else:
            logging.debug(f"Skipping file: {file_path} (no data)")
    return merged_data