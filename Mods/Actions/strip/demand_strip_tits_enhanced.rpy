init 5 python:
    config.label_overrides["demand_strip_tits_label"] = "demand_strip_tits_label_enhanced"

    def demand_strip_tits_requirement_enhanced(the_person):
        if the_person.outfit.tits_visible():
            return False #Can't strip if they're already visible
        elif the_person.obedience < 130:
            return "Requires: 130 Obedience"
        else:
            return True
    demand_strip_tits_requirement = demand_strip_tits_requirement_enhanced


label demand_strip_tits_label_enhanced(the_person):
    #TODO: Most of this dialogue should be moved into a personality specific branch. A task for next update.
    mc.name "You're going to get your tits out for me."
    $ strip_list = the_person.outfit.get_tit_strip_list()
    $ first_item = strip_list[0]
    if the_person.effective_sluttiness("bare_tits") < (40 - (5*the_person.get_opinion_score("showing her tits"))): # She wouldn't normally show off her tits.
        $ the_person.discover_opinion("showing her tits")
        if mc.location.get_person_count() > 1: #We're in public, so she's shy.
            "[the_person.possessive_title] looks around nervously, then back at you."
            the_person "But... Here? Can we go somewhere without other people around first?"
            menu:
                "Find somewhere private":
                    mc.name "Fine, if that's what you need."
                    "She is visibly relieved, and follows you as you find somewhere private for the two of you."
                    "Once you're finally alone she moves to pull off her [first_item.display_name] for you."


                "Stay right here" if the_person.obedience >= 140:
                    "You shake your head."
                    mc.name "No, we're going to stay right here."
                    "[the_person.possessive_title] doesn't argue. She just blushes and starts to pull off her [first_item.display_name] for you."

                "Stay right here\n{color=#ff0000}{size=18}Requires: 140 Obedience{/size}{/color} (disabled)" if the_person.obedience < 140:
                    pass
            $ top_strip_description(the_person, strip_list)


        else:
            #We're in private, so she's a little more brave. If she loves you she might even do it for fun
            if the_person.effective_sluttiness("bare_tits") + the_person.love < (40 - (5*the_person.get_opinion_score("showing her tits"))):
                #Pure Obedience going on
                "[the_person.possessive_title] seems uncomfortable, but she doesn't hesitate to follow instructions. She begins to take off her [first_item.display_name]."

            else:
                #She loves you, this is just cutting to the chase.
                "[the_person.possessive_title] nods obediently and begins to take off her [first_item.display_name] while you watch."
            $ top_strip_description(the_person, strip_list)

    else:
        # She doesn't have any problem showing off her tits, so she doesn't care if she's in public or not.
        $ the_person.discover_opinion("showing her tits")
        the_person "Oh, is that all?"
        if mc.location.get_person_count() > 1:
            "[the_person.possessive_title] doesn't seem to care about the other people around and starts to pull off her [first_item.display_name] right away."
        else:
            "[the_person.possessive_title] starts to pull off her [first_item.display_name] right away."
        $ top_strip_description(the_person, strip_list)

    $ del first_item
    $ strip_list = None

    $ the_person.update_outfit_taboos()

    if the_person.effective_sluttiness() < (40 - (5*the_person.get_opinion_score("showing her tits"))): # She's shy
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
            "You watch her put her clothes back on, covering up her tits."
            $ the_person.apply_outfit()
            $ the_person.draw_person()

        "Keep your tits out":
            mc.name "I think you look good with your tits out. Stay like this for a while, okay?"
            if the_person.effective_sluttiness() < (40 - (5*the_person.get_opinion_score("showing her tits"))):
                the_person "I... Okay, if that's what you want [the_person.mc_title]."
                $ the_person.change_slut(1, 35)
                $ the_person.change_happiness(-2)
            else:
                the_person "Okay, if that's what you want me to do [the_person.mc_title]."
    return
