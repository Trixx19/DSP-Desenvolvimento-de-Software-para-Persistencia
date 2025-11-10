#uvicorn servidor:app --reload
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import os
import asyncio

app = FastAPI() #iniciar api
lock = asyncio.Lock() #Protege a região crítica quando várias requisições paralelas tentam modificar o DataFrame ao mesmo tempo.
CSV_FILE = "produtos.csv"

class Produto(BaseModel):
    id: int | None = None
    nome: str
    categoria: str
    preco: float

if os.path.exists(CSV_FILE):
    produtos_df = pd.read_csv(CSV_FILE)
else:
    print("Arquivo produtos.csv não encontrado. Criando arquivo vazio...")
    produtos_df = pd.DataFrame(columns=["id", "nome", "categoria", "preco"])

next_id = produtos_df["id"].max() + 1 if not produtos_df.empty else 1
#print("Primeira ID:", next_id) #está certo

@app.get("/produtos") #todos produtos
def listar_produtos():
    return produtos_df.to_dict(orient='records')

@app.post("/produtos")
async def criar_produto(produto: Produto):
    async with lock:
        global next_id, produtos_df
        
        novo_produto_data = {
            'id': int(next_id),
            'nome': produto.nome,
            'categoria': produto.categoria,
            'preco': produto.preco
        }
        
        novo_produto_df = pd.DataFrame([novo_produto_data])
        produtos_df = pd.concat([produtos_df, novo_produto_df], ignore_index=True)
        
        next_id += 1 
        produtos_df.to_csv("produtos.csv", index=False)
        return {
            "mensagem": "Produto criado com sucesso!",
            "produto": novo_produto_data
        }

@app.put("/produtos/{id}")
async def atualizar_produto(id: int, produto: Produto):
    global produtos_df
    async with lock:
        antigo_idx = produtos_df.index[produtos_df["id"] == id]
        if antigo_idx.empty:
            raise HTTPException(status_code=404, detail=f"Produto id:{id} não encontrado")

        produtos_df.loc[antigo_idx, ["nome", "categoria", "preco"]] = [
            produto.nome, produto.categoria, produto.preco
        ]

        produtos_df.to_csv(CSV_FILE, index=False)

        return {
            "mensagem": f"Produto {id} atualizado com sucesso!",
            "produto": produtos_df.loc[antigo_idx].to_dict(orient="records")[0]
        }

@app.delete("/produtos/{id}")
async def apagar_produto(id: int):
    global produtos_df
    async with lock:
        produto_apagar_idx = produtos_df.index[ produtos_df["id"] == id ]
        if produto_apagar_idx.empty:
            raise HTTPException(status_code=404, detail=f"Produto com id:{id}, não encontrado")
        produtos_df = produtos_df.drop(produto_apagar_idx).reset_index(drop = True)
        produtos_df.to_csv(CSV_FILE, index=False)
        return { "mensagem":  f"Produto com id {id} apagado com sucesso!"}

#SERVIÇOS ADICIONAIS___________________________________________
#O produto de maior preço e o nome do produto;
@app.get("/produtos/maior_preco")
def maior_preco():
    produto = produtos_df.loc[produtos_df["preco"] == produtos_df["preco"].max()].iloc[0]
    return {
        "mensagem": f"Produto de maior preço é '{produto['nome']}', custando {produto['preco']}.",
        "produto": produto.to_dict()
    }
#O produto de menor preço e o nome do produto;
@app.get("/produtos/menor_preco")
def menor_preco():
    produto = produtos_df.loc[produtos_df["preco"] == produtos_df["preco"].min()].iloc[0]
    return {
        "mensagem": f"Produto de menor preço é '{produto['nome']}', custando {produto['preco']}.",
        "produto": produto.to_dict()
    }


#A média de  preços;
@app.get("/produtos/media_precos")
def media_preco():
    return {"media": produtos_df["preco"].mean()}

#A lista dos produtos mais caros, que estão acima da média (ou igual);
@app.get("/produtos/acima_media")
def acima_media():
    media = produtos_df["preco"].mean()
    return produtos_df[produtos_df["preco"] >= media].to_dict(orient="records")

#A lista dos produtos mais baratos, que estão abaixo da média;
@app.get("/produtos/abaixo_media")
def abaixo_media():
    media = produtos_df["preco"].mean()
    return produtos_df[produtos_df["preco"] < media].to_dict(orient="records")

#________________________
@app.get("/produtos/{id}")#sempre ultima para não pegar rotas erradas(especificas)
def get_produto_by_id(id: int):
    produto = produtos_df[produtos_df['id'] == id]
    if produto.empty:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto.to_dict(orient='records')[0]
