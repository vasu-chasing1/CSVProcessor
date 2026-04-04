# CSV Processor

**Merge, filter, and process CSV files with ease.**

## Features

📊 **Merge Multiple CSVs**
- Combine multiple CSV files into one
- Automatic header handling (keeps only first)
- Handles missing files gracefully

🔍 **Filter CSV Data**
- Search by column value
- Case-insensitive matching
- Extract specific records

💾 **Write CSV Files**
- Export filtered/merged data
- Handles file overwrite safely
- Professional error messages

## Usage
```bash
python3 run.py
```

Follow interactive prompts:
1. Choose operation (merge/filter/exit)
2. Enter file paths (comma-separated)
3. Configure filter options (if filtering)
4. Specify output file

## Example

### Merge CSVs
Choice: 1
Files: /tmp/jan.csv,/tmp/feb.csv
Output: /tmp/merged.csv

### Filter Data
Choice: 2
Files: /tmp/employees.csv
Column: Department
Value: IT
Output: /tmp/it_employees.csv

## Project Structure
csv_processor/
├── csv_processor_pkg/
│   ├── init.py
│   ├── csv_reader.py      (Read CSV files)
│   ├── csv_merger.py      (Merge multiple files)
│   ├── csv_filter.py      (Filter by column value)
│   ├── csv_writer.py      (Write to CSV)
│   └── main.py            (CLI interface)
├── run.py                 (Entry point)
└── README.md

## How Each Module Works

**csv_reader.py**
- Opens CSV file using csv.DictReader
- Returns list of dictionaries
- Handles missing files gracefully

**csv_merger.py**
- Combines multiple CSV files
- Each file read separately
- All rows merged into single list

**csv_filter.py**
- Filters data by exact column match
- Case-insensitive search
- Skips rows with missing columns

**csv_writer.py**
- Writes list of dicts to CSV
- Asks before overwriting existing files
- Professional error handling

**main.py**
- CLI menu interface
- Orchestrates all modules
- Handles user input

## Real-World Uses

- **Data Analysis:** Combine monthly reports
- **HR:** Filter employees by department
- **Finance:** Merge transaction CSVs
- **Analytics:** Process log files
- **Data Migration:** Consolidate spreadsheets

## Error Handling

✅ Missing files - Logged and skipped
✅ Empty data - Notified to user
✅ File overwrite - User confirmation
✅ Invalid input - Clear error messages
✅ Corrupted CSV - Graceful handling

## Requirements

- Python 3.6+
- No external dependencies (uses standard library)

## Future Improvements

- [ ] Add column reordering
- [ ] Support different delimiters (;, |, etc)
- [ ] Batch processing multiple filters
- [ ] Export to Excel format
- [ ] Data validation/cleaning

## Author

Built as portfolio project learning:
- CSV file operations
- Data processing
- CLI applications
- Error handling
- Modular design

## License

Free to use and modify
