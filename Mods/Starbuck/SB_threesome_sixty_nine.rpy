init:
    python:
        SB_threesome_sixty_nine = SB_Threesome_Position(name = "Sixty Nine Plus One",
            slut_requirement = 60,
            slut_cap = 120,
            position_one_tag = "missionary",
            position_two_tag = "cowgirl",
            requires_location = "Lay",
            requires_clothing = "Vagina",
            skill_tag_p1 = "Vaginal",
            skill_tag_p2 = "Oral",
            girl_one_arousal = 22,
            girl_two_arousal = 20,
            girl_one_source = 0,
            girl_two_source = 1,
            guy_arousal = 20,
            guy_source = 1,
            skill_tag_guy = "Vaginal",
            current_girl = 1,
            connections = [],
            intro = "intro_SB_threesome_sixty_nine",
            scenes = ["scene_SB_threesome_sixty_nine_1", "scene_SB_threesome_sixty_nine_2"],
            outro = "outro_SB_threesome_sixty_nine",
            transition_default = "transition_default_SB_threesome_sixty_nine",
            strip_description = "strip_SB_threesome_sixty_nine",
            strip_ask_description = "strip_ask_SB_threesome_sixty_nine",
            orgasm_description = "orgasm_SB_threesome_sixty_nine",
            swap_description = "swap_SB_threesome_sixty_nine",
            verb = "fuck" ,
            opinion_tags = ["missionary style sex","vaginal sex","threesomes", "giving blowjobs", "threesomes"],
            p1_x = 1.0,
            p1_y = 1.05,
            p1_zoom = 0.8,
            p2_x = 0.97,
            p2_y = 0.7,
            p2_zoom = 0.8,
            can_swap = True,
            swap_text = "Swap Between Girls")
        SB_list_of_threesomes.append(SB_threesome_sixty_nine)


label intro_SB_threesome_sixty_nine(the_person_1, the_person_2, the_location, the_object, the_round, current_girl):
    mc.name "[the_person_1.title], why don't you lay down. [the_person_2.title] can get on top of you and you can eat her out while I fuck you."
    "[the_person_1.title] smiles and agrees."
    if SB_get_fetish(the_person_1) == "Vaginal Fetish":
        the_person_1.char "Mmm I can't wait to feel you sliding into me..."
    elif SB_get_fetish(the_person_1) == "Oral Fetish":
        the_person_1.char "Mmm I can't wait to taste that sweet pussy..."
    elif SB_get_fetish(the_person_1) == "Anal Fetish":
        the_person_1.char "Mmm that sounds good... maybe you could stick a finger in my ass once in a while too..."
    else:
        the_person_1.char "Sounds good! I can't wait, I bet this is going to be amazing..."
    "[the_person_1.title] starts to lay down. [the_person_2.title] turns to you."
    if SB_get_fetish(the_person_2) == "Oral Fetish":
        the_person_2.char "This should be good, I've heard [the_person_1.name] has a pretty good tongue..."
    elif SB_get_fetish(the_person_2) == "Vaginal Fetish":
        the_person_2.char "This should be a good warmup... but don't forget, [the_person_2.mc_title], I need you to fuck me sometime too..."
    else:
        the_person_2.char "Sounds good! Don't forget to change it up once in a while... I'd be glad to take a turn sucking you off..."
    "[the_person_2.title] climbs on top of [the_person_1.title] and slowly lowers her pussy down onto her face. She moans as [the_person_1.title] starts to lick between her legs"
    "You get down on your knees and spread [the_person_1.title]'s legs. You position your hips in line with hers and move your cock along her slit."
    if the_person_2.arousal > 60:
        "Her pussy is soaking wet. As you run your length along her hole you are soon slick with her juices."
    else:
        "Her pussy looks absolutely perfect. As you run your length along her hole she starts to squirm."
    "You push yourself into [the_person_1.title]'s steamy cunt and start to fuck her while [the_person_2.title] rides on her face."
    return

