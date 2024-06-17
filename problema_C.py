########################
# Dificultad: 1/5
# Duración: 25m
########################


# class Malla:
#     def __init__(self, n) -> None:
#         self.paltas = n

# Malla(n)

# n = paltas en la malla
# r = tasa de maduracion

n,q,kmin,kmax = map(int, input().split())
paltas = [int(x) for x in input().split()]
tiempos_de_madurez = []
for i in range(0,q):
    tiempos_de_madurez.append(input())

# madurez = r*t

# maduracion = r*t

def comestible(maduracion, kmin, kmax):
    if (maduracion<kmin):
        return False
    if (maduracion>kmax):
        return False
    return True

for i in range(0, q):
    comestibles = 0
    for n in range(0, len(paltas)):
        if(comestible(int(tiempos_de_madurez[i])*int(paltas[n]), kmin, kmax)):
            comestibles=comestibles+1
    print(comestibles)