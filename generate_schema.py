"""generate mysql schema for csv data file"""
import pandas as pd

# Define the MySQL data type mapping
mysql_data_types = {
    'int64': 'INT',
    'float64': 'FLOAT',
    'object': 'VARCHAR(255)',  # You can adjust the length as needed
}


for table_name in ['HRDataset_v13', 'HRDataset_v14']:

    # Create the MySQL table schema
    schema = table_name+'_schema'
    schema = []

    # Read the CSV file into a DataFrame
    df = pd.read_csv(table_name+'.csv', delimiter=',')

    for col_name, col_type in df.dtypes.items():
        mysql_type = mysql_data_types.get(str(col_type), 'VARCHAR(255)')
        schema.append(f'{col_name} {mysql_type}')

    # Combine the schema statements into a CREATE TABLE statement
    create_table_sql = f'CREATE TABLE `{table_name}` (\n    ' + ',\n    '.join(schema) + '\n);'

    # Print the CREATE TABLE statement
    print(create_table_sql)
