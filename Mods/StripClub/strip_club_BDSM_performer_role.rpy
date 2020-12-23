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

    strip_club_dildochair_MC_action = Action("Use the dildo chair {image=gui/heart/Time_Advance.png}", strip_club_bdsm_dildochair_MC_requirements, "strip_club_bdsm_dildochair_MC_label", menu_tooltip = "Use the dildo chair with your BDSM performer.")
    strip_club_dildochair_Mistress_action = Action("Mistress use the chair {image=gui/heart/Time_Advance.png}", strip_club_bdsm_dildochair_Mistress_requirements, "strip_club_bdsm_dildochair_Mistress_label", menu_tooltip = "Have the Mistress use the dildo chair with your BDSM performer.")

    bdsm_performer_role = Role("BDSM performer", [promote_to_manager_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action, strip_club_dildochair_MC_action, strip_club_dildochair_Mistress_action], hidden = False)

    def strip_club_get_caged():
        caged = people_in_role(caged_role)
        if __builtin__.len(caged) > 0:
            return caged[0]
        return None

    def strip_club_cage_her_requirements(the_person):
        if the_person.has_role(caged_role):
            return False
        if mc.location is bdsm_room:
            caged = people_in_role(caged_role)
            if __builtin__.len(caged) < 2:
                return True
        return False

    def strip_club_caged_strip_requirements(the_person):
        if the_person.outfit.tits_visible() and the_person.outfit.vagina_visible() and the_person.outfit.tits_available() and the_person.outfit.vagina_available():
            return False
        return True

    def strip_club_caged_actions_requirements(the_person):
        if the_person.has_role(caged_role):
            return True
        return False

    def add_strip_club_cage_her_action_to_mc_actions():
        strip_club_cage_her_action = Action("Cage her", strip_club_cage_her_requirements, "cage_her_label", menu_tooltip = "Put [the_person.title] in the cage.")
        mc.main_character_actions.append(strip_club_cage_her_action)

    def strip_club_cage_role_on_turn(person):
        if person.obedience < 200:
            person.obedience += 10

    def strip_club_cage_role_on_move(person):
        person.location().move_person(person, bdsm_room)

    def strip_club_cage_role_on_day(person):
        person.clear_situational_slut("being_caged")
        person.clear_situational_obedience("being_caged")
        person.remove_role(caged_role)
        person.apply_planned_outfit()

    caged_strip_action = Action("Strip her", strip_club_caged_strip_requirements, "caged_strip_label", menu_tooltip = "Strip the caged [the_person.title].")
    caged_get_milked_action = Action("Milk her", strip_club_caged_actions_requirements, "caged_get_milked_label", menu_tooltip = "Milk the caged [the_person.title].")
    caged_BJ_action = Action("Get a BJ from her", strip_club_caged_actions_requirements, "caged_BJ_label", menu_tooltip = "Get a BJ from the caged [the_person.title].")
    caged_doggy_action = Action("Fuck her Doggy style", strip_club_caged_actions_requirements, "caged_doggy_label", menu_tooltip = "Fuck the caged [the_person.title] Doggy style.")
    caged_anal_doggy_action = Action("Fuck her anally", strip_club_caged_actions_requirements, "caged_anal_doggy_label", menu_tooltip = "Anal fuck the caged [the_person.title] Doggy style.")
    caged_release_action = Action("Release [the_person.title] from the cage", strip_club_caged_actions_requirements, "caged_release_label", menu_tooltip = "Release [the_person.title] from the cage.")

    caged_role = Role("CAGED !", [caged_strip_action, caged_BJ_action, caged_doggy_action, caged_anal_doggy_action, caged_release_action], \
        on_turn = strip_club_cage_role_on_turn, on_move = strip_club_cage_role_on_move, on_day = strip_club_cage_role_on_day, hidden = True)

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
    if time_of_day == 4:
        "Tired after you spent the night at the club, you go back home, to have a good nights rest."
        $ mc.change_location(bedroom)
        $ mc.location.show_background()
    call advance_time from _call_advance_time_strip_club_end_of_day
    return

