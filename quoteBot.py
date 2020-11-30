import schedule
import time
import requests
import json


url = "https://www.adafruit.com/api/quotes.php"

chat_id = 'XXXXXXXXX'
TOKEN = 'XXXXXXXXX:XXXXXXXXXXXXXxxxxxx'
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def send_message(text, chat_id):
     url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
     get_url(url)
    
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    text = [0, 'text']
    author = [0, 'author']
    text = js[0]['text'], js[0]['author']
    print(text)
    return text
    return js
def bitQuote():
    print("running")
    message = ' '.join(map(str, get_json_from_url(url)))
    send_message(message, chat_id)

schedule.every().day.at("05:00").do(bitQuote)
    
while True:
    schedule.run_pending()
    time.sleep(600)
