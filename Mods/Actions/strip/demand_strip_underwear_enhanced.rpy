init 5 python:
    config.label_overrides["demand_strip_underwear_label"] = "demand_strip_underwear_label_enhanced"
    
    def demand_strip_underwear_requirement_enhanced(the_person):
        if the_person.outfit.tits_visible() and the_person.outfit.vagina_visible():
            return False #Can't strip if we're already past underwear
        elif the_person.outfit.wearing_panties() and not the_person.outfit.panties_covered() and the_person.outfit.wearing_bra() and not the_person.outfit.bra_covered():
            return False #Can't strip if we can already see all of her underwear.
        elif the_person.obedience < 130:
            return "Requires: 130 Obedience"
        else:
            return True
    demand_strip_underwear_requirement = demand_strip_underwear_requirement_enhanced

label demand_strip_underwear_label_enhanced(the_person):
    mc.name "You're going to strip into your underwear for me."
    if not the_person.outfit.wearing_panties() or not the_person.outfit.wearing_bra():
        the_person "I can't do that [the_person.mc_title]."
        mc.name "Yes you can, you..."
        "She interrupts you."
        if not the_person.outfit.wearing_panties() and not the_person.outfit.wearing_bra():
            the_person "No, I can't show you my underwear because... I'm not wearing any."
        elif not the_person.outfit.wearing_panties():
            the_person "No, I can't show you my underwear because... I'm not wearing any panties."
        else:
            the_person "No, I can't show you my underwear because... I'm not wearing a bra in the first place."
        mc.name "Well, that's as good a reason as any."
        return

    $ test_outfit = the_person.outfit.get_copy()
    $ test_outfit.strip_to_underwear(visible_enough = False)
    $ willing_private = demand_strip_judge_private(the_person, test_outfit, "lingerie")
    $ willing_public = demand_strip_judge_public(the_person, test_outfit, "lingerie")

    $ the_person.discover_opinion("lingerie")

    if the_person.location.get_person_count() > 1: #You aren't alone
        if willing_public: #She's into it
            "[the_person.possessive_title] nods obediently, seemingly unbothered by your command."
            call .start_stripping()
            return

        "[the_person.possessive_title] looks around nervously, then back at you."
        $ obedience_requirement = demand_strip_get_obedience_req(the_person, test_outfit, min = 130)
        if willing_private: # She's willing, but shy
            the_person "But... Here? Can we go somewhere without other people around first?"
            menu:
                "Find somewhere private":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're there she starts to pull off her clothes for you."
                    call .start_stripping(private = True)
                    return

                "Stay right here" if the_person.obedience >= obedience_requirement:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    "[the_person.possessive_title] doesn't argue. She just blushes and starts to pull off her clothes."
                    call .start_stripping(ordered = True)
                    return

                "Stay right here\n{color=#ff0000}{size=18}Requires: [obedience_requirement] Obedience{/size}{/color} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Never mind. Let's do something else."
                    return

        else: # She doesn't even want to do it in private
            the_person "Do... do I have to?"
            menu:
                "That's an order" if the_person.obedience >= obedience_requirement:
                    mc.name "Of course you don't. But I'd be disappointed, and you don't want to disappoint me, do you?"
                    "[the_person.possessive_title] stops arguing and meekly starts to pull off her clothes."
                    call .start_stripping(ordered = True)
                    return

                "That's an order\n{color=#ff0000}{size=18}Requires: [obedience_requirement] Obedience{/size}{/color} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Of course you don't. I just thought it'd be fun. Let's do something else."
                    return

    else: #You are alone
        if willing_private: #She's into it.
            the_person "Okay, whatever you want [the_person.mc_title]."
            "She starts to strip down for you."
            call .start_stripping(private = True)
            return

        $ obedience_requirement = demand_strip_get_obedience_req(the_person, test_outfit, min = 130, private = True)
        "[the_person.possessive_title] seems uncomfortable at your request."
        the_person "Do... do I have to?"
        menu:
            "That's an order" if the_person.obedience >= obedience_requirement:
                mc.name "Of course you don't. But I'd be disappointed, and you don't want to disappoint me, do you?"
                "[the_person.possessive_title] stops arguing and meekly starts to pull off her clothes."
                call .start_stripping(private = True, ordered = True)
                return

            "That's an order\n{color=#ff0000}{size=18}Requires: [obedience_requirement] Obedience{/size}{/color} (disabled)" if the_person.obedience < obedience_requirement:
                pass

            "Never mind":
                mc.name "Of course you don't. I just thought it'd be fun. Let's do something else."
                return

    return

label .start_stripping(private = False, ordered = False):
    $ underwear_strip_description(the_person)
    $ the_person.update_outfit_taboos()
    $ person_is_shy = not the_person.judge_outfit(the_person.outfit, temp_sluttiness_boost = 5 * the_person.get_opinion_score("lingere"))

    if person_is_shy: # She's shy
        the_person "Um... So what do we do now?"
        mc.name "Just relax and let me take a look. You look cute."
        $ mc.change_locked_clarity(10)
        "She nods and puts her hands behind her back. She blushes and looks away self-consciously as you ogle her."
        $ the_person.change_slut(1 + the_person.get_opinion_score("lingerie"), 35)
        $ the_person.change_happiness(-2 + the_person.get_opinion_score("lingerie"))
        mc.name "Let me see what it looks like from behind."
        $ the_person.draw_person(position = "back_peek")
        "[the_person.title] spins around obediently."
        "You enjoy the view for a little while longer. [the_person.possessive_title] seems anxious to cover up again."
        the_person "Can I get dressed now?"
        $ the_person.draw_person()
    else:
        "[the_person.title] immediately puts her hands behind her back and pushes her chest forward, accentuating her tits."
        the_person "So, what do you think? Does my underwear look good?"
        mc.name "It does, you look cute."
        $ mc.change_locked_clarity(15)
        "She smiles and gives you a spin, letting you take a look at her from behind."
        $ the_person.draw_person(position = "back_peek")
        "You enjoy the view for a little while longer, then nod approvingly to [the_person.possessive_title]."
        $ the_person.draw_person()
        the_person "Would you like me to get dressed again?"

    menu:
        "Let her get dressed":
            mc.name "Yeah, you can."
            "You watch her put her clothes back on."
            $ the_person.apply_outfit()
            $ the_person.draw_person()

        "Stay in your underwear":
            mc.name "Your underwear is too cute to hide it away, you should should stay in it for a while."
            if willing_public:
                the_person "Okay, if that's what you want me to do [the_person.mc_title]."
                $ the_person.planned_outfit = the_person.outfit.get_copy()
            elif ordered:
                the_person "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.change_slut(1, 35)
                $ the_person.change_happiness(-2)
                $ the_person.planned_outfit = the_person.outfit.get_copy()
            else:
                the_person "Very funny. I'm not about to go out like this."
                "She starts putting her clothes back on."
                $ the_person.change_obedience(-2)
                $ the_person.apply_outfit()
                $ the_person.draw_person()

    return
