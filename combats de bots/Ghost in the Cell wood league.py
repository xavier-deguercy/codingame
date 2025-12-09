import sys
import math

# ---------- Lecture de la carte (une seule fois) ----------

factory_count = int(input())   # nombre d'usines
link_count = int(input())      # nombre de liens entre usines

# Matrice des distances : dist[i][j] = nombre de tours entre i et j
dist = [[None for _ in range(factory_count)] for _ in range(factory_count)]

for _ in range(link_count):
    factory_1, factory_2, d = map(int, input().split())
    dist[factory_1][factory_2] = d
    dist[factory_2][factory_1] = d


class Factory:
    def __init__(self, fid, owner, cyborgs, production):
        self.id = fid
        self.owner = owner          # 1 = toi, -1 = ennemi, 0 = neutre
        self.cyborgs = cyborgs
        self.production = production # 0 à 3


# ---------- Boucle de jeu ----------

while True:
    entity_count = int(input())  # nombre d'entités (usines + troupes)

    factories = {}          # id -> Factory
    my_factories = []       # usines à toi
    neutral_factories = []  # usines neutres
    enemy_factories = []    # usines ennemies

    troops = []             # on les garde pour plus tard si besoin

    for _ in range(entity_count):
        parts = input().split()
        entity_id = int(parts[0])
        entity_type = parts[1]
        arg_1 = int(parts[2])
        arg_2 = int(parts[3])
        arg_3 = int(parts[4])
        arg_4 = int(parts[5])
        arg_5 = int(parts[6])

        if entity_type == "FACTORY":
            owner = arg_1
            cyborgs = arg_2
            production = arg_3

            f = Factory(entity_id, owner, cyborgs, production)
            factories[entity_id] = f

            if owner == 1:
                my_factories.append(f)
            elif owner == 0:
                neutral_factories.append(f)
            elif owner == -1:
                enemy_factories.append(f)

        elif entity_type == "TROOP":
            # Pour l'instant on ne les utilise pas,
            # mais on les stocke pour plus tard si besoin.
            troops.append({
                "id": entity_id,
                "owner": arg_1,
                "source": arg_2,
                "target": arg_3,
                "cyborgs": arg_4,
                "eta": arg_5
            })

    # ---------- Décision : une seule action par tour ----------

    action = "WAIT"  # valeur par défaut

    if my_factories:
        # Usine source : celle qui a le plus de cyborgs
        source = max(my_factories, key=lambda f: f.cyborgs)

        # On attaque seulement si on a au moins 2 cyborgs
        if source.cyborgs > 1:
            # Cibles possibles : toutes les usines qui ne sont pas à nous
            candidates = neutral_factories + enemy_factories

            if candidates:
                # On choisit la cible la plus proche de source.
                # En cas d'égalité de distance, on préfère la meilleure production.
                def target_key(f):
                    return (dist[source.id][f.id], -f.production)

                target = min(candidates, key=target_key)

                # On envoie la moitié des cyborgs de l'usine source
                send = source.cyborgs // 2
                if send > 0:
                    action = f"MOVE {source.id} {target.id} {send}"

    print(action)
