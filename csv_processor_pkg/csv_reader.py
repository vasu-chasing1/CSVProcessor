import csv

def read_csv(file_path):
    try:
        data = []
        with open(file_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
