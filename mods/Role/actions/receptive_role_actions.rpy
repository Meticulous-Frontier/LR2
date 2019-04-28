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
    $ person.willpower = calculate_willpower(person)
    $ mc.power = player_willpower()

    # Pre-check to let the player know base information about the scenario.
    if mc.power > person.willpower:
        "Speaker" "You feel confident that you will be able to sway their opinion..."

    elif mc.power < person.willpower:
        "Speaker" "[person.name] seems to have a sturdy mentality at the moment, proceed with caution"

    else: # Happens if their willpower is equal to your power.
        "Speaker" "This can go either way, don't mess up."

    if len(mc.location.people) > 1: # Check if there are other people nearby and fortify their willpower based on how many.
        "Speaker" "There are [people_nearby] other people around you that might interfer with the process."
        "Speaker" "Try bringing [person.name] to a more secluded area?"

        menu:
            "Yes":
                "Speaker" "You bring [person.name] away from the others"
                "Speaker" "Having isolated the target it is now both more focused and pliable."

                # Might want to assume that a certain personality or opinion makes them uncomfortable being away from others thus it was a mistake luring them away. Hate and unhappiness might also play into it.
                if person.love < 30:
                    $ person.change_willpower(10)   # she becomes more stubborn
                    $ person.draw_person(emotion = "sad")
                    "Speaker" "[person.name] seems to be uncomfortable with being alone in your presence ."

            "No":
                $ person.change_willpower(people_nearby * 5)    # persons nearby will interfere with influence

                pass

            "Back":
                return

    call influence_opinion_input_label(person) # Takes input and returns

    if mc.power > person.willpower:
        "Speaker" "You succeed at making the changes"
        $ person.add_opinion(opinion, degree, discovered)
    elif person.willpower > mc.power :
        "Speaker" "[person.name]'s mind rejects your suggestions"
    else:
        "Speaker" "You are at a stalemate, try changing your approach"

    $ renpy.scene("Active")
    jump game_loop
