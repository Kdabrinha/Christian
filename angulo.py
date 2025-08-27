#@faça um programa que leia um ângulo qualquer e mostre na tela seno cosceno tangente 
import math

ang=float(input("Digite algum ângulo que você deseja saber o seno, cosceno e a tangente dele -> "))#recebe

print("\n", 50* "_")


ra=math.radians(ang)
seno=math.sin(ra)                               #calculo
cosceno=math.cos(ra)
tan=math.tan(ra)


print("Seno -> ", seno)
print("\n", 50* "_")
print("cosceno -> ", cosceno)                      #resultado
print("\n", 50* "_")
print("tangente -> ", tan)




