"""
Filtragem de dados 

Use a mensma Series do 05_pandas_series.py, imprimindo apenas as notas que são maiores que 7.0

Dica: Para filtrar uma Series use: "nome_series <operador> valor" como indice do colchetes de 
series original (nome_series)
"""
import pandas as pd

notas = pd.Series([9.5, 8.0, 6], index=['Matemática', 'Biologia', 'Geografia'])   

notas = notas[notas > 7.0]
print(notas)