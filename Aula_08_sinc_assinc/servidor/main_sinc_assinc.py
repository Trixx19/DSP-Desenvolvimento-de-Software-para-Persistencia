from fastapi import FastAPI
import time
import asyncio

app = FastAPI()


@app.get("/sinc")
#Trabalhar com dados em memória/arquivo, ou bd blocantes,
#use rotas sincronas
def rota_sincrona():
    #operação blocante
    time.sleep(2)
    return {"tipo": "SÍNCRONA"}

#Trabalhar com chamadas assincronas dentro da API, como por exemplo, httpx,
#acessar uma basi de dados com asyncpg ou simulando com asyncio.
@app.get("/assinc")
async def rota_assincrona():
    # simulando uma chamada assincrona!
    await asyncio.sleep(2)
    return {"Tipo": "ASSÍNCRONA"}