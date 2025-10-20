"""
Seja a Series:

São Paulo:  12.3 milhões de habitantes
Rio de Janeiro: 6.7 milhões de habitantes
Salvador: 2.9 milhões de habitantes

Adicione a cidade de Belo Horizonte e remova a cidade de Salvador.

Dica: Para adiconar, você pode atribuir um valor a uma nova chave colchetes.
para remover, use a função .drop(chave)

"""

import pandas as pd

cidades = pd.Series([12.3, 6.7, 2.9], index=["São Paulo", "Rio de Janeiro", "Salvador"])

#cidades["Belo Horizonte"] = 2.5
cidades.loc["Belo Horizonte"] = 2.5
cidades = cidades.drop("Salvador")
print(cidades)