label strip_club_bdsm_dildochair_MC_label(the_person): # MC use the dildo chair with her
    "You decide it's time for [the_person.title] to have some fun, so you approach the chair and set up..."
    menu:
        "One dildo":
            $ the_person.event_triggers_dict["dildochair_dildos"] = 1
        "Two dildos" if the_person.get_opinion_score("anal sex") >= 2:
            $ the_person.event_triggers_dict["dildochair_dildos"] = 2
    mc.name "Ok, [the_person.title]... Get naked and come here!"
    the_person.char "Okay, whatever you want [the_person.mc_title]."
    if mc.location.get_person_count() > 1: # There's other people around
        $ the_person.add_situational_slut("being_chaired", 8, "Everyone can see the slut I am...")
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
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1 and the_person.get_opinion_score("anal sex") >= 2:
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
            mc.name "That your master owns you? You're my good slave, and good slaves should be rewarded."
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
                    "A buzz can be heard in the room, [the_person.title] bites her lips moaning loudly."
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
            $ the_person.clear_situational_slut("being_chaired")
            $ clear_scene()
            call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_MC_1
            return

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
            mc.name "That your master owns you? So that's the right feeling, even if you're not yet a good slave."
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
                    call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_MC_2
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
                    call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_MC_3
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
    call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_MC_4
    return

label strip_club_bdsm_dildochair_Mistress_label(the_person): # The Mistress use the dildo chair with her
    $ mistress = strip_club_get_mistress()
    "You ask [mistress.possessive_title] to set up the dildo chair and have some fun with [the_person.possessive_title]."
    $ the_group = GroupDisplayManager([mistress, the_person], mistress)
    $ the_group.draw_group()
    $ the_group.draw_person(mistress, position = "stand4", emotion = "happy")
    mistress.char "Sure [mistress.mc_title], how many dildos do you want me to install on the chair?"
    menu:
        "One dildo":
            $ the_person.event_triggers_dict["dildochair_dildos"] = 1
        "Two dildos" if the_person.get_opinion_score("anal sex") >= 0:
            $ the_person.event_triggers_dict["dildochair_dildos"] = 2
    mistress.char "Ok, [the_person.name]... Get naked and come here!"
    $ the_group.set_primary(the_person)
    # $ the_group.redraw_group()
    $ the_group.draw_person(the_person, position = "stand3", emotion = "happy")
    if mc.location.get_person_count() > 1: # There's other people around
        $ the_person.add_situational_slut("being_chaired", 8, "Everyone can see the slut I am...")
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
            mistress.char "That your master owns you? You're a good slave, and good slaves should be rewarded."
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
            $ the_person.clear_situational_slut("being_chaired")
            $ clear_scene()
            call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_Mistress_1
            return

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
            mistress.char "That your master owns you? You're a bad slave, and bad slaves should be punished."
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
                    call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_Mistress_2
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
                    "She's very disappointed, not having satisfied her Master."
                    $ clear_scene()
                    call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_Mistress_3
                    return
                "Release her" if the_person.arousal >= 90:
                    $ the_person.arousal == 0
                    "While you stop the chair she begs you."
                    the_person.char "Please [the_person.mc_title]... Master! Yes, Master... Please, let me cum at least one time!"
                    mc.name "[mistress.title], untie [the_person.title]... I think she had enough fun."
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
    call strip_club_end_of_day_label from _call_advance_strip_club_bdsm_dildochair_Mistress_4
    return

