import numpy as np
import pandas as pd

class Card:
    def __init__(self, nom, card_type, cost, effect, points):
        self.nom = nom
        self.card_type = card_type
        self.cost = cost
        self.effect = effect
        self.points = points

    def playable(self, player_resources):
        for resource, quantity in self.cost.items():
            if player_resources.get(resource, 0) < quantity:
                return False
        return True

class Player:
    def __init__(self, name, wonder = None):
        self.nom = name
        self.wonder = wonder
        self.resources = {"wood" : 0, "stone" : 0, "clay" : 0, "ore" : 0, "glass" : 0, "cloth" : 0, "papyrus" : 0}
        self.played_cards = []
        self.points = 0
        self.military = 0
        self.science = {"wheel" : 0, "tablet" : 0, "compass" : 0}

    def play_card(self, card):
        if card.playable(self.resources):
            self.played_cards.append(card)
            self.points += card.points

            # Card effects
            if card.card_type == "military":
                self.military += card.effect.get("military", 0)
            elif card.card_type == "science":
                for symbol, value in card.effect.items():
                    if symbol in self.science:
                        self.science[symbol] += value
            elif card.card_type == "resource":
                for resource, quantity in card.effect.items():
                    self.add_resource(resource, quantity)
            print(f"{self.name} played card {card.name}.")
        else:
            print(f"{self.name} can't play the card {card.name} (conditions not met).")
        


    def add_resource(self, resource, quantity):
        if resource in self.resources:
            self.resources[resource] +=quantity
        else:
            print(f"Resource {resource} does not exist.")

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()