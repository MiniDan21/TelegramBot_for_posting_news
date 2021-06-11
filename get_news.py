from bs4 import BeautifulSoup
import requests


# getting html
def get_html(url):
	res = requests.get(url)
	return res.text


def parse(html):
	link = BeautifulSoup(html, 'html.parser').find('a', class_='news-feed__item js-news-feed-item js-yandex-counter')
	date_theme = link.find('span', class_='news-feed__item__date-text').text
	# news for (not) rich
	if 'Pro' not in date_theme:
		return link.find('span', class_='news-feed__item__title').text.strip(), link.get('href')


def main():
	url = 'https://www.rbc.ru/'
	test_last = parse(get_html(url))
	return test_last


if __name__ == '__main__':
	print(main())
