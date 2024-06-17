########################
# Dificultad: 3/5
# Duración: 55m
########################

def main():
    n, k = map(int, input().split())
    poleras_compradas = [int(x) for x in input().split()]
    poleras_necesitadas = [int(x) for x in input().split()]
    nuevas_poleras = poleras_compradas[:]

    # k = máximo que se puede encoger 
    # i = talla

    compradas_totales = 0
    compradas_necesitadas = 0
    needs = []

    for i in range(len(poleras_compradas)):
        compradas_totales += poleras_compradas[i]
        compradas_necesitadas += poleras_necesitadas[i]
        needs.append(poleras_necesitadas[i] - poleras_compradas[i])

    for i in range(n):
        for p in range(1, k + 1):
            if i - p >= 0 and needs[i - p] > 0:
                if nuevas_poleras[i] >= needs[i - p]:
                    nuevas_poleras[i - p] += needs[i - p]
                    nuevas_poleras[i] -= needs[i - p]
                    needs[i - p] = 0
                else:
                    nuevas_poleras[i - p] += nuevas_poleras[i]
                    needs[i - p] -= nuevas_poleras[i]
                    nuevas_poleras[i] = 0
    for i in range(0, len(poleras_compradas)):
        if nuevas_poleras[i]<poleras_necesitadas[i]:
            return print("NO")
        
    print("SI")
if __name__ == "__main__":
    main()
