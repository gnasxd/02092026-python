resp = input("Deseja começar o sistema de correção?: ").strip().lower()

while resp not in ["nao","não"]:
    r1 = (input("""1 Questão. Qual das alternativas foi selecionada?
    alternativa [a]
    alternativa [b]
    alternativa [c]
    alternativa [d]
    alternativa [e]""")).strip().lower()
    r2 = (input("""2 Questão. Qual das alternativas foi selecionada?
    alternativa [a]
    alternativa [b]
    alternativa [c]
    alternativa [d]
    alternativa [e]""")).strip().lower()
    r3 = (input("""Ultima Questão. Qual das alternativas foi selecionada?
    alternativa [a]
    alternativa [b]
    alternativa [c]
    alternativa [d]
    alternativa [e]""")).strip().lower() 

    if r1 == "b" and r2 == "a" and r3 == "d":
        print("O aluno acertou 3/3 questões.")
    elif r1 == "b" and r2 =="a" and r3 !="d":
        print("o aluno acertou 2/3 questões.")
    elif r1 == "b" and r2 != "a" and r3 == "d":
        print("o aluno acertou 2/3 das questões.")
    elif r1 != "b" and r2 == "a" and r3 =="d":
        print("o aluno acertou 2/3 questões.")
    elif r1 == "b" and r2 != "a" and r3 !="d":
        print("o aluno acertou 1/3 questões.")
    elif r1 != "b" and r2 == "a" and r3 !="d":
        print("o aluno acertou 1/3 questões.")
    elif r1 !="b" and r2 !="a" and r3 == "d":
        print("o aluno acertou 1/3 questões.")
    else: 
        print("o aluno acertou 0/3 questões.")

    resp = input("Deseja começar outra correção? ").strip().lower()


print("Finalizando o sistema de correção...")
print("Finalizado!")