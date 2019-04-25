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
# NOTE: Do checks against the_person.willpower and confirm changes in the_person.willpower with calc_will()

init -1 python:

    # Thematic lists NOTE: These lists should be appendable from within the game
    exhib_list = ["naked", "nude", "topless", "underwear"] # Showing off, not nescessary connected to sluttiness
    voyer_list = ["spying"] # Observing lewd acts
    sub_list = ["submissive"] # Submissive behavior
    preg_list = ["pregnant"] # Pregnancy or pregnancy play
    dom_list = ["dominant"] # Domimant behavior
    sadist_list = [] # Sadistic behavior


    def change_willpower(amount, add_to_log = True):
        the_person.willpower += amount
        if the_person.willpower < 0:
            the_person.willpower = 0

        log_string = ""
        log_string_total = ""
        if amount > 0:
            log_string = "+" + str(amount) + " Willpower"
            log_string_total = str(the_person.willpower) + " Total Willpower"
        else:
            log_string = str(amount) + " Willpower"
            log_string_total = str(the_person.willpower) + " Total Willpower"

        if add_to_log and amount != 0:
            mc.log_event(the_person.name + ": " + log_string, "float_text_blue")
            mc.log_event(the_person.name + ": " + log_string_total, "float_text_blue")
        return the_person.willpower

    def add_opinion(opinion, degree, discovered, add_to_log = True):
        opinion = opinion
        degree = degree
        discovered = discovered
        the_person.opinions[opinion] = [degree, discovered]

        log_string = str(opinion) + " changed"
        if add_to_log:
            mc.log_event("Opinion: " + log_string, "float_text_green")

    def calc_power():
        mc.power = 0

        mc.power += int(mc.charisma*5) # Positive character modifiers
        mc.power += int(mc.current_stamina*1.5)
        return mc.power

    def calc_will(add_to_log = True): # Base calculation. Run this once.

        the_person.willpower = int(the_person.focus * 10 + the_person.happiness * 0.2 - the_person.obedience * 0.1 - the_person.love * 0.2 - the_person.suggestibility * 0.5)

        if the_person.willpower < 0:
            the_person.willpower = 0

        log_string = str(the_person.willpower) + " Willpower"

        if add_to_log:
            mc.log_event(the_person.name + ": " + log_string, "float_text_blue")
        return the_person.willpower

init -1 python:
    pass


label influence_opinion_start_label(the_person): # This is the setup phase that you have to get through.
                                                 # We want to set up the setting and allow for choices to tackle them for better or worse results.
                                                 # Do mood checks, relation to player character, opinion checks, personality checks.
                                                 # calc_will() sets the baseline for the character after that use change_willpower(amount) to add and remove.
                                                 # NOTE: Need to add ways to fail before the final segment.
    $ opinion = None
    $ degree = None
    $ discovered = None
    $ people_nearby = len(mc.location.people)
    $ the_person.willpower = 0
    $ the_person.willpower = calc_will()

    # Pre-check to let the player know base information about the scenario.
    if calc_power() > the_person.willpower:
        "Speaker" "You feel confident that you will be able to sway their opinion..."

    elif calc_power() < the_person.willpower:
        "Speaker" "[the_person.name] seems to have a sturdy mentality at the moment, proceed with caution"

    else: # Happens if their willpower is equal to your power.
        "Speaker" "This can go either way, don't mess up."

    if len(mc.location.people) > 1: # Check if there are other people nearby and fortify their willpower based on how many.
        $ change_willpower(len(mc.location.people)*5)
        "Speaker" "There are [people_nearby] other people around you that might interfer with the process."
        "Speaker" "Try bringing [the_person.name] to a more secluded area?"

        menu:
            "Yes":
                $ change_willpower(-len(mc.location.people)*5) # Run the calculation after making considerable changes.
                "Speaker" "You bring [the_person.name] away from the others"
                if calc_power() > the_person.willpower:

                    "Speaker" "Having isolated the target it is now both more focused and pliable."

                else: # Might want to assume that a certain personality or opinion makes them uncomfortable being away from others thus it was a mistake luring them away. Hate and unhappiness might also play into it.
                    if the_person.love < 0:
                        $ the_person.draw_person(emotion = "sad")
                        "Speaker" "[the_person.name] seems to be uncomfortable with being alone in your presence ."

            "No":
                pass

            "Back":
                return

    call influence_opinion_middle_label()

