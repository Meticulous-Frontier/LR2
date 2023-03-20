# NOTE: Masterfile for objects that can be used in rooms. Since these are only relevant if in use I'd like to just throw them all into one place so they are always available to creators.
# NOTE: If this list ever grows huge and you are just looking for something be smart with search functions Ctrl + F. e.g "bed" or "kneel", "sit"

# Objects aimed at the dungeon. Want to give some bonuses for having purchased it.
# Since the Dungeon itself is fairly cheap the items will cost money to unlock as well.
init -1 python:

    def make_bdsmbed():
        return Object("Bed Cuffs", ["Lay", "Low", "Kneel"], sluttiness_modifier = 0, obedience_modifier = 0) # Normal bed is +10.

    def make_pillory():
        return Object("Pillory", ["Stand", "Lean", "Kneel", "Low"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_woodhorse():
        return Object("Wood Horse", ["Sit", "Lean", "Lay"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_cage():
        return Object("Cage", ["Lay", "Low", "Kneel"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_toilet():
        return Object("Toilet", ["Sit", "Low"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_sink():
        return Object("Bathroom Sinks", ["Sit", "Kneel", "Lean"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_love_rug():
        return Object("Love Rug", ["Kneel", "Lay"], sluttiness_modifier = 0, obedience_modifier = 0)

    # For parks and gym
    def make_bench():
        return Object("Bench", ["Lay", "Sit", "Low", "Kneel"], sluttiness_modifier = 0, obedience_modifier = 0)

    # For R&D:
    def make_examtable():
        return Object("Exam Table", ["Lay", "Sit", "Low", "Kneel"], sluttiness_modifier = 0, obedience_modifier = 0)

    # For strip_club:
    # strip club stage is make_stage()
    def make_pole():
        return Object("Stripper Pole", ["Lean", "Low"], sluttiness_modifier = 0, obedience_modifier = 0)

    # Classic porn audition couch
    def make_white_leather_couch():
        return Object("White Leather Couch",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0)
