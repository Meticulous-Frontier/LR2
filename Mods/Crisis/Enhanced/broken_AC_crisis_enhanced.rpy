init 5 python:
    config.label_overrides["broken_AC_crisis_label"] = "broken_AC_crisis_label_enhanced"

    def broken_AC_crisis_get_sluttiest_person():
        person = get_random_from_list(mc.business.p_div.people)
        for girl in mc.business.p_div.people:
            if girl.sluttiness > person.sluttiness:
                person = girl
        return person

    def broken_AC_crisis_update_stats(happiness, obedience):
        for person in mc.business.p_div.people:
            person.change_stats(happiness = happiness, obedience = obedience)
        return

    def broken_AC_crisis_update_sluttiness():
        for person in mc.business.p_div.people:
            person.change_slut(2, add_to_log = False)
        mc.log_event("All Production Staff: +2 Sluttiness","float_text_pink")
        return

    def broken_ac_crisis_strip_other_girls(person, girl):
        for other_girl in [x for x in mc.business.p_div.people if x not in [person, girl]]:
            scene_manager.add_actor(other_girl, display_transform = character_left)
            # only remove clothing, don't show it on screen
            removed_something = scene_manager.strip_actor_outfit_to_max_sluttiness(other_girl, temp_sluttiness_boost = 20)
            if removed_something:
                if other_girl.outfit.tits_visible():
                    other_girl.break_taboo("bare_tits")
                if other_girl.outfit.vagina_visible():
                    other_girl.break_taboo("bare_pussy")
                if (other_girl.outfit.wearing_panties() and not other_girl.outfit.panties_covered()) or (other_girl.outfit.wearing_bra() and not other_girl.outfit.bra_covered()):
                    other_girl.break_taboo("underwear_nudity")
            else:
                scene_manager.update_actor(other_girl, emotion = "sad")
                renpy.say(None, other_girl.title + " glances at the other girls, but decides against taking off some clothes.")
            scene_manager.remove_actor(other_girl)
        return

    def broken_AC_crisis_get_watch_list_menu(person):
        people_list = [x for x in mc.business.p_div.people if not x is person]
        people_list.insert(0, "Watch")
        return people_list