label cage_her_label(the_person):
    mc.name "I think a some time in the cage will improve your attitude."
    if the_person.obedience < 100:
        $ the_person.draw_person(position = "stand3", emotion = "angry")
        the_person.char "What? Are you crazy?"
        mc.name "Oh, don't worry [the_person.title], you'll enjoy it!"
        if the_person.sluttiness < 60:
            the_person.char "There's no absolutely way I'll do it... Never in my life!"
            "Maybe I need to work a bit on her obedience or her sluttiness before she'll agree to this..."
            mc.name "Ok [the_person.title], but never say never!"
            return
        else:
            $ the_person.draw_person(position = "stand3", emotion = "sad")
            the_person.char "It's so degrading... Do you promise me it'll be worth it?"
            mc.name "Have you ever been disappointed by your master?"
            "She looks deeply in your eyes, you can see her deepest dirty fantasies invade her mind."
            "Then, without a word, she kneels and enter the cage."
    elif the_person.obedience < 200:
        $ the_person.draw_person(position = "stand3", emotion = "default")
        the_person.char "Are you sure it's really necessary?"
        mc.name "That's what I want from you right now, do you want to disappoint your master?"
        "She know there's no return from this; if she accepts this she will forever be in your power."
        "Then, without a word, she kneels and enter the cage."
    else:
        $ the_person.draw_person(position = "stand3", emotion = "happy")
        the_person.char "As you wish, [the_person.mc_title]."
        "Then she kneels and enter the cage."
    $ the_person.add_role(caged_role)
    $ ran_num = renpy.random.randint(1,3)
    if ran_num == 1:
        $ the_person.draw_person(position = "kneeling1")
        $ the_person.event_triggers_dict["bdsm_room_pose"] = "kneeling1"
    elif ran_num == 2:
        $ the_person.draw_person(position = "blowjob")
        $ the_person.event_triggers_dict["bdsm_room_pose"] = "blowjob"
    else:
        $ the_person.draw_person(position = "cowgirl")
        $ the_person.event_triggers_dict["bdsm_room_pose"] = "cowgirl"
    if not "caged_actions" in the_person.event_triggers_dict:
        $ the_person.event_triggers_dict["caged_actions"] = 0
    if the_person.follow_mc:
        $ the_person.follow_mc = False
    if mc.location.get_person_count() > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    $ the_person.add_situational_obedience("being_caged", 10, "I am completely at his mercy.")
    "She now awaits your next move."
    return

label caged_strip_label(the_person):
    mc.name "I want you to be naked there: remove your clothes."
    if mc.location.get_person_count() > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    $ naked_strip_description(the_person)
    the_person.char "Is my master pleased?"
    $ the_person.event_triggers_dict["caged_actions"] += 1
    return

label caged_get_milked_label(the_person):
    if mc.location.get_person_count() > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    # TODO
    $ the_person.event_triggers_dict["caged_actions"] += 1
    return

label caged_BJ_label(the_person):
    "You unzip your pants and pull out your dick in front of the cage."
    if mc.location.get_person_count() > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    if the_person.get_opinion_score("public sex") >= 0:
        $ the_person.add_situational_slut("being_used_in_the_cage", (the_person.get_opinion_score("public sex")*5 +5), "Everyone can see the slut I am...")
    if the_person.has_role(oral_fetish_role) or the_person.get_opinion_score("giving blowjobs") > 0:
        $ the_person.draw_person(position = "cowgirl", emotion = "happy")
        the_person.char "Oh! I like where this is going!"
    else:
        $ the_person.draw_person(position = "cowgirl", emotion = "default")
        the_person.char "Oh! I think I know what you want..."
        if the_person.obedience >= 150:
            the_person.char "If it's the only way to please my master..."
        else:
            the_person.char "Don't you think it's degrading enough for me to being inside... 'this'?"
            "Your gaze fixed in her eyes, you start a willingness fight: you know the first one who look down loses..."
            "After a few seconds [the_person.title] realize where she is and, aware, looks the tip of your shoes."
            mc.name "My dear slave... Open your mouth, would you?"
    call fuck_person(the_person, private = False, start_position = blowjob, start_object = bdsm_room.get_object_with_name("Cage"), skip_intro = True, girl_in_charge = False, position_locked = True, ignore_taboo = True, affair_ask_after = False) from _call_caged_BJ
    $ the_person.clear_situational_slut("being_used_in_the_cage")
    $ the_person.event_triggers_dict["caged_actions"] += 1
    return

