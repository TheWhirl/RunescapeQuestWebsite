import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Clock_Tower(Quest):

    def __init__(self):
        super().__init__("Clock Tower")
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Short"
        self.quest_points = 1