label broken_AC_crisis_label_enhanced():
    $ the_person = broken_AC_crisis_get_sluttiest_person()
    if the_person is None:
        return

    $ scene_manager = Scene()
    "There is a sudden bang in the office, followed by a strange silence. A quick check reveals the air conditioning has died!"
    "The machines running at full speed in the production department kick out a significant amount of heat. Without air condition the temperature quickly rises to uncomfortable levels."
    $ mc.business.p_div.show_background()
    #We're going to use the most slutty girl of the group lead the pack. She'll be the one we pay attention to.
    $ scene_manager.add_actor(the_person)
    if mc.business.p_div.get_person_count() == 1:
        "The air conditioner was under warranty, and a quick call has one of their repair men over in a couple of hours. Until then [the_person.name] wants to know what to do."
    else:
        "The air conditioner was under warranty, and a quick call has one of their repair men over in a couple of hours. Until then, the production staff want to know what to do."

    menu:
        "Take a break":
            "You tell everyone in the production lab to take a break for a few hours while the air conditioning is repaired."
            "The unexpected break raises moral and makes the production staff feel more independent."
            $ broken_AC_crisis_update_stats(5, -2)
            "The repair man shows up early and it turns out to be an easy fix. The lab is soon back up and running."

        "It's not that hot, get back to work!":
            "Nobody's happy working in the heat, but exercising your authority will make your production staff more likely to obey in the future."
            $ broken_AC_crisis_update_stats(-5, 2)
            "The repair man shows up early and it turns out to be an easy fix. The lab is soon back up and running."

        "Tell everyone to strip down and keep working" if casual_uniform_policy.is_active():
            if mc.business.p_div.get_person_count() > 1: #We have more than one person, do a group strip scene.
                mc.name "I know it's uncomfortable in here right now, but we're just going to have to make due."
                mc.name "If anyone feels the need to take something off to get comfortable, I'm lifting the dress code until the air conditioning is fixed."

                $ scene_manager.update_actor(the_person, emotion = "happy")
                if the_person.effective_sluttiness() < 20:
                    the_person "He's got a point girls. Come on, we're all adults here."
                elif the_person.effective_sluttiness() < 60:
                    the_person "He's got a point girls. I'm sure we've all shown a little bit of skin before anyways, right?"
                else:
                    the_person "Let's do it girls! I can't be the only one who loves an excuse to flash her tits, right?"

            else: #There's just one person here, have them strip down.
                $ scene_manager.update_actor(the_person, emotion = "sad")
                mc.name "[the_person.title], I know it's uncomfortable in here right now, but we're going to have to make due."
                mc.name "If you feel like it would help to take something off, I'm lifting the dress code until the air condition is fixed."
                if the_person.effective_sluttiness() < 20:
                    the_person "Taking some of this off would be a lot more comfortable..."
                else:
                    the_person "I might as well. You don't mind seeing a little skin, do you?"

            $ removed_something = scene_manager.strip_actor_outfit_to_max_sluttiness(the_person, temp_sluttiness_boost = 20)

            if removed_something:
                call broken_AC_crisis_break_taboo(the_person) from _call_broken_AC_crisis_break_taboo_the_person
            else:
                "[the_person.possessive_title] fiddles with some of her clothing, then shrugs."
                the_person "I'm not sure I'm comfortable taking any of this off... I'm sure I'll be fine in the heat for a little bit."

            if mc.business.p_div.get_person_count() > 1:
                if removed_something:
                    "The rest of the department follows the lead of [the_person.title], stripping off various amounts of clothing."
                        #Gives you the chance to watch one of the other girls in the department strip.

                    call screen enhanced_main_choice_display(build_menu_items([broken_AC_crisis_get_watch_list_menu(the_person)]))
                    $ girl_choice = _return

                    "You pay special attention to [girl_choice.title] as she follows the lead of [the_person.possessive_title]."

                    $ scene_manager.draw_scene()
                    $ scene_manager.add_actor(girl_choice, display_transform = character_center_flipped)

                    $ removed_something = scene_manager.strip_actor_outfit_to_max_sluttiness(girl_choice, temp_sluttiness_boost = 20)
                    if removed_something:
                        call broken_AC_crisis_break_taboo(girl_choice) from _call_broken_AC_crisis_break_taboo_other_girl
                        $ girl_choice.change_slut(2)
                        if girl_choice.effective_sluttiness() < 40:
                            $ scene_manager.update_actor(girl_choice, emotion = "sad")
                            "[girl_choice.title] definitely saw you watching her as she stripped. She looks at you and blushes slightly and avoids making eye contact."
                        else:
                            $ scene_manager.update_actor(girl_choice, emotion = "happy")
                            $ girl_choice.change_love(2)
                            "[girl_choice.title] definitely saw you watching her as she stripped. She looks at you and gives a quick wink before turning back to [the_person.title]."
                    else:
                        "[girl_choice.title] fiddles with some of her clothing, then shrugs meekly."
                        girl_choice "I'm not sure I'm comfortable taking any of this off... I'm sure I'll be fine in the heat for a little bit."

                    if mc.business.p_div.get_person_count() > 2:
                        "The girls laugh and tease each other as they strip down, and they all seem to be more comfortable with the heat once they are less clothed."
                        "For a while all of the girls work in various states of undress while under your watchful eye."
                        $ broken_ac_crisis_strip_other_girls(the_person, girl_choice)
                        if time_of_day >= 3:
                            "The repair man shows up quickly, and you lead him directly to the AC unit. The problem turns out to be a quick fix, and the production room will be back to a comfortable temperature the next day."
                        else:
                            "The repair man shows up quickly, and you lead him directly to the AC unit. The problem turns out to be a quick fix, and the production room will be back to a comfortable temperature within an hour."

                    $ girl_choice = None
                else:
                    "The other girls exchange glances, and everyone seems decides it's best not to take this too far."
                    "They get back to work fully dressed, and soon the repair man has shown up. The problem turns out to be a quick fix, and production will be back to a comfortable temperature the next day."
            else:
                if removed_something:
                    "[the_person.title] gets back to work. Working in her stripped down attire seems to make her more comfortable with the idea in general."
                    "The repair man shows up early, and you lead him directly to the AC unit. The problem turns out to be a quick fix, and production will be back to a comfortable temperature the next day."
                else:
                    "[the_person.title] gets back to work, still fully clothed."
                    "The repair man shows up early, and you lead him directly to the AC unit. The problem turns out to be a quick fix, and production will be back to a comfortable temperature the next day."

            if removed_something:
                $ broken_AC_crisis_update_sluttiness();

        "Tell everyone to strip down and keep working.\n{color=#ff0000}{size=18}Requires: [casual_uniform_policy.name]{/size}{/color} (disabled)" if not casual_uniform_policy.is_active():
            pass

    $ scene_manager.clear_scene()
    $ clear_scene()
    return

label broken_AC_crisis_break_taboo(the_girl):
    if the_girl.outfit.full_access():
        $ mc.change_locked_clarity(40)
        "Once she's done stripping [the_girl.possessive_title] is practically naked."
        if the_girl.has_taboo(["bare_pussy","bare_tits"]):
            "She makes a vain attempt to keep herself covered with her hands, but soon enough seems to be comfortable being nude in front of you."
            $ the_girl.break_taboo("bare_pussy")
            $ the_girl.break_taboo("bare_tits")
    elif the_girl.outfit.tits_visible():
        $ mc.change_locked_clarity(20)
        "Once she's done stripping [the_girl.possessive_title] has her nice [the_girl.tits] tits out on display."
        if the_girl.has_taboo("bare_tits"):
            if the_girl.has_large_tits():
                "She makes a hopeless attempt to cover her [the_girl.tits_description] with her hands, but comes to the realization it's pointless."
            else:
                "She tries to hide her [the_girl.tits_description] from you with her hands, but quickly realizes how impractical that would be."
            "Soon enough she doesn't even mind having them out."
            $ the_girl.break_taboo("bare_tits")
    elif the_girl.outfit.vagina_visible():
        $ mc.change_locked_clarity(30)
        "Once she's done stripping [the_girl.possessive_title] has her pretty little pussy out on display for everyone."
        if the_girl.has_taboo("bare_pussy"):
            "She tries to hide herself from you with her hand, but quickly realizes how impractical that would be."
            "Soon enough she doesn't seem to mind."
            $ the_girl.break_taboo("bare_pussy")
    else:
        $ mc.change_locked_clarity(10)
        "[the_girl.possessive_title] finishes stripping and looks at back at you."
        if (the_girl.outfit.wearing_panties() and not the_girl.outfit.panties_covered()) or (the_girl.outfit.wearing_bra() and not the_girl.outfit.bra_covered()):
            if the_girl.has_taboo("underwear_nudity"):
                "She seems nervous at first, but quickly gets used to being in her underwear in front of you."
                $ the_girl.break_taboo("underwear_nudity")

    the_girl "Ahh, that's a lot better."
    return
