#This is an expansion of the apron event. It's a shame you can't do more with Jennifer in the event when she is just in an apron...
init 1 python:

    def mom_fuck_during_housework_requirement(the_person):
        if the_person is not mom:
            return False
        if the_person not in kitchen.people:
            return False
        if the_person.effective_sluttiness() < 60:
            return False
        return True

    mom_fuck_during_housework = Action("Mom being naughty", mom_fuck_during_housework_requirement, "mom_fuck_during_housework_label", event_duration = 5)
    limited_time_event_pool.append([mom_fuck_during_housework,4,"on_enter"])


label mom_fuck_during_housework_label(the_person):
    $ the_person.apply_outfit(Outfit("Nude"))
    #$ the_person.outfit = Outfit("Nude") changed v0.24.1
    $ add_mom_outfit_coloured_apron(the_person)
    $ the_person.draw_person(position = "back_peek")
    "You find [the_person.possessive_title] in the kitchen, completely nude except for her apron. She's been doing this more and more lately."
    the_person.char "Hi [the_person.mc_title], I hope you've had a great day. Dinner should be ready soon!"
    "She turns back, wiggling her butt as she works. Her ass is supple. You are tempted to do something with it while she works..."
    menu:
        "Spank her{size=18}May increase submissiveness": #chance to increase her submissiveness based on if she orgasms and if she is currently suggestable.
            $ ass_desc = spanking_get_ass_description(the_person)
            "The swaying of [the_person.title]'s ass is hypnotic. It is [ass_desc]."
            mc.name "I don't mind you dressing like this, [the_person.title], but it is kind of naughty."
            "You step up behind her and start to run your hand along her hips."
            the_person.char "Ah, well, it definitely makes me feel kind of naughty..."
            call fuck_person(the_person, start_position = spanking) from _spank_mommy_during_housework_01
            $ the_report = _return
            if the_person.get_opinion_score("being submissive") < 2:
                if renpy.random.randint(0,100)< ( the_report.get("girl orgasms", 0) + the_person.suggestibility):  #Odds for improvement are 10% per orgasm plus suggestability.
                    the_person.char "Oh... it good to know I have a son who will discipline me if I get too naughty!"
                    $ the_person.increase_opinion_score("being submissive")
            elif not the_person.can_be_spanked():
                $ the_person.unlock_spanking()
                the_person.char "Oh god honey, it's amazing knowing I have such a good son, who keeps her naughty mother in line!"
                "She really seemed to enjoy her spanking. Maybe you should work it into your normal foreplay..."
            "It takes [the_person.possessive_title] a few moments, but she gets back to work, making dinner for the family."
        #TODO fuck her branch
        "Let her work":
            "You stomach growls. As much as you would like to take advantage of [the_person.title], you decide to let her work on dinner instead."

    return
