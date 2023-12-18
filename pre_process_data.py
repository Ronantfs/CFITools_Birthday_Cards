import pandas as pd
from datetime import datetime
import numpy as np
import constants


def add_birthday_details(df: pd.DataFrame, birthday_column:str):

    # Convert the birthday column to datetime
    df[birthday_column] = pd.to_datetime(df[birthday_column], format='%d/%m/%Y')

    # Current date
    now = datetime.now()

    # Function to calculate days until next birthday and age at next birthday
    def birthday_details(birthday: datetime):
        '''takes a birthday datetime object and returns the days until next birthday and age at next birthday(both ints)'''
        # Next birthday year
        next_birthday_year = now.year if now.month < birthday.month or (
                    now.month == birthday.month and now.day < birthday.day) else now.year + 1

        # Next birthday date
        next_birthday = datetime(next_birthday_year, birthday.month, birthday.day)

        #next birthday date, month
        next_birthday_month = constants.int_to_month[next_birthday.month]

        # Days until next birthday
        days_until_next_birthday:int = (next_birthday - now).days

        # Age at next birthday
        age_next_birthday:int = next_birthday_year - birthday.year

        return days_until_next_birthday, age_next_birthday,next_birthday_month

    # Apply the function to each row
    df['Days_Until_Next_Birthday'], df['Age_At_Next_Birthday'],df['next_birthday_month'] = zip(*df[birthday_column].apply(birthday_details))
    # how this works: https://stackoverflow.com/questions/16236684/apply-pandas-function-to-column-to-create-multiple-new-columns

    return df



def preprocess_data(csv_file_path, output_file_path, required_columns, personal_info_columns):
    '''Preprocesses the raw WodBoard data by filtering for specific columns
     and adding empty columns for personal information(to be populated),
    and saves it to a new CSV file with the required columns.'''

    # Load the CSV file
    data = pd.read_csv(csv_file_path)
    data = data[data['Name'].notna() & data['Name'].str.len() >= 1]

    # Filter for specific columns
    data = data[required_columns]

    # Add empty columns for personal information
    for col in personal_info_columns:
        data[col] = ''

    # Add birthday details:
    data = add_birthday_details(data, 'Birthday')

    # Save the preprocessed data to a new CSV file
    data.to_csv(output_file_path, index=False)

    print(f"Raw WodBoard Data Processed in {output_file_path}.")
    print("Please Fill in custom Information for clients so the messages are personal.")


