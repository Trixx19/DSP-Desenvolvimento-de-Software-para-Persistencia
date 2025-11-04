
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

df_alunos = pd.DataFrame(columns=['nota'])
df_alunos.index.name = 'nome'


@app.post("/alunos")
def adicionar_aluno(nome: str, nota: float):
   
    df_alunos.loc[nome] = nota
        
    return {"mensagem": f"Nota de {nome} registrada/atualizada com sucesso para {nota}."}


@app.get("/alunos/{nome}")
def obter_nota(nome: str):
    if nome in df_alunos.index:
        nota_aluno = float(df_alunos.loc[nome, 'nota'])
        return {"nome": nome, "nota": nota_aluno}
    else:
        return print("Aluno não foi registrado.")


@app.get("/alunos")
def listar_alunos():
    
    df_para_json = df_alunos.reset_index()
    
    return df_para_json.to_dict(orient="records")