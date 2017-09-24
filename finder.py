import unicodedata
import requests
from bs4 import BeautifulSoup
import re 

def peopleFinder(name):
	URL = "http://google.org/personfinder/2017-puebla-mexico-earthquake/results?role=seek&query_name="
	name = transformName(name)
	list_people = []
	page = requests.get(URL+name)
	soup = BeautifulSoup(page.content, 'html.parser')
	resultItems = soup.find_all(class_='resultItem')

	for item in resultItems:
		name = re.split(r'\s{2,}', item.find(class_='resultDataTitle').get_text())[1]
		url_person = item['data-url']
		photo = item.find('img')['src']
		data_label = list(item.find_all(class_='resultDataLabel'))
		direccion_data = item.find(class_='resultDataValue').get_text().split()
		estado_data = re.split(r'\s{2,}',item.find(class_='resultDataPersonFound').get_text())[1]
		if len(data_label) == 2:
			direccion = "Dirección: "+" ".join(str(x) for x in direccion_data)
			estado = "Estado: "+str(estado_data)
		elif len(data_label) == 1:
			direccion = "Direccion no disponible"
			estado = "Estado: "+str(estado_data)
		else:
			direccion = "Dirección no disponible"
			estado = "Estado no especificado"
		json = {'name':name, 'url_to_google':url_person, 'photo':photo, 'direccion':direccion, 'estado':estado}
		list_people.append(json)
	return list_people

def transformName(list_names):
	try:
		if len(list_names) == 3:
			return eliminateQuotes(list_names[0].title()+"+"+list_names[1].title()+"+"+list_names[2].title())
		elif len(list_names) == 2:
			return eliminateQuotes(list_names[0].title()+"+"+list_names[1].title())
		else:
			return eliminateQuotes(list_names[0].title())
	except:
		return False

def eliminateQuotes(text):
	return ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))