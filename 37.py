#Web scraping: Extrae enlaces de una página
import requests
from bs4 import BeautifulSoup

#Enlace de la pagina
url = "https://www.python.org/"
#Pedimos la pagina
r = requests.get(url)
#Covertirlo en un objeto beautifulsoup
soup = BeautifulSoup(r.text,"html.parser")

#Buscar las etiquetas <a>
enlaces = soup.find_all("a")

#Mostrar los primeros 15 enlaces de la pagina
for enlace in enlaces[:15]:
    print(enlace.get("href")) 

