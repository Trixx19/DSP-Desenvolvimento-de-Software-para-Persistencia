import httpx

BASE_URL = "http://127.0.0.1:8000"


def listar_produtos():
    response = httpx.get(f"{BASE_URL}/produtos")
    return response.json()

def obter_produto(id: int):
    response = httpx.get(f"{BASE_URL}/produtos/{id}")
    return response.json()

def criar_produto(produto: dict):
    response = httpx.post(f"{BASE_URL}/produtos", json=produto)
    return response.json()

def atualizar_produto(id: int, produto: dict):
    response = httpx.put(f"{BASE_URL}/produtos/{id}", json=produto)
    return response.json()

def apagar_produto(id: int):
    response = httpx.delete(f"{BASE_URL}/produtos/{id}")
    return {"status_code": response.status_code}

if __name__ == "__main__":
    print("--- INICIANDO TESTES DA API DE PRODUTOS ---")
    print("\n[PASSO 1] Listando produtos iniciais:")
    produtos_iniciais = listar_produtos()
    print(produtos_iniciais)
    print("-" * 30)

    print("\n[PASSO 2] Criando um novo produto: 'Corda de Pular'")
    novo_produto_data = {"nome": "Corda de Pular", "categoria": "Acessórios", "preco": 35.00}
    produto_criado = criar_produto(novo_produto_data)
    print("Produto criado:", produto_criado)
    print("-" * 30)
    
    id_do_novo_produto = produto_criado.get("id")

    print("\n[PASSO 3] Listando produtos após a criação:")
    print(listar_produtos())
    print("-" * 30)

    print(f"\n[PASSO 4] Atualizando o produto com ID {id_do_novo_produto}:")
    dados_atualizados = {"nome": "Corda de Pular Profissional", "categoria": "Acessórios", "preco": 55.75}
    produto_atualizado = atualizar_produto(id_do_novo_produto, dados_atualizados)
    print("Produto atualizado:", produto_atualizado)
    print("-" * 30)

    print(f"\n[PASSO 5] Verificando o produto com ID {id_do_novo_produto} individualmente:")
    print(obter_produto(id_do_novo_produto))
    print("-" * 30)

    print(f"\n[PASSO 6] Apagando o produto com ID {id_do_novo_produto}:")
    resultado_delete = apagar_produto(id_do_novo_produto)
    print("Resultado da operação de apagar:", resultado_delete)
    print("-" * 30)

    print("\n[PASSO 7] Listando produtos finais:")
    produtos_finais = listar_produtos()
    print(produtos_finais)
    print("-" * 30)
    
    print("--- TESTES CONCLUÍDOS ---")