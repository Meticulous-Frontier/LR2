## Stripclub storyline Mod by Corrado
#  BDSM performers role definition.
#  The role is appended to BDSM performers after they start to work for you.

init 3305 python:

    def get_bdsm_exhibitions(the_person):
        return the_person.event_triggers_dict.get("exhibitions", 0)

    def increase_bdsm_exhibitions(the_person):
        the_person.event_triggers_dict["exhibitions"] = get_bdsm_exhibitions(the_person) + 1
        return

    def strip_club_bdsm_dildochair_MC_requirements(the_person):
        if the_person.has_role(bdsm_performer_role):
            if mc.location is bdsm_room:
                return True
        return False

    def strip_club_bdsm_dildochair_Mistress_requirements(the_person):
        if the_person.has_role(bdsm_performer_role):
            if strip_club_get_mistress() in mc.location.people:
                if mc.location is bdsm_room:
                    return True
        return False

    BDSM_performer_wardrobe = wardrobe_from_xml("BDSM_Wardrobe")

    strip_club_dildochair_MC_action =Action("Use the dildo chair {image=gui/heart/Time_Advance.png}", strip_club_bdsm_dildochair_MC_requirements, "strip_club_bdsm_dildochair_MC_label", menu_tooltip = "Use the dildo chair with your BDSM performer.")
    strip_club_dildochair_Mistress_action =Action("Mistress use the chair {image=gui/heart/Time_Advance.png}", strip_club_bdsm_dildochair_Mistress_requirements, "strip_club_bdsm_dildochair_Mistress_label", menu_tooltip = "Have the Mistress use the dildo chair with your BDSM performer.")

    bdsm_performer_role = Role("BDSM performer", [promote_to_manager_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action, strip_club_dildochair_MC_action, strip_club_dildochair_Mistress_action], hidden = False)

init -1 python:
    def strip_club_bdsm_strip_description(the_person, the_item, the_group):
        test_outfit = the_person.outfit.get_copy()
        test_outfit.remove_clothing(the_item)
        if test_outfit.tits_visible() and not the_person.outfit.tits_visible():
            if person.has_taboo("bare_tits"):
                renpy.say("", the_person.title + " glances around nervously.")
                renpy.say(the_person.char, "Maybe I can keep my bra on?")
                renpy.say(mc.name, "Relax " + person.title + ", it's your job! Come on, get those tits out for us.")
                renpy.say(the_person.char, "Okay, okay...")

            the_group.draw_animated_removal(the_person, make_primary = True, the_clothing = the_item)
            if the_person.has_large_tits():
                renpy.say("", the_person.title + " pulls off her " + the_item.display_name + ". Her large breasts jiggle briefly as they're released.")
            else: #Peepers
                renpy.say("", the_person.title + " pulls off her " + the_item.display_name + ", setting her tits free.")

            if person.has_taboo("bare_tits"):
                renpy.say("", the_person.title + " tries to keep her breasts covered with her hands, cheeks red.")
                the_person.break_taboo("bare_tits")

        elif test_outfit.vagina_visible() and not the_person.outfit.vagina_visible():
            if the_person.has_taboo("bare_pussy"):
                renpy.say("", the_person.title + " starts to move her " + the_item.display_name + ", but hesitates.")
                renpy.say(the_person.char, "Should I really remove my "+ the_item.display_name + "?")
                renpy.say(mc.name, "Come on " + the_person.title + ", it's your job and the reason we're here.")
                renpy.say("", "She takes a deep breath and gathers up her courage.")
            the_group.draw_animated_removal(the_person, make_primary = True, the_clothing = the_item)
            renpy.say("", the_person.title + " pulls her " + the_item.display_name + " down, peeling them away from her pussy.")

            if the_person.has_taboo("bare_pussy"):
                renpy.say("", the_item.display_name + " off, " + the_person.title + " cover herself as she can, blushing a fierce red.")
                the_person.break_taboo("bare_pussy")

        elif the_person.has_taboo("underwear_nudity") and test_outfit.underwear_visible() and not the_person.outfit.underwear_visible():
            renpy.say("", the_person.title + " glances around nervously.")
            renpy.say(the_person.char, "You don't really want me to take off my " + the_item.display_name + ", do you? I'll just have my underwear on...")
            renpy.say(mc.name, "Come on " + the_person.title + ", that's the whole point of this place! Nobody cares about you just wearing your underwear.")
            renpy.say("","She bites her lip as she considers it, then takes a deep breath.")
            the_group.draw_animated_removal(the_person, make_primary = True, the_clothing = the_item)
            renpy.say("", the_person.title + " pulls off her " + the_item.display_name + " and drops it on the floor.")
            renpy.say(the_person.char, "There, I did it.")
            the_person.break_taboo("underwear_nudity")

        else:
            the_group.draw_animated_removal(the_person, make_primary = True, the_clothing = the_item)
            renpy.say("", the_person.title + " takes her " + the_item.display_name + " off and drops it on the floor.")
            pass

        the_person.update_outfit_taboos()
        return

label strip_club_end_of_day_label():
    "Tired after you spent the night at the stripclub, you come back home."
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "It's time for you to go to sleep."
    call advance_time from _call_advance_time_strip_club_end_of_day
    return

