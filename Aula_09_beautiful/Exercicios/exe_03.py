#Calcula a media da turma!
from bs4 import BeautifulSoup

with open("exe_03.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

table = soup.find("table", {"id":"alunos"})
#print(table)
#para pegar as linhas
rows = table.find_all("tr")

media = contador = 0

for row in rows:
    tds = row.findAll("td")
    if tds and len(tds) > 0:
        #print(tds[2].get_text())
        contador += 1
        media +=  float(tds[2].get_text())

