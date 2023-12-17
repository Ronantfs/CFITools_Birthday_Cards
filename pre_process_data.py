import pandas as pd

def preprocess_data(csv_file_path, output_file_path, required_columns, personal_info_columns):
    '''Takes input and output file paths '''
    # Load the CSV file
    data = pd.read_csv(csv_file_path)
    data = data[data['Name'].notna() & data['Name'].str.len() >= 1]

    # Filter for specific columns
    data = data[required_columns]

    # Add empty columns for personal information
    for col in personal_info_columns:
        data[col] = ''

    # Save the preprocessed data to a new CSV file
    data.to_csv(output_file_path, index=False)

    print("Raw WodBoard Data Processed.")
    print("Please Fill in custom Information for clients so the messages are personal.")


