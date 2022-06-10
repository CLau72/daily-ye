import os
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from twilio.rest import Client

'''
The Daily Ye is a simple daily SMS service that inspires you with daily insight from the mind of Kanye West.

Why? "Because my life is dope, and I do dope shit" -Kanye West 
'''

# Get environment variables
load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_API_KEY =  os.getenv("TWILIO_API_KEY")
FROM_PHONE = os.getenv("FROM_PHONE")
TO_PHONE = os.getenv("TO_PHONE")

# Return a quote from the Kanye West REST API
def get_quote() -> str:
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()

    return data["quote"]

# Send message with returned quote
def send_message(quote:str):

    text_message = f'Today\'s Daily Ye:\n"{quote}"\n -Kanye West' 

    client = Client(TWILIO_SID, TWILIO_API_KEY)

    message = client.messages \
                    .create(
                        body = text_message,
                        from_= FROM_PHONE,
                        to= TO_PHONE
                    )

    print(message.sid)

def main():

    while True:
        current_time = datetime.now()
        if current_time.hour == 8 and 29 <= current_time.minute <= 31:
            send_message(get_quote())
            print("Message Sent. Waiting an hour")
            time.sleep(3600)
        else:
            print("Not time to send. Be back in a minute to check again")
            time.sleep(60)
        
if __name__ == "__main__":
    main()