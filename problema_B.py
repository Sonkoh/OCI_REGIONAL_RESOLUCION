########################
# Dificultad: 2/5
# Duración: 50m
########################

papas, personas, pos_julieta = map(int, input().split())
papas_size = [int(x) for x in input().split()]

papas = len(papas_size)
es_julieta = []
for i in range(0, personas):
    es_julieta.append(i+1 == pos_julieta)
papas_de_otros = 0
papas_de_julieta = 0
racion = 0
papas_size.sort(reverse=True)
while papas > 0:
    for i in range(0, personas):
        if es_julieta[i]:
            racion = racion + papas_size[i]
        papas = papas-1
        papas_size = papas_size[1:]
        if papas == 0:
            break

print(racion)
