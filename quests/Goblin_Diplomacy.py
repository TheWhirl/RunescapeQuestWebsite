import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Goblin_Diplomacy(Quest):

    def __init__(self):
        super().__init__("Goblin Diplomacy")
        self.free = True
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Short"
        self.quest_points = 5
