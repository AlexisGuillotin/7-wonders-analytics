import unittest
import game

class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.first_step = game.Card("first", "civil_buildings", {"clay" : 2}, {}, 0, 3, [], 2, 1)
        cls.second_step = game.Card("second", "scientific_buildings", {"ore" : 2, "cloth": 1}, {"compass" : 1, "tablet" : 1, "wheel" : 1}, 0, 0, [], 2, 2)
        cls.third_step = game.Card("third", "civil_buildings", {"wood" : 4}, {}, 0, 7, [], 2, 3)
        cls.wonder = game.Wonder("Babylon",{"wood" : 1}, cls.first_step, cls.second_step, cls.third_step)
        cls.player = game.Player("player1", cls.wonder)
        cls.card1 = game.Card("atelier", "scientific_buildings", {"glass" : 1}, {"wheel" : 1}, 0, 0, ["target", "lamp"], 7, 1)

    def test_add_resource(self):
        self.player.add_resource("glass", 1)
        self.assertEqual(self.player.resources,{'wood': 0, 'stone': 0, 'clay': 0, 'ore': 0, 'glass': 1, 'cloth': 0, 'papyrus': 0})

    def test_playable(self):
        print(self.player.resources)
        self.assertEqual(self.card1.playable(self.player.shortcuts, self.player.resources, self.player.coins), False)
        self.player.add_resource("glass",1)
        self.assertEqual(self.card1.playable(self.player.shortcuts, self.player.resources, self.player.coins), True)

if __name__ == "__main__":
    unittest.main()