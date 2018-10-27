import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Troll_Romance(Quest):

    def __init__(self):
        super().__init__("Troll Romance")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Medium"
        self.quest_points = 2

        self.agility = 28
