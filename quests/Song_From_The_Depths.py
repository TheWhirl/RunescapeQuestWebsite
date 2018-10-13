import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Song_From_The_Depths(Quest):

    def __init__(self):
        super().__init__("Song from the Depths")
        self.free = True
        self.age = 5
