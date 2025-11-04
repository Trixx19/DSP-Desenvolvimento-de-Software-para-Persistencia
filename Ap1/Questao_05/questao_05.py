from bs4 import BeautifulSoup

regras_vitoria = {
    'pedra': 'tesoura',
    'tesoura': 'papel',
    'papel': 'pedra'
}

vitorias_j1 = 0


with open('jogadas.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

    tabela_corpo = soup.find('tbody')
    
    if tabela_corpo:
        linhas = tabela_corpo.find_all('tr') # 

        for linha in linhas:
            colunas = linha.find_all('td')
            
            if len(colunas) == 2:
                j1 = colunas[0].get_text().strip().lower()
                j2 = colunas[1].get_text().strip().lower()

                if regras_vitoria.get(j1) == j2:
                    vitorias_j1 += 1
    
    print(f"Número de vitórias do Jogador 1: {vitorias_j1}")

