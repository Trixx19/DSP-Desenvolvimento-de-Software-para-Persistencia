import httpx

BASE_URL = "http://127.0.0.1:8000"

def criar_aluno():
    resp = httpx.post(
        f"{BASE_URL}/alunos",
        json = {"nome" : "sicrano", "curso" : "CC", "IRA" : 8.5}
    )
    print(resp.json())

criar_aluno