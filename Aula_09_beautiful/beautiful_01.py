#import requests
from bs4 import BeautifulSoup

#utilizando a beautiful posso ler um arquivo local
with open ("beautiful_01.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

#utilizando a beautiful posso ler um arquivo remoto

#response = requests.get("https://pt.wikipedia.org/wiki/Valeriana_officinalis")
#soup = BeautifulSoup(response.content, "html.parser")

print("Title: ", soup.title)
print("Title: ", soup.title.get_text())

headers = soup.find_all("h1", {"class":"teste", "id":"01"})
for h in headers:
    print(h.get_text())