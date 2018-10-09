import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("quests")])
from QuestInfo import Quest


class Dragon_Slayer(Quest):

    def __init__(self):
        super().__init__("Dragon Slayer")
        self.free = True