label caged_doggy_label(the_person):
    "The sight of [the_person.title] being so powerless intrigues you."
    "With your hand between the bars you start to caress [the_person.title]'s buttocks."
    if mc.location.get_person_count() > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    if the_person.get_opinion_score("public sex") >= 0:
        $ the_person.add_situational_slut("being_used_in_the_cage", (the_person.get_opinion_score("public sex")*5 +5), "Everyone can see the slut I am...")
    "Meanwhile your finger play with [the_person.title]'s wet pussy, with the other hand you unzip your pants and set your hard dick free."
    if the_person.has_role(vaginal_fetish_role) or the_person.get_opinion_score("doggy style sex") > 0:
        $ the_person.draw_person(position = "doggy", emotion = "happy")
        the_person.char "Oh! I like where this is going!"
    else:
        $ the_person.draw_person(position = "doggy", emotion = "default")
        the_person.char "Oh! I think I know what you want..."
        if the_person.obedience >= 150:
            the_person.char "If it's the only way to please my master..."
        else:
            the_person.char "Don't you think it's degrading enough for me to being inside... 'this'?"
            "Disappointed by her behaviour you slap her pussy and [the_person.title] moans loudly: she can't deny anymore what her body disperately want."
            mc.name "My dear slave... Push your ass closer, would you?"
    call fuck_person(the_person, private = False, start_position = doggy, start_object = bdsm_room.get_object_with_name("Cage"), skip_intro = True, girl_in_charge = False, position_locked = True, ignore_taboo = True, affair_ask_after = False) from _call_caged_doggy
    $ the_person.clear_situational_slut("being_used_in_the_cage")
    $ the_person.event_triggers_dict["caged_actions"] += 1
    return

label caged_anal_doggy_label(the_person):
    "Everyone now can see that [the_person.title] belongs to you... But there is a little something more you can do."
    "With your hand between the bars you start to caress [the_person.title]'s buttocks."
    if mc.location.get_person_count() > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    if the_person.get_opinion_score("public sex") >= 0:
        $ the_person.add_situational_slut("being_used_in_the_cage", (the_person.get_opinion_score("public sex")*5 +5), "Everyone can see the slut I am...")
    "Meanwhile your finger circle [the_person.title]'s asshole, with the other hand you unzip your pants and set your hard dick free."
    if the_person.has_role(anal_fetish_role) or the_person.get_opinion_score("anal sex") > 0:
        $ the_person.draw_person(position = "doggy", emotion = "happy")
        the_person.char "Oh! I like where this is going!"
    else:
        $ the_person.draw_person(position = "doggy", emotion = "default")
        the_person.char "Oh! I think I know what you want..."
        if the_person.obedience >= 150:
            the_person.char "If it's the only way to please my master..."
        else:
            the_person.char "Don't you think it's degrading enough for me, being inside... 'this'?"
            "Disappointed by her behaviour, you finger her asshole and [the_person.title] moans loudly, she can't deny anymore what her body disparately wants."
            mc.name "My dear slave... Spread your cheeks, would you?"
    call fuck_person(the_person, private = False, start_position = doggy_anal, start_object = bdsm_room.get_object_with_name("Cage"), skip_intro = True, girl_in_charge = False, position_locked = True, ignore_taboo = True, affair_ask_after = False) from _call_caged_doggy_anal
    $ the_person.clear_situational_slut("being_used_in_the_cage")
    $ the_person.event_triggers_dict["caged_actions"] += 1
    return

label caged_release_label(the_person):
    mc.name "You can leave the cage now."
    $ the_person.clear_situational_slut("being_caged")
    $ the_person.clear_situational_obedience("being_caged")
    $ the_person.remove_role(caged_role)
    $ the_person.draw_person(position = "stand3", emotion = "happy")
    if the_person.event_triggers_dict.get("caged_actions") <= 2:
        if the_person.obedience <= 150:
            the_person.char "I hope you got me out just to have some more fun with me!"
        else:
            the_person.char "I hope my performance has pleased my master."
    else:
        if the_person.obedience <= 150:
            the_person.char "Actually I was starting to enjoy the place!"
        else:
            the_person.char "I'm happy my master played with me!"
    $ the_person.apply_planned_outfit()
    return
