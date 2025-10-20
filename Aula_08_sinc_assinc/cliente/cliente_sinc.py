import httpx

URL = "http://127.0.0.1:8000"

def chamar_rota():
    resp_sinc = httpx.get(f"{URL}/sinc")
    print("RESP SINC: ", resp_sinc.jason())
    resp_assinc = httpx.get(f"{URL}/sinc")
    print("RESP SINC: ", resp_assinc.jason())

if __name__ == "__name__ ":
    chamar_rota()