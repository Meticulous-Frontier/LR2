# Challenge concept:
                  # Baseline should be a 50% success rate as other factors will ALWAYS play in one way or another.
                  # Suggestibility increases success chance by 10% per 10 points. 20 sluttiness = 20% increase
                  # Players charisma increases success chance by 5% per point. 2 Charisma = 10% increase
                   # Targets focus decreases success chance by 10% per point. 2 Focus = 20% decrease
                   # Targets obedience increases success chance by 0.1% per point. 100 obedience = 10% increase.
                   # Being in public adds another 20% decrease in success rate.
# TODO: Make a screen and a room action to develop techniques
      # Make the_person the_person.willpower be affected by choices made through dialogue and not only during final calculation.
      # Create additional actions and labels
      # Create a serum that gives a "Receptive" role. Instead of handing it out to everyone.

init -1 python:

    # Thematic lists NOTE: These lists should be appendable from within the game
    exhib_list = ["naked", "nude"] # Showing off, not nescessary connected to sluttiness
    voyer_list = ["spying"] # Observing lewd acts
    sub_list = ["submissive"] # Submissive behavior
    preg_list = ["pregnant"] # Pregnancy or pregnancy play
    dom_list = ["dominant"] # Domimant behavior
    sadist_list = [] # Sadistic behavior

    #def suggest_training():
    #    training_progress = training_progress
    #    if training_progress == 10:
    #        return "No more stages"
    #    else:
    #        training_progress += 1
    #        return training_progress

    def change_willpower(amount, add_to_log = True):
        the_person.willpower += amount
        if the_person.willpower < 0:
            the_person.willpower = 0

    def change_power(amount, add_to_log = True):
        mc.power += amount
        if mc.power < 0:
            mc.power = 0


    def calc_power():
        mc.power = 0

        mc.power += int(mc.charisma*5) # Positive character modifiers
        mc.power += int(mc.current_stamina*1.5)


        return mc.power

    def calc_willpower(): # Base calculation.
                          # The goal for the player is to bring the the_person.willpower below their suggest_power.
        the_person.willpower = 0

        the_person.willpower += int(the_person.focus * 10)
        the_person.willpower += int(the_person.happiness * 0.2)

        the_person.willpower -= int(the_person.obedience * 0.1)
        the_person.willpower -= int(the_person.love * 0.2)
        the_person.willpower -= int(the_person.suggestibility * 0.5)

        if people_nearby > 1: # If there are more people than just the target.
            the_person.willpower += int(len(mc.location.people)*5)

        if opinion != None: # If the opinion is not set yet it will not be in the calculation
            if any(srchstr in opinion for srchstr in exhib_list): # Check if opinion is in a list
                    if the_person in mc.business.get_employee_list(): # Check if the person is employeed
                        if corporate_enforced_nudity_policy.is_owned():
                            the_person.willpower -= 10

        # Personality checks

        # Opinion checks

        # Salary check
#        if approach == "authority":
#            if the_person in mc.business.get_employee_list():
#                if the_person.calculate_base_salary() < the_person.salary:
#                    the_person.willpower -= 2
        return the_person.willpower

#$ authority_employees = 65 + (mc.charisma*5) + (the_person.obedience * 0.1) + (the_person.suggestibility * 0.5) - (the_person.focus * 10) # Baseline for employed characters. Will take policies into consideration.
#$ authority = 50 + (mc.charisma*5) + (the_person.obedience * 0.1) + (the_person.suggestibility * 0.5) - (the_person.focus * 10) # Baseline if trying to speak to their obedience, will take personality and likes into consideration.
#$ emotional = 50 + (mc.charisma*5) + (the_person.love * 0.2) + (the_person.suggestibility * 0.5) - (the_person.focus * 10) # Baseline if using "emotional manipulation" aka love stat. Will take personality and likes into consideration.
#$ accusing = 50 + (mc.charisma*5) + (the_person.obedience * 0.1) + (the_person.suggestibility * 0.5) - (the_person.happiness * 0.1) # Baseline if being accusing and trying to "correct" their wrong thinking. Given a bonus if target is "unhappy" / "depressed"

init -1 python:
    pass


label influence_opinion_start_label(the_person): # This is the setup phase that you have to get through.

    $ opinion = None
    $ degree = None
    $ discovered = None
    $ people_nearby = len(mc.location.people)
    $ the_person.willpower = calc_willpower()
    $ mc.power = calc_power()

    # Pre-check to let the player know base information about the scenario.
    if mc.power > the_person.willpower:
        "Speaker" "You feel confident that you will be able to sway their opinion..."

    elif mc.power < the_person.willpower:
        "Speaker" "[the_person.name] seems to have a sturdy mentality at the moment, proceed with caution"

    else: # Happens if their willpower is equal to your power.
        "Speaker" "This can go either way, don't mess up."

    if len(mc.location.people) > 1:

        "Speaker" "There are [people_nearby] other people around you that might interfer with the process."
        "Speaker" "Try bringing [the_person.name] to a more secluded area?"

        menu:
            "Yes":
                $ people_nearby = 0
                $ calc_willpower() # Run the calculation after making considerable changes.
                "Speaker" "You bring [the_person.name] away from the others"
                if mc.power > the_person.willpower:

                    "Speaker" "Having isolated the target it is now both more focused and pliable."

                else: # Might want to assume that a certain personality or opinion makes them uncomfortable being away from others thus it was a mistake luring them away. Hate and unhappiness might also play into it.
                    "Speaker" "[the_person.name] seems to be uncomfortable with being alone in your presence ."
            "No":
                pass





    # Have the player input an opinion then run checks on how the_person reacts to it.
    # Reset the opinion variable upon exiting the encounter for it to not preemtively bring it into the calculation.
    "Speaker" "Type an opinion e.g 'sculpting garden gnomes' then hit enter to proceed "
    $ opinion = str(renpy.input("Opinion:"))

    "Speaker" "What is [the_person.name]'s thoughts on the opinion?"


    menu:
        "Hate":
            $ degree = -2

        "Dislike":
            $ degree = -1

        "Neutral": #This will not display, can be used to "remove" an opinion without the need for additional code.
            $ degree = 0

        "Like":
            $ degree = 1

        "Love":
            $ degree = 2

    "Speaker" "Does the player know about [the_person.name]'s opinion?"

    menu:
        "Yes":
            $ discovered = True

        "No":
            $ discovered = False






    if mc.power > the_person.willpower:
        "Speaker" "You succeed at making the changes"
        $ the_person.opinions[opinion] = [degree, discovered]

    if the_person.willpower > mc.power :
        "Speaker" "[the_person.name]'s mind rejects your suggestions"
    else:
        "Speaker" "You are at a stalemate, try changing your approach"
    return
