import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Troll_Stronghold(Quest):

    def __init__(self):
        super().__init__("Troll Stronghold")
        self.age = 5
        self.difficulty = "Experienced"
        self.length = "Short to Medium"
        self.quest_points = 1

        self.agility = 15
        self.thieving = 30
