import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("questseries")])
from QuestSeriesInfo import QuestSeries


class Enchanted_Key_Series(QuestSeries):

    def __init__(self):
        super().__init__("Enchanted Key Series")
