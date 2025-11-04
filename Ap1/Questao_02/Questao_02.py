import pandas as pd

dados = {
    "Luca Brasi": 12000,
    "Peter Clemenza": 17500,
    "Sal Tessio": 14300,
    "Tom Hagen": 16000,
    "Michael Corleone": 19500
}

receitas_series = pd.Series(dados)

print("--- Receitas Semanais da Família Corleone ---")
print(receitas_series)
print("-" * 45)

total = receitas_series.sum()
media = receitas_series.mean()
associado_max = receitas_series.idxmax()

print(f"Total arrecadado: US$ {total}")
print(f"Média das receitas: US$ {media:.2f}")
print(f"Associado que mais arrecadou: {associado_max}")
print("-" * 45)

acima_media = receitas_series[receitas_series > media]

print("Associados com arrecadação acima da média:")
print(acima_media)