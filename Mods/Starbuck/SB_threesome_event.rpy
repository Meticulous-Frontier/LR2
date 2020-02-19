# Before the family threesome flag is set, the crisis chance is high (it unlocks other parts of the game)
# After first occurrence the chance is lowered, since we don't want it to happen too often.

init 2 python:
    def update_family_threesome_crisis(chance):
        found = find_in_list(lambda x: x[0] == SB_fetish_vaginal_family_threesome, crisis_list)
        if found:
            found[1] = chance
        return

    def SB_fetish_vaginal_family_threesome_requirement():
        if mc_asleep() and day % 7 is not 4: # not on Friday nights (we have the kitchen mom event here)
            if mc.energy > 50:  #Must have the energy to handle a long sexy night
                if SB_check_fetish(mom, vaginal_fetish_role) or mom.sluttiness > 60:
                    if SB_check_fetish(lily, vaginal_fetish_role) or lily.sluttiness > 60:
                        return True
        return False

    SB_fetish_vaginal_family_threesome = Action("Family Threesome",SB_fetish_vaginal_family_threesome_requirement,"SB_fetish_vaginal_family_threesome_label")
    crisis_list.append([SB_fetish_vaginal_family_threesome, 3])

init 5 python:
    # we need the label hijacks to correctly set the crisis chance (since it is not stored in the save game)
    add_label_hijack("normal_start", "init_family_threesome_crisis")
    add_label_hijack("after_load", "update_family_threesome_crisis")

label init_family_threesome_crisis(stack):
    python:
        update_family_threesome_crisis(25) 
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_family_threesome_crisis(stack):
    python:
        # assign correct weight to relative recruitment status
        if mc.business.event_triggers_dict.get("family_threesome", False) == False:
            update_family_threesome_crisis(25)
        if mc.business.event_triggers_dict.get("family_threesome", False) == True:
            update_family_threesome_crisis(3)
        execute_hijack_call(stack)
    return



