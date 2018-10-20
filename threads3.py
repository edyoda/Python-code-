import requests
from bs4 import BeautifulSoup
import threading

def get_details(card):
	price  = card.find("div",attrs={"class":"m-srp-card__price"})
	title = card.find("a",attrs={"class":"m-srp-card__title"})
	link = title.get("href")
	title_text = title.text.replace("\n"," ")
	super_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})

	response2 = requests.get(link)
	soup2 = BeautifulSoup(response2.content,"html.parser")
	owner = soup2.find("p",attrs={"class":"CA_agent_name"})
	if owner:
		owner_text = owner.text.replace("\n","")
	else:
		owner_text = None


	data = "{} {} {} {}".format(title_text,price.text,super_area.text,owner_text)
	print(data)


response = requests.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore')

soup = BeautifulSoup(response.content,"html.parser")

cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})

for card in cards:
	t = threading.Thread(target= get_details , args = (card,))
	t.start()
    