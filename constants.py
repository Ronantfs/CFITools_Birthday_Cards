#Data processing:

#columns kept from raw customer birthday data
required_columns = ['Name',
                    'Email',
                    'Phone Number',
                    'Gender',
                    'Birthday']

# Personal info columns to be added
personal_info_cols = [
    'Nickname',
    'Message Style',
    'Favourite Coach',
    'Gym Friends',
    'Notable Gym Achivements',
    'Personal Facts']

#paths
raw_data_file = 'customers-birthdays.csv'
raw_data_file_test = 'customers-birthdays_test.csv'
processed_data_file = 'customers-birthdays_processed.csv'
processed_data_file_test = 'customers-birthdays_processed_test.csv'
prompts = 'customers-birthdays_chatgpt_prompts.csv'
prompts_test = 'customers-birthdays_chatgpt_prompts_test.csv'
messages_path = 'customer_birthday_messages.csv'
messages_path_test = 'customer_birthday_messages_test.csv'

# email
email_pw = 'Blackbelt123'
google_app_pw = 'ljvq zwjl ghdu dudv'
adam_email = "adamfriedlaender@gmail.com"
ut_email = "ronan@understandingtutors.com"
sender_email = "ronantfs@gmail.com"

#open_AI - generating messages:
openai_API_key = "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"
message_generation_instructions ='''You are a caring, and on occasion where it is apt humorous owner of a small crossfit gym, writing short and not overboard birthday messages that should feel as personal as is possible given the data available to you. 

When you refer to people you don't use their surname - this is too formal. 

Use lots of emojis! 
Messages you generate should be ready to send with a simple copy and paste, without any extra formatting required'''


message_tuple_cols = ('Name','Birthday','Phone Number', 'Birthday Message')

images_file_path = "images"