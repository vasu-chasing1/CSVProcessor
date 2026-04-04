def filter_csv(data, column_name, search_value):
    """
    Filter CSV data by column value(exact match, case-sensitive).
    Args:
        data (list): List of dictionaries representing CSV rows
        column_name (str): Column name to filter by
        search_value (str): Value to match in the specified column
    Returns:
        list: Filtered list of dictionaries matching the search criteria
    """

    filtered_data = []
    for row in data:
        if column_name in row and row[column_name].lower() == search_value.lower():
            filtered_data.append(row)
    return filtered_data
