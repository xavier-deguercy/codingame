import sys
import math

class Factory:
    def __init__(self, entity_id, player, cyborgs, production):
        self.entity_id = entity_id
        self.player = player
        self.cyborgs = cyborgs
        self.production = production

class Troop:
    def __init__(self, entity_id, player, source, destination, cyborgs, turns):
        self.entity_id = entity_id
        self.player = player
        self.source = source
        self.destination = destination
        self.cyborgs = cyborgs
        self.turns = turns

class Game:
    def __init__(self):
        self.factories = []
        self.troops = []

    def parse_input(self):
        factory_count = int(input())  # the number of factories
        link_count = int(input())  # the number of links between factories
        for i in range(link_count):
            factory_1, factory_2, distance = [int(j) for j in input().split()]

    def play(self):
        # game loop
        while True:
            entity_count = int(input())  # the number of entities (e.g. factories and troops)
            for i in range(entity_count):
                inputs = input().split()
                entity_id = int(inputs[0])
                entity_type = inputs[1]
                player = int(inputs[2])
                cyborgs = int(inputs[3])
                production = int(inputs[4])
                source = int(inputs[5])
                

                if entity_type == "FACTORY":
                    factory = Factory(entity_id, player, cyborgs, production)
                    self.factories.append(factory)
                elif entity_type == "TROOP":
                    troop = Troop(entity_id, player, source, destination, cyborgs, turns) # type: ignore
                    self.troops.append(troop)

            # Write an action using print
            # To debug: print("Debug messages...", file=sys.stderr, flush=True)

            # Any valid action, such as "WAIT" or "MOVE source destination cyborgs"
            print("WAIT")

game = Game()
game.parse_input()
game.play()
