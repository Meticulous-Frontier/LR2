init 5 python:
    config.label_overrides["demand_strip_naked_label"] = "demand_strip_naked_label_enhanced"

    def demand_strip_naked_requirement_enhanced(the_person):
        if the_person.outfit.tits_visible() and the_person.outfit.vagina_visible() and the_person.outfit.tits_available() and the_person.outfit.vagina_available():
            return False
        if the_person.obedience < 150:
            return "Requires: 150 Obedience"
        return True

    demand_strip_naked_requirement = demand_strip_naked_requirement_enhanced

label demand_strip_naked_label_enhanced(the_person):
    $ mc.change_energy(-5)
    mc.name "You're going to strip naked for me."

    $ test_outfit = Outfit("Nude") # Doesn't include accessories. Don't actually apply this outfit.
    $ willing_private = demand_strip_judge_private(the_person, test_outfit, "not wearing anything")
    $ willing_public = demand_strip_judge_public(the_person, test_outfit, "not wearing anything")

    $ the_person.discover_opinion("not wearing anything")

    if mc.location.get_person_count() > 1: #Other people are around
        if willing_public: #She's into it
            "[the_person.possessive_title] nods and starts to enthusiastically strip down."
            call .start_stripping() from _demand_strip_naked_willing_public
            return

        "[the_person.possessive_title] looks around nervously, then back at you."
        $ obedience_requirement = demand_strip_get_obedience_req(the_person, test_outfit, min = 130)
        if willing_private:
            the_person "But... Here? I don't want to get naked in front of other people."
            menu:
                "Find somewhere private":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're there she starts to strip down immediately."
                    call .start_stripping(private = True) from _demand_strip_naked_move_to_private
                    return

                "Stay right here" if the_person.obedience >= 170:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title] doesn't argue. She just blushes and starts to strip down."
                    call .start_stripping(ordered = True) from _demand_strip_naked_stay_in_public
                    return

                "Stay right here\n{color=#ff0000}{size=18}Requires: 170 Obedience{/size}{/color} (disabled)" if the_person.obedience < 170:
                    pass

                "Never mind":
                    mc.name "Never mind. Let's do something else."
                    $ the_person.change_stats(obedience = -1)
                    return

        elif the_person.obedience >= obedience_requirement - 20: # She doesn't even want to do it in private
            the_person "Do... do I have to?"
            menu:
                "That's an order" if the_person.obedience >= obedience_requirement:
                    mc.name "Of course you do. I {i}want{/i} you to."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title] stops arguing and resignedly starts to pull off her clothes."
                    call .start_stripping(ordered = True) from _demand_strip_naked_ordered_public
                    return

                "That's an order\n{color=#ff0000}{size=18}Requires: [obedience_requirement] Obedience{/size}{/color} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Of course you don't. I just thought it'd be fun. Let's do something else."
                    $ the_person.change_stats(obedience = -1)
                    return
        else:
            $ the_person.change_stats(obedience = -1)
            the_person "I don't think I will. My clothes stay on for now."
            mc.name "For now?"
            "[the_person.title] smirks and changes the subject."
            return

    else: #You are alone
        if willing_private: #She's into it.
            the_person "Okay, whatever you want [the_person.mc_title]."
            "She starts to strip down for you."
            call .start_stripping(private = True) from _demand_strip_naked_willing_private
            return

        $ obedience_requirement = demand_strip_get_obedience_req(the_person, test_outfit, min = 130, private = True)
        if the_person.obedience >= obedience_requirement - 20:
            "[the_person.possessive_title] seems uncomfortable at your request."
            the_person "Do... do I have to?"
            menu:
                "That's an order" if the_person.obedience >= obedience_requirement:
                    mc.name "Of course you do. I {i}want{/i} you to."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title] stops arguing and resignedly starts to pull off her clothes."
                    call .start_stripping(private = True, ordered = True) from _demand_strip_naked_ordered_private
                    return

                "That's an order\n{color=#ff0000}{size=18}Requires: [obedience_requirement] Obedience{/size}{/color} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Of course you don't. I just thought it'd be fun. Let's do something else."
                    $ the_person.change_stats(obedience = -1)
                    return
        else:
            $ the_person.change_stats(obedience = -1)
            the_person "I don't think I will. My clothes stay on for now."
            mc.name "For now?"
            "[the_person.title] smirks and changes the subject."
            return
    return

label .start_stripping(private = False, ordered = False):
    $ remove_shoes = False
    $ the_item = the_person.outfit.get_feet_top_layer()
    if the_item:
        the_person "Do you want me to keep my [the_item.display_name] on?"
        menu:
            "Strip it all off":
                mc.name "Take it all off, I don't want you to be wearing anything."
                $ remove_shoes = True
            "Leave them on":
                mc.name "You can leave them on."
    $ del the_item

    $ generalised_strip_description(the_person, the_person.outfit.get_full_strip_list(strip_feet = remove_shoes))

    $ person_is_shy = not the_person.judge_outfit(the_person.outfit, temp_sluttiness_boost = 5 * the_person.get_opinion_score("not wearing anything"))

    if the_person.update_outfit_taboos() or person_is_shy: # She's shy
        the_person "What would you like me to do now?"
        "She instinctively puts her hands behind her back while she waits for your instructions."
        $ mc.change_locked_clarity(20)
        mc.name "Give me a spin, I want to see your ass."
        "She blushes, but nods and turns around."
        $ the_person.draw_person(position = "back_peek")
        "[the_person.possessive_title] waits patiently until you signal for her to turn around again."
        $ the_person.draw_person()
        the_person "Are we finished? Is that all?"

    else:
        $ mc.change_locked_clarity(20)
        "[the_person.title] puts her hands behind her back and pushes her chest forward, accentuating her tits."
        "She waits silently for you to tell her what to do. You notice her nipples harden as you watch her."
        mc.name "Do you like this?"
        #TODO: THis should probably include dialogue based on their being naked opinions.
        the_person "If I'm doing it for you I do."
        mc.name "Good. Turn around, I want to see your ass."
        $ mc.change_locked_clarity(20)
        "She nods happily and turns around, wiggling her butt for you."
        $ the_person.draw_person(position = "back_peek")
        "You enjoy the view until you're satisfied."
        mc.name "Okay, turn around again."
        $ the_person.draw_person()
        the_person "Is there anything else, [the_person.mc_title]?"

    menu:
        "Let her get dressed":
            mc.name "I've seen enough. You can get dressed."
            "You watch her as she gets dressed again."
            $ the_person.apply_outfit()
            $ the_person.draw_person()

        "Keep her naked":
            mc.name "Your body is way too nice looking to hide away. Stay like this for a while."
            if willing_public:
                the_person "Okay, if that's what you want me to do [the_person.mc_title]."
                "[the_person.title] doesn't seem to mind."
                $ the_person.planned_outfit = the_person.outfit.get_copy()
            elif the_person.obedience >= demand_strip_get_obedience_req(the_person, test_outfit, min = 150):
                the_person "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.change_stats(obedience = 1, slut = 1, max_slut = 75, happiness = -2)
                $ the_person.planned_outfit = the_person.outfit.get_copy()
            else:
                the_person "Very funny. I'm not about to go out like this."
                "She starts putting her clothes back on."
                $ the_person.change_stats(obedience = -1, love = -1)
                $ the_person.apply_outfit()
                $ the_person.draw_person()
    return
