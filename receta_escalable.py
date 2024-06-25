print('Hello World')
import math as m
def receta_mousse(cantidad):
  huevos = m.ceil(int(cantidad) +1)
  azucar = round(int(cantidad))
  chocolate = round(int(cantidad)*25)
  print(f"- {huevos} huevo(s)")
  print(f"- {azucar} cucharada(s) de azúcar")
  print(f"- {chocolate}g de chocolate negro")
n = input("¿Cuantas porciones de mousse de chocolate quieres hacer? ")
receta_mousse(n)