'''Script that generates prompts column for sending to a GPT'''
import pandas as pd

def create_personal_info_dict(row, personal_info_columns):
    """Creates a dictionary of personal info from specified columns in a row, including columns that are non-empty."""
    return {col: row[col] for col in personal_info_columns if pd.notna(row[col])}


def create_chatgpt_prompt(name, birthday, gender, personal_info):
    """Creates a birthday message generting prompt (string) using personal information."""
    prompt = f"Create a birthday message for {name}, a {gender} gym member, whose birthday is on {birthday}."
    if personal_info:
        additional_info = " ".join([f"{key}: {value}." for key, value in personal_info.items()])
        prompt += f" Include personal touches such as {additional_info}"
    else:
        generic = '''Add a generically nice line like that we're happy to have you and looking forward to seeing you in class soon.'''
        prompt += generic
    return prompt

def generate_prompts(csv_file_path, output_file_path, personal_info_columns):
    """Generates ChatGPT prompts from a CSV file and saves them to another CSV file."""
    df = pd.read_csv(csv_file_path)
    df['Personal Info'] = df.apply(create_personal_info_dict, axis=1, personal_info_columns=personal_info_columns)
    df['ChatGPT Prompts'] = df.apply(lambda row: create_chatgpt_prompt(row['Name'], row['Birthday'], row['Gender'], row['Personal Info']), axis=1)
    df.to_csv(output_file_path, index=False)