label influence_opinion_middle_label():
    # Have the player input an opinion then run checks on how the_person reacts to it.
    "Speaker" "Type an opinion e.g 'sculpting garden gnomes' then hit enter to proceed "
    $ opinion = str(renpy.input("Opinion:"))

    if any(srchstr in opinion for srchstr in exhib_list): # This checks any keyword.
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions): # This is limited to exact matches.
            $ change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in exhib_list"

    if any(srchstr in opinion for srchstr in voyer_list):
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions):
            $ change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in voyer_list"

    if any(srchstr in opinion for srchstr in sub_list):
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions):
            $ change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in sub_list"

    if any(srchstr in opinion for srchstr in preg_list):
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions):
            $ change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in preg_list"

    if any(srchstr in opinion for srchstr in dom_list):
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions):
            $ change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in dom_list"

    if any(srchstr in opinion for srchstr in sadist_list):
        if any(srchstr in opinion for srchstr in the_person.sexy_opinions):
            $ change_willpower(-5)
            "Speaker" "[the_person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in sadist_list"

    "Speaker" "How do you want [the_person.name] to feel about [opinion]?"
    menu:
        "Hate":
            $ degree = -2
            if opinion in the_person.sexy_opinions: # Avoids errors.

                if the_person.sexy_opinions[opinion][0] == -1:
                    $ change_willpower(+5)
                    "Speaker" "[the_person.name] dislikes [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == 1:
                    $ change_willpower(+10)
                    "Speaker" "[the_person.name] likes [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == 2:
                    $ change_willpower(+15)
                    "Speaker" "[the_person.name] loves [opinion], so it is going to be difficult to change her mind."

        "Dislike":
            $ degree = -1
            if opinion in the_person.sexy_opinions: # Avoids errors.

                if the_person.sexy_opinions[opinion][0] == -2:
                    $ change_willpower(+5)
                    "Speaker" "[the_person.name] hates [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == 1:
                    $ change_willpower(+5)
                    "Speaker" "[the_person.name] likes [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == 2:
                    $ change_willpower(+10)
                    "Speaker" "[the_person.name] loves [opinion], so it is going to be difficult to change her mind."

        "Neutral": #This will not display, can be used to "remove" an opinion without the need for additional code.
            $ degree = 0
            if opinion in the_person.sexy_opinions: # Avoids errors.
                if the_person.sexy_opinions[opinion][0] == -2:
                    $ change_willpower(+10)
                    "Speaker" "[the_person.name] hates [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == -1:
                    $ change_willpower(+5)
                    "Speaker" "[the_person.name] dislikes [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == 1:
                    $ change_willpower(+5)
                    "Speaker" "[the_person.name] likes [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == 2:
                    $ change_willpower(+10)
                    "Speaker" "[the_person.name] loves [opinion], so it is going to be difficult to change her mind."
        "Like":
            $ degree = 1
            if opinion in the_person.sexy_opinions: # Avoids errors.
                if the_person.sexy_opinions[opinion][0] == -2:
                    $ change_willpower(+10)
                    "Speaker" "[the_person.name] hates [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == -1:
                    $ change_willpower(+5)
                    "Speaker" "[the_person.name] dislikes [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == 2:
                    $ change_willpower(+10)
                    "Speaker" "[the_person.name] loves [opinion], so it is going to be difficult to change her mind."



        "Love":
            $ degree = 2
            if opinion in the_person.sexy_opinions: # Avoids errors.

                if the_person.sexy_opinions[opinion][0] == -2:
                    $ change_willpower(+15)
                    "Speaker" "[the_person.name] hates [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == -1:
                    $ change_willpower(+10)
                    "Speaker" "[the_person.name] dislikes [opinion], so it is going to be difficult to change her mind."

                if the_person.sexy_opinions[opinion][0] == 1:
                    $ change_willpower(+5)
                    "Speaker" "[the_person.name] likes [opinion], so it is going to be difficult to change her mind."



#    "Speaker" "Does the player know about [the_person.name]'s opinion?" NOTE: Might as well assume yes, because the player is determining it.
#
#    menu:
#        "Yes":
#            $ discovered = True
#
#        "No":
#            $ discovered = False
    $ discovered = True
    call influence_opinion_end_label




label influence_opinion_end_label():

    if calc_power() > the_person.willpower:
        "Speaker" "You succeed at making the changes"
        $ add_opinion(opinion, degree, discovered)
    elif calc_will() > calc_power() :
        "Speaker" "[the_person.name]'s mind rejects your suggestions"
    else:
        "Speaker" "You are at a stalemate, try changing your approach"
    jump game_loop
