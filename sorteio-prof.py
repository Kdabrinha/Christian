#sorteio dos alunos para apagar o quadro


import random

al1=input("Digite o nome do aluno -> ")
print(50*"_")
al2=input("Digite o nome do aluno -> ")
print(50*"_")                                        #recebendo
al3=input("Digite o nome do aluno -> ")
print(50*"_")
al4=input("Digite o nome do aluno -> ")
print(50*"_")

lis=[al1, al2,al3,al4]                     #criando lista
escolhido=random.choice(lis)                 #sorteio    

print("O sorteado(a) foi -> ", escolhido)#resultado
