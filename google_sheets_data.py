import gspread
import pandas as pd
import numpy as np
import constants
from gspread_dataframe import set_with_dataframe

# Google Sheets API Service Account Setup
sa = gspread.service_account(filename=constants.google_api_json)

def add_processed_data_to_gs(procssed_data_path: str, sheet_name: str):
    '''...'''

    # access google sheet data base
    sheet = sa.open("customers-birthdays_processed_test")
    worksheet = sheet.worksheet(sheet_name)
    current_db_df = pd.DataFrame(worksheet.get_all_records()) # convert to df

    # prcoess data to add:
    data = pd.read_csv(procssed_data_path)

    # filter for only rows not in databse
    existing_emails: list = current_db_df['Email'].tolist()
    new_data = data[~data['Email'].isin(existing_emails)]

    # Convert NaN to None for JSON serialization
    new_data = new_data.applymap(lambda x: None if pd.isna(x) else x)


    if not new_data.empty:
        # if the sheet is empty, set column headers to current_db_df :
        if current_db_df.empty:
            current_db_df = pd.DataFrame(columns=new_data.columns)

        # Add new data to current_db_df:
        current_db_df = pd.concat([current_db_df, new_data], ignore_index=True)
        current_db_df = current_db_df.applymap(lambda x: None if pd.isna(x) else x)

        #sort sheet by 'Days_Until_Next_Birthday' column:
        current_db_df = current_db_df.sort_values(by=['Days_Until_Next_Birthday'])

        # Clear the worksheet and re-upload the updated DataFrame
        worksheet.clear()
        set_with_dataframe(worksheet, current_db_df)

        print("Notify Adam that new data has been added to Google Sheets")
    else:
        print("No new data to add.")

'''#filter for only 'next birthday month' before end of next month (e.g if it is currently june, only include people with birthdays in june or july):
    now = pd.Timestamp.now()
    next_month = now + pd.DateOffset(months=1)
    new_data = new_data[new_data['next_birthday_month'].isin([constants.int_to_month[now.month],constants.int_to_month[next_month.month]])]'''


def get_processed_birthdays_df():
    # access google sheet
    processed_birthdays_GS = sa.open("customers-birthdays_processed_test")
    processed_birthdays_Sheet = processed_birthdays_GS.worksheet("empty")
    processed_birthdays_Sheet_data = processed_birthdays_Sheet.get_all_values()
    processed_birthdays_Sheet_data_df = pd.DataFrame(processed_birthdays_Sheet_data[1:],
                                                     columns=processed_birthdays_Sheet_data[0])
    return processed_birthdays_Sheet_data_df