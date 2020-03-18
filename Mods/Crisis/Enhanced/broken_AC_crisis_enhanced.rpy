init 5 python:
    config.label_overrides["broken_AC_crisis_label"] = "broken_AC_crisis_label_enhanced"

    def broken_AC_crisis_get_sluttiest_person():
        person = get_random_from_list(mc.business.production_team)
        for girl in mc.business.production_team:
            if girl.sluttiness > person.sluttiness:
                person = girl
        return person

    def broken_AC_crisis_update_stats(happiness, obedience):
        for person in mc.business.production_team:
            person.change_happiness(happiness)
            person.change_obedience(obedience)
        return

    def broken_AC_crisis_update_sluttiness():
        for person in mc.business.production_team:
            person.change_slut_temp(10, add_to_log = False)
        mc.log_event("All Production Staff: +10 Sluttiness","float_text_pink")
        return

    def broken_ac_crisis_strip_other_girls(person, girl):
        for other_girl in [x for x in mc.business.production_team if x not in [person, girl]]:
            test_outfit = other_girl.outfit.get_copy()
            clothing = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True) #Remove something from our test outfit.
            while clothing and other_girl.judge_outfit(test_outfit, 20): #This will loop over and over until she is out of things to remove OR nolonger can strip something that is appropriate.
                other_girl.outfit.remove_clothing(clothing)
                clothing = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True)
        return

    def broken_AC_crisis_strip_outfit(person):
        test_outfit = person.outfit.get_copy()
        removed_something = False

        clothing = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True) #Remove something from our test outfit.
        while clothing and person.judge_outfit(test_outfit, 20): #This will loop over and over until she is out of things to remove OR nolonger can strip something that is appropriate.
            #Note: there can be some variation in this event depending on if the upper or lower was randomly checked first.
            person.draw_animated_removal(clothing) #Draw the item being removed from our current outfit
            #$ person.outfit = test_outfit.get_copy() #Swap our current outfit out for the test outfit. Changed in v0.24.1
            person.apply_outfit(test_outfit, ignore_base = True, update_taboo = False) #Swap our current outfit out for the test outfit, apply any taboo effects that happen as a result.
            ran_num = renpy.random.randint(0,4)
            if ran_num == 0 or not removed_something:
                renpy.say("", person.title + " pulls off her " + clothing.name + " and puts it aside.") #Always called first.
            elif ran_num == 1:
                renpy.say("", person.title + " takes off her " + clothing.name + " and adds it to the pile of clothing.")
            elif ran_num == 2:
                renpy.say("", person.title + " strips off her " + clothing.name + " and tosses it to the side.")
            elif ran_num == 3:
                renpy.say("", person.title + " removes her " + clothing.name + " and tosses it with the rest of her stuff.")
            else: # ran_num == 4:
                renpy.say("", person.title + " quickly slides off her " + clothing.name + " and leaves it on the ground.")
            removed_something = True
            clothing = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True)
        return removed_something

