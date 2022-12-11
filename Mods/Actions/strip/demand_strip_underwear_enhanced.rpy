init 5 python:
    config.label_overrides["demand_strip_underwear_label"] = "demand_strip_underwear_label_enhanced"
    
    def demand_strip_underwear_requirement_enhanced(the_person):
        if the_person.outfit.tits_visible() or the_person.outfit.vagina_visible():
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

    if mc.location.get_person_count() > 1: #You aren't alone.
        if the_person.effective_sluttiness("underwear_nudity") < (40 - (5*the_person.get_opinion_score("lingerie"))): #She's shy and wants to go somewhere private
            "[the_person.possessive_title] looks around nervously, then back at you."
            the_person "But... Here? Can we go somewhere without other people around first?"
            menu:
                "Find somewhere private":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're there she starts to pull off her clothes for you."


                "Stay right here" if the_person.obedience >= 140:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    "[the_person.possessive_title] doesn't argue. She just blushes and starts to pull off her clothes."

                "Stay right here\n{color=#ff0000}{size=18}Requires: 140 Obedience{/size}{/color} (disabled)" if the_person.obedience < 140:
                    pass

        else: #She's into it
            "[the_person.possessive_title] nods obediently, seemingly unbothered by your command."


        $ underwear_strip_description(the_person)


    else: #You are alone
        if the_person.effective_sluttiness("underwear_nudity") < (40 - (5*the_person.get_opinion_score("lingerie"))): #She's shy
            "[the_person.possessive_title] seems uncomfortable, but she nods obediently and starts to pull off her clothes."

        else: #She's into it.
            the_person "Okay, whatever you want [the_person.mc_title]."
            "She starts to strip down for you."

        $ underwear_strip_description(the_person)

    $ the_person.update_outfit_taboos()

    if the_person.effective_sluttiness() < (40 - (5*the_person.get_opinion_score("lingerie"))): # She's shy
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
            if the_person.effective_sluttiness() < (40 - (5*the_person.get_opinion_score("lingerie"))):
                the_person "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.change_slut(1, 35)
                $ the_person.change_happiness(-2)
            else:
                the_person "Okay, if that's what you want me to do [the_person.mc_title]."
    return