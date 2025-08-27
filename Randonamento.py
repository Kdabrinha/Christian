import math
import random

na= random.random()
print(f"\nnNúmero aleatório de 0 a 1 -> ", na)

print("\n", 50* "_")


na2= random.randrange(0, 100)

print(f"\nNúmero aleatório de 0 a 100 -> ", na2)

print("\n", 50* "_")


na3= random.randrange(0, 100, 5)

print(f"\nNúmero aleatório de 0 a 100, de 5 em 5 -> ", na3)

print("\n", 50* "_")


lista = ["Pão", "Leite", "Batata", "Dinossario"]

print("Lista de compra 1 -> ", random.choice(lista))

print("\n", 50* "_")

print("Lista de compra 2 -> ", random.choices(lista, k=2))

print("\n", 50* "_")