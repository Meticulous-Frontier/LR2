init -1 python:
    SB_tutorial_crisis_weight = 5

init 2 python:
    def SB_tutorial_event_requirement():
        if mc.location in [mall, mall_salon, gym, home_store, clothing_store, sex_store]:
            unknown, known = get_people_with_status()
            if (len(known) > 0):
                return True
        return False

    def get_known_person():
        unknown, known = get_people_with_status()
        if len(known) == 0:
            return None

        person = get_random_from_list(known)
        # don't flirt in the mall with family members, the dialog feels wrong for this.
        while person in [mom, lily, aunt, cousin]:
            known.remove(person)
            if len(known) == 0:
                return None
            person = get_random_from_list(known)
        return person

    SB_tutorial_crisis = ActionMod("Mall Flirt", SB_tutorial_event_requirement, "SB_tutorial_event",
        menu_tooltip = "You have a short flirt with someone in the mall.", category = "Mall", is_crisis = True, crisis_weight = SB_tutorial_crisis_weight)

label SB_tutorial_event():
    $ the_person = get_known_person()

    if the_person is None:
        return

    $ the_person.draw_person()
    the_person.char "Oh, hey [the_person.mc_title]!"
    mc.name "Hello, [the_person.title]. How are you doing today."
    "[the_person.possessive_title] smiles and bats her eyelashes a few times."
    the_person.char "Well, to be honest, it is much better now that you are here!"
    menu:
        "Looking good girl!":
            the_person.char "Aww, thanks! You're looking pretty sexy yourself..."
            "[the_person.possessive_title] looks your up and down a few times. Her eyes tend to linger on your crotch each time they pass."
            $ the_person.change_slut_temp(5)
            "You flirt back and forth with [the_person.possessive_title], but soon it is time to part ways."
            the_person.char "It was great seeing you! Take care [the_person.mc_title]!"
        "Thank you.":
            "You make some small talk with [the_person.possessive_title]. You catch up on a few various things, but soon it is time to part ways."
            the_person.char "It was great seeing you! Take care [the_person.mc_title]!"
            $ the_person.change_happiness(5)

    $ change_scene_display(mc.location)
    $ renpy.scene("Active")
    return
