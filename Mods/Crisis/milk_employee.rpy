###Scene Idea: Girl is pumping milk. MC can help or watch
#
#   In this scene, player is walking by some kind of private room when he hears moaning coming from inside
#   After investigating, player finds NPC masturbating
#   Player choices include walking away and watching
#   If watching, NPC has chance to notice PC watching. If slutty, NPC continues, if not, stops and gets angry
#   If watching, and NPC is slutty, have a chance if we went unnoticed for NPC to call out PC name
#   Give PC option to just continue watching, leave NPC a note saying thanks for the show, or to make self known
#   If make self known trigger sex scene
#
#
###
init -1 python:
    milk_employee_crisis_weight = 5

init 2 python:
    def milk_employee_requirement():
        if mc.business.get_employee_count() > 0:
            if mc.business.is_open_for_business():
                if mc.is_at_work():
                    if select_girl_lactating == None:
                        return False
                    else:
                        return True
        return False

    def select_girl_lactating():
        lactating_people = []
        for person in [x for x in mc.business.get_employee_list() if x.is_available() and x.lactation_sources > 0]:
            lactating_people.append(person)
        if len(lactating_people) == 0:
            return None
        return get_random_from_list(lactating_people)

    milk_employee_crisis = ActionMod("Employee Needs Milked",milk_employee_requirement,"milk_employee_crisis_label",
        menu_tooltip = "An employee is struggling to milk herself.", category = "Business", is_crisis = True, crisis_weight = milk_employee_crisis_weight)

