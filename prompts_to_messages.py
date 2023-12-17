from openai import OpenAI
import pandas as pd
import os
import constants

# Set the API key for OpenAI
OpenAI.api_key = constants.openai_API_key
client = OpenAI(api_key=OpenAI.api_key)
system_role =constants.message_generation_instructions

def generate_birthday_message_from_prompt(prompt, count, total):
    '''Use Chat GPT LLM to return message when prompt input '''
    try:

        response = client.chat.completions.create(
            model= "gpt-4",
            messages=[
                {"role": "system","content": system_role},
                {"role": "user", "content": prompt}
            ]
        )
        print(f'Message returned {count}/{total}')
        
        return response.choices[0].message
    except Exception as e:
        print(f"Error generating response for prompt: {prompt}\nError: {e}")
        return None


def generate_messages(prompts_path, messages_path):
    '''Reads in DF of prompts and converts these to birthday messages'''

    # Load prompts from CSV file
    data = pd.read_csv(prompts_path)

    data = data[data['Name'].str.len() >= 1]
    data = data[data['Name'].notna()]

    # Ensure there's a column for the responses
    data['Birthday Message'] = ''

    count: int = 1
    total:int = data.shape[0]

    # Iterate over each row in the DataFrame
    for index, row in data.iterrows():
        if pd.notna(row['ChatGPT Prompts']):
            response = generate_birthday_message_from_prompt(row['ChatGPT Prompts'], count, total)
            if response:
                data.at[index, 'Birthday Message'] = response.content
                count += 1
            else:
                print(f"Error: No response received for prompt at row {index}")

    # Save the updated DataFrame to a new CSV file
    data.to_csv(messages_path, index=False)

def messages_to_tuple(messages_path:str, tuple_cols: tuple[str,...]):
    messages_df= pd.read_csv(messages_path)

    #select columns to output
    name = tuple_cols[0]
    birthday = tuple_cols[1]
    phone_number = tuple_cols[2]
    birthday_message = tuple_cols[3]

    return [(row[name],row[birthday], row[phone_number],row[birthday_message]) for index, row in messages_df.iterrows()]



#TODO configure GPT
#TODO have a csv that can store emojis !

