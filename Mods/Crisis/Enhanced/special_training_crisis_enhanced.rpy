# Originally written by Pilotus13
init 10 python:
    config.label_overrides["special_training_crisis_label"] = "enhanced_special_training_crisis_label"

init 2 python:
    dict_work_skills = {
        "hr_skill": ["Human Resources", "hr_skill"],
        "market_skill": ["Marketing", "market_skill"],
        "research_skill": ["Research & Development", "research_skill"],
        "production_skill": ["Production", "production_skill"],
        "supply_skill": ["Supply Procurement", "supply_skill"]
        }

    def build_seminar_improvement_menu(person):
        work_seminar = [] # NOTE: We can allow seminars for both main and sex skills, e.g through introducing a company hosted seminar type.
        for skill in dict_work_skills:
            work_seminar.append([dict_work_skills[skill][0] + "\nCurrent: " + str(getattr(person, dict_work_skills[skill][1])), dict_work_skills[skill][1]])
        work_seminar.insert(0, "Work Skills")
        return [work_seminar]

    def return_from_seminar_action_requirement():
        return mc.business.is_open_for_business() and mc.is_at_work()

    def add_return_from_seminar_action(person):
        return_from_seminar_action = Action("Return From Seminar Thank You",return_from_seminar_action_requirement,"return_from_seminar_action_label", args = person)
        mc.business.add_mandatory_crisis(return_from_seminar_action)
        return

label enhanced_special_training_crisis_label():
    if not mc.business.get_employee_count() > 0:
        return #We must have had someone quit or be fired, so we no longer can get a random person.

    $ the_person = get_random_from_list(mc.business.get_employee_list())
    show screen person_info_ui(the_person)
    $ mc.start_text_convo(the_person)
    the_person "[the_person.mc_title], I've just gotten word about a training seminar going on right now a few blocks away. I would love to take a trip over and see if there is anything I could learn."
    the_person "There's a sign up fee of $500. If you can cover that, I'll head over right away."
    if the_person.effective_sluttiness() >= 20:
        the_person "I'll personally repay you for it later..."
    menu:
        "Send [the_person.title] to Seminar\n{color=#ff0000}{size=18}Costs: $500{/size}{/color}" if mc.business.has_funds(500):
            mc.name "That sounds like a great idea. I'll call and sort out the fee, you start heading over."
            the_person "Understood, thank you sir! What would you like me to focus on?"

            call screen enhanced_main_choice_display(build_menu_items(build_seminar_improvement_menu(the_person)))
            if _return != "None":
                $ mc.business.change_funds(-500)
                $ setattr(the_person, _return, getattr(the_person, _return) + 2) #TODO: Make this line be generic.
                $ mc.log_event((the_person.title or the_person.name) + ": +2 " + dict_work_skills[_return][0], "float_text_grey")
                $ renpy.say(mc.name, "Work on your " + dict_work_skills[_return][0] + " skills.")
                if the_person.effective_sluttiness() >= 20:
                    # follow up on promise made
                    $ add_return_from_seminar_action(the_person)

        "Send [the_person.title] to Seminar\n{color=#ff0000}{size=18}Requires: $500{/size}{/color} (disabled)" if not mc.business.has_funds(500):
            pass

        "Tell her to stay at work":
            mc.name "I'm sorry [the_person.title], but there aren't any extra funds in the budget right now."
            the_person "Noted, maybe some other time then."

    $ mc.end_text_convo()
    return

