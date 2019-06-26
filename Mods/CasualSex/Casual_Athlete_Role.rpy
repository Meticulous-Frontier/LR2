#************* Casual Sex Role: College Athlete  *******************
#Outline
#-College Athlete
 # Looking for casual sex while she focuses on her school and athletic program
# Tends to hang out at the Gym
#  First event: She invites you to work out with her. You work up a sweat together, then sneak into a changing room for sex
#  Second event: She invites you to compete with her in distance race (10k? something similar). Makes a wager if you win she'll let you "do what you want" with her
#  Event Requirements: Advances with sluttiness and player stamina. Stamina takes the place of physical fitness during this storyline
#  Girl requirements: Age <25, skinny body type.
#  Other notes: She calls it off if she "catches feels" (love > 50). Will start warning player at > 40 love

init -2 python:
    def casual_athlete_get_to_know_requirement(the_person):
        return True

    def casual_athlete_phase_one_requirement(the_person):
        if the_person.event_triggers_dict.get("athlete_progress", 0) < 1:
            return False
        if the_person.love > 50:
            return "She is uneasy about falling for you."
        if time_of_day < 4:
            if mc.max_stamina > 2:
                if the_person.sluttiness < 20:
                    return "Requires 20 Sluttiness"
                return True
            else:
                return "Requires More Max Stamina"
        return False

    def casual_athlete_phase_two_requirement(the_person):
        if the_person.event_triggers_dict.get("athlete_progress", 0) < 2:
            return False
        if the_person.love > 50:
            return "She is uneasy about falling for you."
        if time_of_day < 4:
            if mc.max_stamina > 4:
                if the_person.sluttiness < 40:
                    return "Requires 40 Sluttiness"
                return True
            else:
                return "Requires More Max Stamina"
        return False


#*************Create Casual Athlete Role***********#
init -1 python:
    casual_athlete_get_to_know = Action("Get to know Her", casual_athlete_get_to_know_requirement, "casual_athlete_get_to_know_label",
        menu_tooltip = "Make an observation about her.")
    casual_athlete_phase_one = Action("Workout Together", casual_athlete_phase_one_requirement, "casual_athlete_phase_one_label",
        menu_tooltip = "Work up a sweat.")
    casual_athlete_phase_two = Action("Challenge to Race", casual_athlete_phase_two_requirement, "casual_athlete_phase_two_label",
        menu_tooltip = "No risk, no reward.")
    casual_athlete_role = Role(role_name ="College Athlete", actions =[casual_athlete_get_to_know , casual_athlete_phase_one, casual_athlete_phase_two])


#*************TODO*****************
#Implement some method of adding this role to random towngirls.



###DEBUG TESTING FUNCTIONS###
label casual_athlete_debug(the_person):
    "attempting to add role to [the_person.title]."
    $ the_person.special_role.append(casual_athlete_role)
    "role added to [the_person.title]."
    return


###Athlete ACTION LABELS###
label casual_athlete_get_to_know_label(the_person):
    if "athlete_progress" not in the_person.event_triggers_dict:
        $ the_person.event_triggers_dict["athlete_progress"] = 0
    if the_person.event_triggers_dict.get("athlete_progress", 0) < 1:
        "You look up and down [the_person.title]. You can tell she takes care of herself."
        mc.name "You seem like you like to work out."
        the_person.char "Yeah! You could say that. I'm actually on the state college track and field team!"
        "You aren't surprised, she certainly has the look of an athlete."
        "You talk with her for a while about sports. She has a healthy interest in just about all things physical."
        the_person.char "Well, I need to get going. It was nice talking with you, [the_person.mc_title]!"
        $ the_person.event_triggers_dict["athlete_progress"] = 1
    elif the_person.event_triggers_dict.get("athlete_progress", 0) == 1:
        "TODO: do some text here"






    return

label casual_athlete_phase_one_label(the_person):
    if the_person.event_triggers_dict.get("athlete_progress", 0) == 1:
        "workout together and move on to phase 2"
        $ the_person.event_triggers_dict["athlete_progress"] = 2
    elif the_person.event_triggers_dict.get("athlete_progress", 0) == 2:
        "Workout together again, already did this once."
    return

label casual_athlete_phase_two_label(the_person):
    if the_person.event_triggers_dict.get("athlete_progress", 0) == 2:
        "You race her, win, and have sexy times"
        $ the_person.event_triggers_dict["athlete_progress"] = 3
    elif the_person.event_triggers_dict.get("athlete_progress", 0) > 2:
        "You already beat her once!"

    return
