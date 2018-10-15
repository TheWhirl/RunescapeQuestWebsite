import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Creature_Of_Fenkenstrain(Quest):

    def __init__(self):
        super().__init__("Creature of Fenkenstrain")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 2

        self.crafting = 20
        self.thieving = 25
