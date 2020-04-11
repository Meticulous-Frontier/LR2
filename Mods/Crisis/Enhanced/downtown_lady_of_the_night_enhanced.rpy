init 5 python:
    config.label_overrides["lady_of_the_night_label"] = "lady_of_the_night_label_enhanced"

label lady_of_the_night_label_enhanced():
    # You run into a lady who propositions you for money.
    $ the_person = create_hooker()

    "You're lost in thought when a female voice calls out to you."
    the_person.char "Excuse me, [the_person.mc_title]."
    $ the_person.draw_person()
    mc.name "Yes?"
    the_person.char "You're looking a little lonely all by yourself. Are you looking for a friend to keep you warm?"
    "Her tone suggests that her \"friendship\" won't come free."
    menu:
        "Pay her   -$200":
            $ the_person.generate_home()
            $ downtown.add_person(the_person) #If you pay her add her to the location so that she is kept track of in the future.
            mc.name "That sounds nice. It's nice to meet you..."
            $ the_person.set_title(get_random_title(the_person))
            $ the_person.set_possessive_title(get_random_possessive_title(the_person))
            the_person.char "You can call me [the_person.title]. For two hundred dollars I'll be your best friend for the next hour."
            $ mc.business.change_funds(-200)
            $ the_person.change_obedience(1)
            "The streets are quiet this time of night. You pull your wallet out and hand over the cash."
            "She takes it with a smile and tucks it away, then wraps herself around your arm."
            $ the_person.add_situational_obedience("prostitute", 40, "I'm being paid for this, I should do whatever he wants me to do.")
            call fuck_person(the_person, private = True, ignore_taboo = True) from _call_fuck_person_lady_of_the_night_enhanced
            $ the_report = _return
            $ the_person.clear_situational_obedience("prostitute")

            if the_report.get("girl orgasms",0) > 0:
                "It takes [the_person.title] a few moments to catch her breath."
                the_person.char "Maybe I should be paying you... Whew!"

            $ the_person.review_outfit()

            the_person.char "It's been fun, if you ever see me around maybe we can do this again."
            "She gives you a peck on the cheek, then turns and struts off into the night."

        "Say no":
            mc.name "Thanks for the offer, but no thanks."
            "She shrugs."
            the_person.char "Suit yourself."
            $ the_person.remove_person_from_game()

    $ renpy.scene("Active")
    return    