import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Spirits_Of_The_Elid(Quest):

    def __init__(self):
        super().__init__("Spirits of the Elid")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Medium"
        self.quest_points = 2

        self.magic = 33
        self.ranged = 37
        self.mining = 37
        self.thieving = 37
