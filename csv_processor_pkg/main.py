from .csv_reader import read_csv
from .csv_filter import filter_csv
from .csv_merge import merge_csv
from .csv_writer import write_csv
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main CLI interface for CSV Processor
    Allows user to read, filter, merge, and write CSV files through command-line prompts.
    """
    try:
        print("--- CSV Processor ---")
        print("1. Merge CSV ")
        print("2. Filter CSV")
        print("3. Exit")

        choice = input("Enter your choice (1-3):) ")

        if choice == '1':
            file_paths = input("Enter CSV file paths to merge (comma-separated): ").split(',')
            merged_data = merge_csv(file_paths)
            output_path = input("Enter output CSV file path: ")
            write_csv(output_path, merged_data)
            logging.info(f"Merged data written to {output_path}")

        elif choice == '2':
            file_paths = input("Enter CSV file paths to filter (comma-separated): ").split(',')
            merged_data = merge_csv(file_paths)
            if not merged_data:
                logging.warning("No data to filter.")
            filter_column = input("Enter column name to filter by: ")
            filter_value = input("Enter value to filter for: ")
            filtered_data = filter_csv(merged_data, filter_column, filter_value)
            output_path = input("Enter output CSV file path for filtered data: ")
            write_csv(output_path, filtered_data)
            logging.info(f"Filtered data written to {output_path}")

        elif choice == '3':
            logging.info("Exiting CSV Processor.")
            return
        else:
            logging.error("Invalid choice. Please enter 1, 2, or 3.")
            return

    except KeyboardInterrupt:
        logging.info("Process interrupted by user. Exiting.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()