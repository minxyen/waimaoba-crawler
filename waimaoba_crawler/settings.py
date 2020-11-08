import os

from dotenv import load_dotenv
load_dotenv()

APPLICATION_PASSWORD = os.getenv('APPLICATION_PASSWORD')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')

# print(APPLICATION_PASSWORD)
# print(SENDER_EMAIL)
