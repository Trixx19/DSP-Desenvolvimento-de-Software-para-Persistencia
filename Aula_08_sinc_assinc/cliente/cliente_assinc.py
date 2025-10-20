import httpx
import time
import asyncio

URL = "http://127.0.0.1:8000"

#def chamar_rota():
    #resp_assinc = httpx.get(f"{URL}/assinc")
    #print("RESP  ASSINC: ", resp_assinc.jason())
async def chamar_rota():

    inicio = time.time()
    async with httpx.AsyncCliente() as cliente:
        r1, r2 = await asyncio.gather(
            cliente.get(f"{URL}/assinc"),
            cliente.get(f"{URL}/sinc")
        )
        print("Resp r1:", r1.jason())
        print("Resp r2:", r2.jason())
    fim = time.time()
    print(f"Tempo total: {fim-inicio:.2f} segundos")


if __name__ == "__name__ ":
    asyncio.run(chamar_rota)