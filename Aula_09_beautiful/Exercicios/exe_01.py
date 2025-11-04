#tem que impremit o texto do <title> e 
# o conteudo da <meta name="description">, ou seja, o "content"
from bs4 import BeautifulSoup

with open("exe_01.html", encoding = "utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

print(soup.title.string)

#print(soup.find("meta", {"name":"descpition"}))

tag_meta_description = soup.find("meta", {"name":"descpition"})
print(tag_meta_description["content"])