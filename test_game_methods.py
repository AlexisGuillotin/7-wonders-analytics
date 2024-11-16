import unittest
import game

class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.first_step = game.Card("first", "civil_buildings", {"clay" : 2}, {}, 0, 3, [], 2, 1)
        cls.second_step = game.Card("second", "scientific_buildings", {"ore" : 2, "cloth": 1}, {"compass" : 1, "tablet" : 1, "wheel" : 1}, 0, 0, [], 2, 2)
        cls.third_step = game.Card("third", "civil_buildings", {"wood" : 4}, {}, 0, 7, [], 2, 3)
        cls.Wonder = game.Wonder("Babylon",{"wood" : 1}, cls.first_step, cls.second_step, cls.third_step)
        cls.Player = game.Player("player1", cls.Wonder)
        cls.card1 = game.Card("atelier", "scientific_buildings", {"glass" : 1}, {"wheel" : 1}, 0, 0, ["target", "lamp"], 7, 1)

    def test_add_resource(self):
        self.Player.add_resource("glass", 1)
        self.assertEqual(self.Player.resources,{"glass" : 1})

    def test_playable(self):
        
        self.assertEqual(self.card1.playable(self.Player.shortcuts, self.Player.resources, self.Player.coins), True)
        #self.Player.add_resource("glass",1)
        #self.assertEqual(self.card1.playable(self.Player.shortcuts, self.Player.resources, self.Player.coins), True)

if __name__ == "__main__":
    unittest.main()