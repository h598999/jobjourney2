import os
from dotenv import load_dotenv

# Laster inn variabler fra .env filen
load_dotenv()

# Fetch the API key from environment variables
API_KEY = os.environ.get("CHATGPT_API_KEY")

if not API_KEY:
    raise ValueError("Please set the CHATGPT_API_KEY environment variable.")