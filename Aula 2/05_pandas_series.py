"""]
Crie uma series com as seguintes notas do aluno:

Matemática: 9.5
Biologia: 8.0
Geografia: 7.5

Em seguida, você deve ADICONAR 0,5 a TODAS as notas de uma unica vez.

Dica: Para somar numa series, use a função .add(valor)
Lembre-se: essa operação NÃO modifica a Series original e sim gera um nova.
"""

import pandas as pd

notas = pd.Series([9.5, 8.0, 7.5], index=['Matemática', 'Biologia', 'Geografia'])   
#notas_ajustadas = notas.add(0.5)

notas = notas.add(0.5)
print(notas)
#print("-------- Notas Ajustadas ----------")
#print(notas_ajustadas)