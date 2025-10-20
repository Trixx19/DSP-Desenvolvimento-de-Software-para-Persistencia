with open("./aula 1/arquivos/02_arquivo.txt", "r") as file:
    linha = file.readline()
    #print(linha)
    while (linha):
        #.strip
        print(linha, end="")
        linha = file.readline()