#Girl 1 = missionary, Girl 2 = oral#
label scene_SB_threesome_sixty_nine_1(the_person_1, the_person_2, the_location, the_object, the_round, current_girl):
    if current_girl == 1:
        "You run your hands along [the_person_1.title]'s hips as you fuck her. You can see her hands groping [the_person_2.title]'s ass cheeks as she pleasures her with her tongue."
        if the_person_2.has_large_tits() :
            if the_person_2.outfit.tits_available():
                "In front of you, you can see [the_person_2.title]'s huge tits heaving up and down as she slowly rocks her hips back and forth across [the_person_1.title]'s tongue."
            else:
                $top_clothing = the_person_2.outfit.get_upper_ordered()[-1]
                "In front of you, you can see [the_person_2.title]'s huge tits heaving up and down, barely contained in her [top_clothing.name] as she slowly rocks her hips back and forth across [the_person_1.title]'s tongue."
                "You decide they've been contained for too long."
                while not the_person_2.outfit.tits_available():    #If covered up, have her take her top off
                    $ the_clothing = the_person_2.outfit.get_upper_ordered()[-1]
                    "You take off [the_person_2.title]'s [the_clothing.name]"
                    $ the_person_2.outfit.remove_clothing(the_clothing)
                    $ SB_threesome_sixty_nine.redraw_scene(the_person_1, the_person_2)
        else:
            if the_person_2.outfit.tits_available():
                "In front of you, you can see [the_person_2.title]'s perky tits swaying up and down as she slowly rocks her hips back and forth across [the_person_1.title]'s tongue."
            else:
                $top_clothing = the_person_2.outfit.get_upper_ordered()[-1]
                "In front of you, you can see [the_person_2.title]'s perky tits swaying up and down as she slowly rocks her hips back and forth across [the_person_1.title]'s tongue."
                "They look great in her [top_clothing.name], but you decide they've been contained for too long."
                while not the_person_2.outfit.tits_available():    #If covered up, have her take her top off
                    $ the_clothing = the_person_2.outfit.get_upper_ordered()[-1]
                    "You take off [the_person_2.title]'s [the_clothing.name]"
                    $ the_person_2.outfit.remove_clothing(the_clothing)
                    $ SB_threesome_sixty_nine.redraw_scene(the_person_1, the_person_2)

        menu:
            "Squeeze her tits.":
                "You grab [the_person_2.title]'s tits. They feel warm and soft in your hands. You pinch and tug at her nipples."
                the_person_2.char "Mmmm, [the_person_2.mc_title]. I love your hands on me."
                $the_person_2.change_arousal(mc.sex_skills["Foreplay"])
            "Suck her nipples." if the_person_2.outfit.tits_available():
                "You lean forward and run your tongue all around one of [the_person_2.title]'s nipples."
                the_person_2.char "Oh! [the_person_2.mc_title]! That feels good!."
                "You suck one of [the_person_2.possessive_title] into your mouth. You flip it up and down with your tongue a few times."
                $the_person_2.change_arousal(mc.sex_skills["Oral"])
            "Suck her nipples.\n{size=22}Obstucted by Clothing{/size} (disabled)" if not the_person_2.outfit.tits_available():
                pass
        "While you give attention to [the_person_2.possessive_title]'s tits, you never stop pistoning your cock in and out of [the_person_1.title]'s slick pussy."
    else:
        "You rest one hand on [the_person_2.title]'s head, guiding her as she sucks you off. With you other hand you continue to finger fuck [the_person_1.title]."
        if the_person_2.get_opinion_score("giving blowjobs") > 0:
            "You can see that [the_person_2.title] is really moving her hips back and forth roughly on [the_person_1.title]'s face. She gets off on having a dick in her mouth!"
            $the_person_2.change_arousal(the_person_2.get_opinion_score("giving blowjobs") * 3)
        else:
            "You can see that [the_person_2.title] is bobbing her head on your cock in time with her hip movement as she grinds against [the_person_1.title]'s face"
        mc.name "Mmm, that feels great. When I blow my load, do you want it in your mouth or all over your face, [the_person_2.title]?"
        if the_person_2.get_opinion_score("cum facials") > the_person_2.get_opinion_score("drinking cum"):
            "[the_person_2.possessive_title] pops off your cock for a second."
            the_person_2.char "I want you to just blow all over my face..."
            if SB_get_fetish(the_person_1) == "External Cum Fetish" or SB_get_fetish(the_person_1) == "Internal Cum Fetish":
                "You hear a muffled voice speak up."
                the_person_1.char "Hey! [the_person_1.mc_title], make sure I get some too!"
        else:
            "[the_person_2.possessive_title] pops off your cock for a second."
            the_person_2.char "You should just cum in my mouth! I'll swallow it all for you..."
            if SB_get_fetish(the_person_1) == "External Cum Fetish" or SB_get_fetish(the_person_1) == "Internal Cum Fetish":
                "You hear a muffled voice speak up."
                the_person_1.char "Hey! That's no fair! [the_person_1.mc_title], make sure I get some too!"



    return

