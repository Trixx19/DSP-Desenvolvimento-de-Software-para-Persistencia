import requests

BASE_URL = "http://127.0.0.1:8000"

def adicionar_aluno(nome, nota):
    print(f"\nTentando adicionar/atualizar: {nome} com nota {nota}")
    response = requests.post(f"{BASE_URL}/alunos", params={"nome": nome, "nota": nota})
    
    if response.status_code == 200:
        print("Resposta do servidor:", response.json())
    else:
        print(f"Erro ao adicionar: {response.status_code}")

def obter_nota(nome):
    print(f"\nTentando obter nota de: {nome}")
    
    response = requests.get(f"{BASE_URL}/alunos/{nome}")
    
    if response.status_code == 200:
        print("Resposta do servidor:", response.json())
    elif response.status_code == 404:
        print("Resposta do servidor (Erro 404):", response.json())
    else:
        print(f"Erro ao buscar: {response.status_code}")

def listar_alunos():
    print("\nTentando listar TODOS os alunos...")
    
    response = requests.get(f"{BASE_URL}/alunos")
    
    if response.status_code == 200:
        print("Resposta do servidor (Todos os alunos):")
        lista_de_alunos = response.json()
        
        
        print(lista_de_alunos)
    else:
        print(f"Erro ao listar: {response.status_code}")

if __name__ == "_main_":
    try:
        adicionar_aluno("Mariana Costa", 9.5)
        adicionar_aluno("Pedro Álvares", 7.0)
        adicionar_aluno("Bia Gomes", 8.2)

        listar_alunos()
        obter_nota("Pedro Álvares")
        adicionar_aluno("Mariana Costa", 9.8) 
        listar_alunos()
        obter_nota("Aluno Fantasma")

    except requests.exceptions.ConnectionError:
        print("\n" + "="*50)
        print("ERRO: Não foi possível conectar à API.")
        print(f"Verifique se o servidor FastAPI (uvicorn) está rodando em {BASE_URL}")
        print("="*50)