label broken_AC_crisis_label_enhanced:
    $ the_person = broken_AC_crisis_get_sluttiest_person()
    if the_person is None:
        return

    "There is a sudden bang in the office, followed by a strange silence. A quick check reveals the air conditioning has died!"
    "The machines running at full speed in the production department kick out a significant amount of heat. Without air condition the temperature quickly rises to uncomfortable levels."
    $ mc.business.p_div.show_background()
    #We're going to use the most slutty girl of the group lead the pack. She'll be the one we pay attention to.
    $ the_person.draw_person()
    if len(mc.business.production_team) == 0:
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

        "Tell everyone to strip down and keep working" if casual_uniform_policy.is_owned():
            if len(mc.business.production_team) > 1: #We have more than one person, do a group strip scene.
                mc.name "I know it's uncomfortable in here right now, but we're just going to have to make due."
                mc.name "If anyone feels the need to take something off to get comfortable, I'm lifting the dress code until the air conditioning is fixed."

                if the_person.effective_sluttiness() < 20:
                    the_person.char "He's got a point girls. Come on, we're all adults here."
                elif the_person.effective_sluttiness() < 60:
                    the_person.char "He's got a point girls. I'm sure we've all shown a little bit of skin before anyways, right?"
                else:
                    the_person.char "Let's do it girls! I can't be the only one who loves an excuse to flash her tits, right?"

            else: #There's just one person here, have them strip down.
                $ the_person.draw_person()
                mc.name "[the_person.title], I know it's uncomfortable in here right now, but we're going to have to make due."
                mc.name "If you feel like it would help to take something off, I'm lifting the dress code until the air condition is fixed."
                if the_person.effective_sluttiness() < 20:
                    the_person.char "Taking some of this off would be a lot more comfortable..."
                else:
                    the_person.char "I might as well. You don't mind seeing a little skin, do you?"

            $ removed_something = broken_AC_crisis_strip_outfit(the_person)
            if removed_something:
                call broken_AC_crisis_break_taboo(the_person) from _call_broken_AC_crisis_break_taboo_the_person
            else:
                "[the_person.possessive_title] fiddles with some of her clothing, then shrugs."
                the_person.char "I'm not sure I'm comfortable taking any of this off... I'm sure I'll be fine in the heat for a little bit."

            if len(mc.business.production_team) > 1:
                if removed_something:
                    "The rest of the department follows the lead of [the_person.title], stripping off various amounts of clothing."
                        #Gives you the chance to watch one of the other girls in the department strip.
                    
                    if "build_menu_items" in globals():
                        call screen main_choice_display(build_menu_items([broken_AC_crisis_get_watch_list_menu(the_person)]))
                    else:
                        call screen main_choice_display([broken_AC_crisis_get_watch_list_menu(the_person)])

                    $ girl_choice = _return

                    "You pay special attention to [girl_choice.title] as she follows the lead of [the_person.possessive_title]."

                    $ removed_something = broken_AC_crisis_strip_outfit(girl_choice)
                    if removed_something:
                        call broken_AC_crisis_break_taboo(girl_choice) from _call_broken_AC_crisis_break_taboo_other_girl
                        $ slut_report = girl_choice.change_slut_temp(10)
                        if girl_choice.effective_sluttiness() < 40:
                            "[girl_choice.title] definitely saw you watching her as she stripped. She looks at you and blushes slightly and avoids making eye contact."
                        else:
                            $ girl_choice.change_love(2)
                            "[girl_choice.title] definitely saw you watching her as she stripped. She looks at you and gives a quick wink before turning back to [the_person.title]."
                    else:
                        "[girl_choice.title] fiddles with some of her clothing, then shrugs meekly."
                        girl_choice.char "I'm not sure I'm comfortable taking any of this off... I'm sure I'll be fine in the heat for a little bit."

                    $ broken_ac_crisis_strip_other_girls(the_person, girl_choice)
                    $ girl_choice = None
                    "The girls laugh and tease each other as they strip down, and they all seem to be more comfortable with the heat once they are less clothed."
                    "For a while all of the girls work in various states of undress while under your watchful eye."
                    "The repair man shows up early, and you lead him directly to the the AC unit. The problem turns out to be a quick fix, and production is back to a comfortable temperature within a couple of hours."
                else:
                    "The other girls exchange glances, and everyone seems decides it's best not to take this too far."
                    "They get back to work fully dressed, and soon the repair man has shown up. The problem turns out to be a quick fix, and production is back to a comfortable temperature within a couple of hours."
            else:
                if removed_something:
                    "[the_person.title] gets back to work. Working in her stripped down attire seems to make her more comfortable with the idea in general."
                    "The repair man shows up early, and you lead him directly to the AC unit. The problem turns out to be a quick fix, and production is back to a comfortable temperature within a couple of hours."
                else:
                    "[the_person.title] gets back to work, still fully clothed."
                    "The repair man shows up early, and you lead him directly to the the AC unit. The problem turns out to be a quick fix, and production is back to a comfortable temperature within a couple of hours."

            if removed_something:
                $ broken_AC_crisis_update_sluttiness();

        "Tell everyone to strip down and keep working.\n{color=#ff0000}{size=22}Requires: [casual_uniform_policy.name]{/color} (disabled)" if not casual_uniform_policy.is_owned():
            pass
    $renpy.scene("Active")
    return

label broken_AC_crisis_break_taboo(the_girl):
    if the_girl.outfit.tits_visible() and the_girl.outfit.vagina_visible():
        "Once she's done stripping [the_girl.possessive_title] is practically naked."
        if the_girl.has_taboo(["bare_pussy","bare_tits"]):
            "She makes a vain attempt to keep herself covered with her hands, but soon enough seems to be comfortable being nude in front of you."
            $ the_girl.break_taboo("bare_pussy")
            $ the_girl.break_taboo("bare_tits")
    elif the_girl.outfit.tits_visible():
        "Once she's done stripping [the_girl.possessive_title] has her nice [the_girl.tits] tits out on display."
        if the_girl.has_taboo("bare_tits"):
            if the_girl.has_large_tits():
                "She makes a hopeless attempt to cover her large tits with her hands, but comes to the realization it's pointless."
            else:
                "She tries to hide her tits from you with her hands, but quickly realizes how impractical that would be."
            "Soon enough she doesn't even mind having them out."
            $ the_girl.break_taboo("bare_tits")
    elif the_girl.outfit.vagina_visible():
        "Once she's done stripping [the_girl.possessive_title] has her pretty little pussy out on display for everyone."
        if the_girl.has_taboo("bare_pussy"):
            "She tries to hide herself from you with her hand, but quickly realizes how impractical that would be."
            "Soon enough she doesn't seem to mind."
            $ the_girl.break_taboo("bare_pussy")
    else:
        "[the_girl.possessive_title] finishes stripping and looks at back at you."
        if (the_girl.outfit.wearing_panties() and not the_girl.outfit.panties_covered()) or (the_girl.outfit.wearing_bra() and not the_girl.outfit.bra_covered()):
            if the_girl.has_taboo("underwear_nudity"):
                "She seems nervous at first, but quickly gets use to being in her underwear in front of you."
                $ the_girl.break_taboo("underwear_nudity")

    the_girl.char "Ahh, that's a lot better."
    return