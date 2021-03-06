import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Cabin_Fever(Quest):

    def __init__(self):
        super().__init__("Cabin Fever")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 2

        self.agility = 42
        self.crafting = 45
        self.smithing = 50
        self.ranged = 40
