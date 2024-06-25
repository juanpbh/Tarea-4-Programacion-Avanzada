

print('Hello World')
p_a_n = {"piedra":0, "papel":1, "tijera":2} # para convertir de palabra a número
n_a_p = ["piedra", "papel", "tijera"] # para convertir de número a palabra
def juega():
    from random import randint
    programa=randint(0,2)
    usuario=p_a_n[input("¿piedra, papel o tijera? ")]
    resultado="Empate" if programa==usuario else\
        "Gana Usuario" if (programa+1)%3==usuario else "Gana Programa"
    print("Usuario juega", n_a_p[usuario])
    print("Programa juega", n_a_p[programa])
    print("Resultado:", resultado)

juega()