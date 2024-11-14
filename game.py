import numpy as np
import pandas as pd
import ast


class Wonder:
    def __init__(self, name, starting_resource, first_step, second_step, third_step):
        self.name = name
        self.starting_resource = starting_resource
        self.first_step = first_step
        self.second_step = second_step
        self.third_step = third_step

class Card:
    def __init__(self, name, card_type, cost, effect, war, points, shortcuts, min_players, age):
        self.name = name
        self.card_type = card_type
        self.cost = cost
        self.effect = effect
        self.war = war
        self.points = points
        self.shortcuts = shortcuts
        self.min_players = min_players
        self.age = age

    def playable(self, player_shortcuts, player_resources, player_coins):
        # Shortcut
        if self.shortcuts:
            for item in self.shortcuts:
                if item in player_shortcuts:
                    return True

        # Coins cost
        elif "coins" in self.cost:
            if player_coins >= self.cost["coins"]:
                return True
            else:
                return False

        # Resources cost
        # still need choice implementation !     
        else:
            for resource, quantity in self.cost.items():
                if player_resources.get(resource, 0) < quantity:
                    return False

        return True
    
    def __repr__(self):
        return f"Name: {self.name}, Type: {self.card_type}, Coût: {self.cost}, Effet: {self.effect}, War: {self.war}, Points: {self.points}, shortcuts: {self.shortcuts}, Min_player: {self.min_players}, Age: {self.age} \n"

class Player:
    def __init__(self, name, wonder = None):
        self.name = name
        self.wonder = wonder
        self.resources = {"wood" : 0, "stone" : 0, "clay" : 0, "ore" : 0, "glass" : 0, "cloth" : 0, "papyrus" : 0}
        self.played_cards = []
        self.points = 0
        self.war = 0
        self.sciences = {"wheel" : 0, "tablet" : 0, "compass" : 0}
        self.coins = 3
        self.shortcuts = []

    def play_card(self, card):

        # Make sure you can play the card
        if card.playable(self.shortcuts, self.resources, self.coins):
            self.played_cards.append(card)

            # Card effects
            if card.card_type == "raw_materials":
                # TODO
                if "choice" in card.effect:
                    pass
                else:
                    for resource, quantity in card.effect:
                        self.add_resource(resource, quantity)

            if card.card_type == "manufactured_goods":
                for resource, quantity in card.effect:
                    self.add_resource(resource, quantity)

            if card.card_type == "civil_buildings":
                self.points += card.points

            if card.card_type == "war_buildings":
                self.war += card.war
            
            if card.card_type == "scientific_buildings":
                for science, quantity in card.effect:
                    self.add_science(science, quantity)
            
            if card.card_type == "comercial_buildings":
                #TODO
                pass

            if card.card_type == "guilde":
                #TODO
                pass
            

            print(f"{self.name} played card {card.name}.")
        else:
            print(f"{self.name} can't play the card {card.name} (conditions not met).")
        


    def add_resource(self, resource, quantity):
        if resource in self.resources:
            self.resources[resource] +=quantity
        else:
            print(f"Resource {resource} does not exist.")
    
    def add_science(self, science, quantity):
        if science in self.sciences:
            self.sciences[science] +=quantity
        else:
            print(f"Science {science} does not exist.")

# generics methods
def import_cards(path):
    deck_cards = []
    cards = pd.read_excel(path)
    for index, row in cards.iterrows():
        name = row["name"]
        card_type = row["card_type"]
        cost = ast.literal_eval(row["cost"])
        effect = ast.literal_eval(row["effect"])
        war = int(row["war"])
        points = int(row["points"])
        shortcuts = ast.literal_eval(row["shortcuts"])
        min_players = int(row["min_players"])
        age = int(row["age"])

        card = Card(name, card_type, cost, effect, war, points, shortcuts, min_players, age)
        deck_cards.append(card)
    return deck_cards

def main():
    deck_cards = import_cards('resources/cards.xlsx')
    print(deck_cards)
    print(deck_cards[0].shortcuts[0])
    
    


if __name__ == "__main__":
    main()