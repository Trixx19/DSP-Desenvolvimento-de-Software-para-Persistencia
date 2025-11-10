import httpx
BASE_URL = "http://127.0.0.1:8000"

def listar_produtos():
    response = httpx.get(f"{BASE_URL}/produtos")
    return response.json()

def get_produto_by_id(id: int):
    response = httpx.get(f"{BASE_URL}/produtos/{id}")
    return response.json()

def criar_produto(produto: dict): #dict ou Produto? #Servidor o BaseModel Produto para validar entrada
    response = httpx.post(f"{BASE_URL}/produtos", json=produto)
    return response.json()

def atualizar_produto(id: int, produto: dict):
    response = httpx.put(f"{BASE_URL}/produtos/{id}", json=produto)
    return response.json()

def apagar_produto(id: int):
    response = httpx.delete(f"{BASE_URL}/produtos/{id}")
    return {"status_code": response.status_code}

def maior_preco():
    response = httpx.get(f"{BASE_URL}/produtos/maior_preco")
    return response.json()

def menor_preco():
    response = httpx.get(f"{BASE_URL}/produtos/menor_preco")
    return response.json()

def media_precos():
    response = httpx.get(f"{BASE_URL}/produtos/media_precos")
    return response.json()

def acima_media():
    response = httpx.get(f"{BASE_URL}/produtos/acima_media")
    return response.json()

def abaixo_media():
    response = httpx.get(f"{BASE_URL}/produtos/abaixo_media")
    return response.json()


if __name__ == "__main__":
    print("Testando todos os serviços de forma separada....")
    print("\nListando produtos iniciais:")
    print(listar_produtos())
    print("-" * 30)

    print("\nCriando novo produto 'Corda de Pular':")
    novo_produto = {"nome": "Corda de Pular", "categoria": "Fitness", "preco": 35.00}
    produto_criado = criar_produto(novo_produto)
    print(produto_criado)
    print("-" * 30)


    print("\nAtualizando produto que acabou de ser criado:")
    id_produto = produto_criado.get("id")
    dados_atualizados = {"nome": "Corda de Pular Profissional", "categoria": "Fitness PRO", "preco": 55.75}
    print(atualizar_produto(id_produto, dados_atualizados))
    print("-" * 30)

    print("\nObtendo produto atualizado:")
    print(get_produto_by_id(id_produto))
    print("-" * 30)

    print("\nApagando produto:")
    print(apagar_produto(id_produto))
    print("-" * 30)

    print("\nListando produtos finais:")
    print(listar_produtos())
    print("-" * 30)

    print("TESTANDO OPERAÇÕES ADICIONAIS")
    print("Pegando produto com maior preço:")
    print(maior_preco())
    print("-" * 30)

    print("Pegando produto com menor preço:")
    print(menor_preco())
    print("-" * 30)

    print("Calculando média de preços:")
    print(media_precos())
    print("-" * 30)

    print("Listando produtos acima da média:")
    print(acima_media())
    print("-" * 30)

    print("Listando produtos abaixo da média:")
    print(abaixo_media())
    print("-" * 30)
    
    print("TESTES CONCLUÍDOS")
