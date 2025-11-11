import httpx
import asyncio
import time

BASE_URL = "http://127.0.0.1:8000"

async def criar_produto_async(produto):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/produtos",
            json={
                "nome": produto["nome"],
                "categoria": produto["categoria"],
                "preco": produto["preco"]
            }
        )
        return response.json()
    
def listar_produtos():
    response = httpx.get(f"{BASE_URL}/produtos")
    return response.json()

#simular vários clientes em paralelo
async def executar_em_paralelo():
    
    async with httpx.AsyncClient() as cliente:
        inicio = time.time()
        await asyncio.gather(
            criar_produto_async({"nome":"Arma de fogo", "categoria":"utensilio","preco":120}),
            criar_produto_async({"nome":"Boné", "categoria":"vestimenta","preco":7.80}),
            criar_produto_async({"nome":"Caderno", "categoria":"material escolar","preco":15.90}),
            criar_produto_async({"nome":"Dado", "categoria":"objeto","preco":0.50}),
            criar_produto_async({"nome":"Estante", "categoria":"movel","preco":200}),
            criar_produto_async({"nome":"Ferro", "categoria":"objeto","preco":20}),
            criar_produto_async({"nome":"Geladeira", "categoria":"eletrodomestico","preco":1500}),
            criar_produto_async({"nome":"Headset", "categoria":"eletronico","preco":250}),
            criar_produto_async({"nome":"Impressora", "categoria":"eletronico","preco":600}),
            criar_produto_async({"nome":"Jaqueta", "categoria":"vestimenta","preco":80}),
            criar_produto_async({"nome":"Arma de fogo", "categoria":"utensilio","preco":120}),
            criar_produto_async({"nome":"Boné", "categoria":"vestimenta","preco":7.80}),
            criar_produto_async({"nome":"Caderno", "categoria":"material escolar","preco":15.90}),
            criar_produto_async({"nome":"Dado", "categoria":"objeto","preco":0.50}),
            criar_produto_async({"nome":"Estante", "categoria":"movel","preco":200}),
            criar_produto_async({"nome":"Ferro", "categoria":"objeto","preco":20}),
            criar_produto_async({"nome":"Geladeira", "categoria":"eletrodomestico","preco":1500}),
            criar_produto_async({"nome":"Headset", "categoria":"eletronico","preco":250}),
            criar_produto_async({"nome":"Impressora", "categoria":"eletronico","preco":600}),
            criar_produto_async({"nome":"Jaqueta", "categoria":"vestimenta","preco":80}),
            criar_produto_async({"nome":"Arma de fogo", "categoria":"utensilio","preco":120}),
            criar_produto_async({"nome":"Boné", "categoria":"vestimenta","preco":7.80}),
            criar_produto_async({"nome":"Caderno", "categoria":"material escolar","preco":15.90}),
            criar_produto_async({"nome":"Dado", "categoria":"objeto","preco":0.50}),
            criar_produto_async({"nome":"Estante", "categoria":"movel","preco":200}),
            criar_produto_async({"nome":"Ferro", "categoria":"objeto","preco":20}),
            criar_produto_async({"nome":"Geladeira", "categoria":"eletrodomestico","preco":1500}),
            criar_produto_async({"nome":"Headset", "categoria":"eletronico","preco":250}),
            criar_produto_async({"nome":"Impressora", "categoria":"eletronico","preco":600}),
            criar_produto_async({"nome":"Jaqueta", "categoria":"vestimenta","preco":80}),
            criar_produto_async({"nome":"Arma de fogo", "categoria":"utensilio","preco":120}),
            criar_produto_async({"nome":"Boné", "categoria":"vestimenta","preco":7.80}),
            criar_produto_async({"nome":"Caderno", "categoria":"material escolar","preco":15.90}),
            criar_produto_async({"nome":"Dado", "categoria":"objeto","preco":0.50}),
            criar_produto_async({"nome":"Estante", "categoria":"movel","preco":200}),
            criar_produto_async({"nome":"Ferro", "categoria":"objeto","preco":20}),
            criar_produto_async({"nome":"Geladeira", "categoria":"eletrodomestico","preco":1500}),
            criar_produto_async({"nome":"Headset", "categoria":"eletronico","preco":250}),
            criar_produto_async({"nome":"Impressora", "categoria":"eletronico","preco":600}),
            criar_produto_async({"nome":"Jaqueta", "categoria":"vestimenta","preco":80}),
            criar_produto_async({"nome":"Arma de fogo", "categoria":"utensilio","preco":120}),
            criar_produto_async({"nome":"Boné", "categoria":"vestimenta","preco":7.80}),
            criar_produto_async({"nome":"Caderno", "categoria":"material escolar","preco":15.90}),
            criar_produto_async({"nome":"Dado", "categoria":"objeto","preco":0.50}),
            criar_produto_async({"nome":"Estante", "categoria":"movel","preco":200}),
            criar_produto_async({"nome":"Ferro", "categoria":"objeto","preco":20}),
            criar_produto_async({"nome":"Geladeira", "categoria":"eletrodomestico","preco":1500}),
            criar_produto_async({"nome":"Headset", "categoria":"eletronico","preco":250}),
            criar_produto_async({"nome":"Impressora", "categoria":"eletronico","preco":600}),
            criar_produto_async({"nome":"Jaqueta", "categoria":"vestimenta","preco":80}),
            criar_produto_async({"nome":"Arma de fogo", "categoria":"utensilio","preco":120}),
            criar_produto_async({"nome":"Boné", "categoria":"vestimenta","preco":7.80}),
            criar_produto_async({"nome":"Caderno", "categoria":"material escolar","preco":15.90}),
            criar_produto_async({"nome":"Dado", "categoria":"objeto","preco":0.50}),
            criar_produto_async({"nome":"Estante", "categoria":"movel","preco":200}),
            criar_produto_async({"nome":"Ferro", "categoria":"objeto","preco":20}),
            criar_produto_async({"nome":"Geladeira", "categoria":"eletrodomestico","preco":1500}),
            criar_produto_async({"nome":"Headset", "categoria":"eletronico","preco":250}),
            criar_produto_async({"nome":"Impressora", "categoria":"eletronico","preco":600}),
            criar_produto_async({"nome":"Jaqueta", "categoria":"vestimenta","preco":80}),
            criar_produto_async({"nome":"Arma de fogo", "categoria":"utensilio","preco":120}),
            criar_produto_async({"nome":"Boné", "categoria":"vestimenta","preco":7.80}),
            criar_produto_async({"nome":"Caderno", "categoria":"material escolar","preco":15.90}),
            criar_produto_async({"nome":"Dado", "categoria":"objeto","preco":0.50}),
            criar_produto_async({"nome":"Estante", "categoria":"movel","preco":200}),
            criar_produto_async({"nome":"Ferro", "categoria":"objeto","preco":20}),
            criar_produto_async({"nome":"Geladeira", "categoria":"eletrodomestico","preco":1500}),
            criar_produto_async({"nome":"Headset", "categoria":"eletronico","preco":250}),
            criar_produto_async({"nome":"Impressora", "categoria":"eletronico","preco":600}),
            criar_produto_async({"nome":"Jaqueta", "categoria":"vestimenta","preco":80}),
            criar_produto_async({"nome":"Arma de fogo", "categoria":"utensilio","preco":120}),
            criar_produto_async({"nome":"Boné", "categoria":"vestimenta","preco":7.80}),
            criar_produto_async({"nome":"Caderno", "categoria":"material escolar","preco":15.90}),
            criar_produto_async({"nome":"Dado", "categoria":"objeto","preco":0.50}),
            criar_produto_async({"nome":"Estante", "categoria":"movel","preco":200}),
            criar_produto_async({"nome":"Ferro", "categoria":"objeto","preco":20}),
            criar_produto_async({"nome":"Geladeira", "categoria":"eletrodomestico","preco":1500}),
            criar_produto_async({"nome":"Headset", "categoria":"eletronico","preco":250}),
            criar_produto_async({"nome":"Impressora", "categoria":"eletronico","preco":600}),
            criar_produto_async({"nome":"Jaqueta", "categoria":"vestimenta","preco":80})
        )
        fim = time.time()
        print(f"TOTAL: {fim-inicio} segundos")

if __name__ == "__main__":
   asyncio.run(executar_em_paralelo())
   print(listar_produtos())