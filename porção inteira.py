#crie um programa que leia um numero decimal e mostre ele em sua porção inteira, EX: digite 5.55 e o resultado vai ser 5

import math

nu=float(input("Digite um número quebrado -> ")) #recebe
nu= math.trunc(nu)#conta

print("\n", 50* "_")#organizar

print("Seu número inteiro é -> ", nu) #resultado