import datetime
import json
import os
import re
from dotenv import load_dotenv
import pytz

load_dotenv()  # take environment variables from .env.


AUTH_PW = os.getenv("AUTH_PW")


def clean_text(text):
    text.replace("”", '"')
    text.replace("“", '"')
    text.replace("’", "'")
    text.replace("‘", "'")
    text.replace("–", "-")
    text.replace("…", "...")
    return text


def authenticate(request):
    auth_header = request.headers.get("X-Password")
    if auth_header == AUTH_PW:
        return True
    else:
        return False


def get_time_gmt2_naive():
    """Returns the current time in GMT+2, formatted as 'Month Day Year - Hour:Minute', as a naive datetime."""
    gmt2_tz = pytz.timezone(
        "Europe/Helsinki"
    )  # Or another appropriate region within GMT+2
    now_gmt2 = datetime.datetime.now(gmt2_tz)
    naive_gmt2 = now_gmt2.replace(
        tzinfo=None
    )  # Remove timezone information (make it naive)
    formatted_time = naive_gmt2.strftime("%B %d %Y - %H:%M")
    return formatted_time


def add_entry_to_json(data):
    if "content" in data:
        data["content"] = clean_text(data["content"])

    data["date"] = get_time_gmt2_naive()
    with open("entries.json", "r") as file:
        entries = json.load(file)
    entries.append(data)
    with open("entries.json", "w") as file:
        json.dump(entries, file, indent=4)
