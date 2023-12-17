# main.py
import pandas as pd
import constants
from pre_process_data import preprocess_data
from generate_prompts import generate_prompts
from prompts_to_messages import generate_messages, messages_to_tuple
from prompts_to_birthday_card import generate_cards, get_card_file_paths
from email_messages import send_email, compile_email

required_columns = constants.required_columns
personal_info_cols = constants.personal_info_cols

# File paths
raw_data_file = constants.raw_data_file
raw_data_file_test =  constants.raw_data_file_test

processed_data_file = constants.processed_data_file
processed_data_file_test = constants.processed_data_file_test

prompts = constants.prompts
prompts_test = constants.prompts_test

messages_path = constants.messages_path
messages_path_test = constants.messages_path_test

def main():

    # User input to select the function to run
    print("Select the function to run:")
    print("1: Process Raw Wodboard Data (so that you cna fill in personal details)")
    print("2: Generate Birthday Messages")
    print("3: Email Birthday Message to Adam")
    choice = int(input("Enter your choice (1,2 or 3): "))

    if choice == 1:
        # Step 1: Preprocess the data
        preprocess_data(raw_data_file_test, processed_data_file_test, required_columns, personal_info_cols)
    elif choice == 2:
        # Step 2: Generate ChatGPT prompts and ChatGPT birthday messages via API
        #messages:

        generate_prompts(processed_data_file_test, prompts_test, personal_info_cols)
        generate_messages(prompts_test, messages_path_test)

        #cards:
        generate_cards(prompts_test, messages_path_test)

    elif choice == 3:
        #send email
        list_of_message_tuples =  messages_to_tuple(messages_path_test,constants.message_tuple_cols)
        email_body:str = compile_email(list_of_message_tuples)
        image_paths = get_card_file_paths(constants.images_file_path)
        send_email('test subject', email_body, image_paths)

    else:
        print("Invalid choice. Enter integer in specifed range")

if __name__ == "__main__":
    main()


#TODO issue is phone numbers not being read through correctly:
