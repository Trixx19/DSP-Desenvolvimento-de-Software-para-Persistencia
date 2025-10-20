from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
#import uvicorn

contador_id = 1
alunos_df = pd.read_csv("Aula 3/alunos.csv")

class Aluno(BaseModel):
    nome: str
    curso: str
    IRA: float

def criar_aluno (aluno: Aluno):
    novo = {
        "id": contador_id,
        "nome": aluno.nome,
        "curso": aluno.curso,
        "IRA": aluno.IRA
    }
    