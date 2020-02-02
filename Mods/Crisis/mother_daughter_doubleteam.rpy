## Mother Daughter Double Team
init -1 python:
    mother_daughter_doubleteam_weight = 5

init 2 python:
    def mother_daughter_doubleteam_requirement():
        if mc.business.is_weekend():
            return False
        if mc.is_at_work():
            if time_of_day > 0 and time_of_day < 4: # only during morning afternoon or evening
                for person in town_relationships.get_business_relationships(["Daughter"]):
                    if willing_to_threesome( person.person_a, person.person_b):
                        return True
        return False

    mother_daughter_doubleteam_action = ActionMod("Mother Daughter Blowjob", mother_daughter_doubleteam_requirement, "mother_daughter_doubleteam_action_label",
        menu_tooltip = "A mother and daughter compete to give a better blowjob.", category = "Business", is_crisis = True, crisis_weight = mother_daughter_doubleteam_weight)

label mother_daughter_doubleteam_action_label():
    python:
        mother_list = []
        daughter_list = []
        if town_relationships.get_business_relationships(["Daughter"]):   #Is a mom
            for person in town_relationships.get_business_relationships(["Daughter"]):
                if willing_to_threesome( person.person_a, person.person_b):
                    mother_list.append(person.person_a) #Now have a list of mothers

        scene_manager = Scene() # make sure we have a clean scene manager
        the_person_one = get_random_from_list(mother_list)
        daughter_req = town_relationships.get_existing_children(the_person_one)

        for daughter_person in daughter_req:
            #renpy.say("", "[daughter_person.title]")
            if willing_to_threesome(the_person_one, daughter_person):
                daughter_list.append(daughter_person) #Now a list of her existing daughters
        the_person_two = get_random_from_list(daughter_list)

    "As you are walking around the office, you hear some arguing coming from the break room."
    "When you look inside, you see [the_person_one.possessive_title] having a discussion with her daughter."
    $ scene_manager.add_actor(the_person_one)
    $ scene_manager.add_actor(the_person_two,  character_placement = character_center_flipped)
    the_person_two.char "I know, I know, dad always said you were good in bed. I'm not disputing that! I'm just saying I'm pretty good at giving blowjobs and I might even be better than you..."
    the_person_one.char "Honey, blowjobs are an art that takes YEARS to master. I understand that you have enthusiasm, but that doesn't make up for practiced technique."
    the_person_two.char "What makes you think I don't have practice? Oh! Hey [the_person_two.mc_title]"
    "They both look at you as you walk into the breakroom."
    the_person_one.char "Hey [the_person_one.mc_title], maybe you could help us settle something. In your experience, who gives better blowjobs, enthusiastic, younger girls or experienced older women?"
    "Oh boy, you walked into hornet's nest."
    mc.name "Well, to be honest I've had both that were amazing, it really just depends on the situation."
    the_person_two.char "See mom? It's totally plausible I'm just as good, if not better than you."
    the_person_one.char "I suppose, but, I really feel like you are underestimating your mother here dear."
    mc.name "Why don't you two just find some hapless guy at the bar tonight. You can both blow him and then find out who he thinks is better?"
    the_person_two.char "That's a good idea! Except... I mean some random guy? He may not be experienced or have a clue."
    the_person_one.char "That IS a good idea [the_person_two.mc_title], except we need someone with a bit more experience... like say... you!"
    the_person_two.char "Hey! There we go! [the_person_two.mc_title], you should let us blow you and decide who is better!"
    "Hmmm, you wonder. Maybe you could talk them into doing it at the same time? It would be easier to judge technique if they were both on their knees in front of you..."
    menu:
        "Let's settle this right now":
            mc.name "I have one condition though. Why don't you both go at the same time, that way I can go back and forth and make up my mind easier."
            the_person_two.char "Yes! Let's do it mom! Loser has to cook dinner tonight!"
            the_person_one.char "Okay, let's do it!"
            "As the mother and daughter walk over to you and get on their knees, you feel a burst of energy. A competitive blowjob. This should be fun!"
            python:
                mc.change_energy(50)
                the_person_one.change_energy(50)
                the_person_two.change_energy(50)
            call start_threesome(the_person_one, the_person_two, start_position = threesome_double_blowjob, private = True, position_locked = True, affair_ask_after = False) from mother_daughter_teamup_call1
            $ sex_log = _return
            if sex_log.get("guy orgasms", 0) > 0:
                "You sigh happily after you finish receiving your double blowjob from the girls. For a moment, you forgot that it was a competition."
            else:
                "You decide who you think is the better oral giver, so you pull back to deliver the news."
            the_person_two.char "So? How'd I do? Who do you think is better at giving blowjobs?"
            menu:
                "[the_person_one.title]":
                    "[the_person_two.title] is disappointed, but she quickly smiles."
                    the_person_two.char "I see. Well, I guess I'm making dinner tonight mom. But we should revisit this in the future, I bet with a bit more practice, this might go differently."
                "[the_person_two.title]":
                    "[the_person_one.title] is stunned by your verdict."
                    the_person_one.char "That... I can't believe it. Have I let myself get comfortable after all these years? Maybe I should practice more."
                    the_person_one.char "Alright, I'll make dinner tonight, but this isn't over girl! We'll revisit this another time!"
            $ scene_manager.update_actor(the_person_one, position = "walking_away")
            $ scene_manager.update_actor(the_person_two, position = "walking_away")
            "The two girls walk out of the breakroom, the competition settled.... for now..."
        "Too busy":
            mc.name "I'm sorry, I have a lot on my to do list right now. Perhaps another time."
            the_person_two.char "Oof. Okay, maybe we're both bad if [the_person_two.mc_title] won't even accept a free blowjob from us mom?"
            the_person_one.char "That's... no, I'm sure he's just busy honey."
            $ scene_manager.update_actor(the_person_one, position = "walking_away")
            $ scene_manager.update_actor(the_person_two, position = "walking_away")
            "The two girls walk out of the breakroom, still discussing their issue."

    $ scene_manager.clear_scene()
    python:
        mc.location.show_background()
        # Release variables
        del the_person_one
        del the_person_two
        del mother_list
        del daughter_list
    return
