import pickle
from time import sleep
from telebot import TeleBot
from get_news import main


# use real token and id
token = 'TOKEN'
my_id = 'MY_ID'


bot = TeleBot(token=token)


def send_news(user_id):
	try:
		with open('news.pickle', 'rb') as f:
			old = pickle.load(f)
	except FileNotFoundError:
		# the list with posted news
		old = []
	while True:
		# our function from get_news.py
		res = main()
		if res and not (res in old):
			# posted news we are remembering
			old.append(res)
			# and then send the news us
			bot.send_message(user_id, res[0] + '\n\n' + res[1])
		# write the list at the file
		with open('news.pickle', 'wb') as f:
			pickle.dump(old, f)
		sleep(2)


if __name__ == '__main__':
	send_news(my_id)