label milk_employee_crisis_label():
    $ the_person = select_girl_lactating()
    if the_person is None:
        # "No one is lactating!"
        return

    $the_person.strip_outfit(exclude_lower = True, exclude_feet = True, delay = 0) #Make sure she is topless

    "You decide to take a quick break from what you are doing. You stand up and stretch your legs, and go for a quick walk."
    "While you are walking by the break room, you hear someone inside muttering to herself."
    the_person.char "These stupid pumps... I hate these things..."
    $ the_person.draw_person(position = "sitting")
    "Looking inside, you see [the_person.title] sitting at a table, a couple of breast pumps sitting in front of her."
    menu:
        "Ask how she is doing":
            pass
        "Leave her alone":
            "You decide to leave her to her pumping."
            return
    mc.name "Hey [the_person.title]. You doing okay in here?"
    if the_person.sluttiness_tier() == 0:  #She's a prude
        the_person.char "Oh! I'm sorry [the_person.mc_title]... I totally forgot I was just sitting here with my tits out..."
        "She quickly puts her clothes back on."
        $ the_person.apply_planned_outfit()
        $ the_person.draw_person(position = "sitting")
        mc.name "That's okay. This isn't medieval times, if you need to pump or whatever you can do it where you need."
        $ the_person.change_stats(happiness = 5, obedience = 3, love = 2)
        the_person.char "I know, I just don't normally do it somewhere quite this public. I'm trying to build up a milk supply, but these stupid pumps are awful."
        mc.name "I understand. Anything I can do to help?"
        the_person.char "No sir, I'll try to be more discrete in the future."
        mc.name "Like I said, don't feel like you have to, but I also respect your privacy."
    elif the_person.sluttiness_tier() == 1: #She's a little slutty.
        the_person.char "Hey [the_person.mc_title]. Just giving my poor chest a break from these awful pumps. I hate these things."
        mc.name "Plastic and silicone is certainly no substitute for human interaction."
        the_person.char "Yeah... I think I'm just going to hand express this time."
        "She grabs one of the plastic containers from the table, then grabs one of her boobs in her hand and starts to squeeze until her milky cream starts to drip from it in to the container."
        the_person.char "I'm trying to build up my supply some. It's nice working somewhere I can take a few minutes a couple times a day to do something like this."
        mc.name "Of course. This isn't medieval times, if you need to pump or whatever you can do it when and where you need."
        $ the_person.change_stats(obedience = 3, slut_temp = 3, slut_core = 3)
        "You watch intently as she continues to milk herself. She seems to like the attention."
    elif the_person.sluttiness_tier() == 2:
        the_person.char "Hey [the_person.mc_title]. My tits are so sore from these stupid pumps. I wish there was an easier way to do this."
        mc.name "Easier? Well I would be glad to help."
        the_person.char "Oh, would you? The plastic and silicone in these things are so irritating... A nice set of manly hands would be amazing..."
        mc.name "Of course, I would be glad to."
        "You step around behind [the_person.possessive_title] while she picks up her milk containers and puts them up against her chest."
        mc.name "Plus, this will be a bit faster than if you did it by hand, since I can milk both at the same time."
        the_person.char "Exactly! All in the name of efficiency!"
        "You put your hands on her engorged mammaries. The skin is hot and feels like its pulled tight, her tits are so full of milk."
        the_person.char "Aahhh... I mean... it feels really good too..."
        "You start to squeeze them in rhythm. First one, then the other. It takes several seconds, but soon milk starts to dribble out of the tip."
        # We don't have access to multiple lactation sources yet, but assume at some point we can make cows that can really crank out milk
        if the_person.lactation_sources > 2:
            "[the_person.title] gives a moan, and the floodgates open as her breasts let down. Milk is now coming out in a steady stream from both tits, and everytime you squeeze it spurts out forcefully."
            the_person.char "Oh god... that feels so good..."
            $ the_person.change_arousal(20)
            "[the_person.possessive_title] is panting as her tits rapidly fill the milk containers. She is expressing an impressive amount."
        else:
            "[the_person.title] gives a moan as she lets down. Now with each squeeze, her nipples emit a short but steady squirt."
            the_person.char "Mmm, that feels so good..."
            $ the_person.change_arousal(10)
        $ the_person.change_stats(happiness = 5, slut_temp = 3, slut_core = 3)
        "Eventually the bottles fill up and the milk being expressed with each grope is decreasing."
        the_person.char "Mmm... thanks... you can stop now. If you want to..."
        menu:
            "Keep groping her":
                mc.name "I don't think I want to stop yet."
                call fuck_person(the_person, start_position = standing_grope ) from _milking_cowgirl_02
            "Let her go":
                "You hesitantly let go of her body."

    else:
        the_person.char "My tits are so sore from these stupid pumps. I need to make sure I'm pumping multiple times a day to keep my supply up."
        the_person.char "Would you be willing to help me out? It would be nice to have something a little softer than these plastic things."
        mc.name "I can help, what would you like me to do?"
        the_person.char "Can you milk me? You could use your hands, or even suckle if you want to."
        mc.name "A mid day snack sounds perfect."
        the_person.char "Come here and sit next to me."
        "You sit down next to [the_person.title] in an awkward move, she gently lowers you on to her lap. You look up at her full, milk laden tits hungrily."
        "You bring your lips to her nipple and begin to suckle. Tiny drips begin to escape it, giving you a taste of milk."
        $ the_person.change_arousal(10)
        the_person.char "Mmm, that's it. Don't worry, I'll let down in a second..."
        if the_person.lactation_sources > 2:
            "Suddenly, the milk begins to flow much more rapidly as [the_person.possessive_title] starts to let down. Milk is pouring into your mouth at an alarming rate."
            "You quickly swallow gulp after gulp, just keeping up with her production. Her milk is smooth, sweet, and creamy."
            $ the_person.change_arousal(25)
            $ mc.arousal += 15              #Fun for everyone
            the_person.char "Oh my god, yes that's it."
            "Her hand is running through your hair. It is a very intimate encounter to suckle from her like this."
        else:
            "[the_person.possessive_title] milk starts to flow more freely as she lets down. You are able to spend a few seconds at a time sucking, swallow, then repeat."
            "Her milk is smooth, sweet, and creamy."
            $ the_person.change_arousal(15)
            $ mc.arousal += 10              #Fun for everyone
            the_person.char "Mmm, that feels really nice..."
        "She takes one of your hands and puts it on her other breast."
        the_person.char "Here... squeeze this side too..."
        "She holds one of the milk containers up as your begin to squeeze. Soon, droplets of milk are beginning to drip from her other breast."
        if the_person.lactation_sources > 2:
            the_person.char "Oh... oh that's so good..."
            "Her other breast let's down and begins to spray milk into the bottle. With each squeeze it comes out forcefully, but never stops spraying."
            "One hand continues to run through your hair, while her other hand holds the bottle. You look up and see her eyes are closed as she enjoys her milking."
            $ the_person.change_arousal(25)
            $ mc.arousal += 15
        else:
            the_person.char "Oh my god, yes that's it..."
            "Her other breast lets down. With each squeeze it sprays into the bottle, and in between squeezes her milk still slowly dribbles out."
            "She holds the bottle carefully, collecting the milk from one side, while you consume the milk from the other. You look up and see her eyes are closed as she enjoys her milking."
            $ the_person.change_arousal(15)
            $ mc.arousal += 10
        "You enjoy drinking deep from [the_person.possessive_title]'s breast. When her supply is depleted, you sit back up, feeling energized from your fresh serving of milk."
        $ mc.change_energy(50)
        $ the_person.change_stats(obedience = 5, slut_temp = 3, slut_core = 3)
        the_person.char "Thank you so much, you have no idea how much I needed that..."
        "[the_person.title] notices your erection."
        the_person.char "So... want me to return the favor? Looks like you could use a little release too."
        "She puts her hand on your crotch and begins to run it through your pants."
        menu:
            "Relieve your pressure":
                mc.name "That sounds nice to me!"
                the_person.char "Mmm. Just lay back, I'll take care of everything!"
                $ the_person.strip_outfit()
                # call fuck_person(the_person, start_position = cowgirl, start_object = make_desk(), girl_in_charge = True) from _milking_cowgirl_01
                call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, start_object = make_desk(), allow_continue = True) from _milking_cowgirl_01
            "Get back to work":
                mc.name "I need to get back to work, but I'll take you up on that another time."
    "Once you are finished, you leave [the_person.title] in the break room and get back to work."
    $ the_person.apply_planned_outfit()
    $ mc.location.show_background()
    $ clear_scene()
    return
