import pandas as pd

#serie não rotulada 
#notas = pd.Series([9.5, 8.0, 7.5, 6.0, 10.0])
#print(notas)

#serie rotulada
#index serve para rotular os elementos da série
notas = pd.Series([9.5, 8.0, 7.5, 6.0, 10.0], index=['Ana', 'Bruno', 'Carlos', 'Daniel', 'Eduardo'])
#print(notas[2])
#print(notas.iloc[2])

#forma pelo label
try:
    print(notas['Ana'])
except Exception as e:
    print("Ocorreu uma exceção:", type(e).__name__)