label scene_SB_threesome_sixty_nine_2(the_person_1, the_person_2, the_location, the_object, the_round, current_girl):
    if current_girl == 1:
        "[the_person_1.title]'s whole body is jostling forward and backward as you fuck her roughly. Her tight pussy feels silky smooth around your dick."
        "You lean forward and grab the back of [the_person_2.title]'s head, bring her in for a kiss. Your tongues meet together and you start to make out on top of [the_person_1.title]."
        "You decide its time for [the_person_2.possessive_title] to put her mouth to better use."
        "You pull back from making out with [the_person_2.title]."
        mc.name "I think [the_person_1.title] needs a little more attention..."
        "You grab [the_person_2.possessive_title]'s head by her hair and start to pull her head downwards. You pull out of [the_person_1.title]'s pussy partially to give her room to work."
        "She starts to lap at [the_person_1.title]'s cunt. You can feel her tongue brushing up against you cock."
        "You give [the_person_1.title] a few slow thrusts, making sure to give [the_person_2.title] room to work."
        the_person_1.char "Mmmm..."
        "Muffled moans come from [the_person_1.title]. Your cock is buried deep inside her while [the_person_2.possessive_title] licks and sucks at her clit."
        $ the_person_1.change_arousal(the_person_2.sex_skills["Oral"] * 2)

    else:
        "[the_person_2.title]'s mouth pops off you for a second. She starts to run her tongue up and down the length of your shaft."
        "The view is incredible. [the_person_2.possessive_title] is service you while she rides [the_person_1.title]'s face."
        "You can't believe how lucky you are."
        "You push your fingers deep into [the_person_1.title]. She moans into [the_person_2.title]'s pussy, who in turn moans around your cock."
        "The vibrations from the moaning set off an incredible wave of pleasure in your amazing love triangle."
        "[the_person_2.title] opens her mouth wide and takes your cock back into her mouth again, wrapping her velvet tongue and lips around your erection."

    return

