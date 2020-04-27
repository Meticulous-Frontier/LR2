## Morning Shower Crisis Mod by Tristimdorion
# Based on the Pilotus13 Vanilla extension

## Crisis has been merged with default game see morning_shower_enhanced.
## Remove this file at next release (for now left in for save game compatibility)

init -1 python:
    shower_mod_weight = 5

init 2 python:
    def shower_crisis_requirement():
        return False

    def shower_mod_initialization(self):
        return

    shower_crisis_action = ActionMod("Morning Shower", shower_crisis_requirement,"shower_crisis_action_label", initialization = shower_mod_initialization, allow_disable = False,
        menu_tooltip = "In the morning you notice the door to shower is open and someone is in there.", category="Home", is_crisis = True, is_morning_crisis = True, crisis_weight = 0)

label shower_crisis_action_label:
    return
