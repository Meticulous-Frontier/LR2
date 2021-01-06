init -1 python:
    def SB_fetish_vaginal_visit_requirement(person):
        if person.sex_skills["Vaginal"] >= 6:
            if not SB_FETISH_EVENT_ACTIVE():
                return True
            else:
                return "Someone else is coming over tonight"
        return

    def SB_fetish_vaginal_mom_kitchen_requirement(person):
        if person is mom:
            if mc.location == kitchen:
                if mc.energy > 30:
                    return True
                else:
                    return "You're too tired for sex"
            return "You aren't in the kitchen"
        return

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

    def SB_fetish_anal_staylate_requirement(person):
        if mc.is_at_work():
            if person.sex_skills["Anal"] >= 6:
                if not SB_FETISH_EVENT_ACTIVE():
                    return True
                else:
                    return "Someone else is coming over tonight"
        return False

    def SB_fetish_starbuck_anal_swing_demo_requirement(person):
        if person is starbuck:
            if mc.location == sex_store:
                return True
            else:
                return "Must be at the Sex Shop"
        else:
            return False


    def SB_fetish_cum_getdosage_requirement(person):
        if mc.energy > 30:
            if time_of_day < 4:
                return True
        else:
            return "You're too tired"

    def SB_breeding_fetish_on_day(person):
        if person.knows_pregnant() or person.is_lactating():
            person.change_happiness(2, add_to_log = False)
        elif person.is_highly_fertile(): #Always aroused when fertile.
            if person.arousal < 50:
                person.arousal = 50

    # Initialize vaginal fetish role
    SB_fetish_vaginal_visit = Action("Sleepover Tonight (Vaginal)", SB_fetish_vaginal_visit_requirement, "SB_fetish_vaginal_visit_label",
        menu_tooltip = "Ask her over for some fun tonight.")
    SB_fetish_vaginal_mom_kitchen = Action("Kitchen Sex (Vaginal)", SB_fetish_vaginal_mom_kitchen_requirement, "SB_fetish_vaginal_mom_kitchen_label",
        menu_tooltip = "Bend her over the kitchen counter.")
    vaginal_fetish_role = Role(role_name ="Vaginal Fetish", actions =[SB_fetish_vaginal_visit, SB_fetish_vaginal_mom_kitchen])

    # Initialize anal fetsh role
    SB_fetish_anal_staylate = Action("See me after work", SB_fetish_anal_staylate_requirement, "SB_fetish_anal_staylate_label",
        menu_tooltip = "Ask her to stay after work is over.")
    SB_fetish_anal_mom_kitchen = Action("Kitchen Sex (Anal)", SB_fetish_anal_mom_kitchen_requirement, "SB_fetish_anal_mom_kitchen_label",
        menu_tooltip = "Bend her over the kitchen counter.")
    SB_lily_anal_in_room = Action("Use Strap On", SB_lily_anal_in_room_requirement, "SB_lily_anal_in_room_label",
        menu_tooltip = "Double Penetration on the bed.")
    SB_fetish_starbuck_anal_swing_demo = Action("Have Sex Swing Demo", SB_fetish_starbuck_anal_swing_demo_requirement, "SB_starbuck_anal_swing_demo",
        menu_tooltip = "Anal Sex in the Swing")
    anal_fetish_role = Role(role_name ="Anal Fetish", actions =[SB_fetish_anal_staylate, SB_fetish_anal_mom_kitchen, SB_lily_anal_in_room, SB_fetish_starbuck_anal_swing_demo])

    # Initialize Cum Fetish role
    SB_fetish_cum_getdosage = Action("Give her cum dosage", SB_fetish_cum_getdosage_requirement, "SB_fetish_cum_getdosage_label",
        menu_tooltip = "Give her cum, right here, right now.")
    cum_internal_role = Role(role_name = "Internal Cum Fetish", actions = [SB_fetish_cum_getdosage])
    cum_external_role = Role(role_name = "External Cum Fetish", actions = [SB_fetish_cum_getdosage])

    # Initialize Oral Fetish role
    oral_fetish_role = Role(role_name = "Oral Fetish", actions = [])
    #TODO: Add some actions when 'afflicted'

    breeding_fetish_role = Role(role_name = "Breeding Fetish", actions = [breeding_fetish_bend_her_over], on_day = SB_breeding_fetish_on_day)

init 1 python:
    def SB_get_fetish_count(person):
        fetish_count = 0
        for role in person.special_role:
            if role in [vaginal_fetish_role, anal_fetish_role, cum_internal_role, cum_external_role, oral_fetish_role, breeding_fetish_role]:
                fetish_count += 1
        return fetish_count

    def SB_get_fetishes_description(person):
        description = ""
        for role in person.special_role:
            if role in [vaginal_fetish_role, anal_fetish_role, cum_internal_role, cum_external_role, oral_fetish_role, breeding_fetish_role]:
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


