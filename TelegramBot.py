import logging
# use the pickle for remembering posted news
import pickle
from time import sleep
from telebot import TeleBot
from config import bot_token as token, my_id
from GetLink import main


logging.basicConfig(level=logging.INFO)

bot = TeleBot(token=token)


def send_news(id=my_id):
	try:
		with open('news.pickle', 'rb') as f:
			old = pickle.load(f)
	except Exception:
		# the list with posted news
		old = []
	while True:
		# our function from GetLink.py
		res = main()
		if res and not (res in old):
			# posted news we are remembering
			old.append(res)
			# and then send the news us
			bot.send_message(id, res[0]+'\n\n'+res[1])
		# write the list at the file
		with open('news.pickle', 'wb') as f:
			pickle.dump(old, f)
		sleep(2)


if __name__ == '__main__':
	send_news()
