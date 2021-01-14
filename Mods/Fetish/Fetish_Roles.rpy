init -1 python:

    def SB_fetish_anal_mom_kitchen_requirement(person):
        if person is mom:
            if  mc.location == kitchen:
                if mc.energy > 30:
                    return True
                else:
                    return "You're too tired for sex"
            return "You aren't in the kitchen"
        return

    def SB_lily_anal_in_room_requirement(person): #She'll only strip if you're in her bedroom and alone.
        if not person is lily:
            return
        if not mc.location is lily_bedroom:
            return "Must be in Lily's bedroom"
        elif lily_bedroom.get_person_count() > 1:
            return "Must be alone with Lily"
        elif mc.energy > 30:
            return True
        else:
            return "You are too tired."






    def SB_fetish_cum_getdosage_requirement(person):
        if mc.energy > 30:
            if time_of_day < 4:
                return True
        else:
            return "You're too tired"


    # Initialize anal fetsh role
    SB_lily_anal_in_room = Action("Use Strap On", SB_lily_anal_in_room_requirement, "SB_lily_anal_in_room_label",
        menu_tooltip = "Double Penetration on the bed.")


    # Initialize Cum Fetish role
    SB_fetish_cum_getdosage = Action("Give her cum dosage", SB_fetish_cum_getdosage_requirement, "SB_fetish_cum_getdosage_label",
        menu_tooltip = "Give her cum, right here, right now.")
    cum_internal_role = Role(role_name = "Internal Cum Fetish", actions = [SB_fetish_cum_getdosage])
    cum_external_role = Role(role_name = "External Cum Fetish", actions = [SB_fetish_cum_getdosage])
    cum_fetish_role = Role(role_name = "Cum Fetish", actions = [SB_fetish_cum_getdosage])


    # Initialize Oral Fetish role
    oral_fetish_role = Role(role_name = "Oral Fetish", actions = [])
    #TODO: Add some actions when 'afflicted'



    exhibition_fetish_role = Role(role_name = "Exhibitionist", actions = [])

init 1 python:
    def SB_get_fetish_count(person):
        fetish_count = 0
        for role in person.special_role:
            if role in [anal_fetish_role, cum_fetish_role, breeding_fetish_role]:
                fetish_count += 1
        return fetish_count

    def SB_get_fetishes_description(person):
        description = ""
        for role in person.special_role:
            if role in [anal_fetish_role, cum_fetish_role, breeding_fetish_role]:
                if __builtin__.len(description) > 0:
                    description += ", "
                description += role.role_name
        return description

    def SB_fetish_get_employee_percent():
        total_count = 0
        fetish_count = 0
        if __builtin__.len(mc.business.get_employee_list()) == 0:
            return 0
        for person in mc.business.get_employee_list():
            total_count += 1
            if SB_get_fetish_count(person) > 0:
                fetish_count += 1
        return __builtin__.int((fetish_count / total_count) * 100)





#SBR30
label SB_fetish_cum_getdosage_label(the_person):
    mc.name "[the_person.title] get on your knees. Its time for your dosage of cum."
    "[the_person.possessive_title] smiles wide."
    the_person.char "Oh!? Yes! its my favorite!"
    "[the_person.possessive_title] immediately drops to her knees. She doesn't even seem to care that there could be other people around."
    $ the_person.draw_person(position = "blowjob")
    # call fuck_person(the_person, private = False, start_position = cum_fetish_blowjob, start_object = make_floor(), girl_in_charge = True, position_locked = True) from _call_fuck_person_SBR30
    call get_fucked(the_person, private= False, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = False, allow_continue = False) from _call_get_fucked_SBR030
    return


#SBR50
label SB_lily_anal_in_room_label(the_person):
    "You give [the_person.possessive_title] a quick proposition."
    mc.name "Hey [the_person.title]. What do you say we get out that strap on again?"
    "[the_person.possessive_title] looks at you and smiles."
    the_person.char "Mmm that sounds pretty good [the_person.mc_title]... Here, let me take a couple... precautions."
    "[the_person.possessive_title] walks over and closes her door and locks it. She turns on some music and turns the volume up."
    the_person.char "Don't want mom to find out..."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] goes over to her dresser. She's going through a drawer looking for the toy."
    if the_person.outfit.vagina_available():
        mc.name "Mmmm, [the_person.title], your ass looks amazing. I can't wait to see that hole stretched around my cock..."
    else:
        "You step up behind [the_person.possessive_title] and start to grope her ass. She sighs as you massage it."
        "You decide to start getting her ready while she looks for the the toy. You start peeling her clothes off."
        $ the_person.strip_outfit(position = "standing_doggy", exclude_upper = True)
        mc.name "Mmmm, [the_person.title], your ass looks amazing. I can't wait to see that hole stretched around my cock..."
    the_person.char "Ah! Here it is. I know I can't wait, you know I love when you fuck me in the ass [the_person.mc_title]."
    "[the_person.possessive_title] hands you a bottle of lube and the dildo, then heads over to her bed and gets on her hands and knees with her ass in the air."
    $ the_person.draw_person(position = "doggy")
    "You put the dildo on and lube yourself up. You get behind [the_person.possessive_title] on the bed and start to line yourself up."
    "You cock sinks easily into her greedy back passage. She is so accustomed to being fucked anally now she accommodates you easily."
    the_person.char "Oh thank god... I was starting to consider jumping you in the middle of the night. You know I need your cock in my ass [the_person.mc_title]..."
    the_person.char "Now fuck me good! I'm ready for it!"
    call fuck_person(the_person, start_position = SB_doggy_anal_dildo_dp, start_object = make_bed(), skip_intro = True) from _call_sex_description_SBR50
    the_person.char "Yes... Thanks [the_person.mc_title]... Don't be a stranger now!"
    "[the_person.possessive_title] wiggles her ass back and forth a bit, still lying face down on her bed. You politely excuse yourself."
    $ the_person.event_triggers_dict["LastAnalFetish"] = day
    $ the_person.apply_planned_outfit()
    return
