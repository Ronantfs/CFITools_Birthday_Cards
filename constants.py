#paths
raw_data_file = 'csvs\customers-birthdays.csv'
raw_data_file_test = 'csvs\customers-birthdays_test.csv'
processed_data_file = 'csvs\customers-birthdays_processed.csv'
processed_data_file_test = 'csvs\customers-birthdays_processed_test.csv'
prompts = 'csvs\customers-birthdays_chatgpt_prompts.csv'
prompts_test = 'csvs\customers-birthdays_chatgpt_prompts_test.csv'
messages_path = 'csvs\customer_birthday_messages.csv'
messages_path_test = 'csvs\customer_birthday_messages_test.csv'
images_file_path = "images"


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


#open_AI - generating messages:
openai_API_key = "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"
message_generation_instructions ='''You are a caring, and on occasion where it is apt humorous owner of a small crossfit gym, writing short and not overboard birthday messages that should feel as personal as is possible given the data available to you. 
When you refer to people you don't use their surname - this is too formal. 
Use lots of emojis! 
Messages you generate should be ready to send with a simple copy and paste, without any extra formatting required'''

message_tuple_cols = ('Name','Birthday','Phone Number', 'Birthday Message')

#google sheets
google_api_json ="cfitoolsbirthdays-36316556d8af.json"
int_to_month = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'}
sheet_name = 'DataBase'

#email
email_pw = 'Blackbelt123'
google_app_pw = 'ljvq zwjl ghdu dudv'
adam_email = "adamfriedlaender@gmail.com"
ut_email = "ronan@understandingtutors.com"
sender_email = "ronantfs@gmail.com"