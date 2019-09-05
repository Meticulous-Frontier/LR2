## Booty Call Crisis. Girl you are FWB with calls you for some casual sex.
init -1 python:
    booty_call_mod_weight = 5     # Set High for testing. TODO set lower after play testing

init 3 python:
    #sports_bar = Room("bar", "Bar", [], room_background_image("bar_background.png"), [make_floor(), make_wall(), make_chair(), make_window()], [], [], True, [6,5], None, True)
    def casual_sex_booty_call_requirement():
        if time_of_day > 0 : #Not early morning
            if time_of_day < 4: #Not night
                return True
        return False

    def get_casual_sex_booty_call_person():
        possible_people = []
        for person in known_people_in_the_game([mc]):
            # check if person has a casual sex role and we have her phone number
            # only works for role names and not objects since the casual_role object has a name of ??????
            if any([x.role_name for x in person.special_role] for x in ["College Athlete", "Hotwife", "Flight Attendant"]) and person.event_triggers_dict.get("booty_call", False):
                possible_people.append(person)

        return get_random_from_list(possible_people)

    casual_sex_booty_call = ActionMod("Booty Call", casual_sex_booty_call_requirement,"casual_sex_booty_call_label",
        menu_tooltip = "A friend sends you a phone message", is_crisis = True, crisis_weight = booty_call_mod_weight)

label casual_sex_booty_call_label:
    $ the_person = get_casual_sex_booty_call_person()
    # No one qualified so end here
    if the_person is None:
        return

    "While you're going about your day you get a text from [the_person.possessive_title]."
    the_person.char "Hey stud! Up for some fun?"
    menu:
        "Definitely":
            the_person.char "Great!"
            python: #For now, make them naked upon arrival at the hookup scene.
                for i in range(3):
                    the_person.outfit.remove_random_upper(top_layer_first = True)
                    the_person.outfit.remove_random_lower(top_layer_first = True)
            $ the_person.call_dialogue("hookup_accept")
            if the_person.arousal > 100 and the_person.core_sluttiness < 100:
                $ the_person.change_slut_core(2)

        "Not Now":
            "After a few minutes, you get a response."
            $ the_person.call_dialogue("hookup_rejection")
            python:
                for i in range(3):
                    the_person.outfit.remove_random_upper(top_layer_first = True)
                    the_person.outfit.remove_random_lower(top_layer_first = True)
            $ the_person.draw_person(position = the_person.event_triggers_dict.get("reject_position", "missionary"))
            "She sends you a pic of herself masturbating."
    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
    $renpy.scene("Active")
    return