label outro_SB_threesome_sixty_nine(the_person_1, the_person_2, the_location, the_object, the_round, current_girl):
    if current_girl == 1:
        "Between [the_person_1.title]'s steamy pussy and [the_person_2.title]'s heaving tits in front of you, you find yourself going past the point of no return."
        mc.name "Oh fuck I'm gonna cum!"
        menu:
            "Cum inside [the_person_1.title].":
                "You thrust yourself deep inside of [the_person_1.title]'s cunt as you climax."
                if the_person_1.arousal > 100:
                    "Your cock bursting deep inside her triggers another orgasm for [the_person_1.title]. She is moaning non stop."
                    $ the_person_1.change_happiness(5)
                $ the_person_1.cum_in_vagina()
                if SB_get_fetish(the_person_2) == "External Cum Fetish" or SB_get_fetish(the_person_2) == "Internal Cum Fetish":
                    the_person_2.char "Hey! No fair! I want some of that!"
                    "As you slowly pull out of [the_person_1.title], a trickle of your cum starts to escape her."
                    "[the_person_2.title] immediately moves her head down to [the_person_1.title]'s pussy and starts to lick up the cum leaking out."
                    "Desperate for more of your cum, she sticks her tongue deep into [the_person_1.title]."
                    if the_person_2.outfit.can_add_accessory(mouth_cum):
                        $the_cumshot = mouth_cum.get_copy()
                        $the_cumshot.layer = 0 #TODO: make sure this doesn't break things by being on layer 0
                        $the_person_2.outfit.add_accessory(the_cumshot)
                    $ SB_threesome_sixty_nine.redraw_scene(the_person_1, the_person_2)
                    if the_person_2.arousal > 100:
                        "Getting a dose of your cum triggers another orgasm in [the_person_2.possessive_title]. Her body twitches as orgasm goes through it."
                    "When she finally sits up, you can see traces of your cum on the corners of [the_person_2.title]'s mouth."
                else:
                    "As you slowly pull out of [the_person_1.title], a trickle of your cum starts to escape her."
                "You give a sigh, deeply contented with having dumped your load inside of [the_person_1.title]."

            "Cum on [the_person_2.title]'s face.":
                "You pull out of [the_person_1.title] and grab the back of [the_person_2.title]'s head, bringing it toward your cock."
                "She instinctively reaches out and starts to stroke you, pointing your cock right at her face."
                "Your orgasm erupts and you begin spraying cum across her face."
                $ the_person_2.cum_on_face()
                $ SB_threesome_sixty_nine.redraw_scene(the_person_1, the_person_2)
                if SB_get_fetish(the_person_2) == "External Cum Fetish":
                    "You can see [the_person_2.title]'s pupils dilate as you fulfil her cum fetish."
                    "[the_person_2.title] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                    "She truly is addicted to your cum."
                "Some of your cum runs down off [the_person_2.title]'s face and onto [the_person_1.title]'s belly."
                $ the_person_1.cum_on_stomach()
                $ SB_threesome_sixty_nine.redraw_scene(the_person_1, the_person_2)
                if SB_get_fetish(the_person_1) == "External Cum Fetish":
                    "[the_person_1.possessive_title]'s body quivers as your cum splashes down onto her. She runs her hands through your cum and rubs it into her belly."
                "You give a sigh. Two girls covered in your cum is an amazing sight to behold."

    else:
        "[the_person_2.possessive_title]'s talented mouth suddenly pushes you past the point of no return. Her tongue slithers and swirly relentlessly around your cock."
        mc.name "Oh fuck I'm gonna cum!"
        menu:
            "Cum inside [the_person_2.title]'s mouth'.":
                "You put your hand on the back of [the_person_2.possessive_title]'s head."
                mc.name "That's it [the_person_2.title]. I want you to swallow it all!"
                "[the_person_2.title] moans and looks you in the eyes. She pulls off until just the tip of your cock is in her mouth and she begins to stroke out off eagerly."
                "Your cock explodes in orgasm into her greedy mouth."
                if SB_get_fetish(the_person_2) == "Internal Cum Fetish":
                    "Her pupils dilate as her cum addicted brain registers the presence of your cum in her mouth."
                    "[the_person_2.possessive_title] is moaning uncontrollably around your spasming cock."
                $ the_person_2.cum_in_mouth()

                $ SB_threesome_sixty_nine.redraw_scene(the_person_1, the_person_2)
                "After you finish cumming, [the_person_2.possessive_title] slowly pulls away from your cock."
                "You give a sigh, deeply contented with having dumped your load inside of [the_person_2.possessive_title]'s mouth."

            "Cum on [the_person_2.title]'s face.":
                "You pull out of [the_person_2.title]'s mouth."
                "She instinctively reaches out and starts to stroke you, pointing your cock right at her face."
                "Your orgasm erupts and you begin spraying cum across her face."
                $ the_person_2.cum_on_face()
                $ SB_threesome_sixty_nine.redraw_scene(the_person_1, the_person_2)
                if SB_get_fetish(the_person_2) == "External Cum Fetish":
                    "You can see [the_person_2.title]'s pupils dilate as you fulfil her cum fetish."
                    "[the_person_2.title] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                    "She truly is addicted to your cum."
                "Some of your cum runs down off [the_person_2.title]'s face and onto [the_person_1.title]'s belly."
                $ the_person_1.cum_on_stomach()
                $ SB_threesome_sixty_nine.redraw_scene(the_person_1, the_person_2)
                if SB_get_fetish(the_person_1) == "External Cum Fetish":
                    "[the_person_1.possessive_title]'s body quivers as your cum splashes down onto her. She runs her hands through your cum and rubs it into her belly."
                "You give a sigh. Two girls covered in your cum is an amazing sight to behold."

    return

label transition_default_SB_threesome_sixty_nine(the_person_1, the_person_2, the_location, the_object, the_round, current_girl):
    "This is just a test to see if this position is working."
    "This is the default transition!"
    return

label strip_SB_threesome_sixty_nine(the_person_1, the_person_2, the_location, the_object, the_round, current_girl):
    "This is just a test to see if this position is working."
    "This is the Strip Scene!"
    return

label strip_ask_SB_threesome_sixty_nine(the_person_1, the_person_2, the_location, the_object, the_round, current_girl):
    "This is just a test to see if this position is working."
    "This is the ask to strip Scene!"
    return

