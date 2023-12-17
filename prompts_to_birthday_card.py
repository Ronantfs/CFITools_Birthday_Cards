from openai import OpenAI
import pandas as pd
import os
import constants
import requests
import datetime
from typing import List

# Set the API key for OpenAI
OpenAI.api_key = constants.openai_API_key
client = OpenAI(api_key=OpenAI.api_key)
system_role = constants.message_generation_instructions


def generate_birthday_card_url(prompt: str):
    '''str -> url with image file (using Dall-e API)'''

    image_params = {
        "model": "dall-e-3",  # Defaults to dall-e-2
        "n": 1,  # Between 2 and 10 is only for DALL-E 2
        "size": "1024x1024",  # 256x256, 512x512 only for DALL-E 2 - not much cheaper
        "prompt": prompt,  # DALL-E 3: max 4000 characters, DALL-E 2: max 1000
        "user": "Ronantfs",  # pass a customer ID to OpenAI for abuse monitoring
    }
    image_params.update({"style": "natural"})

    try:
        image_response = client.images.generate(**image_params)
    except openai.APIConnectionError as e:
        print("Server connection error: {e.__cause__}")  # from httpx.
        raise
    except openai.RateLimitError as e:
        print(f"OpenAI RATE LIMIT error {e.status_code}: (e.response)")
        raise
    except openai.APIStatusError as e:
        print(f"OpenAI STATUS error {e.status_code}: (e.response)")
        raise
    except openai.BadRequestError as e:
        print(f"OpenAI BAD REQUEST error {e.status_code}: (e.response)")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

    image_url = image_response.data[0].url

    return image_url

def download_image_from_url(url:str, file_path:str):
    """
    Download an image from a given URL and save it to a specified file path.

    Args:
    url (str): URL of the image to be downloaded.
    file_path (str): File path where the image will be saved.

    Returns:
    bool: True if download is successful, False otherwise.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Write the content of the response to a file
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def generate_cards(prompts_path, messages_path):
    '''Reads in DF of prompts and converts these to birthday messages'''

    # Load prompts from CSV file
    data = pd.read_csv(prompts_path)

    data = data[data['Name'].str.len() >= 1]
    data = data[data['Name'].notna()]

    count: int = 1
    total: int = data.shape[0]


    # Iterate over each row in the DataFrame
    for index, row in data.iterrows():
        if pd.notna(row['ChatGPT Prompts']):

            # Generate a birthday card image
            image_url = generate_birthday_card_url(row['Name'] + 'funny crossfit' + 'Birthday Card')  # TODO customise this birthday prompt
            download_image_from_url(image_url, f'images\{row["Name"]}image_test.jpeg')
            print(f'Image returned {count}/{total}')
            count += 1

def get_card_file_paths(folder_path: str) -> List[str]:
    """
    Get the paths of all files in a specified folder.

    Args:
    folder_path (str): The path to the folder from which to get file paths.

    Returns:
    List[str]: A list of file paths.
    """
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

