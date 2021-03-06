import os
import sys
import sqlite3

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("db")])

from QuestSetUp import create_all_quests


def populate_db(db):
    quests, quest_series = create_all_quests()
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    for quest in quests:
        cur.execute("""
                    INSERT INTO quest_details VALUES(
                        ?, ?, ?, ?, ?, ?
                    );
                    """, (quest.name,
                          quest.free,
                          quest.age,
                          quest.difficulty,
                          quest.length,
                          quest.quest_points))

        cur.execute(""" INSERT INTO quest_levels VALUES (
                        ?, ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?, ?, ?);
        """, (quest.name,
              quest.agility,
              quest.attack,
              quest.constitution,
              quest.construction,
              quest.cooking,
              quest.crafting,
              quest.defence,
              quest.divination,
              quest.dungeoneering,
              quest.farming,
              quest.firemaking,
              quest.fishing,
              quest.fletching,
              quest.herblore,
              quest.hunter,
              quest.magic,
              quest.mining,
              quest.prayer,
              quest.ranged,
              quest.runecrafting,
              quest.slayer,
              quest.smithing,
              quest.strength,
              quest.summoning,
              quest.thieving,
              quest.woodcutting)
        )

    for main_quest in quests:
        for pre_quest in main_quest.pre_quests:
            cur.execute("""
                       INSERT INTO pre_quests VALUES(?, ?);
             """, (main_quest.name, pre_quest.name))

    for quest in quests:
        for requirement in quest.other_requirements:
            cur.execute("""
                        INSERT INTO quest_other_requirements VALUES(?, ?);
            """, (quest.name, requirement))

    for quest_s in quest_series:
        for quest in quest_s.quests:
            cur.execute("""
                        INSERT INTO quest_series VALUES (?, ?, ?);
            """, (quest_s.name, quest[0].name, quest[1]))

        for quest in quest_s.related_quests:
            cur.execute("""
                        INSERT INTO quest_series_related VALUES (?, ?);
            """, (quest_s.name, quest.name))

    conn.commit()

    cur.close()
    conn.close()


def init_db(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS quest_details""")
    cur.execute("""DROP TABLE IF EXISTS quest_levels""")
    cur.execute("""DROP TABLE IF EXISTS pre_quests""")
    cur.execute("""DROP TABLE IF EXISTS quest_other_requirements""")
    cur.execute("""DROP TABLE IF EXISTS quest_series""")
    cur.execute("""DROP TABLE IF EXISTS quest_series_related""")

    # Set up table of quest details
    cur.execute('''
                CREATE TABLE quest_details (
                    name TEXT PRIMARY KEY,
                    is_free BOOLEAN NOT NULL,
                    age INTEGER NOT NULL,
                    difficulty TEXT NOT NULL,
                    length TEXT NOT NULL,
                    quest_points INTEGER NOT NULL
                );
            ''')

    cur.execute('''
                CREATE TABLE quest_levels(
                    name TEXT PRIMARY KEY,
                    agility INTEGER,
                    attack INTEGER,
                    constitution INTEGER,
                    construction INTEGER,
                    cooking INTEGER,
                    crafting INTEGER,
                    defence INTEGER,
                    divination INTEGER,
                    dungeoneering INTEGER,
                    farming INTEGER,
                    firemaking INTEGER,
                    fishing INTEGER,
                    fletching INTEGER,
                    herblore INTEGER,
                    hunter INTEGER,
                    magic INTEGER,
                    mining INTEGER,
                    prayer INTEGER,
                    ranged INTEGER,
                    runecrafting INTEGER,
                    slayer INTEGER,
                    smithing INTEGER,
                    strength INTEGER,
                    summoning INTEGER,
                    thieving INTEGER,
                    woodcutting INTEGER,
                    FOREIGN KEY (name) REFERENCES quest_details(name)
                );
            ''')

    cur.execute('''
                CREATE TABLE pre_quests (
                    main_quest TEXT,
                    pre_quest TEXT,
                    PRIMARY KEY (main_quest, pre_quest)
                    FOREIGN KEY (main_quest) REFERENCES quest_details (name),
                    FOREIGN KEY (pre_quest) REFERENCES quest_details (name)
                );
                ''')

    cur.execute('''
                CREATE TABLE quest_other_requirements(
                    name TEXT,
                    requirement TEXT,
                    PRIMARY KEY (name, requirement)
                    FOREIGN KEY (name) REFERENCES quest_details(name)
                );
                ''')

    cur.execute('''
                CREATE TABLE quest_series(
                    name TEXT,
                    quest TEXT,
                    number INTEGER,
                    PRIMARY KEY (name, quest)
                    FOREIGN KEY (quest) REFERENCES quest_details(name)
                );
                ''')

    cur.execute('''
                CREATE TABLE quest_series_related(
                    name TEXT,
                    quest TEXT,
                    PRIMARY KEY (name, quest)
                    FOREIGN KEY (quest) REFERENCES quest_details(name)
                );
                ''')

    conn.commit()
    cur.close()
    conn.close()

    # Set up table containing other requirements


if __name__ == '__main__':
    init_db('quests.db')
    populate_db('quests.db')
