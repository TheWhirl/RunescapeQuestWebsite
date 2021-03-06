import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Mournings_End_Part_I(Quest):

    def __init__(self):
        super().__init__("Mourning's End Part I")
        self.age = 5
        self.difficulty = "Master"
        self.length = "Long to Very Long"
        self.quest_points = 2

        self.ranged = 60
        self.thieving = 50
