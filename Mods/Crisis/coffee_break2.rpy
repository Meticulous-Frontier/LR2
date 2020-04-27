## Coffee Break 2 Crisis Mod by Tristimdorion
init -1 python:
    coffee_break2_weight = 5

init 2 python:
    def coffee_break2_requirement():
        if not mc.business.is_weekend():
            if mc.is_at_work():
                if time_of_day > 0 and time_of_day < 4: # only during morning afternoon or evening
                    if len(mc.business.get_requirement_employee_list(slut_required = 20)) >= 3:
                        return True
        return False

    coffee_break2_action = ActionMod("Coffee Break 2", coffee_break2_requirement, "coffee_break2_action_label",
        menu_tooltip = "A group of employees is having a coffee break.", category = "Business", is_crisis = True, crisis_weight = coffee_break2_weight)

label coffee_break2_action_label:
    $ (person_one, person_two, person_three) = get_random_employees(3, slut_required = 20)

    mc.name "As you are walking around the office, you see several employees at the coffee machine. They haven't noticed you, but you can hear what they are saying."
    call coffee_break2_food_delivery_label(person_one, person_two, person_three) from _call_coffee_break2_food_delivery_label_1

    python:
        mc.location.show_background()
        # Release variables
        del person_one
        del person_two
        del person_three
    return "Advance Time"

