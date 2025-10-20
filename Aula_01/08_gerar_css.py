#importando pandas como pd
import pandas as pd

#criar o dataframe
dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "curso": ["Matemática", "Física", "Química"],
    "nota": [9.5, 8.7, 7.8]
}

#gerando o dataframe
alunos_df = pd.DataFrame(dados)

# faz a media geral dos alunos --> print(alunos_df["nota"].mean())

# imprime apenas os alunos com media maior que 8 --> print(alunos_df[alunos_df["nota"] > 8])

# imprime o resultado em valor boleano --> print(alunos_df["nota"] > 8)

#alunos_df.to_csv("alunos.csv", index=False)  # Salva o DataFrame em um arquivo CSV 
alunos_df.to_parquet("alunos.parquet", index=False)  # Salva o DataFrame em um arquivo Parquet
