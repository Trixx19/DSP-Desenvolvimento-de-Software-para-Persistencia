from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class Produto(BaseModel):
    nome: str
    categoria: str
    preco: float

class ProdutoInDB(Produto):
    id: int

data = {
    'id': [1, 2, 3],
    'nome': ['Tênis de Corrida', 'Camiseta Esportiva', 'Garrafa de Água'],
    'categoria': ['Calçados', 'Vestuário', 'Acessórios'],
    'preco': [399.90, 79.90, 25.50]
}
produtos_df = pd.DataFrame(data)

next_id = produtos_df['id'].max() + 1 if not produtos_df.empty else 1

@app.get("/produtos", response_model=list[ProdutoInDB])
def get_produtos():
    return produtos_df.to_dict(orient='records')

@app.get("/produtos/{id}", response_model=ProdutoInDB)
def get_produto_by_id(id: int):
    produto = produtos_df[produtos_df['id'] == id]
    if produto.empty:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto.to_dict(orient='records')[0]

@app.post("/produtos", response_model=ProdutoInDB, status_code=201)
def create_produto(produto: Produto):
    global next_id, produtos_df
    
    novo_produto_data = {
        'id': next_id,
        'nome': produto.nome,
        'categoria': produto.categoria,
        'preco': produto.preco
    }
    
    novo_produto_df = pd.DataFrame([novo_produto_data])
    produtos_df = pd.concat([produtos_df, novo_produto_df], ignore_index=True)
    
    next_id += 1 
    
    return novo_produto_data

@app.put("/produtos/{id}", response_model=ProdutoInDB)
def update_produto(id: int, produto_update: Produto):
    global produtos_df
    
    if id not in produtos_df['id'].values:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
        
    produtos_df.loc[produtos_df['id'] == id, 'nome'] = produto_update.nome
    produtos_df.loc[produtos_df['id'] == id, 'categoria'] = produto_update.categoria
    produtos_df.loc[produtos_df['id'] == id, 'preco'] = produto_update.preco
    
    produto_atualizado = produtos_df[produtos_df['id'] == id].to_dict(orient='records')[0]
    return produto_atualizado

@app.delete("/produtos/{id}", status_code=204)
def delete_produto(id: int):
    global produtos_df
    
    if id not in produtos_df['id'].values:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    produtos_df = produtos_df[produtos_df['id'] != id]
    
    return {}