label coffee_break2_food_delivery_label(person_one, person_two, person_three):
    python:
        office.show_background()
        scene_manager = Scene()
        scene_manager.add_actor(person_one, emotion="default", character_placement = character_left_flipped)
        scene_manager.add_actor(person_two, emotion="default", character_placement = character_center_flipped)
        scene_manager.add_actor(person_three, emotion="default")
        scene_manager.draw_scene()

        loser_index = renpy.random.randint(0, 2)
        if loser_index == 0:
            loser = person_one
            winner_one = person_two
            winner_two = person_three
        elif loser_index == 1:
            loser = person_two
            winner_one = person_one
            winner_two = person_three
        else:
            loser = person_three
            winner_one = person_one
            winner_two = person_two

    winner_one.char "Ok, listen up girls, whoever gets the shortest straw will pickup the food from the delivery guy in the lobby."
    $ scene_manager.update_actor(winner_two, emotion = "happy")
    "[winner_two.possessive_title] draws a long straw."
    winner_one.char "Right, [loser.name], it's between you and me now, pick one."
    $ scene_manager.update_actor(winner_one, emotion = "happy")
    $ scene_manager.update_actor(loser, emotion = "sad")
    "[loser.possessive_title] draws the short straw."
    winner_two.char "Don't forget [loser.name], you have to take of some clothes before you pickup the food."
    if loser.sluttiness >= 40:
        $ scene_manager.update_actor(loser, emotion = "happy")
        loser.char "Great, let's give this guy a show!"
        $ loser.change_slut_temp(5)

        if loser.sluttiness >= 60:
            $ scene_manager.update_actor(winner_one, position = "walking_away")
            $ scene_manager.update_actor(winner_two, position = "walking_away")
            "As [loser.possessive_title] turns around, she walks right into you."
            loser.char "Hey [mc.name] do you mind helping me out real quick?"
            $ scene_manager.remove_actor(winner_one)
            $ scene_manager.remove_actor(winner_two)

            menu:
                "Help her":
                    loser.char "Awesome! Cum on my face real quick. The delivery guy just pulled into the parking lot."
                    $ scene_manager.update_actor(loser, position = "blowjob")
                    "[loser.possessive_title] gives you a quick blowjob and you splatter your cum all over her face, she smears it around and into her hair for added effect."
                    $ loser.cum_on_face()
                    $ scene_manager.update_actor(loser, position = "standing")
                    loser.char "Thanks, these delivery boys love it when I do this."
                "Refuse":
                    loser.char "Aww you're no fun, [loser.mc_title]. If he makes me pay this time it's your fault."

            "You watch as [loser.possessive_title] strips down."
            $ scene_manager.strip_actor_outfit_to_max_sluttiness(loser, temp_sluttiness_boost = 40)

            # TODO: Figure out how to keep the cum on the face, just calling the cum_on_face() method does not work ????
            "She gives you a wink and turns around to pickup the food."
            $ scene_manager.update_actor(loser, position = "walking_away")

            if loser.sluttiness >= 90 and loser.outfit.vagina_visible():
                "When [loser.possessive_title] reaches the lobby she pulls the sweaty guy into an empty office."
                loser.char "I left my purse at my desk. I can go get it... or maybe I could pay another way."
                $ scene_manager.update_actor(loser, position = "standing_doggy")
                "[loser.possessive_title] turns around and presents herself, the sweaty guy quickly drops his pants and pushes his cock against her pussy."
                loser.char "Oh, hard already. We must be getting so predictable."
                "The delivery man begins thrusting as hard and fast as he can. He seems to be in a hurry to finish and get back to work."
                loser.char "Ah yes, fill me up. Fuck me you sweaty pig."
                "His face turns bright red as he pushes [loser.possessive_title]'s face into the desk."
                loser.char "Oh yes. I'm cumming!"
                $ loser.change_stats(slut_temp = 3, slut_core = 3)
                "He finishes leaving her quivering against the desk. As he walks away he says: 'Enjoy your food, slut!'"
                $ loser.cum_on_ass()
                "She gathers her clothes and takes the food back to her colleagues. "
                $ scene_manager.update_actor(loser, position = "walking_away")
                if winner_one.sluttiness > 60 and winner_two.sluttiness > 60:
                    "You are thoroughly turned on after witnessing these events. You follow [loser.possessive_title] as she takes the delivery to the break room."
                    $ scene_manager.update_actor(loser, character_placement = character_center_flipped)
                    "She steps into the break room and sets the food on the table."
                    loser.char "Lunch is here!"
                    $ scene_manager.add_actor(winner_one, emotion="happy", character_placement = character_left_flipped)
                    $ scene_manager.add_actor(winner_two, emotion="happy")
                    "You enter the room and see [winner_one.title] and [winner_two.title] waiting. They see you enter the room and fall silent."
                    "You start to walk up behind [loser.title] and quietly start to take your dick out of your pants."
                    loser.char "Hey, I see the food is here, why are you two acting so funny?"
                    mc.name "That was quite the show [loser.title]."
                    $ scene_manager.update_actor(loser, position = "back_peek")
                    "You put your hands on her hips, her ass still slick with the delivery guy's cum."
                    mc.name "I only got to cum on your face, it doesn't seem right the delivery guy got more than me."
                    loser.char "Hey now, it's not like that, you know you can claim me anytime you want, we just looking for some free... FUCK"
                    "You grab her hips and ram yourself forward into [loser.possessive_title]'s sopping wet pussy."
                    if winner_one.sluttiness > 90 and winner_one.outfit.vagina_visible():
                        winner_one.char "Holy shit he's gonna fuck her right here!"
                        $ scene_manager.update_actor(winner_one, position = "kneeling1")
                        "While watching you, [winner_one.title] begins to touch herself and masturbate."
                        $ winner_two.change_happiness(3)
                        $ winner_two.change_slut_temp(5)
                    else:
                        winner_one.char "Holy!... Wow I was not expecting this!"
                        "[winner_one.title] watches you closely."
                    "You pound [loser.title] hard. She so wet from her earlier sex that you easily slide in and out of her."
                    "You look down and see the soft wet lips of her labia gripping and pulling at you everytime you start to slide out. It feels amazing."
                    if winner_two.sluttiness > 90 and winner_two.get_opinion_score("public sex") > 0:
                        winner_two.char "Fuck yeah! Give it to her good [winner_two.mc_title]!"
                        "[winner_two.title] is watching intently, cheering you on as you give it to [loser.possessive_title]."
                        $ winner_two.change_happiness(3)
                        $ winner_two.change_slut_temp(5)
                    else:
                        winner_two.char "Wow, that looks like it feels good..."
                        "[winner_two.title] is watching intently."
                    loser.char "Oh god... I'm gonna... It's so good!"
                    $ scene_manager.update_actor(loser, position = "standing_doggy")
                    "[loser.title] bends over the lunch table and pushes herself back against you as she orgasms."
                    loser.char "Yes... YES!!!"
                    "Her pussy clenching you drives you over the edge as well. You ram yourself deep and dump your cum inside of her."
                    $ loser.cum_in_vagina()
                    "You pull out and look at [loser.possessive_title]. She has cum on her face, on her ass, and now running down the inside of her legs as your seed spills out of her."
                    $ mc.listener_system.fire_event("girl_climax", the_person = loser, the_position = "standing_doggy")
                    $ loser.change_stats(obedience = 5, happiness = 5, love = 3, slut_temp = 5, slut_core = 2)
                    if winner_one.sluttiness > 90 and winner_one.outfit.vagina_visible():
                        winner_one.char "Oh god, so hot..."
                        "[winner_one.title] can't help herself. She is so turned on watching, she makes herself cum."
                        winner_one.char "Oh Fuck!"
                        $ mc.listener_system.fire_event("girl_climax", the_person = winner_one, the_position = "kneeling1")
                        $ winner_one.change_stats(obedience = 5,slut_temp = 5, slut_core = 2)
                    if winner_two.sluttiness > 90 and winner_two.get_opinion_score("public sex") > 0:
                        winner_two.char "God... Damn... maybe next time I can set it up so I get the short straw."
                    "You turn and walk out of the room without saying a word. You can feel the three girls looking at you as you leave the room."

                else:
                    "While enjoying the view you decide to go back to work."
            else:
                $ scene_manager.update_actor(loser, position = "back_peek")
                "Seems he has seen this before since he doesn't move a muscle when she looks back in your direction."
                $ scene_manager.update_actor(loser, position = "walking_away")
                "While enjoying the view you decide to go back to work."
        else:
            "You watch as [loser.possessive_title] strips down."
            $ scene_manager.strip_actor_outfit_to_max_sluttiness(loser, temp_sluttiness_boost = 40)
            "[loser.possessive_title] turns around walking down to the lobby to pick up the food."
            $ scene_manager.update_actor(loser, position = "walking_away")
            "You decide to go back to work and let the girls sort this out."

    else:
        loser.char "This is not fair [winner_one.name], you wanted me to loose."
        winner_one.char "No I didn't. And you know the rules!"

        $ scene_manager.update_actor(loser, emotion = "angry")
        # the loser feels betrayed by winner_one who is holding the straws
        $ town_relationships.worsen_relationship(winner_one, loser)

        loser.char "Fine, I'll do it but only my top and if I get it a third time in a row I swear..."
        # strip at least one item
        $ the_clothing = loser.outfit.get_upper_top_layer()
        if the_clothing:
            $ loser.draw_animated_removal(the_clothing)
            $ the_clothing = None
        # do we strip more?
        $ scene_manager.strip_actor_outfit_to_max_sluttiness(loser, exclude_lower = True, temp_sluttiness_boost = 10)
        if loser.outfit.tits_visible():
            "[loser.possessive_title] sheepishly walks down the lobby trying to cover her breasts."
        else:
            "[loser.possessive_title] sheepishly walks down the lobby."
        $ scene_manager.update_actor(loser, position = "walking_away")
        "The other girls stand back and watch, giggling amongst themselves."
        $ loser.change_slut_temp(5)
        $ scene_manager.remove_actor(loser)
        "You walk up to [winner_one.possessive_title] and [winner_two.possessive_title]."
        mc.name "Ok, girls you had your fun, now back to work."
        winner_two.char "Yes [winner_two.mc_title], right away."
        $ scene_manager.update_actor(winner_one, position = "walking_away")
        $ scene_manager.update_actor(winner_two, position = "walking_away")
        $ winner_one.change_happiness(2)
        $ winner_two.change_happiness(2)
        "Although not professional, you can't help but smile and enjoy the situation."

    python: # Release variables
        del winner_one
        del winner_two
        del loser
        scene_manager.clear_scene()
    return "Advance Time"
