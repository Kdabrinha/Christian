#ordem da apresentação
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
embaralhamento=random.shuffle(lis)               #embaralhando a lista  

print("A ordem é -> ", lis)#resultado
