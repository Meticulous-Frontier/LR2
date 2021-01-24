# This is a hidden role designed to track changes in jealousy status in the sister pair Ashley and Stephanie
# In general, sexual actions performed with the non jeaouls girl increases jealousy score in the jealous sister
# when scores get high enough, jealous sister may approach MC looking for sex or force satisfaction.
# Possibly add an option to convince a girl to stop being so jealous



init 2 python:
    def jealous_sister_on_turn(person):
        pass
        return

    def jealous_sister_on_day(person): #Use this function to determine if she is going to act on jealous score.
        pass
        return

    def jealous_score(person):
        return person.event_triggers_dict.get("jealous_score", 0)

    def jealous_score_reset(person):
        person.event_triggers_dict["jealous_score"] = 0
        return

    def jealous_change_score(person, the_score):
        person.event_triggers_dict["jealous_score"] = person.event_triggers_dict.get("jealous_score", 0) + the_score
        return



    jealous_sister_role = Role("Jealous sister", [], hidden = True,  on_turn = jealous_sister_on_turn, on_move = None, on_day = jealous_sister_on_day)

    def assign_jealous_sister_role(person):
        person.event_triggers_dict["jealous_score"] = 0
        person.add_role(jealous_sister_role)
        return

    def is_jealous_sister(person):
        return person.has_role(jealous_sister_role)

    def girlfriend_wakeup_jealous_sister_requirement(the_person):
        if the_person == stephanie and is_jealous_sister(ashley):
            return True
        if the_person == ashley and is_jealous_sister(stephanie):
            return True
        return False


label girlfriend_wakeup_jealous_sister_label(the_person):
    $ jealous_sister = None
    if the_person == stephanie:
        $ jealous_sister = ashley
    else:
        $ jealous_sister = stephanie
    the_person "I'm gonna hop in the shower. Try not to miss me too much while I'm in there's okay?"
    "Of course."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.title] hops out of bed and heads to the shower. She stops at the door, then turns back and blows you a kiss."
    $ clear_scene()
    "[the_person.possessive_title] disappears behind the door as she closes it behind her. You can hear the shower turn on and you start to drift off to sleep again."
    "..."
    "You don't hear her come in, but the weight on the bed shifts. You open your eyes and see [jealous_sister.title], climbing on top of you."
    $ jealous_sister.draw_person(position = "cowgirl")
    #TODO make her actually naked
    "Her lower half is naked, and she straddles your hips with her cunt pressed against your rapidly hardening cock."
    "You start to say something, but ashley puts a finger on your lips."
    jealous_sister "Shhhh, if we're quiet, she'll never even know."
    "She leans forward and replaces her finger with her lips. She kisses you hungrily, making her need for you known."
    "Without breaking the kiss, she reaches down between you and grabs your dick, pointing it up. A quick movement of her hips, and your manhood slips inside of her."
    call get_fucked(jealous_sister, the_goal = "get off", start_position = cowgirl, skip_intro = True) from _jealous_sister_special_wakeup_01
    "As you are both recovering, you suddenly hear the water in the shower stop. [jealous_sister.possessive_title] quickly springs up, and quietly slips out the door, leaving you alone in [the_person.title]'s bed."
    $ clear_scene()
    "You take a few moments to make sure you are presentable. You don't want [the_person.title] to get suspicious... Soon the bathroom door opens."
    $ apply_towel_outfit(the_person)
    $ the_person.draw_person()
    "[the_person.title] walks in, wrapped in a towel."
    the_person "Mmm, that felt good. Do you want to shower now?"
    mc.name "No thanks, I'd probably better head out."
    the_person "Hmm, okay. Thanks for coming over last night... It was nice."
    $ clear_scene()
    "You get yourself dressed and say goodbye. You step out of [the_person.title]'s room and into the hall."
    $ jealous_sister.planned_outfit = jealous_sister.decide_on_outfit() # choose a new outfit for the day
    $ jealous_sister.apply_planned_outfit()
    $ jealous_sister.draw_person(position = "sitting")
    "As you walk to the door, you see [jealous_sister.title] at the table, having a cup of coffee and some toast."
    jealous_sister "Bye [jealous_sister.mc_title], hope you had a good time..."
    "She gives you a wink."
    mc.name "I definitely did. Take care [jealous_sister.title]"
    "You walk out the front door. Things in that place are crazy..."
    $ jealous_score_reset(jealous_sister)
    $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    $ the_person.apply_planned_outfit()
    return
