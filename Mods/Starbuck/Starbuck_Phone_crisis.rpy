# SB will ask MC for some help after she developed an anal fetish

init -1 python:
    SB_fetish_phone_crisis_weight = 5

init 2 python:
    def SB_fetish_phone_requirement():
        if starbuck.has_role(anal_fetish_role):
            if time_of_day > 0 and time_of_day < 4: # only during daytime
                return True
        return False

    SB_fetish_phone_crisis = ActionMod("Starbuck Phone Message", SB_fetish_phone_requirement ,"SB_fetish_phone_crisis_label",
        menu_tooltip = "Starbuck has developed an anal fetish and requests your help from time to time.", category = "Mall", is_crisis = True, crisis_weight = SB_fetish_phone_crisis_weight)

label SB_fetish_phone_crisis_label():
    python:
        current_action = "None"
        if renpy.random.randint(0, 100) <= 25:
            current_action = "masturbate"

    if current_action == "masturbate":
        call starbuck_anal_fetish_masturbate from _call_starbuck_anal_fetish_masturbate_phone_crisis
    elif starbuck.arousal > 60:
        call starbuck_anal_fetish_request from _call_starbuck_anal_fetish_request_phone_crisis
    else:
        call starbuck_anal_fetish_checkup from _call_starbuck_anal_fetish_checkup_phone_crisis

    return