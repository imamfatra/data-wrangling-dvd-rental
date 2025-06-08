from tabulate import tabulate
from data.data_source_full import data_full
from data.requirments import requirements_data

# check table name 
def check_table_requirements(actual_table: dict, requirement_table: dict):
    actual_table_name = list(actual_table.keys())
    requirement_table_name = list(requirement_table.keys())

    table_checking = []
    for table_name in requirement_table_name:
        if table_name in actual_table_name:
            table_checking.append([table_name, "✓"])
        else:
            table_checking.append([table_name, "✗"])
    
    table_headers = ["Table name", "Is exist"]
    table = tabulate(table_checking, headers=table_headers, tablefmt="grid")
    print("=> STEP 1: CHECK TABLE")
    print(table)

# check table shape (rows, columns)
def check_data_shape(actual_table: dict):
    table_shape = []

    for table_name in actual_table:
        rows, cols = actual_table[table_name].shape
        table_shape.append([table_name, rows, cols])
    
    table_headers = ["Table name", "Number of rows", "Number of columns"]
    table = tabulate(table_shape, headers=table_headers, tablefmt="grid")
    print("=> STEP 2: CHECK TABLE SHAPE")
    print(table)

# check columns name
def check_columns(actual_table: dict, requirement_table: dict):
    print("=> STEP 3: CHECK COLUMNS")

    for table_name in requirement_table:
        result = []
        actual_columns = list(actual_table[table_name].columns)
        requirement_columns = []

        for data in requirement_table[table_name]:
            requirement_columns.append(data["column_name"])
        
        for column_name in set(actual_columns + requirement_columns):
            in_actual_table = "✔" if column_name in actual_columns else "✘"
            in_requirement_table = "✔" if column_name in requirement_columns else "✘"
            result.append([column_name, in_actual_table, in_requirement_table])

        if set(actual_columns) == set(requirement_columns):
            pass
        else:
            print(table_name)
            table_headers = ["Column name", "In actual table", "In requirement table"]
            table = tabulate(result, headers=table_headers, tablefmt="grid")
            print(table)
            print("\n")

# check data type
def check_data_type(actual_table: dict, requirement_table: dict):
    result = []

    for table_name, df in actual_table.items():
        if table_name in requirement_table:
            for info_table in requirement_table[table_name]:
                column_name = info_table["column_name"] 
                data_type_req = info_table["data_type"]
                if column_name in df.columns:
                    data_type_actual = df[column_name].dtype
                    result_data_type = "✔" if data_type_req == data_type_actual else "✘"
                    result.append([table_name, column_name, data_type_actual, 
                                   data_type_req, result_data_type])
                else:
                    result.append([table_name, column_name, "N/A", 
                                   data_type_req, "✘ (Column not found)"])
    
    print("=> STEP 4: CHECK DATA TYPE")
    table_headers = ["Table name", "Column name", "Actual type", "Requirement type", "Match"]
    
    missmatch_data = [row for row in result if "✘" in row[4]] 
    if missmatch_data:
        print("\nSummary of Mismatches Data Types:")
        table = tabulate(missmatch_data, headers=table_headers, tablefmt="grid")
        print(table)
    else:
        print("All data types match")

# check missing value all table
def check_missing_values(actual_table: dict):
    result = []

    for table_name, df in actual_table.items():
        missing_count = df.isna().sum()
        total_data = df.shape[0]
        
        for column, missing in missing_count.items():
            missing_count_percantage = round((missing / total_data * 100), 2)
            result.append([table_name, column, missing, missing_count_percantage])
    
    table_headers = ["Table name", "Column name", "Missing value count", 
                     "Missing value percentage"]
    missing_value = [row for row in result if row[2] != 0]
    if missing_value:
        table = tabulate(missing_value, headers=table_headers, tablefmt="grid")
        print("=> STEP 5: CHECK MISSING VALUE")
        print(table)
    else:
        print("There's no Missing Values")

# check duplicates data
def check_duplicates_data(actual_table: dict):
    result = []

    for table_name, df in actual_table.items():
        # duplicate_rows = df[df.duplicated(keep=False)]
        duplicate_rows = df.astype(str).duplicated(keep=False).sum()
        result.append([table_name, duplicate_rows])
    
    duplicate_data = [row for row in result if row[1] != 0]
    if duplicate_data:
        table_headers = ["Table name", "Duplicate rows count"]
        duplicates_data = [row for row in result if row[1] != 0]
        table = tabulate(duplicates_data, headers=table_headers, tablefmt="grid")
        print("=> STEP 6: CHECK DUPLICATES DATA")
        print("Duplicate Data Summary:")
        print(table)
    else:   
        print("No Duplicate Data Found")

if __name__ == "__main__":
    actual_table = data_full()
    requirement_table = requirements_data()

    check_table_requirements(actual_table, requirement_table)
    print("-"*100)
    print("\n")

    check_data_shape(actual_table)
    print("-"*100)
    print("\n")

    check_columns(actual_table, requirement_table)
    print("-"*100)
    print("\n")

    check_data_type(actual_table, requirement_table)
    print("-"*100)
    print("\n")

    check_missing_values(actual_table)
    print("-"*100)
    print("\n")

    check_duplicates_data(actual_table)
    