label strip_club_bdsm_dildochair_MC_label(the_person): # MC use the dildo chair with her
    "You decide it's time for [the_person.title] to have some fun, so you approach the chair and set up..."
    menu:
        "One dildo":
            $ the_person.event_triggers_dict["dildochair_dildos"] = 1
        "Two dildos" if the_person.get_opinion_score("anal sex") >= 0:
            $ the_person.event_triggers_dict["dildochair_dildos"] = 2
    mc.name "Ok, [the_person.title]... Get naked and come here!"
    the_person.char "Okay, whatever you want [the_person.mc_title]."
    "She starts to strip down for you."
    $ naked_strip_description(the_person)
    $ the_person.draw_person(emotion = "happy", position = "stand4")
    the_person.char "Are you planning something naughty for me, [the_person.mc_title]?"
    menu:
        "Reward her (tooltip)Let her to orgasm":
            mc.name "Since you've been a good girl [the_person.title], I will let you have as many orgasm your body can take."
            if get_bdsm_exhibitions <= 3 and the_person.get_opinion_score("public sex") <= 0: # She's still a bit shy
                the_person.char "Really [the_person.mc_title]? Here in front of everyone? I don't know if I..."
            elif the_person.obedience <= 200:
                the_person.char "Really [the_person.mc_title]? I don't know if I..."
            else:
                the_person.char "I'm your slave [the_person.mc_title]: I'll do as you command."
            mc.name "Sit on this chair [the_person.title], I'm going to tie you."
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1 and the_person.get_opinion_score("anal sex") >= 0:
                the_person.char "Where should I put the dildo?"
                menu:
                    "Vaginal fun":
                        mc.name "I think your pussy will be pleased by this toy!"
                        $ the_person.draw_person(emotion = "happy", position = "sitting")
                        "Her eyes are glued to yours while she slowly slips the big dildo in her pussy."
                    "Anal fun":
                        $ the_person.event_triggers_dict["dildochair_dildos"] = 3
                        mc.name "I think your lil' asshole will be pleased by this toy!"
                        $ the_person.draw_person(emotion = "happy", position = "sitting")
                        "Her eyes are glued to yours while she slowly slips the big dildo in her asshole."
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 1:
                "She obey your command and sit."
                $ the_person.draw_person(emotion = "happy", position = "sitting")
                "Her eyes are glued to yours while she slowly slips the big dildo in her pussy."
            else:
                "She obey your command and sit."
                $ the_person.draw_person(emotion = "happy", position = "sitting")
                "Her eyes are glued to yours while she slowly slips the big dildos in both her holes."
            "You lock the belts on her legs, arms, neck and stomach: she can't move anymore."
            the_person.char "Oh my god! I feel..."
            mc.name "That your master own you? You're my good slave, and good slaves should be rewarded."
            $ the_person.change_obedience (5)
            "You turn on the chair and set the vibrations at:"
            menu dildochair_reward_menu:
                "Speed 1 (tooltip)Slowly increase her arousal" if the_person.energy >= 10: # Each action use 10 energy and give 10 arousal and 1 obedience
                    "A feeble buzz can be heard in the room, [the_person.title] bite her lips."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "Bzzz !... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Oh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (1, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "It's so pleasant this feeling: this thing tickle my pussy very nicely!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "It's so pleasant this feeling: both my holes tickled so nicely!"
                    else: # One dildo in the ass
                        the_person.char "It's so pleasant this feeling: this thing tickle my ass very nicely!"
                    $ the_person.change_obedience (1, add_to_log = False)
                    if the_person.arousal >= 100:
                        $ the_person.draw_person(emotion = "orgasm", position = "sitting")
                        the_person.char "Oh my god, I'm cumming....Ahhh....YES!....please [the_person.mc_title], increase the speed!"
                        $ the_person.arousal //= 2
                        $ the_person.change_slut_temp (10)
                    "You decide what to do next."
                    jump dildochair_reward_menu
                "Speed 1\n{color=#ff0000}{size=18}Requires at least 10 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 10:
                    pass
                "Speed 2 (tooltip)Moderately increase her arousal" if the_person.energy >= 10: # Each action use 10 energy and give 20 arousal and 2 obedience
                    "A soft buzz can be heard in the room, [the_person.title] bite her lips moaning."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZzz !!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (2, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "It's so good this feeling: this thing fills my pussy very nicely!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "It's so good this feeling: both my holes filled so nicely!"
                    else: # One dildo in the ass
                        the_person.char "It's so good this feeling: this thing fills my ass very nicely!"
                    $ the_person.change_obedience (2, add_to_log = False)
                    if the_person.arousal >= 100:
                        $ the_person.draw_person(emotion = "orgasm", position = "sitting")
                        the_person.char "Oh my god, I'm cumming....Aahhh....YES!....please [the_person.mc_title], increase the speed!"
                        $ the_person.arousal //= 2
                        $ the_person.change_slut_temp (10)
                    "You decide what to do next."
                    jump dildochair_reward_menu
                "Speed 2\n{color=#ff0000}{size=18}Requires at least 10 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 10:
                    pass
                "Speed 3 (tooltip)Strongly increase her arousal" if the_person.energy >= 10: # Each action use 10 energy and give 30 arousal and 3 obedience
                    "A buzz can be heard in the room, [the_person.title] bite her lips moaning loudly."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZZz !!!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (3, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "Ahh! This feeling is amazing: this cock fills my pussy so good!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "Ahh! This feeling is amazing: both my holes filled so good!"
                    else: # One dildo in the ass
                        the_person.char "Ahh! This feeling is amazing: this cock fills my ass so good!"
                    $ the_person.change_obedience (3, add_to_log = False)
                    if the_person.arousal >= 100:
                        $ the_person.draw_person(emotion = "orgasm", position = "sitting")
                        the_person.char "Oh my god, I'm cumming....Aaahhh....YES!....please [the_person.mc_title], increase the speed!"
                        $ the_person.arousal //= 2
                        $ the_person.change_slut_temp (10)
                    "You decide what to do next."
                    jump dildochair_reward_menu
                "Speed 3\n{color=#ff0000}{size=18}Requires at least 10 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 10:
                    pass
                "Max speed (tooltip)Extremely increase her arousal" if the_person.energy >= 10: # Each action use 10 energy and give 40 arousal and 4 obedience
                    "A loud buzz can be heard in the room, [the_person.title]'s tongue is out and begs to lick something!"
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZZZ !!!!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (4, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "YES! YES! YES! Fill my pussy this way! More! Give me more!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "YES! YES! YES! Fill my holes this way! More! Give me more!"
                    else: # One dildo in the ass
                        the_person.char "YES! YES! YES! Fill my ass this way! More! Give me more!"
                    $ the_person.change_obedience (4, add_to_log = False)
                    if the_person.arousal >= 100:
                        $ the_person.draw_person(emotion = "orgasm", position = "sitting")
                        the_person.char "Oh my god, I'm cumming so hard! ....Aaaahhh ....YES! ....please [the_person.mc_title], don't stop, give me more!"
                        $ the_person.arousal //= 2
                        $ the_person.change_slut_temp (10)
                    "You decide what to do next."
                    jump dildochair_reward_menu
                "Max speed\n{color=#ff0000}{size=18}Requires at least 10 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 10:
                    pass
                "Release her" if the_person.energy < 10:
                    $ the_person.arousal == 0
                    the_person.char "I'm exhausted, but it was worth every second: thank you Master for granting your slave this much pleasure!"
                    mc.name "Please me and you'll be pleased. Now you can get dressed."
                    $ the_person.apply_planned_outfit()
                    $ the_person.draw_person(emotion = "happy", position = "stand3")
                    $ the_person.change_obedience (20)
                    $ increase_bdsm_exhibitions(the_person)
                    "Her eyes are full of love for her Master."
            $ clear_scene()
            call advance_time from _call_advance_strip_club_bdsm_dildochair_MC_1
            return # jump game_loop ???

        "Punish her (tooltip)Prevent her to orgasm":
            mc.name "Since you've not been a good slave [the_person.title], you will be pleased but you're not allowed to orgasm."
            $ the_person.draw_person(emotion = "sad", position = "stand4")
            if get_bdsm_exhibitions <= 3 and the_person.get_opinion_score("public sex") <= 0: # She's still a bit shy
                the_person.char "Really [the_person.mc_title]? Here in front of everyone? I don't know if I..."
            elif the_person.obedience <= 200:
                the_person.char "Really [the_person.mc_title]? I don't know if I..."
            else:
                the_person.char "I'm your slave [the_person.mc_title]: I'll do as you command."
            mc.name "Sit on this chair [the_person.title], I'm going to tie you."
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1 and the_person.get_opinion_score("anal sex") >= 0:
                the_person.char "Where should I put the dildo?"
                menu:
                    "Vaginal fun":
                        mc.name "I think your pussy is the right place for this toy!"
                        $ the_person.draw_person(emotion = "sad", position = "sitting")
                        "Her eyes are glued to yours while she slowly slips the big dildo in her pussy."
                    "Anal fun":
                        $ the_person.event_triggers_dict["dildochair_dildos"] = 3
                        mc.name "I think your lil' asshole is the right place for this toy!"
                        $ the_person.draw_person(emotion = "sad", position = "sitting")
                        "Her eyes are glued to yours while she slowly slips the big dildo in her asshole."
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 1:
                "She obey your command and sit."
                $ the_person.draw_person(emotion = "sad", position = "sitting")
                "Her eyes are glued to yours while she slowly slips the big dildo in her pussy."
            else:
                "She obey your command and sit."
                $ the_person.draw_person(emotion = "happy", position = "sitting")
                "Her eyes are glued to yours while she slowly slips the big dildos in both her holes."
            "You lock the belts on her legs, arms, neck and stomach: she can't move anymore."
            the_person.char "Oh my god! I feel..."
            mc.name "That your master own you? So that's the right feeling, even if you're not yet a good slave."
            $ the_person.change_obedience (5)
            "You turn on the chair and set the vibrations at:"
            menu dildochair_punish_menu:
                "Speed 1 (tooltip)Slowly increase her arousal" if the_person.energy >= 10 and the_person.arousal <= 89: # Each action use 10 energy and give 10 arousal and 1 obedience
                    "A feeble buzz can be heard in the room, [the_person.title] bite her lips."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "Bzzz !... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Oh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (1, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "It's so pleasant this feeling: this thing tickle my pussy very nicely!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "It's so pleasant this feeling: both my holes tickled so nicely!"
                    else: # One dildo in the ass
                        the_person.char "It's so pleasant this feeling: this thing tickle my ass very nicely!"
                    $ the_person.change_obedience (1, add_to_log = False)
                    if the_person.arousal >= 70:
                        the_person.char "Please [the_person.mc_title], I promise I will be the best slave of your! Please, let me cum!"
                    "You decide what to do next."
                    jump dildochair_punish_menu
                "Speed 1\n{color=#ff0000}{size=18}She will orgasm!{/size}{/color} (disabled)" if the_person.arousal >= 90:
                    pass
                "Speed 2 (tooltip)Moderately increase her arousal" if the_person.energy >= 10 and the_person.arousal <= 79: # Each action use 10 energy and give 20 arousal and 2 obedience
                    "A soft buzz can be heard in the room, [the_person.title] bite her lips moaning."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZzz !!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (2, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "It's so good this feeling: this thing fills my pussy very nicely!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "It's so good this feeling: both my holes filled so nicely!"
                    else: # One dildo in the ass
                        the_person.char "It's so good this feeling: this thing fills my ass very nicely!"
                    $ the_person.change_obedience (2, add_to_log = False)
                    if the_person.arousal >= 70:
                        the_person.char "Please [the_person.mc_title], I promise I will be the best slave of your! Please, let me cum!"
                    "You decide what to do next."
                    jump dildochair_punish_menu
                "Speed 2\n{color=#ff0000}{size=18}She will orgasm!{/size}{/color} (disabled)" if the_person.arousal >= 80:
                    pass
                "Speed 3 (tooltip)Strongly increase her arousal" if the_person.energy >= 10 and the_person.arousal <= 69: # Each action use 10 energy and give 30 arousal and 3 obedience
                    "A buzz can be heard in the room, [the_person.title] bite her lips moaning loudly."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZZz !!!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (3, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "Ahh! This feeling is amazing: this cock fills my pussy so good!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "Ahh! This feeling is amazing: both my holes filled so good!"
                    else: # One dildo in the ass
                        the_person.char "Ahh! This feeling is amazing: this cock fills my ass so good!"
                    $ the_person.change_obedience (3, add_to_log = False)
                    if the_person.arousal >= 70:
                        the_person.char "Please [the_person.mc_title], I promise I will be the best slave of your! Please, let me cum!"
                    "You decide what to do next."
                    jump dildochair_punish_menu
                "Speed 3\n{color=#ff0000}{size=18}She will orgasm!{/size}{/color} (disabled)" if the_person.arousal >= 70:
                    pass
                "Max speed (tooltip)Extremely increase her arousal" if the_person.energy >= 10 and the_person.arousal <= 59: # Each action use 10 energy and give 40 arousal and 4 obedience
                    "A loud buzz can be heard in the room, [the_person.title]'s tongue is out and begs to lick something!"
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZZZ !!!!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (4, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "YES! YES! YES! Fill my pussy this way! More! Give me more!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "YES! YES! YES! Fill my holes this way! More! Give me more!"
                    else: # One dildo in the ass
                        the_person.char "YES! YES! YES! Fill my ass this way! More! Give me more!"
                    $ the_person.change_obedience (4, add_to_log = False)
                    if the_person.arousal >= 70:
                        the_person.char "Please [the_person.mc_title], I promise I will be the best slave of your! Please, let me cum!"
                    "You decide what to do next."
                    jump dildochair_punish_menu
                "Max speed\n{color=#ff0000}{size=18}She will orgasm!{/size}{/color} (disabled)" if the_person.arousal >= 60:
                    pass
                "Change your mind (tooltip)Change your mind and let her cum." if the_person.energy >=10 and the_person.arousal >= 80:
                    "You decide to let her finally cum: the chair is set now at the maximum speed."
                    "A loud buzz can be heard in the room, [the_person.title]'s tongue is out and begs to lick something!"
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZZZ !!!!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (4, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "YES! YES! YES! Fill my pussy this way! More! Give me more!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "YES! YES! YES! Fill my holes this way! More! Give me more!"
                    else: # One dildo in the ass
                        the_person.char "YES! YES! YES! Fill my ass this way! More! Give me more!"
                    $ the_person.draw_person(emotion = "orgasm", position = "sitting")
                    "She finally reached her coveted orgasm: the chair is now wet for her flooding juices."
                    $ the_person.arousal == 0
                    $ the_person.change_stats(obedience = 20, slut_temp = 10, slut_core = 2, happiness = 10, love = 2)
                    $ the_person.draw_person(emotion = "happy", position = "sitting")
                    the_person.char "Thank you [the_person.mc_title], let me always cum like this and I'll be your devoted slave!"
                    "You release her from the chair and let her dress."
                    $ the_person.apply_planned_outfit()
                    $ the_person.draw_person(emotion = "happy", position = "stand3")
                    $ increase_bdsm_exhibitions(the_person)
                    "She still can't properly stand on her trembling, after-orgasm, legs."
                    $ clear_scene()
                    call advance_time from _call_advance_strip_club_bdsm_dildochair_MC_2
                    return
                "Release her" if the_person.energy < 10:
                    $ the_person.arousal == 0
                    the_person.char "I'm exhausted, but I got your lesson [the_person.mc_title], I promise I'll be your devoted slave."
                    mc.name "Please me and you'll be pleased. Now you can get dressed."
                    "You release her from the chair's belts."
                    $ the_person.apply_planned_outfit()
                    $ the_person.draw_person(emotion = "sad", position = "stand3")
                    $ the_person.change_stats(obedience = 10, slut_temp = 5, slut_core = 1)
                    $ increase_bdsm_exhibitions(the_person)
                    "Her eyes are full of love for her Master."
                    $ clear_scene()
                    call advance_time from _call_advance_strip_club_bdsm_dildochair_MC_3
                    return
                "Release her" if the_person.arousal >= 90:
                    $ the_person.arousal == 0
                    "While you stop the chair and start to release the belts she beg you."
                    the_person.char "Please [the_person.mc_title]... Master! Yes, Master... Please, let me cum at least one time!"
                    mc.name "Please me and you'll be pleased. Now you can get dressed."
                    $ the_person.apply_planned_outfit()
                    $ the_person.draw_person(emotion = "sad", position = "stand3")
                    $ the_person.change_stats(obedience = 10, slut_temp = 5, slut_core = 1, happiness = -5)
                    $ increase_bdsm_exhibitions(the_person)
                    the_person.char "I promise I'll do my best to please my Master!"
    $ clear_scene()
    call advance_time from _call_advance_strip_club_bdsm_dildochair_MC_4
    return

label strip_club_bdsm_dildochair_Mistress_label(the_person): # The Mistress use the dildo chair with her
    $ mistress = strip_club_get_mistress()
    "You ask [mistress.possessive_title] to set up the dildo chair and have some fun with [the_person.possessive_title]."
    $ the_group = GroupDisplayManager([mistress, the_person], mistress)
    $ the_group.draw_group()
    $ the_group.draw_person(mistress, position = "stand4", emotion = "happy")
    mistress.char "Sure [mistress.mc_title], how many dildos do you want I install on the chair?"
    menu:
        "One dildo":
            $ the_person.event_triggers_dict["dildochair_dildos"] = 1
        "Two dildos" if the_person.get_opinion_score("anal sex") >= 0:
            $ the_person.event_triggers_dict["dildochair_dildos"] = 2
    mistress.char "Ok, [the_person.name]... Get naked and come here!"
    $ the_group.set_primary(the_person)
    # $ the_group.redraw_group()
    $ the_group.draw_person(the_person, position = "stand3", emotion = "happy")
    the_person.char "Okay Mistress, whatever [the_person.mc_title] wants."
    "She starts to strip down while she look at you."
    $ the_item = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
    while the_item is not None:
        $ the_group.draw_animated_removal(the_person, make_primary = True, the_clothing = the_item)
        python:
            renpy.say("", the_person.title + " takes her " + the_item.display_name + " off and drops it on the floor.")
        $ the_item = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
        pass
    $ the_person.update_outfit_taboos()
    the_person.char "Are you guys planning something naughty for me?"
    menu:
        "Reward her (tooltip)Let her to orgasm":
            mc.name "[the_person.title], since you've been a good girl I'll let [mistress.title] let you have as many orgasm your body can take."
            if get_bdsm_exhibitions <= 3 and the_person.get_opinion_score("public sex") <= 0: # She's still a bit shy
                the_person.char "Really [mistress.title]? Here in front of everyone? I don't know if I..."
            elif the_person.obedience <= 200:
                the_person.char "Really [mistress.title]? I don't know if I..."
            else:
                the_person.char "I'm [the_person.mc_title]'s slave [mistress.title], and a slave obey."
            $ the_group.set_primary(mistress)
            $ the_group.draw_person(mistress, position = "stand5", emotion = "happy")
            mistress.char "Sit on this chair [the_person.name], I'm going to tie you."
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1 and the_person.get_opinion_score("anal sex") >= 0:
                $ the_group.set_primary(the_person)
                # $ the_group.redraw_group()
                the_person.char "Where should I put the dildo?"
                menu:
                    "Vaginal fun":
                        mistress.char "I think your pussy will be pleased by this toy!"
                        $ the_group.draw_person(the_person, position = "sitting", emotion = "happy")
                        "Her eyes are glued to yours while she slowly slips the big dildo in her pussy."
                    "Anal fun":
                        $ the_person.event_triggers_dict["dildochair_dildos"] = 3
                        mistress.char "I think your lil' asshole will be pleased by this toy!"
                        $ the_group.draw_person(the_person, position = "sitting", emotion = "happy")
                        "Her eyes are glued to yours while she slowly slips the big dildo in her asshole."
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 1:
                $ the_group.set_primary(the_person)
                $ the_group.draw_person(the_person, position = "sitting", emotion = "happy")
                "She obey the Mistress's command and sit."
                "Her eyes are glued to yours while she slowly slips the big dildo in her pussy."
            else:
                $ the_group.set_primary(the_person)
                $ the_group.draw_person(the_person, position = "sitting", emotion = "happy")
                "She obey the Mistress's command and sit."
                "Her eyes are glued to yours while she slowly slips the big dildos in both her holes."
            $ the_group.set_primary(mistress)
            $ the_group.draw_person(mistress, position = "standing_doggy", emotion = "happy")
            "[mistress.possessive_title] lock the belts on her legs, arms, neck and stomach: she can't move anymore."
            $ the_group.set_primary(the_person)
            $ the_group.draw_person(the_person, position = "sitting", emotion = "default")
            the_person.char "Oh my god! I feel..."
            $ the_group.set_primary(mistress)
            $ the_group.draw_person(mistress, position = "standing_doggy", emotion = "happy")
            mistress.char "That your master own you? You're a good slave, and good slaves should be rewarded."
            $ the_group.draw_person(mistress, position = "stand4", emotion = "happy")
            $ the_group.set_primary(the_person)
            $ the_group.draw_person(the_person, position = "sitting", emotion = "happy")
            $ the_person.change_obedience (5)
            "You turn on the chair and set the vibrations at:"
            menu dildochair_Mistress_reward_menu:
                "Speed 1 (tooltip)Slowly increase her arousal" if the_person.energy >= 10: # Each action use 10 energy and give 10 arousal and 1 obedience
                    "A feeble buzz can be heard in the room, [the_person.title] bite her lips."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "Bzzz !... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Oh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (1, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "It's a pleasant feeling: this thing tickle my pussy very nicely!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "It's a pleasant feeling: both my holes tickled so nicely!"
                    else: # One dildo in the ass
                        the_person.char "It's a pleasant feeling: this thing tickle my ass very nicely!"
                    $ the_person.change_obedience (1, add_to_log = False)
                    if the_person.arousal >= 100:
                        $ the_group.draw_person(the_person, position = "sitting", emotion = "orgasm")
                        the_person.char "Oh my god, I'm cumming....Ahhh....YES!....please [the_person.mc_title], increase the speed!"
                        $ the_person.arousal //= 2
                        $ the_person.change_slut_temp (10)
                        $ mistress.change_slut_temp (3)
                    "You decide what to do next."
                    jump dildochair_Mistress_reward_menu
                "Speed 1\n{color=#ff0000}{size=18}Requires at least 10 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 10:
                    pass
                "Speed 2 (tooltip)Moderately increase her arousal" if the_person.energy >= 10: # Each action use 10 energy and give 20 arousal and 2 obedience
                    "A soft buzz can be heard in the room, [the_person.title] bite her lips moaning."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZzz !!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (2, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "It's a good feeling: this thing fills my pussy very nicely!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "It's a good feeling: both my holes filled so nicely!"
                    else: # One dildo in the ass
                        the_person.char "It's a good feeling: this thing fills my ass very nicely!"
                    $ the_person.change_obedience (2, add_to_log = False)
                    if the_person.arousal >= 100:
                        $ the_group.draw_person(the_person, position = "sitting", emotion = "orgasm")
                        the_person.char "Oh my god, I'm cumming....Aahhh....YES!....please [the_person.mc_title], increase the speed!"
                        $ the_person.arousal //= 2
                        $ the_person.change_slut_temp (10)
                        $ mistress.change_slut_temp (3)
                    "You decide what to do next."
                    jump dildochair_Mistress_reward_menu
                "Speed 2\n{color=#ff0000}{size=18}Requires at least 10 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 10:
                    pass
                "Speed 3 (tooltip)Strongly increase her arousal" if the_person.energy >= 10: # Each action use 10 energy and give 30 arousal and 3 obedience
                    "A buzz can be heard in the room, [the_person.title] bite her lips moaning loudly."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZZz !!!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (3, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "Ahh! This feeling is amazing: this cock fills my pussy so good!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "Ahh! This feeling is amazing: both my holes filled so good!"
                    else: # One dildo in the ass
                        the_person.char "Ahh! This feeling is amazing: this cock fills my ass so good!"
                    $ the_person.change_obedience (3, add_to_log = False)
                    if the_person.arousal >= 100:
                        $ the_group.draw_person(the_person, position = "sitting", emotion = "orgasm")
                        the_person.char "Oh my god, I'm cumming....Aaahhh....YES!....please [the_person.mc_title], increase the speed!"
                        $ the_person.arousal //= 2
                        $ the_person.change_slut_temp (10)
                        $ mistress.change_slut_temp (3)
                    "You decide what to do next."
                    jump dildochair_Mistress_reward_menu
                "Speed 3\n{color=#ff0000}{size=18}Requires at least 10 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 10:
                    pass
                "Max speed (tooltip)Extremely increase her arousal" if the_person.energy >= 10: # Each action use 10 energy and give 40 arousal and 4 obedience
                    "A loud buzz can be heard in the room, [the_person.title]'s tongue is out and begs to lick something!"
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZZZ !!!!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (4, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "YES! YES! YES! Fill my pussy this way! More! Give me more!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "YES! YES! YES! Fill my holes this way! More! Give me more!"
                    else: # One dildo in the ass
                        the_person.char "YES! YES! YES! Fill my ass this way! More! Give me more!"
                    $ the_person.change_obedience (4, add_to_log = False)
                    if the_person.arousal >= 100:
                        $ the_group.draw_person(the_person, position = "sitting", emotion = "orgasm")
                        the_person.char "Oh my god, I'm cumming so hard! ....Aaaahhh ....YES! ....please [the_person.mc_title], don't stop, give me more!"
                        $ the_person.arousal //= 2
                        $ the_person.change_slut_temp (10)
                        $ mistress.change_slut_temp (3)
                    "You decide what to do next."
                    jump dildochair_Mistress_reward_menu
                "Max speed\n{color=#ff0000}{size=18}Requires at least 10 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 10:
                    pass
                "Release her" if the_person.energy < 10:
                    $ the_person.arousal == 0
                    mc.name "Please [mistress.title], untie [the_person.title]... I think she can't resist anymore."
                    $ the_group.set_primary(mistress)
                    $ the_group.draw_person(mistress, position = "standing_doggy", emotion = "happy")
                    mistress.char "Sure thing, Master !"
                    $ the_group.draw_person(mistress, position = "stand4", emotion = "happy")
                    $ the_group.set_primary(the_person)
                    $ the_group.draw_person(the_person, position = "stand5", emotion = "happy")
                    "She still can't properly stand on her trembling, after-orgasm, legs."
                    the_person.char "I'm exhausted, but it was worth every second: thank you Master for granting your slave this much pleasure!"
                    mc.name "Please me and you'll be pleased. Now you can get dressed."
                    $ the_person.apply_planned_outfit()
                    $ the_group.draw_person(the_person, position = "stand3", emotion = "happy")
                    $ the_person.change_stats(obedience = 20, slut_temp = 10, slut_core = 2, happiness = 10, love = 2)
                    $ mistress.change_stats(obedience = 3, slut_temp = 10, slut_core = 2)
                    $ increase_bdsm_exhibitions(the_person)
                    "Her eyes are full of love for her Master."
            $ clear_scene()
            if time_of_day == 4:
                call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_Mistress_1
            else:
                call advance_time from _call_advance_strip_club_bdsm_dildochair_Mistress_11
            return # jump game_loop ???

        "Punish her (tooltip)Prevent her to orgasm":
            mc.name "Since you've not been a good slave [the_person.title], you will be pleased but you're not allowed to orgasm."
            $ the_person.draw_person(emotion = "sad", position = "stand4")
            if get_bdsm_exhibitions <= 3 and the_person.get_opinion_score("public sex") <= 0: # She's still a bit shy
                the_person.char "Really [the_person.mc_title]? Here in front of everyone? I don't know if I..."
            elif the_person.obedience <= 200:
                the_person.char "Really [the_person.mc_title]? I don't know if I..."
            else:
                the_person.char "I'm [the_person.mc_title]'s slave [mistress.title], and a slave obey."
            $ the_group.set_primary(mistress)
            $ the_group.draw_person(mistress, position = "stand5", emotion = "happy")
            mistress.char "Sit on this chair [the_person.name], I'm going to tie you."
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1 and the_person.get_opinion_score("anal sex") >= 0:
                the_person.char "Where should I put the dildo?"
                menu:
                    "Vaginal fun":
                        mistress.char "I think your pussy will be pleased by this toy!"
                        $ the_group.draw_person(the_person, position = "sitting", emotion = "sad")
                        "Her eyes are glued to yours while she slowly slips the big dildo in her pussy."
                    "Anal fun":
                        $ the_person.event_triggers_dict["dildochair_dildos"] = 3
                        mistress.char "I think your lil' asshole will be pleased by this toy!"
                        $ the_group.draw_person(the_person, position = "sitting", emotion = "sad")
                        "Her eyes are glued to yours while she slowly slips the big dildo in her asshole."
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 1:
                $ the_group.set_primary(the_person)
                $ the_group.draw_person(the_person, position = "sitting", emotion = "sad")
                "She obey the Mistress's command and sit."
                "Her eyes are glued to yours while she slowly slips the big dildo in her pussy."
            else:
                $ the_group.set_primary(the_person)
                $ the_group.draw_person(the_person, position = "sitting", emotion = "happy")
                "She obey the Mistress's command and sit."
                "Her eyes are glued to yours while she slowly slips the big dildos in both her holes."
            $ the_group.set_primary(mistress)
            $ the_group.draw_person(mistress, position = "standing_doggy", emotion = "happy")
            "[mistress.possessive_title] lock the belts on her legs, arms, neck and stomach: she can't move anymore."
            $ the_group.set_primary(the_person)
            $ the_group.draw_person(the_person, position = "sitting", emotion = "default")
            the_person.char "Oh my god! I feel..."
            $ the_group.set_primary(mistress)
            $ the_group.draw_person(mistress, position = "standing_doggy", emotion = "happy")
            mistress.char "That your master own you? You're a bad slave, and bad slaves should be punished."
            $ the_group.draw_person(mistress, position = "stand4", emotion = "happy")
            $ the_group.set_primary(the_person)
            $ the_group.draw_person(the_person, position = "sitting", emotion = "sad")
            $ the_person.change_obedience (5)
            "You turn on the chair and set the vibrations at:"
            menu dildochair_Mistress_punish_menu:
                "Speed 1 (tooltip)Slowly increase her arousal" if the_person.energy >= 10 and the_person.arousal <= 89: # Each action use 10 energy and give 10 arousal and 1 obedience
                    "A feeble buzz can be heard in the room, [the_person.title] bite her lips."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "Bzzz !... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Oh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (1, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "It's a pleasant feeling: this thing tickle my pussy very nicely!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "It's a pleasant feeling: both my holes tickled so nicely!"
                    else: # One dildo in the ass
                        the_person.char "It's a pleasant feeling: this thing tickle my ass very nicely!"
                    $ the_person.change_obedience (1, add_to_log = False)
                    if the_person.arousal >= 70:
                        the_person.char "Please [the_person.mc_title], I promise I will be the best slave of your! Please, let me cum!"
                    "You decide what to do next."
                    jump dildochair_Mistress_punish_menu
                "Speed 1\n{color=#ff0000}{size=18}She will orgasm!{/size}{/color} (disabled)" if the_person.arousal >= 90:
                    pass
                "Speed 2 (tooltip)Moderately increase her arousal" if the_person.energy >= 10 and the_person.arousal <= 79: # Each action use 10 energy and give 20 arousal and 2 obedience
                    "A soft buzz can be heard in the room, [the_person.title] bite her lips moaning."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZzz !!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (2, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "It's a good feeling: this thing fills my pussy very nicely!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "It's a good feeling: both my holes filled so nicely!"
                    else: # One dildo in the ass
                        the_person.char "It's a good feeling: this thing fills my ass very nicely!"
                    $ the_person.change_obedience (2, add_to_log = False)
                    if the_person.arousal >= 70:
                        the_person.char "Please [the_person.mc_title], I promise I will be the best slave of your! Please, let me cum!"
                    "You decide what to do next."
                    jump dildochair_Mistress_punish_menu
                "Speed 2\n{color=#ff0000}{size=18}She will orgasm!{/size}{/color} (disabled)" if the_person.arousal >= 80:
                    pass
                "Speed 3 (tooltip)Strongly increase her arousal" if the_person.energy >= 10 and the_person.arousal <= 69: # Each action use 10 energy and give 30 arousal and 3 obedience
                    "A buzz can be heard in the room, [the_person.title] bite her lips moaning loudly."
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZZz !!!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (3, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "Ahh! This feeling is amazing: this cock fills my pussy so good!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "Ahh! This feeling is amazing: both my holes filled so good!"
                    else: # One dildo in the ass
                        the_person.char "Ahh! This feeling is amazing: this cock fills my ass so good!"
                    $ the_person.change_obedience (3, add_to_log = False)
                    if the_person.arousal >= 70:
                        the_person.char "Please [the_person.mc_title], I promise I will be the best slave of your! Please, let me cum!"
                    "You decide what to do next."
                    jump dildochair_Mistress_punish_menu
                "Speed 3\n{color=#ff0000}{size=18}She will orgasm!{/size}{/color} (disabled)" if the_person.arousal >= 70:
                    pass
                "Max speed (tooltip)Extremely increase her arousal" if the_person.energy >= 10 and the_person.arousal <= 59: # Each action use 10 energy and give 40 arousal and 4 obedience
                    "A loud buzz can be heard in the room, [the_person.title]'s tongue is out and begs to lick something!"
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZZZ !!!!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (4, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "YES! YES! YES! Fill my pussy this way! More! Give me more!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "YES! YES! YES! Fill my holes this way! More! Give me more!"
                    else: # One dildo in the ass
                        the_person.char "YES! YES! YES! Fill my ass this way! More! Give me more!"
                    $ the_person.change_obedience (4, add_to_log = False)
                    if the_person.arousal >= 70:
                        the_person.char "Please [the_person.mc_title], I promise I will be the best slave of your! Please, let me cum!"
                    "You decide what to do next."
                    jump dildochair_Mistress_punish_menu
                "Max speed\n{color=#ff0000}{size=18}She will orgasm!{/size}{/color} (disabled)" if the_person.arousal >= 60:
                    pass
                "Change your mind (tooltip)Change your mind and let her cum." if the_person.energy >=10 and the_person.arousal >= 80:
                    "You decide to let her finally cum: the chair is set now at the maximum speed."
                    "A loud buzz can be heard in the room, [the_person.title]'s tongue is out and begs to lick something!"
                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, "BZZZ !!!!... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Ohh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal (4, add_to_log = False)
                            the_person.change_energy (-1, add_to_log = False)
                            renpy.pause(1)
                    if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                        the_person.char "YES! YES! YES! Fill my pussy this way! More! Give me more!"
                    elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                        the_person.char "YES! YES! YES! Fill my holes this way! More! Give me more!"
                    else: # One dildo in the ass
                        the_person.char "YES! YES! YES! Fill my ass this way! More! Give me more!"
                    $ the_group.draw_person(the_person, position = "sitting", emotion = "orgasm")
                    "She finally reached her coveted orgasm: the chair is now wet for her flooding juices."
                    $ the_person.arousal == 0
                    mc.name "Please [mistress.title], untie [the_person.title]... I think she can't resist anymore."
                    $ the_group.set_primary(mistress)
                    $ the_group.draw_person(mistress, position = "standing_doggy", emotion = "happy")
                    mistress.char "Sure thing, Master !"
                    $ the_group.draw_person(mistress, position = "stand4", emotion = "happy")
                    $ the_group.set_primary(the_person)
                    $ the_group.draw_person(the_person, position = "stand5", emotion = "happy")
                    "She still can't properly stand on her trembling, after-orgasm, legs."
                    the_person.char "Thank you [the_person.mc_title], let me always cum like this and I'll be your devoted slave!"
                    mc.name "Please me and you'll be pleased. Now you can get dressed."
                    $ the_person.apply_planned_outfit()
                    $ the_group.draw_person(the_person, position = "stand3", emotion = "happy")
                    $ the_person.change_stats(obedience = 20, slut_temp = 10, slut_core = 2, happiness = 10, love = 2)
                    $ mistress.change_stats(obedience = 3, slut_temp = 5, slut_core = 2)
                    $ increase_bdsm_exhibitions(the_person)
                    $ clear_scene()
                    if time_of_day == 4:
                        call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_Mistress_2
                    else:
                        call advance_time from _call_advance_strip_club_bdsm_dildochair_Mistress_21
                    return
                "Release her" if the_person.energy < 10:
                    $ the_person.arousal == 0
                    mc.name "Please [mistress.title], untie [the_person.title]... I think she can't resist anymore."
                    $ the_group.set_primary(mistress)
                    $ the_group.draw_person(mistress, position = "standing_doggy", emotion = "happy")
                    mistress.char "Sure thing, Master !"
                    $ the_group.draw_person(mistress, position = "stand4", emotion = "happy")
                    $ the_group.set_primary(the_person)
                    $ the_group.draw_person(the_person, position = "stand5", emotion = "happy")
                    the_person.char "I'm exhausted, but I got your lesson [the_person.mc_title], I promise I'll be your devoted slave."
                    mc.name "Please me and you'll be pleased. Now you can get dressed."
                    $ the_person.apply_planned_outfit()
                    $ the_group.draw_person(the_person, position = "stand3", emotion = "sad")
                    $ the_person.change_stats(obedience = 10, slut_temp = 5, slut_core = 1)
                    $ mistress.change_stats(obedience = 1, slut_temp = 5, slut_core = 1)
                    $ increase_bdsm_exhibitions(the_person)
                    "She's now very displeased of not have satisfied her Master."
                    $ clear_scene()
                    if time_of_day == 4:
                        call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_Mistress_3
                    else:
                        call advance_time from _call_advance_strip_club_bdsm_dildochair_Mistress_31
                    return
                "Release her" if the_person.arousal >= 90:
                    $ the_person.arousal == 0
                    "While you stop the chair she beg you."
                    the_person.char "Please [the_person.mc_title]... Master! Yes, Master... Please, let me cum at least one time!"
                    mc.name "[mistress.title], untie [the_person.title]... I think she got enough fun."
                    $ the_group.set_primary(mistress)
                    $ the_group.draw_person(mistress, position = "standing_doggy", emotion = "happy")
                    mistress.char "Sure thing, Master !"
                    $ the_group.draw_person(mistress, position = "stand4", emotion = "happy")
                    $ the_group.set_primary(the_person)
                    $ the_group.draw_person(the_person, position = "stand5", emotion = "sad")
                    mc.name "Please me and you'll be pleased. Now you can get dressed."
                    $ the_person.apply_planned_outfit()
                    $ the_group.draw_person(the_person, position = "stand3", emotion = "sad")
                    $ the_person.change_stats(obedience = 10, slut_temp = 5, slut_core = 1, happiness = -5)
                    $ increase_bdsm_exhibitions(the_person)
                    the_person.char "I promise I'll do my best to please my Master!"
    $ clear_scene()
    if time_of_day == 4:
        call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_Mistress_4
    else:
        call advance_time from _call_advance_strip_club_bdsm_dildochair_Mistress_41
    return
