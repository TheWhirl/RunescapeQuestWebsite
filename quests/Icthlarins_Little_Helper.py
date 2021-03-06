import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Icthlarins_Little_Helper(Quest):

    def __init__(self):
        super().__init__("Icthlarin's Little Helper")
        self.age = 5
        self.difficulty = "Intermediate"
        self.length = "Long"
        self.quest_points = 2
