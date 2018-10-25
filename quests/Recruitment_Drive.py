import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Recruitment_Drive(Quest):

    def __init__(self):
        super().__init__("Recruitment Drive")
        self.age = 5
        self.difficulty = "Novice"
        self.length = "Medium"
        self.quest_points = 1

        self.herblore = 3
        self.other_requirements.append("Have a female character (can visit Makeover Mage")
