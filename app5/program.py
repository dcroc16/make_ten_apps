import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')

def main():
	print_the_header()

	code = input("Enter a zip code (61109)?  ")
	html = get_html_from_web(code)
	report = get_weather_from_html(html)

	print("The temp in {} is {} {} and {}".format(report.loc,
						report.temp,
						report.scale,
						report.cond))

def print_header():
	print('------------------------------')
	print('        WEATHER APP           ')
	print('------------------------------')
	print()


def get_weather_from_html(html):
	soup = bs4.BeautifulSoup(html, 'html.parser')
	loc = soup.find(id='location').find('h1').get_text()
	condition = soup.find(id='curCond').find(class_='wx-value').get_text()


def find_city_and_state_from_location(loc: str):
	parts = loc.split('\n')
	return parts[0].strip()


def cleanup_text(text: str):
	if not text:
		return text
	
	text = text.strip()
	return text


if __name__ == "__main__":
	main()
