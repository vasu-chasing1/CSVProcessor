import csv

def read_csv(file_path):

    """
    Read CSV file and return list of dictionaries.
    
    Args:
        file_path (str): Path to CSV file
    
    Returns:
        list: List of dictionaries (one per row)
    """
    try:
        data = []
        with open(file_path) as f:
            reader = csv.DictReader(f)     #craete a DictReader object to read the CSV file as dictionaries
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    data = read_csv('data.csv')
    print(data)