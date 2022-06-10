import requests
from twilio.rest import Client

'''
The Daily Ye is a simple daily SMS service that inspires you with daily insight from the mind of Kanye West.

Why? "Because my life is dope, and I do dope shit" -Kanye West 
'''

# Return a quote from the Kanye West REST API
def get_quote() -> str:
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()

    return data["quote"]

def main():
    print(get_quote())

if __name__ == "__main__":
    main()