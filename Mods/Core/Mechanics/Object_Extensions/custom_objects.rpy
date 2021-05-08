# NOTE: Masterfile for objects that can be used in rooms. Since these are only relevant if in use I'd like to just throw them all into one place so they are always available to creators.
# NOTE: If this list ever grows huge and you are just looking for something be smart with search functions Ctrl + F. e.g "bed" or "kneel", "sit"

# Objects aimed at the dungeon. Want to give some bonuses for having purchased it.
# Since the Dungeon itself is fairly cheap the items will cost money to unlock as well.
init -1 python:

    def make_bdsmbed():
        return Object("Bed Cuffs", ["Lay", "Low", "Kneel"], sluttiness_modifier = 10, obedience_modifier = 20) # Normal bed is +10.

    def make_pillory():
        return Object("Pillory", ["Stand", "Lean", "Kneel", "Low"], sluttiness_modifier = 15, obedience_modifier = 25)

    def make_woodhorse():
        return Object("Wood Horse", ["Sit", "Lean", "Lay"], sluttiness_modifier = 20, obedience_modifier = 30)

    def make_cage():
        return Object("Cage", ["Lay", "Low", "Kneel"], sluttiness_modifier = 10, obedience_modifier = 20)

    def make_toilet():
        return Object("Toilet", ["Sit", "Low"], sluttiness_modifier = 10, obedience_modifier = 5)

    def make_love_rug():
        return Object("Love Rug", ["Kneel", "Lay"], sluttiness_modifier = 5, obedience_modifier = 10)

    # For parks and gym
    def make_bench():
        return Object("Bench", ["Lay", "Sit", "Low", "Kneel"], sluttiness_modifier = 0, obedience_modifier = -5)

    # For R&D:
    def make_examtable():
        return Object("Exam Table", ["Lay", "Sit", "Low", "Kneel"], sluttiness_modifier = 0, obedience_modifier = 20)

    # For strip_club:
    # strip club stage is make_stage()
    def make_pole():
        return Object("Stripper Pole", ["Lean", "Low"], sluttiness_modifier = 10, obedience_modifier = -5)

    # For renovated MC Bedroom:
    def make_impressive_bed():
        return Object("Impressive Bed", ["Lay", "Low", "Kneel"], sluttiness_modifier = 15, obedience_modifier = 15)

    # Bring out the comfy chair! Nobody expects the Spanish Inquisition!
    def make_comfy_chair():
        return Object("Comfy Chair",["Sit","Low"], sluttiness_modifier = 5, obedience_modifier = 5)

    # Classic porn audition couch
    def make_black_leather_couch():
        return Object("Black Leather Couch",["Sit","Lay","Low"], sluttiness_modifier = 15, obedience_modifier = 5)
