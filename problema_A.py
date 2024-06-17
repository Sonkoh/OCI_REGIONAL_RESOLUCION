########################
# Dificultad: 1/5
# Duración: 20m
########################

torrents_count = int(input())
torrents = []
for i in range(0, torrents_count):
    seeds, peers = map(int, input().split())
    torrents.append((seeds, peers))

def ctr(a):
    return (-a[0], a[1])

print(torrents.index(sorted(torrents, key=ctr)[0])+1)