import pandas as pd

#alunos_dic = {
 #   "nome": "Bia",
  #  "curso": "CC",
   # "IRA" : 6.5
#}

#Isso gera um erro, pois alunos_dic Não está formatado como uma lista de dicionários
#alunos_df = pd.DataFrame(alunos_dic)
#rint(alunos_df)

#caso 2 - formatando o objeto de entrada

#alunos_dic = {
 #   "nome": ["Bia"],
  #  "curso": ["CC"],
   # "IRA" : [6.5]
#}

#alunos_df = pd.DataFrame(alunos_dic)
#print(alunos_df)

#caso 3 - alterando todo o objeto de uma vez

alunos_dic = {
   "nome": "julia",
   "curso": "CC",
    "IRA" : 6.5
}

#alunos_df = pd.DataFrame([alunos_dic])
#print(alunos_df)

#persistindo a base de dados em um arquivo csv

alunos_csv = pd.read_csv("Aula 4/alunos.csv")
#print(alunos_csv)

#Problema: persistir o alunos_dic em alunos_csv

#solução 1 - concatenando dois dataframes

#concat recebe uma lista de dataframes
#alunos_csv = pd.concat([alunos_csv, alunos_df], ignore_index=True)
#print(alunos_csv)
#alunos_csv.to_csv("aula3/alunos.csv", index=False)

#solução 2 - "apendando" o objeto ao dataframe original

alunos_csv = alunos_csv._append(alunos_dic, ignore_index=True)
print(alunos_csv)
alunos_csv.to_csv(r"Aula 4\alunos.csv", index=False)
