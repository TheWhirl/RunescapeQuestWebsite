import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Smoking_Kills(Quest):

    def __init__(self):
        super().__init__("Smoking Kills")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Short"
        self.quest_points = 1

        self.slayer = 35
        self.crafting = 25
