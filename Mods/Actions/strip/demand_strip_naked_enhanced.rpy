init 5 python:
    config.label_overrides["demand_strip_naked_label"] = "demand_strip_naked_label_enhanced"

    def demand_strip_naked_requirement_enhanced(the_person):
        if the_person.outfit.tits_visible() and the_person.outfit.vagina_visible() and the_person.outfit.tits_available() and the_person.outfit.vagina_available():
            return False
        elif the_person.obedience < 160:
            return "Requires: 160 Obedience"
        else:
            return True
    demand_strip_naked_requirement = demand_strip_naked_requirement_enhanced

label demand_strip_naked_label_enhanced(the_person):
    if mc.location.get_person_count() > 1: #Other people are around
        if the_person.effective_sluttiness(["bare_tits","bare_pussy"]) < (80 - (5*the_person.get_opinion_score("not wearing anything"))): #She's shy and wants to go somewhere private
            "[the_person.possessive_title] looks around nervously, then back at you."
            the_person "But... Here? I don't want to get naked in front of other people."
            menu:
                "Find somewhere private":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're there she starts to strip down immediately."


                "Stay right here" if the_person.obedience >= 170:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    "[the_person.possessive_title] doesn't argue. She just blushes and starts to strip down."

                "Stay right here\n{color=#ff0000}{size=18}Requires: 170 Obedience{/size}{/color} (disabled)" if the_person.obedience < 170:
                    pass
        else:
            "[the_person.possessive_title] nods and starts to enthusiastically strip down."

    else:
        if the_person.effective_sluttiness(["bare_tits","bare_pussy"]) < (80 - (5*the_person.get_opinion_score("not wearing anything"))): #She's shy
            "[the_person.possessive_title] seems uncomfortable, but she nods obediently and starts to pull off all her clothes."
        else:
            the_person "Okay, whatever you want [the_person.mc_title]."
            "She starts to strip down for you."

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

    if the_person.update_outfit_taboos() or the_person.effective_sluttiness() < (80 - (5*the_person.get_opinion_score("not wearing anything"))): # She's shy
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
            if the_person.effective_sluttiness() < (80 - (5*the_person.get_opinion_score("not wearing anything"))):
                the_person "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.change_slut(1, 75)
                $ the_person.change_happiness(-2)
            else:
                the_person "Okay, if that's what you want me to do [the_person.mc_title]."
                "[the_person.title] doesn't seem to mind."
    return