from bs4 import BeautifulSoup
import telebot
import requests
import schedule
import random
import time

#Create a sender BOT
TOKEN = 'your token'
bot = telebot.TeleBot(TOKEN)
group_id = 'your telegram id'
#Parser body
url = 'http://tafsir.ru'
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
titles = soup.findAll('p')

hadis = []
for x in titles:
	hadis.append(x.text.strip())

random_hadis = hadis.reverse()

res = random.choice(random_hadis)

def get_hadis_today():
	bot.send_message(group_id, f' Bugunlik matn : \n << {res} >>')

schedule.every().day.at('08:15').do(get_hadis_today)

while True:
	schedule.run_pending()
	time.sleep(1)