label orgasm_SB_threesome_sixty_nine(the_person_1, the_person_2, the_location, the_object, the_round, current_girl):
    $ SB_threesome_sixty_nine.redraw_scene(the_person_1, the_person_2)
    if current_girl == 1:
        if the_person_1.arousal > 100 and the_person_2.arousal > 100:  #Both girls orgasm#
            "You can feel [the_person_1.title] trembling beneath you. [the_person_2.title] opens her mouth and moans as [the_person_1.title] licks her in just the right spot."
            $ the_person_2.call_dialogue("climax_responses")
            "[the_person_1.title] is moaning loudly but it all gets muffled as [the_person_2.title] grinds against her face roughly."
            "They both orgasm. [the_person_1.title]'s cunt pulses around your cock as she cums, while [the_person_2.title] moans and closes her eyes."
            "As they start to wind down, you continue fucking [the_person_1.title]'s now considerably slicker pussy."
            return

        elif the_person_1.arousal > 100:   #Just girl 1 orgasms
            "You can feel [the_person_1.title] trembling beneath you. She moans loudly but its muffled by [the_person_2.title] grinding her pussy in her face."
            "She orgasms, per pussy quivering around your cock. You grab her hips and give a few extra rough thrusts."
            "You don't even both to slow down. As [the_person_1.title] comes down from her orgasm you continue your relentless fucking."
            return

        elif the_person_2.arousal > 100:   #Just girl 2 orgasms
            "[the_person_2.title] opens her mouth and moans as [the_person_1.title] licks her in just the right spot."
            $ the_person_2.call_dialogue("climax_responses")
            "[the_person_2.title] grinds her pussy against the other girl's face as she orgasms."

    elif current_girl == 2:
        if the_person_1.arousal > 100 and the_person_2.arousal > 100:  #Both girls orgasm#
            "You can feel [the_person_1.title] trembling as you finger her. [the_person_2.title] moans around your cock as [the_person_1.title] licks her in just the right spot."
            $ the_person_2.call_dialogue("climax_responses")
            "[the_person_1.title] is moaning loudly but it all gets muffled as [the_person_2.title] grinds against her face roughly."
            "They both orgasm. [the_person_1.title]'s cunt quivers around yourfingers as she cums, while [the_person_2.title] moans and closes her eyes."
            "As they start to wind down, you put your hand on the back of [the_person_2.title]'s head and remind her to keep sucking."
            return
        elif the_person_1.arousal > 100:   #Just girl 1 orgasms
            "You can feel [the_person_1.title] trembling at your touch. She moans loudly but its muffled by [the_person_2.title] grinding her pussy in her face."
            "She orgasms, per pussy quivering around your fingers. You thrust them into her roughly."
            "As [the_person_1.title] comes down from her orgasm you continue stimulating her with your hand."
            return

        elif the_person_2.arousal > 100:   #Just girl 2 orgasms
            "[the_person_2.title] moans around your cock as [the_person_1.title] licks her in just the right spot."
            "She grinds her pussy against the other girl's face as she orgasms."
    return

#Girl 1 = missionary, Girl 2 = oral#
label swap_SB_threesome_sixty_nine(the_person_1, the_person_2, the_location, the_object, the_round, current_girl):
    if current_girl == 1:
        "You slowly pull out of [the_person_1.title]'s pussy. You run your hands through [the_person_2.title]'s hair for a second, then slowly pull her mouth down towards your cock."
        mc.name "Lick me clean, [the_person_2.title]."
        "[the_person_2.title] opens her mouth and begins to greedily slurp at your cock. Her mouth feels great sliding up and down your erection."
        "You reach down with one hand and hold [the_person_2.title]'s hair off to one side for her, and with your other hand you start to play with [the_person_1.title]'s pussy."
        $ guy_source = 2
        $ girl_one_source = 0
        $ girl_two_source = 1
        $ skill_tag_guy = "Oral"
        $ skill_tag_p1 = "Foreplay"
        $ skill_tag_p2 = "Oral"
        return
    else:
        "You pull back on [the_person_2.title]'s hair for a bit. Your cock springs free from her mouth with a satisfying plop. She looks up at you and smiles."
        mc.name "Mmm, that was good [the_person_2.title]. Time to get back to [the_person_1.title]..."
        "You lower yourself down until you are lined up with [the_person_1.title]'s pussy. She moans as you slide yourself back into her, but it is muffled by [the_person_2.title]'s hips as she rides her face."
        "You slide yourself into her slick cunt a few times, filling her eager hole with your dick."
        $ guy_source = 1
        $ girl_one_source = 0
        $ girl_two_source = 1
        $ skill_tag_guy = "Vaginal"
        $ skill_tag_p1 = "Vaginal"
        $ skill_tag_p2 = "Oral"
        return

    return