label SB_fetish_vaginal_family_threesome_label():
    $ the_person_one = lily
    $ the_person_two = mom
    $ scene_manager = Scene()

    $ mc.change_location(bedroom) #Make sure we're in our bedroom.

    #Make sure everyone is up for this because sex is fun and getting tired after one round of sex isn't
    if the_person_one.energy < the_person_one.max_energy:
        $ the_person_one.energy = the_person_one.max_energy
    if the_person_two.energy < the_person_two.max_energy:
        $ the_person_two.energy = the_person_two.max_energy

    "Laying in your bed, you hear a knock on your door. You hear [the_person_one.possessive_title] from the other side of the door."
    the_person_one.char "Hey [the_person_one.mc_title], you still up? I was just wondering if I could come in for a bit?"
    "You invite [the_person_one.possessive_title] in. You immediately start to get aroused when you see what she is wearing."
    $ the_person_one.apply_outfit(the_person_one.wardrobe.get_random_appropriate_underwear(the_person_one.sluttiness, guarantee_output = True))
    $ the_person_two.apply_outfit(the_person_two.wardrobe.get_random_appropriate_underwear(the_person_two.sluttiness, guarantee_output = True))
    $ scene_manager.add_actor(the_person_one)
    the_person_one.char "So... I was wondering... is it okay if I sleep in here with you tonight?"
    menu:
        "Not tonight":
            mc.name "Sorry [the_person_one.title]... I had a long day and I'm pretty wore out... maybe tomorrow?"
            "She is clearly disappointed."
            the_person_one.char "Whatever [the_person_one.mc_title]... see you in the morning I guess?"
            "You head for bed, looking forward to a restful night's sleep."
            $ the_person_one.change_obedience(-2)
            $ the_person_one.change_happiness(-5)
            return
        "Strip first" if (not the_person_one.outfit.vagina_available() or not the_person_one.outfit.tits_available()):
            mc.name "That sounds good [the_person_one.title], I could use a bed warmer. Why don't you get naked first?"
            "[the_person_one.possessive_title] smiles at you."
            the_person_one.char "Aww, does my [the_person_one.mc_title] wanna see his [the_person_one.title] get naked for him? What a pervert!"
            "[the_person_one.possessive_title] winks at you before stripping down."
            $ scene_manager.strip_actor_outfit_to_max_sluttiness(the_person_one, temp_sluttiness_boost = 50)
            mc.name "Damn [the_person_one.title], you are really getting good at that..."
            $ scene_manager.update_actor(the_person_one, position="kneeling1", character_placement = character_center_flipped)
            "She begins to crawl up your bed towards you."
        "Hop in!" if (the_person_one.outfit.vagina_available() and the_person_one.outfit.tits_available()):
            mc.name "I was just thinking my bed felt cold."
            the_person_one.char "Mmmm, I can think of a few ways to keep you warm."
            $ scene_manager.update_actor(the_person_one, position="kneeling1", character_placement = character_center_flipped)
            "[the_person_one.possessive_title] gives you a wink and then begins to crawl up the bed towards you."

    "You are so busy checking out [the_person_one.possessive_title], your brain barely registers a knock on your door. [the_person_one.possessive_title] is just sitting down in your lap when you hear a gasp from your door."
    if mc.business.event_triggers_dict.get("family_threesome", False) == True:
        $ scene_manager.add_actor(the_person_two, emotion = "happy")
        the_person_two.char "Is that [the_person_one.name]? Ah good, I thought I heard you come in here."
        the_person_one.char "Mom! Going to join us again tonight?"
        the_person_two.char "If that's okay with you two... I don't want to be a bother."
        mc.name "[the_person_two.title]. Having you here can only make things even better."
        $ scene_manager.strip_actor_outfit_to_max_sluttiness(the_person_two, temp_sluttiness_boost = 50)
        $ scene_manager.update_actor(the_person_two, position = "sitting")
        "[the_person_two.title] sits on the edge of your bed."
        the_person_one.char "So... how are we doing it tonight?"
        "They both look to you."
        the_person_two.char "[the_person_two.mc_title], you're the man here. What do you want to do?"
        call start_threesome(lily, mom) from _threesome_family_evening_event_1
        $ scene_manager.update_actor(the_person_one, position = "back_peek", character_placement = character_center_flipped)
        $ scene_manager.update_actor(the_person_two, position = "missionary", character_placement = character_right)
        $ sex_report = _return
        if sex_report["girl one orgasms"] > 0 and sex_report["girl two orgasms"] > 0 and sex_report["guy orgasms"] > 0:  #Happy family
            "[the_person_one.possessive_title] falls into your bed on one side of you on her side, while [the_person_two.title] lays on her back next to you."
            the_person_two.char "Oh my god... you two... that was amazing!"
            $ the_person_two.change_happiness(10)
            the_person_one.char "I know... I swear [the_person_one.mc_title] makes me cum my brains out."
            $ the_person_one.change_obedience(10)
            "You all lay together for a while in your sex induced afterglow. You enjoy the two girls warming you from each side."
        else:
            "The girls fall into your bed beside you. You relax for a little bit, enjoying the warmth of their bodies."
        the_person_two.char "Well. I should get up before I fall asleep. Goodnight you two!"
        $ scene_manager.update_actor(the_person_two, position = "walking_away")
        the_person_one.char "Goodnight mom! Actually, I should probably get to bed as well, I just remembered I have to get up early..."
        $ scene_manager.remove_actor(the_person_two)
        $ scene_manager.update_actor(the_person_one, position = "walking_away", character_placement = character_right)
        "You watch as [the_person_one.possessive_title] gets up and excuses herself, her ass swaying back and forth as she walks away."
        "God damn you love this family!"
        $ scene_manager.remove_actor(the_person_one)

    else:
        $ scene_manager.add_actor(the_person_two, emotion = "angry")
        the_person_two.char "Is that... [the_person_one.name]!?! What are you... why are you naked in [the_person_two.mc_title]'s room?" #NOTE: the_person_one doesn't nescessarily know the_person_two's title for the MC, but still somewhat makes sense.
        "[the_person_two.possessive_title] is shocked to discover that you and [the_person_one.possessive_title] are in your room, clearly about to get busy."
        the_person_one.char "Mom! Nothing was... wait... what are you wearing?"
        "[the_person_two.possessive_title] quickly realizes that [the_person_one.possessive_title] is here... doing exactly what she was coming here to do. Her cheeks turn red with embarassment."
        "You think quickly. Maybe you can salvage this situation?"
        mc.name "Hey [the_person_two.title]... you look amazing! Want to come in for a little bit? [the_person_one.title] and I are just getting started."
        "You can see a clear look of conflict in [the_person_two.possessive_title]'s eyes. Up until now, your antics have been isolated to you and her, in her mind anyway. She's slowly processing that you have a similar relationship with [the_person_one.possessive_title] "
        the_person_two.char "I mean... I suppose I could... for a bit..."
        "Still in a bit of a daze, [the_person_two.possessive_title] comes into your room, closing the door behind her. She sits over at your desk and looks over at you and [the_person_one.possessive_title] ."
        $ scene_manager.update_actor(the_person_two, position = "sitting")
        "[the_person_one.possessive_title] looks back at you, still a little unsure of herself. You hold up your hands and beckon her."
        $ scene_manager.update_actor(the_person_one, position = "cowgirl")
        "You draw her into your arms. She melts into you giving you a kiss."
        #$ SB_draw_two_person_scene(person_one = the_person_one, person_two = the_person_two, one_pos_x = 0.7, one_position = "kissing", two_position = "sitting")
        "Your lips lock together in a passionate kiss. [the_person_one.possessive_title]'s body melts into yours in surrender, even as [the_person_two.possessive_title] looks on."
        the_person_two.char "Oh my... [the_person_two.mc_title]... [the_person_one.name]..."
        "You move your hands down [the_person_one.possessive_title]'s waist and around to her butt. You give both cheeks a squeeze."
        "She presses her body against yours and sighs."
        the_person_one.char "Mmm... I can't wait for you to fuck me..."
        $ the_person_one.change_arousal(10)
        if the_person_two.outfit.vagina_available():
            "You glance over at [the_person_two.possessive_title]. She is watching you and [the_person_one.possessive_title] intently and has one hand between her legs, stroking the outer lips of her pussy."
        else:
            "You glance over and see that [the_person_two.possessive_title] has her hand down her clothes, playing with herself as she watches."
        $ the_person_two.change_arousal(10)
        "This is going better than you expected! You get a little braver."
        mc.name "Hey [the_person_two.title]... why don't you join us? There's no reason we can't all have a little family fun together..."
        "[the_person_two.possessive_title] sighs. She gives in to her arousal and need."
        the_person_two.char "Okay... What do you want me to do?"
        mc.name "Come here. I'll please you with my mouth while [the_person_one.title] rides my cock."
        "[the_person_two.title] hesitates for a second, but then relents."
        the_person_two.char "That sounds like fun... Okay! I'll do it!"
        $ scene_manager.strip_actor_outfit_to_max_sluttiness(the_person_two, temp_sluttiness_boost = 50)
        #call SB_threesome_description(the_person_two, the_person_one, SB_threesome_sixty_nine, make_bed(), 0, private = True, girl_in_charge = False) from _call_SB_threesome_description_SB_fetish_vaginal_family_threesome
        call start_threesome(lily, mom, start_position = Threesome_double_down) from threesome_event_test_call_2
        $ mc.business.event_triggers_dict["family_threesome"] = True
        $ update_family_threesome_crisis(3)
        "Wow, you just had sex with [the_person_one.possessive_title] and [the_person_two.possessive_title]! You can't believe how lucky you are."
        "Maybe this is the event that will finally set things in motion for you family. All three of you are in this sexually together."
        "Eventually, the girls get up."
        $ scene_manager.update_actor(the_person_one, position = "stand2", character_placement = character_center_flipped)
        $ scene_manager.update_actor(the_person_two, position = "stand4", character_placement = character_right)
        the_person_two.char "Mmm... wow... I guess... that was really good actually... Maybe we should do this more often..."
        $ scene_manager.update_actor(the_person_two, position = "walking_away")
        "[the_person_two.possessive_title] turns and starts to walk out."
        $ scene_manager.remove_actor(the_person_two)
        the_person_one.char "Holy fuck [the_person_one.mc_title], that was so hot, I can't believe you got mom to join us..."
        mc.name "I know! This might not be the last time that happens."
        the_person_one.char "Oh god, I can't wait. See you in the morning bro!"
        "[the_person_one.possessive_title] says goodnight and then turns to leave."
        $ scene_manager.remove_actor(the_person_one)

    python:
        the_person_one.reset_arousal()
        the_person_one.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.

        the_person_two.reset_arousal()
        the_person_two.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.

        # release variables
        del the_person_one
        del the_person_two

        mc.location.show_background()
        renpy.scene("Active")
    return
