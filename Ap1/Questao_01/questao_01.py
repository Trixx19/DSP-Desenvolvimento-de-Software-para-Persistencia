alunos = []
total_notas = 0.0

with open('dados_alunos.txt', 'r', encoding='utf-8') as f:
    for linha in f:
        linha = linha.strip() 
            
        if linha: 
            nome, curso, nota_str = linha.split('#')                
            nota = float(nota_str)               
            alunos.append({'nome': nome, 'nota': nota})
            total_notas += nota

    if not alunos:
        print("Arquivo 'dados_alunos.txt' está vazio ou não foi processado.")
    else:
       
        media = total_notas / len(alunos)        
        aluno_maior_nota = max(alunos, key=lambda x: x['nota'])
        aluno_menor_nota = min(alunos, key=lambda x: x['nota'])

        print(f"Média da turma: {media:.2f}")
        print(f"Maior nota: {aluno_maior_nota['nota']} ({aluno_maior_nota['nome']})")
        print(f"Menor nota: {aluno_menor_nota['nota']} ({aluno_menor_nota['nome']}")
