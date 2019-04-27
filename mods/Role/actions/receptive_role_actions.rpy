# Actions for the receptive role in suggestibility_roles.rpy

init 2 python: # Define actions and requirements for the actual mod here.

    def influence_opinion_requirement(person): # Shows only if person has been affected by suggestibility serum.
        if person.suggestibility > 0:
            return True
        else:
            return False

    influence_opinion = Action("Influence an opinion", influence_opinion_requirement, "influence_opinion_start_label",
        menu_tooltip = "Influence an opinion")








label influence_opinion_start_label(person): # This is the setup phase that you have to get through.
                                                 # We want to set up the setting and allow for choices to tackle them for better or worse results.
                                                 # Do mood checks, relation to player character, opinion checks, personality checks.
                                                 # calc_will() sets the baseline for the character after that use change_willpower(amount) to add and remove.
                                                 # NOTE: Need to add ways to fail before the final segment.
    $ opinion = None
    $ degree = None
    $ discovered = None
    $ people_nearby = len(mc.location.people)
    $ person.willpower = 0
    $ person.willpower = calc_will()

    # Pre-check to let the player know base information about the scenario.
    if calc_power() > person.willpower:
        "Speaker" "You feel confident that you will be able to sway their opinion..."

    elif calc_power() < person.willpower:
        "Speaker" "[person.name] seems to have a sturdy mentality at the moment, proceed with caution"

    else: # Happens if their willpower is equal to your power.
        "Speaker" "This can go either way, don't mess up."

    if len(mc.location.people) > 1: # Check if there are other people nearby and fortify their willpower based on how many.
        $ person.change_willpower(len(mc.location.people)*5)
        "Speaker" "There are [people_nearby] other people around you that might interfer with the process."
        "Speaker" "Try bringing [person.name] to a more secluded area?"

        menu:
            "Yes":
                $ person.change_willpower(-len(mc.location.people)*5) # Run the calculation after making considerable changes.
                "Speaker" "You bring [person.name] away from the others"
                if calc_power() > person.willpower:

                    "Speaker" "Having isolated the target it is now both more focused and pliable."

                else: # Might want to assume that a certain personality or opinion makes them uncomfortable being away from others thus it was a mistake luring them away. Hate and unhappiness might also play into it.
                    if person.love < 0:
                        $ person.draw_person(emotion = "sad")
                        "Speaker" "[person.name] seems to be uncomfortable with being alone in your presence ."

            "No":
                pass

            "Back":
                return

    call influence_opinion_input_label() # Takes input then calls end label
    return

label influence_opinion_end_label():

    if calc_power() > the_person.willpower:
        "Speaker" "You succeed at making the changes"
        $ the_person.add_opinion(opinion, degree, discovered)
    elif calc_will() > calc_power() :
        "Speaker" "[the_person.name]'s mind rejects your suggestions"
    else:
        "Speaker" "You are at a stalemate, try changing your approach"
    $ renpy.scene("Active")
    jump game_loop
