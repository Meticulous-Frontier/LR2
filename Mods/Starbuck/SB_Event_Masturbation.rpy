###Scene Idea: Caught Masturbating
#
#   In this scene, player is walking by some kind of private room when he hears moaning coming from inside
#   After investigating, player finds NPC masterbating
#   Player choices include walking away and watching
#   If watching, NPC has chance to notice PC watching. If slutty, NPC continues, if not, stops and gets angry
#   If watching, and NPC is slutty, have a chance if we went unnoticed for NPC to call out PC name
#   Give PC option to just continue watching, leave NPC a note saying thanks for the show, or to make self known
#   If make self known trigger sex scene
#
#
###
init -1 python:
    SB_caught_masturbating_crisis_weight = 5

init 2 python:
    def SB_caught_masturbating_requirement():
        if mc.business.get_employee_count() > 0:
            if mc.business.is_open_for_business():
                if mc.is_at_work():
                    for person in mc.business.get_employee_list():
                        if person.get_opinion_score("masturbating") > 0:
                            return True
                        elif person.sluttiness > 50:
                            return True
        return False

    SB_caught_masturbating_crisis = ActionMod("Office Masturbation",SB_caught_masturbating_requirement,"SB_caught_masturbating_crisis_label", 
        menu_tooltip = "You find an employee masturbating in an empty storage room.", category = "Business", is_crisis = True, crisis_weight = SB_caught_masturbating_crisis_weight)