#Vaginal Fetish Events#
label SB_fetish_vaginal_visit_label(the_person):
    if the_person is mom:
        mc.name "Hey [the_person.title], it's been kind of a rough day, would you be willing to spend the night in my room tonight?"
        "[the_person.possessive_title] smiles at you before replying."
        the_person.char "Oh [the_person.mc_title], I love it that we are so close that you feel comfortable asking me that. That souds fine."
        "You coordinate with [the_person.possessive_title] on what time you'll be home tonight."
        the_person.char "I'll see you tonight then!"
    elif the_person is lily:
        mc.name "Hey [the_person.title]. What are you up to tonight?"
        "[the_person.possessive_title] frowns at you before replying."
        the_person.char "Well, I was supposed to have a date tonight and I was hoping to get lucky, but he just called and cancelled on me!"
        mc.name "Well, if you want to, we could always hang out in my room tonight."
        "[the_person.possessive_title] smiles at you and nods."
        the_person.char "Actually, that sounds fun!"
        "You coordinate with [the_person.possessive_title] on what time you'll be home tonight."
        the_person.char "I'll see you tonight then!"
    else:
        mc.name "Hey, [the_person.title], have any plans for tonight?"
        "[the_person.possessive_title] smiles at you before replying."
        the_person.char "Nothing that can't be rearranged. Have anything in mind?"
        mc.name "Why don't you come over to my place later? I'm sure we could find something to keep ourselves busy..."
        the_person.char "Sounds great, [the_person.mc_title]!"

        mc.name "Don't forget to bring a toothbrush, [the_person.title]..."
        "[the_person.possessive_title] smiles, clearly enjoying your obvious innuendo."
        the_person.char "I'll see you tonight then!"

    $ add_sb_fetish_vaginal_event(the_person)
    return

#SBR10
label SB_fetish_vaginal_mom_kitchen_label(the_person):
    $ the_person = mom
    $ the_clothing = the_person.outfit.get_lower_top_layer() #Get the very top item of clothing.

    mc.name "Hey [the_person.title], dinner sure smells good. Just keep working on it, don't mind me!"
    "[the_person.possessive_title] hesitates for a second, clearly realizing you are up to something."
    "You pretend to look in the fridge for something as [the_person.possessive_title] resumes dinner preparations. She bends over the counter and starts to chop up some vegetables."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person.outfit.vagina_available():
        "You steal a few glances over at [the_person.possessive_title]'s exposed ass. It looks soft and supple, and shakes a bit as she prepares dinner."
    else:
        "You steal a glance over at [the_person.possessive_title]'s ass as she is bent over. It looks great in her [the_clothing.name]."
    "Getting a naughty idea, you quietly move behind [the_person.possessive_title]."
    if the_person.outfit.vagina_available():
        "You slowly reach down and start to slowly caress her cunt."
    else:
        "You slowly reach down and start to slowly rub her pussy through her [the_clothing.name]."
    the_person.char "Hey! What are you doing? Stop that!"
    "You continue rubbing her."
    mc.name "Stop? But doesn't that feel good, [the_person.title]?"
    the_person.char "Of course it does... But your sister, she could walk in anytime..."
    if the_person.outfit.vagina_available():
        "Shhh, just be quiet. Your ass looks so amazing [the_person.title]... I should just fuck you right here..."
    else:
        "Shhh, just be quiet. Your ass looks so good in your [the_clothing.name]... I should just pull it down and fuck you right here..."
    $ the_person.change_arousal(10)
    "[the_person.possessive_title] stifles a moan, she pushes her hips back against you as you continue to stroke her."
    the_person.char "Mmmmmm... Okay... Do it! Just go quick! I don't want your sister to catch us."
    if the_person.outfit.vagina_available():           #If its available no need to strip.
        "You quickly pull your cock out and line it up with her wet slit."
    else:                                              #Otherwise, strip her down.
        "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy"

        $ the_person.strip_outfit(position = "standing_doggy", exclude_upper = True)

        "With her pussy finally exposed you waste no time. You quickly pull your cock out and line it up with her wet slit."

    call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_table(), skip_intro = True) from _call_sex_description_SBR10

    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title] is positively glowing. She knows that even while preparing dinner, you may come and fuck her at any time."
    else:
        "[the_person.possessive_title] remains silent. She knows that even while preparing dinner, you may come use her for your pleasure at any time."

    $ the_person.event_triggers_dict["LastAnalFetish"] = day
    $ the_person.apply_planned_outfit()
    "As [the_person.possessive_title] continues dinner preparation, you take a quick look around. It doesn't look like Lily noticed anything happened between you and [the_person.possessive_title]."

    $ the_clothing = None
    return

