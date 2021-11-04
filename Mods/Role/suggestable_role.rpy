# if suggestibility is enabled now depends on the lysergide_n2o_serum
# the serum adds the role action to a person and removes it when
# the serum wears off

init 2 python: # Define actions and requirements for the actual mod here.

    def influence_opinion_requirement(person): # Shows only if person has been affected by suggestibility serum.
        return person.has_role(suggestable_role)

    influence_opinion_action = Action("Influence an opinion", influence_opinion_requirement, "influence_opinion_label",
        menu_tooltip = "Influence a person's opinion regarding a specific topic")

    suggestable_role = Role("Suggestible", [influence_opinion_action])

# Actions for the receptive role in suggestable_role.rpy

label influence_opinion_label(person): #Input a custom opinion, check if they have the opinion or not and base difficulty on how big the change is, or random up to 80 if it's a unrelated opinion

    $ opinion = None
    $ degree = None
    $ discovered = True
    # Pre-check to let the player know base information about the scenario.
    "Type an opinion, e.g 'sculpting garden gnomes', then hit Enter to proceed."
    $ opinion = str(renpy.input("Opinion:")).lower()
    python: # capitalize if needed
        if opinion == "hr work":
            opinion = "HR work"
        if opinion == "mondays":
            opinion = "Mondays"
        if opinion == "fridays":
            opinion = "Fridays"

    "How do you want [person.name] to feel about [opinion]?"
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

    python:
        score = person.get_opinion_score(opinion)
        degrees = [-2,-1,0,1,2]
        ran_num = __builtin__.abs(degrees.index(score) - degrees.index(degree)) # How far is the degree away from current opinion (max 4 steps)
        cur_score = opinion_score_to_string(score)

    if score is not 0:
        "[person.possessive_title] [cur_score] [opinion]; depending on how drastic the change and how suggestible the person is, you might succeed."
    else:
        "[person.possessive_title] currently has no opinion regarding [opinion]; depending on how suggestible the person is, you might succeed."

    if ran_num == 1: # small change
        $ difficulty = renpy.random.randint(0, 20) # Using ranges so people can get lucky, and it can give different outcomes faking simulation of psychology
    elif ran_num == 2: # medium change
        $ difficulty = renpy.random.randint(20, 40)
    elif ran_num == 3: # large change
        $ difficulty = renpy.random.randint(40, 60)
    elif ran_num == 4: # very large change
        $ difficulty = renpy.random.randint(60, 80)
    else:
        $ difficulty = renpy.random.randint(0, 80) #Anything above 80 should be an auto- success

    if person.suggestibility >= difficulty:
        $ person.add_opinion(opinion, degree, discovered)
        $ new_score = opinion_score_to_string(person.get_opinion_score(opinion))
        "You succeed at influencing [person.possessive_title!l]'s opinion; she now [new_score] [opinion]."


    else:
        "[person.possessive_title] doesn't seem to agree with your suggestion regarding [opinion]."
        "Making her more suggestible might help you out."

    $ person.remove_role(suggestable_role)
    $ mc.log_event((person.title or person.name) + " is no longer suggestible.", "float_text_blue")

    $ clear_scene()
    return
