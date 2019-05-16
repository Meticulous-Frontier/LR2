

init 2 python:
    def SB_fetish_vaginal_family_threesome_requirement():
        if mc_asleep():
            if mc.current_stamina > 0:  #Must have the stamina to handle a long sexy night
                if SB_get_fetish(mom) == "Vaginal Fetish" or mom.sluttiness > 50:
                    if SB_get_fetish(lily) == "Vaginal Fetish" or lily.sluttiness > 50:
                        return True
        return False

    SB_fetish_vaginal_family_threesome = Action("Family Threesome",SB_fetish_vaginal_family_threesome_requirement,"SB_fetish_vaginal_family_threesome_label")
    crisis_list.append([SB_fetish_vaginal_family_threesome,8])


label SB_fetish_vaginal_family_threesome_label():
    $ the_person_one = lily
    $ the_person_two = mom

    "Before going to bed, you hear a knock on your door. You hear [the_person_one.possessive_title] from the other side of the door."
    show screen person_info_ui(the_person_one)
    the_person_one.char "Hey [the_person_one.mc_title], you still up? I was just wondering if I could come in for a bit?"
    "You invite [the_person_one.possessive_title] in. You immediately start to get aroused when you see what she is wearing."
    $ the_person_one.outfit = SB_vaginal_lily_outfit.get_copy()
    $ the_person_two.outfit = SB_vaginal_outfit.get_copy()
    $ the_person_one.draw_person()
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
        "Strip first":
            mc.name "That sounds good [the_person.title]... why don't you give me a show before we go to bed?"
            "[the_person_one.possessive_title] smiles at you."
            the_person_one.char "Aww, does my [the_person_one.mc_title] wanna see his [the_person.title] get naked for him? What a pervert!"
            "[the_person_one.possessive_title] winks at you before beginning her routine."
            call SB_free_strip_scene(the_person_one) from _SB_free_strip_scene_SBT_10
            mc.name "Damn [the_person_one.title], you are really getting good at that..."

    "You are so busy checking out [the_person_one.possessive_title], your brain barely registers a knock on your door. [the_person_one.possessive_title] is just sitting down in your lap when you hear a gasp from your door."
    $ SB_draw_two_person_scene(person_one = the_person_one, person_two = the_person_two, one_pos_x = 0.7, two_emotion = "angry")
    hide screen person_info_ui
    show screen SB_two_person_info_ui(the_person_two, the_person_one)
    the_person_two.char "Is that... [the_person_one.name]!?! What are you... why are you naked in your [the_person_two.mc_name]'s room?" #NOTE: the_person_one doesn't nescessarily know the_person_two's title for the MC, but still somewhat makes sense.
    "[the_person_two.possessive_title] is shocked to discover that you and [the_person_one.possessive_title] are in your room, clearly about to get busy."
    the_person_one.char "Mom! Nothing was... wait... what are you wearing?"
    "[the_person_two.possessive_title] quickly realizes that [the_person_one.possessive_title] is here... doing exactly what she was coming here to do. Her cheeks turn red with embarassment."
    "You think quickly. Maybe you can salvage this situation?"
    mc.name "Hey [the_person_two.title]... you look amazing! Want to come in for a little bit? [the_person_one.title] and I are just getting started."
    "You can see a clear look of conflict in [the_person_two.possessive_title]'s eyes. Up until now, your antics have been isolated to you and her, in her mind anyway. She's slowly processing that you have a similar relationship with [the_person_one.possessive_title] "
    the_person_two.char "I mean... I suppose I could... for a bit..."
    "Still in a bit of a daze, [the_person_two.possessive_title] comes into your room, closing the door behind her. She sits over at your desk and looks over at you and [the_person_one.possessive_title] ."
    $ SB_draw_two_person_scene(person_one = the_person_one, person_two = the_person_two, one_pos_x = 0.7, two_position = "sitting")
    "[the_person_one.possessive_title] looks back at you, still a little unsure of herself. You stand up and move in close to her."
    "You put your hands on her hips and draw [the_person_one.possessive_title] into your arms. She looks up into your eyes, her hesitation melting away."
    $ SB_draw_two_person_scene(person_one = the_person_one, person_two = the_person_two, one_pos_x = 0.7, one_position = "kissing", two_position = "sitting")
    "Your lips lock together in a passionate kiss. [the_person_one.possessive_title]'s body melts into yours in surrender, even as [the_person_two.possessive_title] looks on."
    the_person_two.char "Oh my... [the_person_two.mc_title]... [the_person_one.name]..."
    "You move your hands down [the_person_one.possessive_title]'s waist and around to her butt. You give both cheeks a squeeze."
    "She presses her body against yours and sighs."
    the_person_one.char "Mmm... I can't wait for you to fuck me..."
    $ the_person_one.change_arousal(10)
    "You glance over at [the_person_two.possessive_title]. She is watching you and [the_person_one.possessive_title] intently and has one hand between her legs, stroking the outer lips of her pussy."
    $ the_person_one.change_arousal(5)
    "This is going better than you expected! You get a little braver."
    mc.name "Hey [the_person_two.title]... why don't you join us? There's no reason we can't all have a little family fun together..."
    "[the_person_two.possessive_title] sighs. She gives in to her arousal and need."
    the_person_two.char "Okay... What do you want me to do?"

    call SB_threesome_description(the_person_two, the_person_one, SB_threesome_sixty_nine, make_bed(), 0, private = True, girl_in_charge = False)
    "Wow, you just had sex with [the_person_one.possessive_title] and [the_person_two.possessive_title]! You can't believe how lucky you are."
    "Eventually, the girls get up."
    $ SB_draw_two_person_scene(person_one = the_person_one, person_two = the_person_two, one_pos_x = 0.7)
    the_person_two.char "Mmm... wow... I guess... that was really good actually... Maybe we should do this more often..."
    $ SB_draw_two_person_scene(person_one = the_person_one, person_two = the_person_two, one_pos_x = 0.7, two_position = "walking_away")
    "[the_person_two.possessive_title] turns and starts to walk out."
    the_person_one.char "Holy fuck [the_person_one.mc_title], that was so hot, I can't believe you got mom to join us..."
    "[the_person_one.possessive_title] says goodnight and then turns to leave."
    hide screen SB_two_person_info_ui

    return