#Anal Fetish Events#
label SB_fetish_anal_staylate_label(the_person):
    mc.name "[the_person.title], I need you to stay after work today."
    the_person.char "Oh, of course sir. I'm not in trouble am I?"
    "You give [the_person.possessive_title] a reassuring smile."
    mc.name "No, of course not, you are a wonderful asset to the company..."
    "You lower your voice and whisper in her ear so others don't overhear."
    mc.name "...but I might have to spank your ass a bit anyway."
    "You look [the_person.possessive_title] in the eyes. Her pupils dilate a bit as she realizes the reasoning behind asking her to stay late."
    the_person.char "Oh! Thank you sir! I'll look forward to it!"
    "You say goodbye to [the_person.possessive_title]."
    $ add_sb_fetish_anal_staylate_event(the_person)
    return

#SBR30
label SB_fetish_cum_getdosage_label(the_person):
    mc.name "[the_person.title] get on your knees. Its time for your dosage of cum."
    "[the_person.possessive_title] smiles wide."
    the_person.char "Oh!? Yes! its my favorite!"
    "[the_person.possessive_title] immediately drops to her knees. She doesn't even seem to care that there could be other people around."
    $ the_person.draw_person(position = "blowjob")
    # call fuck_person(the_person, private = False, start_position = SB_cum_fetish_blowjob, start_object = make_floor(), girl_in_charge = True, position_locked = True) from _call_fuck_person_SBR30
    call get_fucked(the_person, private= False, start_position = SB_cum_fetish_blowjob, start_object = make_floor(), skip_intro = False, allow_continue = False) from _call_get_fucked_SBR030
    return

#SBR40
label SB_fetish_anal_mom_kitchen_label(the_person):
    $ the_clothing = the_person.outfit.get_lower_top_layer() #Get the very top item of clothing.

    mc.name "Hey [the_person.title], dinner sure smells good. Just keep working on it, don't mind me!"
    "[the_person.possessive_title] hesitates for a second, clearly realizing you are up to something."
    "You pretend to look in the fridge for something as [the_person.possessive_title] resumes dinner preparations. She bends over the counter and starts to chop up some vegetables."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person.outfit.vagina_available():
        "You steal a few glances over at [the_person.possessive_title]'s exposed ass. It looks soft and supple, and shakes a bit as she prepares dinner."
    else:
        "You steal a glance over at [the_person.possessive_title]'s ass as she is bent over. It looks great in her [the_clothing.name]."
    "Getting a naughty idea, you quietly move behind [the_person.possessive_title]."
    "You reach down and grope her ass aggressively."
    the_person.char "Hey! What are you doing? Stop that!"
    "You continue groping her. You give her ass a solid swat."
    mc.name "Stop? But doesn't that feel good, [the_person.title]?"
    the_person.char "Of course it does... But your sister, she could walk in anytime..."
    if the_person.outfit.vagina_available():
        mc.name "Shhh, just be quiet. Your ass looks so amazing [the_person.title]... I should just fuck it right here..."
    else:
        mc.name "Shhh, just be quiet. Your ass looks so good in your [the_clothing.name]... I should just pull it down and fuck you in the ass right here..."
    $ the_person.change_arousal(10)
    "[the_person.possessive_title] stifles a moan, she pushes her hips back against you as you continue to stroke her."
    the_person.char "Mmmmmm... Okay... Do it! Just go quick! I don't want your sister to catch us."
    if the_person.outfit.vagina_available():           #If its available no need to strip.
        "You quickly pull your cock out and begin to rub it between her cheeks."
    else:                                              #Otherwise, strip her down.
        "You don't bother to reply, instead you begin stripping away anything between you and her supple ass."

        $ the_person.strip_outfit(position = "standing_doggy", exclude_upper = True)

        "With her ass finally exposed you waste no time. You quickly pull your cock out and rub it between her cheeks."
    "[the_person.possessive_title] pulls some lube out of one of the kitchen drawers."
    mc.name "Wait... you keep lube in the...?"
    the_person.char "Shut up just fuck me before your sister notices!"
    "You rub some lube on your cock and on [the_person.title]'s ass hole. You grab her by the hips and then roughly pull her back until your cock is buried inside her rump."

    call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_table(), skip_intro = True) from _call_sex_description_SBR40

    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title] is positively glowing. She knows that even while preparing dinner, you may come and fuck her at any time."
    else:
        "[the_person.possessive_title] remains silent. She knows that even while preparing dinner, you may come use her for your pleasure at any time."

    $ the_person.event_triggers_dict["LastAnalFetish"] = day
    $ the_person.apply_planned_outfit()
    "As [the_person.possessive_title] continues dinner preparation, you take a quick look around. It doesn't look like Lily noticed anything happened between you and [the_person.possessive_title]."

    $ the_clothing = None
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
