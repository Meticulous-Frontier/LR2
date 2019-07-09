## Booty Call Crisis. Girl you are FWB with calls you for some casual sex.
init -1 python:
    booty_call_mod_weight = 7     # Set High for testing. TODO set lower after playtesting

init 3 python:
    #sports_bar = Room("bar", "Bar", [], room_background_image("bar_background.png"), [make_floor(), make_wall(), make_chair(), make_window()], [], [], True, [6,5], None, True)
    def casual_sex_booty_call_requirement():
        if time_of_day > 0 : #Not early morning
            if len(casual_sex_list) > 0:   #Must have atleast one FWB
                return True
        return False

    casual_sex_booty_call = ActionMod("Booty Call", casual_sex_booty_call_requirement,"casual_sex_booty_call_label",
        menu_tooltip = "A friend sends you a phone message", category="Home", is_crisis = True, crisis_weight = booty_call_mod_weight)

label casual_sex_booty_call_label:

    $ the_person = get_random_from_list(casual_sex_list)

    "While you're going about your day you get a text from [the_person.possessive_title]."
    the_person.char "Hey stud! Up for some fun?"
    menu:
        "Definitely":
            the_person.char "Great! Meet me at the bar downtown in 15 minutes"
            #TODO this scene.... writer's block ARG


        "Not Now":
            "After a few minutes, you get a response."
            $ the_person.call_dialogue("hookup_rejection")
            python:
                for i in range(3):
                    the_person.outfit.remove_random_upper(top_layer_first = True)
                    the_person.outfit.remove_random_lower(top_layer_first = True)
            $ the_person.draw_person(position = the_person.event_triggers_dict.get("reject_position", "missionary"))
            "She sends you a pic of herself masturbating."

    $ the_person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
    $renpy.scene("Active")
    return
