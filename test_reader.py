from csv_processor_pkg.csv_reader import read_csv
import csv

with open('/tmp/test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Prabhav', '22', 'Mawana'])

data = read_csv('/tmp/test.csv')
print("Data:", data)