label SB_caught_masturbating_crisis_label():
    python:
        masturbating_people = []
        for person in mc.business.get_employee_list():
            if person.get_opinion_score("masturbating") > 0 or person.sluttiness > 50:
                masturbating_people.append(person)
        the_person = get_random_from_list(masturbating_people)

    if the_person is None:
        "No one eligible for masturbating!"
        return

    $ the_person = get_random_from_list(masturbating_people)
    $ the_place = mc.business.get_employee_workstation(the_person)
    $ ordered_bottom = the_person.outfit.get_lower_ordered()
    if len(ordered_bottom) > 0:
        $ the_clothing = the_person.outfit.get_lower_ordered()[-1] #Get the very top item of clothing.

    "You decide to take a quick break from what you are doing. You stand up and stretch your legs, and go for a quick walk"
    "While you are walking by an unused storage room, you hear some muffled sounds coming from inside"
    "Looking inside, you see [the_person.possessive_title] on all fours, with her back to you, quietly moaning"
    $ the_person.draw_person(position = "doggy")
    the_person.char "mmmmmmmfff... oh..."
    $ the_person.change_arousal(50)
    $ the_person.discover_opinion("masturbating")
    if the_person.outfit.vagina_available(): #If she is naked below
        "With her pussy on full display, you can see she is masturbating vigorously. Her pink lips glisten with moisture"
    else:
        "While it is kind of hard to see, it appears that [the_person.possessive_title] has one hand in her [the_clothing.name] and is masturbating"

    menu:
        "Watch her masturbate":
             "You shift your weight slightly to get comfortable. The sight of [the_person.possessive_title] brazenly masturbating while at work has you mesmerized."
             the_person.char "yes... fuck yes"
             $ the_person.change_arousal(10)
             "[the_person.possessive_title] continues to moan to herself, lost in whatever fantasy she is masturbating to"
             #Get Caught?
             $ random_roll = renpy.random.randint(0,100)
             $ success_chance = 10*(mc.focus + 1)
             if random_roll < success_chance: #If player does not get caught
                   "[the_person.possessive_title] is breathing heavily. It is clear from how vigorously she is touching herself that she is going to orgasm soon." #TODO finish this
                   if the_person.sluttiness < 20:   #She's not interested in MC yet...
                       $ fantasy_guy = get_random_male_name()
                       "[the_person.possessive_title] seems really into it. Her back is arched as her hand works its magic on her groin"
                       $ the_person.change_arousal(10)
                       the_person.char "Mmm, [fantasy_guy], that's it... I wanna be your slut..."
                       $ the_person.change_arousal(10)
                       "Hmm, she must be fantasizing about some other guy. Does she have a boyfriend or something maybe?"
                       the_person.char "Yes [fantasy_guy]... its feels so good when you do that..."
                       $ the_person.change_arousal(10)
                       "You aren't sure what she is fantasizing about, but she is getting really into it..."
                       "As [the_person.possessive_title] continues to masturbate, you can tell she is getting ready to finish."
                       $ the_person.change_arousal(10)
                       "[the_person.possessive_title] whimpers as she cums. Her legs spasm and she gasps for air"
                       $ the_person.change_slut_temp(2)
                       $ the_person.change_happiness(3)
                       "You decide to make a quick exit before she has a chance to recover. As quietly as you can, you close the door behind you and head back to your previous work."
                   else:
                        if mc.sex_skills["Oral"] > 4 or the_person.get_opinion_score("getting head") > 0 :    #Reward oral skill, OR if girl loves "getting head" ?
                             the_person.char "Oh God, [the_person.mc_title], that's it. Eat my pussy!"      #Get a chance to eat her
                             $ the_person.change_arousal(10)
                             "It seems that [the_person.possessive_title] is fantasizing about you eating her out!"
                             "You decide that this is an opportunity too good to pass up."
                             mc.name "I'd be happy to [the_person.title]"
                             $ the_person.draw_person(position = "missionary")
                             "You startle [the_person.possessive_title] and she quickly turns over on her back."
                             the_person.char "[the_person.mc_title]? Oh God, how long have you been here?"
                             if the_person.outfit.vagina_available():           #If its available no need to strip.
                                  "You drop down on the floor in front of her. With her pussy exposed you waste no time diving right in"
                             else:                                              #Otherwise, strip her down.
                                  "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy"

                                  python:
                                         for clothing in the_person.outfit.get_lower_ordered():
                                              the_person.outfit.remove_clothing(clothing)
                                              the_person.draw_person(position = "missionary")
                                              renpy.say("","")

                                  "With her pussy finally exposed you waste no time diving right in"

                             "Cupping her ass with your hands, you circle your tongue all around her wet, inviting cunt."
                             $ the_person.change_arousal(10)
                             the_person.char "Oh [the_person.mc_title], you have no idea how bad I need this."
                             "[the_person.possessive_title] runs her hands your hair. You bury your nose in her mound and flick your tongue in and out of her slick hole"
                             "You circle her clit a few times with your tongue. You suck it into your mouth roughly a couple of times and then release it, you lips making a wet, lewd smackin noise"
                             $ the_person.change_arousal(10)
                             the_person.char "I am so close... I'm sorry [the_person.mc_title], I'm not going to last much longer"
                             $ the_person.draw_person(emotion="orgasm", position ="missionary")
                             "You double your efforts, licking, sucking, and teasing every corner of her pleasing slit"
                             $ the_person.change_arousal(10)
                             "[the_person.possessive_title] begins to orgasm convulsively, and she cries out."
                             the_person.char "Yes [the_person.mc_title]! Yes! Yes! Oh fuck how do you do that"
                             $ mc.listener_system.fire_event("girl_climax", the_person = the_person, the_position = "missionary")
                             $ the_person.change_happiness(5)
                             $ the_person.change_obedience(5)
                             $ the_person.change_slut_core(2)
                             $ the_person.change_slut_temp(5)
                             $ the_person.change_love(3)
                             #show screen float_up_screen(["+5 Happiness","+5 Obedience","+2 Core Sluttiness" ],["float_text_yellow","float_text_grey","float_text_pink"])
                             "[the_person.possessive_title] runs her hands through your hair one last time. You get up and give her a kiss, letting her taste herself on your tongue."
                             "You excuse yourself and then head to the bathroom and get cleaned up before returning to your work."
                        else:
                             "[the_person.possessive_title] seems really into it. Her back is arched as her hand works its magic on her groin"  ##TODO: this scene
                             the_person.char "Mmm, [the_person.mc_title], that's it... I wanna be your slut..."
                             $ the_person.change_arousal(10)
                             "You hear [the_person.possessive_title] mumble your name. She's fantasizing about you! You stay as quiet as possible and continue to watch in amazement."
                             if the_person.get_opinion_score("giving blowjobs") > 0:
                                  the_person.char "Yeah [the_person.mc_title]... that it... let me suck on that delicious cock... I'll take care of it for you..."
                                  "She's fantasizing about sucking you off! Maybe you should pay her a visit later..."
                                  $ the_person.discover_opinion("giving blowjobs")
                             elif the_person.get_opinion_score("anal sex") > 0:
                                  the_person.char "Oh god [the_person.mc_title], be careful! It feels so full when stick it in my ass like that..."
                                  "She's fantasizing about you fucking her ass! Maybe you should pay her a visit later..."
                                  $ the_person.discover_opinion("anal sex")
                             else:
                                  the_person.char "Yes [the_person.mc_title]... you make me feel so good... I just wanna make you feel good too baby"
                                  "Sounds like she is really into you. Maybe you should pay her a visit later..."
                             $ the_person.change_arousal(10)
                             "[the_person.possessive_title]'s hand continues to work furiously on her pussy. You can tell from her proficiency that she probably does this often."
                             "As [the_person.possessive_title] continues to masturbate, you can tell she is getting ready to finish."
                             $ the_person.change_arousal(10)
                             "[the_person.possessive_title] whimpers as she cums. Her legs spasm and she gasps for air"
                             $ mc.listener_system.fire_event("girl_climax", the_person = the_person, the_position = "doggy")
                             $ the_person.change_slut_temp(2)
                             $ the_person.change_happiness(5)
                             "You back out of the room before she has a chance to recover. You can't believe your good luck, catching an employee masturbating... while thinking of you of all people!"
                             "On your way back to your work, you swing by [the_person.possessive_title]'s desk. You write her a quick note."
                             "Thanks for the show!"
                             "You finish it with your initials and leave it next to her computer monitor"
                             "Half an hour later while you are back into your work, you get a text message from [the_person.possessive_title]"
                             if the_person.sluttiness > 60:
                                the_person.char "Next time join in!!!"
                             else :
                                the_person.char ";)"
                                "It is a winking face emoji!"

             else: #Player gets caught
                   "Straining to get a better a view, for a brief moment you lose your focus. You accidentally drop a pen you were holding onto and it clatters loudly across the floor."
                   "[the_person.possessive_title] immediately stops and looks back at the source of the noise. She immediately locks eyes with you and the realization that she just got caught masturbating at work sinks in"
                   if the_person.sluttiness < 20: #She is not slutty. 50/50 she runs out of the room apologizing or gets pissed
                        $ the_person.draw_person()
                        "[the_person.possessive_title] quickly stands up."
                        $ random_roll2 = renpy.random.randint(0,100)
                        if random_roll2 < 50: #She's pissed
                             $ the_person.draw_person(emotion="angry")
                             the_person.char "What the fuck?!? Were you just standing there watching me? Oh my god..."
                             mc.name "No, I was... I heard a noise... I was just trying to see what it was..."
                             if mc.charisma > 4:    #Charisma check to limit the damage
                                  $ the_person.draw_person(emotion="happy")
                                  "[the_person.possessive_title] hesitates for a moment, then turns to you."
                                  the_person.char "Okay.... I believe you... but still, maybe you could knock or something? You scared the shit out of me!"
                                  "It looks like you've managed to convince her."
                                  $ the_person.draw_person(position = "walking_away")
                                  $ the_person.change_happiness(-2)
                                  $ the_person.change_obedience(-2)
                                  "After a quick apology, [the_person.possessive_title] excuses herself. You see her head into the women's restroom. You decide it would be a bad idea to try and follow her there."
                                  "You finish up your walk and return back to your previous work"
                             else:
                                  $ the_person.change_happiness(-5)
                                  $ the_person.change_obedience(-5)
                                  # show screen float_up_screen(["-5 Happiness","-5 Obedience"],["float_text_yellow","float_text_grey"])
                                  the_person.char "I know I shouldn't have been... but you shouldn't just... UGH!!!"
                                  $ the_person.draw_person(position = "walking_away")
                                  "[the_person.possessive_title] storms off. While the situation was awkward, it left a bit of tension in the air..."
                                  $ the_person.change_slut_temp(10)
                                  #show screen float_up_screen([slut_report],["float_text_pink"])   ###OLD code
                                  "You finish up your walk and return back to your previous work"
                        else: #She's embarassed
                             "Mortified, [the_person.possessive_title] makes a run for the door"
                             $ the_person.draw_person(position = "walking_away")
                             the_person.char "Oh my god... I'm so sorry [the_person.mc_title]. I just couldn't help myself. I won't let this happen again!"
                             "You try to reassure [the_person.possessive_title], but she quickly runs off before you can speak"
                             $ the_person.change_happiness(-5)
                             $ the_person.change_obedience(5)
                             $ the_person.change_slut_temp(5)
                             #show screen float_up_screen(["-5 Happiness","+5 Obedience"],["float_text_yellow","float_text_grey","float_text_pink"])    ###OLD code
                             "You finish up your walk and return back to your previous work"
                   elif the_person.sluttiness < 60:#She is a bit slutty
                        "[the_person.possessive_title] is stunned. You can see the conflict in her eyes. She just got caught masturbating at work, by her boss of all people."
                        "Sensing her conflict, you decide to give her a bit of encouragement. You reach down and begin to stroke yourself through your slacks."
                        $ the_person.draw_person(position = "missionary")
                        "[the_person.possessive_title] rolls over on her back and continues masturbating."
                        $ the_person.change_arousal(20)
                        if the_person.outfit.vagina_available():
                             "Her delicious pussy on full display, [the_person.possessive_title] increases her pace while closely watching you."
                        else:
                             "[the_person.possessive_title] has her hand in her [the_clothing.name]. Her movements get faster while closely watching you"
                        the_person.char "Oh my god. [the_person.mc_title], I can't believe this is happening..."
                        if the_person.get_opinion_score("public sex") > 0:
                            "[the_person.possessive_title]'s cheeks are flush with arousal. Her eyes stare straight into yours as she continues to touch herself."
                            the_person.char "Does it excite you, [the_person.mc_title]? To see me here, touching myself like this...?"
                            "You can tell tell she likes having an audience."
                            mc.name "Of course, [the_person.title]. And you like having someone here to watch you, don't you?"
                            "[the_person.possessive_title] doesn't respond with words, but moans at your words. It is clear she enjoys when others watch her doing sexual things..."
                            $ the_person.discover_opinion("public sex")
                        else :
                            "[the_person.possessive_title]'s cheeks are flush with arousal. She closes her eyes and concentrates on whatever fantasy she is lost in"
                            "Her breathing gets ragged as she nears the finish line."
                        $ the_person.change_arousal(20)
                        the_person.char "Oh fuck... I'm gonna cum!"
                        $ the_person.draw_person(emotion="orgasm", position ="missionary")
                        "[the_person.possessive_title] whimpers and her eyes glaze over as she cums. Her legs spasm and she gasps for air"
                        "Catching her breath, [the_person.possessive_title] looks up at you but doesn't say a word. It is clear that masturbating in front of her boss has left a lasting impression."
                        $ mc.listener_system.fire_event("girl_climax", the_person = the_person, the_position = "missionary")
                        $ the_person.change_happiness(5)
                        $ the_person.change_obedience(5)
                        $ the_person.change_slut_core(2)
                        #show screen float_up_screen(["+5 Happiness","+5 Obedience","+2 Core Sluttiness" ],["float_text_yellow","float_text_grey","float_text_pink"])
                        "You decide to give [the_person.possessive_title] a chance to recover. You nod at her and then back out of the room."
                        "You finish up your walk and return back to your previous work"
                   else: #She is very slutty
                       the_person.char "Oh [the_person.mc_title]! Thank god, I could really use your help here..."
                       if the_person.outfit.vagina_available() == False:
                           "[the_person.possessive_title] begins to pull off her clothes."
                           python:
                               for clothing in the_person.outfit.get_lower_ordered():
                                    the_person.outfit.remove_clothing(clothing)
                                    the_person.draw_person(position = "doggy")
                                    renpy.say("","")
                       the_person.char "Could you just give me a little quickie? I'm all warmed up, you could just stick it in right now..."
                       menu:
                           "Fuck her" if mc.current_stamina > 0:
                               mc.name "Sure, I could go for a quick fuck right now."
                               "You quickly pull your pants down. [the_person.possessive_title] is wiggling her ass back and forth, waiting for you."
                               "You rub the tip of your penis against [the_person.possessive_title]'s cunt. She is already soaking wet."
                               "When you're ready you push forward, slipping your shaft deep inside of [the_person.possessive_title]. She moans and quivers as you start to pump in and out."
                               call sex_description(the_person, doggy, make_floor(), round = 1, private = True, girl_in_charge = False) from _call_sex_sb_event_masturbation_010
                               if the_person.arousal > 130:
                                   "[the_person.possessive_title] is exhausted. She came so hard, it is all she can do to pant and catch her breath."
                                   $ the_person.change_happiness(5)
                                   $ the_person.change_obedience(5)
                                   $ the_person.change_slut_core(2)
                                   $ the_person.change_slut_temp(5)
                               else:
                                   "[the_person.possessive_title] quickly recovers after you finish."
                                   $ the_person.change_happiness(3)
                                   $ the_person.change_slut_temp(3)
                               the_person.char "Mmmm, thanks [the_person.mc_title]! That was just what I needed..."
                               "You decide to give [the_person.possessive_title] a chance to recover. You make yourself decent, then leave the room, closing the door on the way out."
                               "You finish up your walk and return back to your previous work"
                           "Fuck her\n{size=22}Requires Stamina{/size} (disabled)" if mc.current_stamina == 0:
                               pass

                           "Just watch":
                               mc.name "I'm afraid I can't right now, but that's okay, I'm definitely enjoying the view."
                               "She looks back at you. You can see the hunger in her eyes."
                               the_person.char "Ok [the_person.mc_title], but if you change your mind..."
                               "[the_person.possessive_title] continues rubbing her exposed pussy. Once in a while she peeks back at you to see if you are still watching."
                               $ the_person.change_arousal(20)

                               if the_person.get_opinion_score("public sex") > 0:
                                   "[the_person.possessive_title]'s cheeks are flush with arousal. She peeks back and stares straight into your eyes as she continues to touch herself."
                                   the_person.char "Does it excite you, [the_person.mc_title]? To see me here, touching myself like this...?"
                                   "You can tell tell she likes having an audience."
                                   mc.name "Of course, [the_person.title]. And you like having someone here to watch you, don't you?"
                                   "[the_person.possessive_title] moans. It is clear she enjoys when others watch her doing sexual things..."
                                   $ the_person.discover_opinion("public sex")
                               else :
                                   "[the_person.possessive_title]'s cheeks are flush with arousal. She closes her eyes and concentrates on whatever fantasy she is lost in"
                                   "Her breathing gets ragged as she nears the finish line."
                               $ the_person.change_arousal(20)
                               the_person.char "Oh fuck... I'm gonna cum!"
                               "[the_person.possessive_title] whimpers and her eyes glaze over as she cums. Her legs spasm and she gasps for air"
                               "Catching her breath, [the_person.possessive_title] leans forward, leaving her ass up in the air. It is clear that masturbating in front of her boss has left a lasting impression."
                               $ mc.listener_system.fire_event("girl_climax", the_person = the_person, the_position = "doggy")
                               $ the_person.change_happiness(5)
                               $ the_person.change_obedience(5)
                               $ the_person.change_slut_core(2)
                               $ the_person.change_slut_temp(3)
                               #show screen float_up_screen(["+5 Happiness","+5 Obedience","+2 Core Sluttiness" ],["float_text_yellow","float_text_grey","float_text_pink"])
                               "You decide to give [the_person.possessive_title] a chance to recover. You nod to her and then back out of the room."
                               "You finish up your walk and return back to your previous work"

             $ the_person.reset_arousal()
             $ the_person.review_outfit(show_review_message = False)
        "Keep walking":
            "You decide to give [the_person.possessive_title] some privacy. As quietly as you can, you close the door behind you and continue walking"

    $ the_person.reset_arousal()
    $ the_person.review_outfit() #Make sure to reset her outfit so she is dressed properly.
    $ change_scene_display(mc.location)
    $ renpy.scene("Active")
    return