label return_from_seminar_action_label(the_person):
    if the_person.effective_sluttiness() >= 20:
        $ the_person.draw_person(position="stand4")
        $ ceo_office.show_background()
        "[the_person.title] enters your office where you are in your chair, idly tending to your duties."
        the_person "There you are, [the_person.mc_title]! I'm back from the seminar and ready to show you the gratitude I promised."
        $ the_clothing = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
        if the_clothing is not None:
            $ the_person.draw_animated_removal(the_clothing)
            "Before you have time to reply, [the_person.title] begins stripping off her [the_clothing.display_name] right in front of you."
            $ mc.change_locked_clarity(10)
            the_person "I thought it wouldn't hurt to show you a bit of skin, hope you don't mind?"
            mc.name "Not at all, I always appreciate a pleasant sight, [the_person.title]."
        if the_person.effective_sluttiness() >= 50:
            $ the_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
            if the_clothing is not None:
                "[the_person.possessive_title] isn't impressed by your reaction to her display. Wanting to sweeten the deal for you, she continues on."
                the_person "You deserve a bit more I guess... How about I take off my [the_clothing.display_name] for you?"
                $ the_person.draw_animated_removal (the_clothing)
                the_person "Do you like the view of [the_person.possessive_title] undressing?"
            $ mc.change_locked_clarity(10)
            if the_person.age > 30:
                "Your dick twitches at the sight of [the_person.title]'s mature body."
            else:
                "Your dick twitches at the sight of [the_person.title]'s nubile body."
            if the_person.effective_sluttiness() >= 80:
                $ the_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                if the_clothing is not None:
                    the_person "You know... the seminar really did help me out..."
                    #$ the_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                    $ the_person.draw_animated_removal(the_clothing)
                the_person "You like when I'm a bit naked, huh?"
                $ mc.change_locked_clarity(10)
                "You feel like you could explode just from the view of [the_person.title]'s naked body as she stands there, teasing you."
        $ the_clothing = None

    if the_person.effective_sluttiness() >= 60:
        $ the_person.draw_person(emotion="sad")
        "She stops to think for a second, putting on a frown before turning it into a bright, mischievous smile."
        $ the_person.draw_person(emotion="happy")
        the_person "Being naked in front of you makes me so... horny! You deserve some real gratitude! How about a quick BJ?"
        "\"There's always time for a quick blowjob\" you think to yourself before swiftly unzipping your pants as [the_person.possessive_title] gets onto her knees."
        $ the_person.draw_person(position="kneeling1")
        the_person "[the_person.mc_title], you have such a nice cock, it'll be perfect inside of my mouth..."
        $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
        $ mc.change_locked_clarity(10)
        "[the_person.title] opens her mouth and begins to vigorously suck on your dick with the full intent of giving you at least $500's worth of suction." #Nice. SUUUCTIIIIOOON
        mc.name "I truly appreciate having such a grateful employee, just keep on going [the_person.title]."
        $ the_person.draw_person(position="blowjob")
        "[the_person.title] lets your cock drop out of her mouth as she grabs a hold of it, administrating an enthusiastic handjob as she looks in your eyes with a smile plastered onto her face."
        the_person "And I truly appreciate working for such a wonderful man!"
        "Meanwhile, she keeps tugging at your length, cherishing your compliment."
        the_person "You know... [the_person.mc_title], I owe you and your company a lot. I hope you know that I'll go to any lengths to make the company succeed."
        "She speeds up stroking your dick while cupping and massaging your balls with her other hand."
        the_person "I hope the company will come to benefit from the techniques the seminar taught me... Don't you agree, [the_person.mc_title]?"
        $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
        "Before you can answer her, [the_person.title] swallows all of your cock into her mouth and begins moaning around it."
        the_person "Mrmrmm... Mrmmmmm..."
        "[the_person.title] continues to speed up and you begin to feel that it won't be long before you explode."
        if the_person.get_opinion_score("giving blowjobs") > 0:
            mc.name "It feels great, [the_person.title]! Get ready for a big one."

        if the_person.effective_sluttiness() >= 90 and the_person.sex_skills["Oral"] >= 5 and the_person.happiness > 130: # devoted slutty employee with high oral skills
            $ the_person.draw_person(position="kneeling1")
            "Right before you hit your climax she pulls your cock out of her mouth and looks up into your eyes."
            the_person "Yes, [the_person.mc_title]! I want to be covered by your sperm! Unleash it onto me, please!"
            the_person.mc_title "OK, [the_person.title], keep still. Here it goes!"
            $ the_person.cum_on_face()
            "You start to unleash your load onto [the_person.possessive_title]'s face."
            $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
            "She opens her mouth and attempts to catch some of the load that is being sprayed onto her face, cherishing each drop that falls inside."
            $ the_person.cum_in_mouth()
            $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
            "Soon [the_person.title]'s mouth is filled to the brim with your sperm from the torrent you're unleashing upon her, but you just cannot stop."
            $ the_person.cum_on_tits()
            $ the_person.draw_person(position="kneeling1")
            "She closes her mouth to secure the load in her stomach while the excess cum drips down onto her tits, painting them white."
            mc.name "There you go, [the_person.title]! That's how a proper [mc.business.name] employee should look!"
            #"The image of [the_person.title] sitting contently in front of with her body coated in your sperm really fires you up."
            $ the_person.draw_person(position = "stand2", emotion = "happy")
            "[the_person.title] pushes herself up off the floor while you take in the spectacle of her body. Her eyes trail down her chest as drops of your sperm fall onto the carpet below."
            the_person "Really, [the_person.mc_title]? Maybe you would like to have a better look?"
            $ the_person.draw_person(position = "back_peek")
            "[the_person.title] starts to turn around with the intention of striking various poses, allowing you to enjoy the sight of her cum drenched body."
            $ the_person.draw_person(position = "missionary", emotion = "happy")
            "She lies herself back onto the floor before spreading her legs, giving you a perfect view of her now dripping vagina. Her juices flow onto the carpet, mixing themselves with yours."
            the_person "Do you prefer this view? My pussy is yours to use however you want for the sake of [mc.business.name]." # Should probably include some less NTR- suggestive dialogue depending on preferences etc.
            "She basks in the pleasurable sensation of announcing her devotion to you and [mc.business.name]."
            the_person "If my pussy is off limits... then how about this."
            $ the_person.draw_person(position = "kneeling1", emotion = "happy")
            "[the_person.title] rolls herself onto her stomach, then gets up on her knees as she opens her mouth, licking her lips, while reaching down to rub at her clit."
            if persistent.show_ntr:
                the_person "I can be on my knees handing out blowjobs to whoever you want..."
                the_person "I'll gladly suck any dick you instruct me to if it helps [mc.business.name] prosper."
            $ the_person.draw_person(position = "standing_doggy", emotion = "happy", the_animation = ass_bob, animation_effect_strength = 0.7)
            "[the_person.title] then rotates her back towards you, reaching up to support herself by resting her arms on the desk as she arches her back, pushing her ass in your direction, wiggling it left and right."
            if persistent.show_ntr:
                the_person "You should also check out this ass. It is usable if you would like."
                the_person "I wouldn't mind if you share this ass of mine with your investors or friends either. I'd actually love that, [the_person.mc_title]!"
            $ the_person.draw_person(position = "back_peek", emotion = "happy")
            "[the_person.title] straightens her back then walks towards the door that leads out of your office. In the doorway she stops and turns to you."
            the_person "Remember [the_person.mc_title], I'll do anything for this company."
            $ the_person.apply_planned_outfit()
            return
        else:
            $ ran_num = renpy.random.randint(1, 2)
            if ran_num == 1:
                if the_person.get_opinion_score("drinking cum") > the_person.get_opinion_score("being covered in cum"):
                    "She withdraws her mouth from your cock, resting it by the tip as she looks into your eyes with her mouth wide open."
                    $ the_person.cum_in_mouth()
                    $ the_person.draw_person(position="blowjob")
                    $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
                    the_person "Yes, [the_person.mc_title]! Shoot your load right into my mouth. I love the taste of you."
                else:
                    "She pulls your cock out of her mouth then looks intently at your eyes."
                    $ the_person.cum_on_face()
                    $ the_person.draw_person(position="blowjob")
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_person)
                    the_person "Yes, [the_person.mc_title]. Shoot it right onto me! Give me one... big... facial."
            else:
                if the_person.get_opinion_score("giving tit fucks") > the_person.get_opinion_score("being covered in cum"):
                    "She pulls your cock out of her mouth then looks up into your eyes as she presents her chest to you."
                    $ the_person.cum_on_tits()
                    $ the_person.draw_person(position="blowjob")
                    $ ClimaxController.manual_clarity_release(climax_type = "tits", the_person = the_person)
                    the_person "Like my tits, [the_person.mc_title]? They'll look much better covered in your cum..."
                else:
                    "She pulls your cock out of her mouth then looks up into your eyes as she leans away from you."
                    the_person "Oh, [the_person.mc_title]. I just applied new makeup. Please, don't ruin it."
                    $ the_person.cum_on_stomach()
                    $ the_person.draw_person(position="blowjob")
                    $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
                    "[the_person.title] keeps sitting on her knees while receiving your load on her body."

            the_person "Aaaah, it feels great!"
            $ the_person.draw_person(position = "stand3", emotion = "happy")
            "[the_person.title] kisses the tip of your cock before standing up, smiling."
            the_person "Thanks, [the_person.mc_title]. That's just what I needed! I hope you found my repayment adequate."
            mc.name "Very adequate indeed, now back to work."

    if the_person.effective_sluttiness() >= 60:
        "She leans in, kisses you on the cheek and gives your cock a final squeeze, then leaves the room."
    else:
        "She gives you a kiss on the cheek before leaving the room."

    $ the_person.apply_planned_outfit()
    return
