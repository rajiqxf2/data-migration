import pandas as pd

# Read the CSV file into a DataFrame
HRDataset_v13_df = pd.read_csv(r'C:\code\kaggle\HRDataset_v13.csv', delimiter=',')
HRDataset_v14_df = pd.read_csv(r'C:\code\kaggle\HRDataset_v14.csv', delimiter=',')

# Define the MySQL data type mapping
mysql_data_types = {
    'int64': 'INT',
    'float64': 'FLOAT',
    'object': 'VARCHAR(255)',  # You can adjust the length as needed
}

HRDataset_v13_schema = []
HRDataset_v14_schema = []

for table_name in ['HRDataset_v13', 'HRDataset_v14']:
    # Create the MySQL table schema
    df = globals()[table_name + '_df']
    for col_name, col_type in df.dtypes.items():
        mysql_type = mysql_data_types.get(str(col_type), 'VARCHAR(255)')
        globals()[table_name + '_schema'].append(f'{col_name} {mysql_type}')

    # Combine the schema statements into a CREATE TABLE statement
    create_table_sql = f'CREATE TABLE `{table_name}` (\n    ' + ',\n    '.join(globals()[table_name + '_schema']) + '\n);'

    # Print the CREATE TABLE statement
    print(create_table_sql)
