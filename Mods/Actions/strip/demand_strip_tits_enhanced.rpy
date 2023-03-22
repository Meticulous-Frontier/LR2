init 5 python:
    config.label_overrides["demand_strip_tits_label"] = "demand_strip_tits_label_enhanced"

    def demand_strip_tits_requirement(the_person):
        if the_person.tits_visible():
            return False #Can't strip if they're already visible
        if the_person.obedience < 140:
            return "Requires: 140 Obedience"
        return __builtin__.len(the_person.outfit.get_tit_strip_list()) > 0


label demand_strip_tits_label_enhanced(the_person):
    $ mc.change_energy(-5)
    mc.name "You're going to get your tits out for me."

    $ test_outfit = the_person.outfit.get_copy()
    $ test_outfit.strip_to_tits(visible_enough = False)
    $ willing_private = demand_strip_judge_private(the_person, test_outfit, "showing her tits")
    $ willing_public = demand_strip_judge_public(the_person, test_outfit, "showing her tits")
    $ obedience_requirement = demand_strip_get_obedience_req(the_person, test_outfit, min = 140, private = not willing_public)
    $ test_outfit = None

    $ strip_list = the_person.outfit.get_tit_strip_list()
    $ first_item = strip_list[0]

    $ the_person.discover_opinion("showing her tits")

    if the_person.location.get_person_count() > 1: #You aren't alone
        if willing_public: #She's into it
            "[the_person.possessive_title] doesn't seem to care about the other people around and starts to pull off her [first_item.display_name] right away."
            call .start_stripping() from _demand_strip_tits_willing_public
            return

        "[the_person.possessive_title] looks around nervously, then back at you."
        if willing_private: # She's willing, but shy
            the_person "But... Here? Can we go somewhere without other people around first?"
            menu:
                "Find somewhere private":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're finally alone she moves to pull off her [first_item.display_name] for you."
                    call .start_stripping(private = True) from _demand_strip_tits_move_to_private
                    return

                "Stay right here" if the_person.obedience >= obedience_requirement:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title] doesn't argue. She just blushes and starts to pull off her [first_item.display_name] for you."
                    call .start_stripping(ordered = True) from _demand_strip_tits_stay_in_public
                    return

                "Stay right here\n{color=#ff0000}{size=18}Requires: [obedience_requirement] Obedience{/size}{/color} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Never mind. Let's do something else."
                    $ the_person.change_stats(obedience = -1)

        elif the_person.obedience >= obedience_requirement - 20: # She doesn't even want to do it in private
            the_person "Do... do I have to?"
            menu:
                "That's an order" if the_person.obedience >= obedience_requirement:
                    mc.name "Of course you do. I {i}want{/i} you to."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title] stops arguing and resignedly starts to pull off her [first_item.display_name]."
                    call .start_stripping(ordered = True) from _demand_strip_tits_ordered_public
                    return

                "That's an order\n{color=#ff0000}{size=18}Requires: [obedience_requirement] Obedience{/size}{/color} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Of course you don't. I just thought it'd be fun. Let's do something else."
                    $ the_person.change_stats(obedience = -1)
        else:
            $ the_person.change_stats(obedience = -1)
            the_person "I don't think I will. My clothes stay on for now."
            mc.name "For now?"
            "[the_person.title] smirks and changes the subject."

    else: #You are alone
        if willing_private: #She's into it.
            "[the_person.possessive_title] nods obediently and begins to take off her [first_item.display_name] while you watch."
            call .start_stripping(private = True) from _demand_strip_tits_willing_private
            return

        if the_person.obedience >= obedience_requirement - 20: # She's considering it
            "[the_person.possessive_title] seems uncomfortable and hesitates to follow instructions."
            the_person "Do... do I have to?"
            menu:
                "That's an order" if the_person.obedience >= obedience_requirement:
                    mc.name "Of course you do. I {i}want{/i} you to."
                    $ the_person.change_stats(happiness = -2)
                    "[the_person.possessive_title] stops arguing and resignedly begins to take off her [first_item.display_name]."
                    call .start_stripping(private = True, ordered = True) from _demand_strip_tits_ordered_private
                    return

                "That's an order\n{color=#ff0000}{size=18}Requires: [obedience_requirement] Obedience{/size}{/color} (disabled)" if the_person.obedience < obedience_requirement:
                    pass

                "Never mind":
                    mc.name "Of course you don't. I just thought it'd be fun. Let's do something else."
                    $ the_person.change_stats(obedience = -1)
        else:
            $ the_person.change_stats(obedience = -1)
            the_person "I don't think I will. My clothes stay on for now."
            mc.name "For now?"
            "[the_person.title] smirks and changes the subject."

    $ strip_list = None
    $ first_item = None
    return

label .start_stripping(private = False, ordered = False):
    $ top_strip_description(the_person, strip_list)

    $ strip_list = None
    $ first_item = None

    $ person_is_shy = not the_person.judge_outfit(the_person.outfit, temp_sluttiness_boost = 5 * the_person.get_opinion_score("showing her tits"))

    if the_person.update_outfit_taboos() or person_is_shy: # She's shy
        "[the_person.title] brings her hands up to cover her breasts."
        the_person "Are we done?"
        mc.name "I want to get a look first, and I can't see anything if you're hiding like this."
        $ mc.change_locked_clarity(10)
        "She nods and moves her hands to her side again. She blushes and looks away as you ogle her tits."
        $ the_person.change_slut(1 + the_person.get_opinion_score("showing her tits"), 35)
        $ the_person.change_happiness(-2 + the_person.get_opinion_score("showing her tits"))
        "When you've seen enough you give her an approving nod. She sighs and moves towards her clothes."
        the_person "Can I get dressed now?"
    else: # She's into it
        $ the_person.draw_person(the_animation = blowjob_bob) #TODO Make sure this effect looks right
        $ mc.change_locked_clarity(20)
        "[the_person.title] places her hands behind her and bounces on her feet, jiggling her tits for your amusement."
        "When you've seen enough you nod approvingly. [the_person.possessive_title] smiles happily."
        the_person "So you want me to get dressed again?"

    menu:
        "Let her get dressed":
            mc.name "Yeah, you can."
            $ the_person.apply_outfit()
            $ the_person.draw_person()
            "You watch her put her clothes back on, covering up her tits."

        "Keep your tits out":
            mc.name "I think you look good with your tits out. Stay like this for a while, okay?"
            if willing_public:
                the_person "Okay, if that's what you want me to do [the_person.mc_title]."
                $ the_person.planned_outfit = the_person.outfit.get_copy()
            elif the_person.obedience >= obedience_requirement:
                $ the_person.change_stats(obedience = 1, slut = 1, max_slut = 35, happiness = -2)
                the_person "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.planned_outfit = the_person.outfit.get_copy()
            else:
                $ the_person.change_stats(obedience = -1, love = -1)
                the_person "Very funny. I'm not about to go out like this."
                $ the_person.change_obedience(-2)
                $ the_person.apply_outfit()
                $ the_person.draw_person()
                "She starts putting her clothes back on."

    return
