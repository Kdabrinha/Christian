#faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo, calcule e mostre a hipotenusa
import math

ca=float(input("Digite o cateto adjacente ->  "))
                                                                    #recebe
co=float(input("Digite o cateto oposto ->  "))

hi= math.sqrt(ca**2 + co**2)#conta

print("\n", 50* "_")#organizar

print("A hipotenusa desse triângulo retângulo é -> ", hi)#resultado