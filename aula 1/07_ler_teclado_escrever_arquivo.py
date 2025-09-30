import sys 

with open("07_ler_escrever.txt", "w") as file:
   linha = input("Digite algo: ")

while linha:
    print("-->" + linha.strip() + "<--")
    linha = sys.stdin.readline()

    
    