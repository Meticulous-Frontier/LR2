# Challenge concept:
                  # Baseline should be a 50% success rate as other factors will ALWAYS play in one way or another.
                  # Suggestibility increases success chance by 10% per 10 points. 20 sluttiness = 20% increase
                  # Players charisma increases success chance by 5% per point. 2 Charisma = 10% increase
                   # Targets focus decreases success chance by 10% per point. 2 Focus = 20% decrease
                   # Targets obedience increases success chance by 0.1% per point. 100 obedience = 10% increase.
                   # Being in public adds another 20% decrease in success rate.
# TODO: Make a screen and a room action to develop techniques
      # Make person person.willpower be affected by choices made through dialogue and not only during final calculation.
      # Create additional actions and labels
      # Create a serum that gives a "Receptive" role. Instead of handing it out to everyone.
# NOTE: Do checks against person.willpower and confirm changes in person.willpower with calc_will()

init -1 python:

    # Thematic lists NOTE: These lists should be appendable from within the game
    exhib_list = ["naked", "nude", "topless", "underwear"] # Showing off, not nescessary connected to sluttiness
    voyer_list = ["spying"] # Observing lewd acts
    sub_list = ["submissive"] # Submissive behavior
    preg_list = ["pregnant"] # Pregnancy or pregnancy play
    dom_list = ["dominant"] # Domimant behavior
    sadist_list = [] # Sadistic behavior
#    lewd_list = [] # Keywords that are considered sexual, to determine if something is to be thrown into sexy_opinions_list or opinions_list


label influence_opinion_input_label(person):
    # Have the player input an opinion then run checks on how person reacts to it.
    "Speaker" "Type an opinion e.g 'sculpting garden gnomes' then hit enter to proceed "
    $ opinion = str(renpy.input("Opinion:"))

    if any(srchstr in opinion for srchstr in exhib_list): # This checks any keyword.
        if any(srchstr in opinion for srchstr in person.sexy_opinions): # This is limited to exact matches.
            $ person.change_willpower(-5)
            "Speaker" "[person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in exhib_list"

    if any(srchstr in opinion for srchstr in voyer_list):
        if any(srchstr in opinion for srchstr in person.sexy_opinions):
            $ person.change_willpower(-5)
            "Speaker" "[person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in voyer_list"

    if any(srchstr in opinion for srchstr in sub_list):
        if any(srchstr in opinion for srchstr in person.sexy_opinions):
            $ person.change_willpower(-5)
            "Speaker" "[person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in sub_list"

    if any(srchstr in opinion for srchstr in preg_list):
        if any(srchstr in opinion for srchstr in person.sexy_opinions):
            $ person.change_willpower(-5)
            "Speaker" "[person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in preg_list"

    if any(srchstr in opinion for srchstr in dom_list):
        if any(srchstr in opinion for srchstr in person.sexy_opinions):
            $ person.change_willpower(-5)
            "Speaker" "[person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in dom_list"

    if any(srchstr in opinion for srchstr in sadist_list):
        if any(srchstr in opinion for srchstr in person.sexy_opinions):
            $ person.change_willpower(-5)
            "Speaker" "[person.name] already has similar opinions making it easier to convince her."
        "Speaker" "This is in sadist_list"

    $ log_willpower(mc)

    "Speaker" "How do you want [person.name] to feel about [opinion]?"
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
        "Back":
            return

    if not person.get_opinion_topic(opinion) is None:
        python:
            score = person.get_opinion_score(opinion)
            degrees = [-2,-1,0,1,2]
            change = abs(degrees.index(score) - degrees.index(degree)) # How far is the degree away from current opinion (max 4 steps)
            cur_score = opinion_score_to_string(score)
            person.change_willpower(change * 5)

        if change == 1: # small change
            "Speaker" "[person.name] [cur_score] [opinion], so she will put up not much resistance."
        elif change == 2: # medium change
            "Speaker" "[person.name] [cur_score] [opinion], so she will put up a little resistance."
        elif change == 3: # large change
            "Speaker" "[person.name] [cur_score] [opinion], so she will put up some resistance."
        elif change == 4: # very large change
            "Speaker" "[person.name] [cur_score] [opinion], so she will put up a lot of resistance."

    $ log_willpower(person)

#    "Speaker" "Does the player know about [person.name]'s opinion?" NOTE: Might as well assume yes, because the player is determining it.
#
#    menu:
#        "Yes":
#            $ discovered = True
#
#        "No":
#            $ discovered = False
#    $ add_opinion(opinion, degree, discovered)
    $ discovered = True
    return
