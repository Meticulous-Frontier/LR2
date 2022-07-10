# Enhance Cat Fight with multi person rendering and updated dialog

init 5 python:
    config.label_overrides["cat_fight_crisis_label"] = "cat_fight_crisis_enhanced_label"

    def cat_fight_crisis_get_girls():
        the_relationship = get_random_from_list(town_relationships.get_business_relationships(["Rival","Nemesis"])) #Get a random rival or nemesis relationship within the company
        if the_relationship is None:
            return (None, None)

        if renpy.random.randint(0,1) == 1: #Randomize the order so that repeated events with the same people alternate who is person_one and two.
            person_one = the_relationship.person_a
            person_two = the_relationship.person_b
        else:
            person_one = the_relationship.person_b
            person_two = the_relationship.person_a
        return (person_one, person_two)

label cat_fight_crisis_enhanced_label():
    #Two girls have an argument. Side with one over the other or neither (for about break even cost). At higher sluttiness have them kiss and make up.
    if not cat_fight_crisis_requirement(): #If something has changed since we added this crisis as a valid one just return. Should not happen often.
        return

    python:
        (person_one, person_two) = cat_fight_crisis_get_girls()
        if not person_one or not person_two:
            renpy.return_statement() #Just in case something goes wrong getting a relationship we'll exit gracefully.
        scene_manager = Scene()

    person_one "Excuse me, [person_one.mc_title]?"
    $ scene_manager.add_actor(person_one, emotion = "angry")
    $ scene_manager.add_actor(person_two, emotion = "angry", display_transform = character_center_flipped)
    "You feel a tap on your back while you're working. [person_one.title] and [person_two.title] are glaring at each other while they wait to get your attention."
    person_one "I was just in the break room and saw [person_two.fname] digging around in the fridge looking for other people's lunches."
    $ scene_manager.update_actor(person_two, position = "stand4")
    person_two "That's a lie and you know it! I was looking for my own lunch and you're just trying to get me in trouble!"
    "[person_two.title] looks at you and pleads."
    person_two "You have to believe me, [person_one.fname] is making all of this up! That's just the kind of thing she would do, too."
    $ scene_manager.update_actor(person_one, position = "stand4")
    if person_two.sluttiness > 50:
        person_one "Jesus, why don't you just suck his cock and get it over with. That's how you normally convince people, right?"
    else:
        person_one "Oh boo hoo, you got caught and now you're going to get in trouble. Jesus, is this what you're always like?"
    $ scene_manager.update_actor(person_two, position = "stand3")
    "[person_two.title] spins to glare at [person_one.title]."
    if person_one.sluttiness > 50:
        person_two "At least I'm not slave to some guy's dick like you are. You're such a worthless slut."
    else:
        person_two "Oh fuck you. You're just a stuck up bitch, you know that?"

    $ scene_manager.update_actor(person_one, position = "stand2")
    menu:
        "Side with [person_one.fname]":
            #Obedience and happiness boost to p1, reduction for p2
            call cat_fight_pick_winner_enhanced(scene_manager, person_one, person_two) from _call_cat_fight_pick_winner_enhanced_1


        "Side with [person_two.fname]":
            #Obedience and happiness boost to p2, reductio n for p1
            call cat_fight_pick_winner_enhanced(scene_manager, person_two, person_one) from _call_cat_fight_pick_winner_enhanced_2


        "Stop the argument, side with no one":
            #Obedience boost to both, happiness drop to both. At high sluttiness have them "kiss and make up"
            mc.name "Enough! I can't be the arbitrator for every single conflict we have in this office. You two are going to have to figure this out between yourselves."
            $ scene_manager.update_actor(person_one, emotion="sad")
            person_one "But sir..."
            if person_one.sluttiness > 50 and person_two.sluttiness > 50:
                mc.name "I said enough. Clearly you need help sorting this out."
                "You stand up and take [person_one.title]'s hand in your right hand, then take [person_two.title]'s hand in your left."
                mc.name "The two of you are part of a larger team. I need you to work together."
                "You bring the girls hands together and wrap yours around both of theirs."
                person_one "Sorry sir, you're right."
                $ scene_manager.update_actor(person_two, emotion="sad")
                person_two "You're right, I'm sorry sir. And I'm sorry [person_one.fname]."
                "You bring your hands back, leaving [person_one.title] and [person_two.title] holding hands. They look away from each other sheepishly."
                mc.name "Good to hear. Now kiss and make up, then you can get back to work."
                "The girls glance at you, then at each other. After a moment of hesitation [person_two.title] leans forward and kisses [person_one.title] on the lips."
                $ scene_manager.update_actor(person_one, position = "kissing", emotion="default")
                $ scene_manager.update_actor(person_two, position = "kissing", emotion="default")
                "You watch for a moment as your two employees kiss next to your desk. What starts out as a gentle peck turns into a deep, heavy kiss."
                $ scene_manager.update_actor(person_one, position = "stand3")
                $ scene_manager.update_actor(person_two, position = "stand2")
                "[person_one.title] breaks the kiss and steps back, blushing and panting softly."
                $ person_one.change_stats(obedience = 5, slut = 1, max_slut = 65)
                person_one.name "I should... I should get back to work. Sorry for causing any trouble."
                $ scene_manager.update_actor(person_one, position = "walking_away")
                $ scene_manager.update_actor(person_two, emotion = "happy")
                "[person_two.title] watches [person_one.title] leave, eyes lingering on her ass as she walks away."
                $ scene_manager.remove_actor(person_one)
                mc.name "Go on, you should get back to work too."
                $ person_two.change_stats(obedience = 5, slut = 1, max_slut = 65)
                $ scene_manager.update_actor(person_two, position = "back_peek")
                "You give [person_two.title] a light slap on the butt to pull her attention back to you. She nods quickly and heads the other way."
            else:
                mc.name "I said enough. Now do you need my help talking this out?"
                $ person_one.change_stats(happiness = -5, obedience = 5)
                $ scene_manager.update_actor(person_one, emotion="sad")
                person_one "No sir, I think we will be alright."
                $ person_two.change_stats(happiness = -5, obedience = 5)
                $ scene_manager.update_actor(person_two, emotion="sad")
                person_two "Understood sir, there won't be any more problems."
                mc.name "Good to hear. Now get back to work."
                $ scene_manager.update_actor(person_one, position = "walking_away")
                $ scene_manager.update_actor(person_two, position = "walking_away")
                "You watch them both walking off in a different direction."

        "Stay silent and let them fight it out":
            "Both of the girls look at you, waiting to see who's side you take."
            mc.name "This isn't my fight. You two are going to have to sort this out yourselves."
            if renpy.random.randint(0,1) == 0: #Establish a winner and loser for the fight, random here so that the earlieer section of the event doesn't suggest which one it is.
                $ winner = person_one
                $ loser = person_two
            else:
                $ winner = person_two
                $ loser = person_one

            winner "Hear that? We're going to have to sort this out, right here. Right now."
            "[winner.title] takes a step towards [loser.title], invading her personal space."
            $ scene_manager.update_actor(loser, position = "stand5")
            loser "What, is that supposed to scare me? Back up."
            "[loser.title] plants a hand on [winner.title]'s chest and shoves her backwards. [winner.title] stumbles a step and bumps into a desk behind her."
            $ scene_manager.update_actor(loser, position = "stand4")
            $ scene_manager.update_actor(winner, position = "stand5")
            winner "Oh that's fucking IT! COME HERE BITCH!"
            "[winner.title] throws herself at [loser.title]. Before you can say anything else they're grabbing at each others hair, yelling and screaming as they bounce around the office."
            $ scene_manager.update_actor(winner, position = "stand3")
            #Random piece of clothing is lost from a random member of the fight, after which time they run off to get things organised again.
            $ the_clothing = loser.choose_strip_clothing_item()

            if person_one.sluttiness < 40 or person_two.sluttiness < 40:
                #Catfight starts! Neither is particularly slutty, fight ends once one has their clothing damaged (if they're wearing some clothing, make sure to account for that).
                $ the_clothing = loser.choose_strip_clothing_item()
                if the_clothing:
                    "While they fight [winner.title] gets a hold of [loser.title]'s [the_clothing.name]. She tugs on it hard while she swings [loser.title] around and there's a loud rip."
                    $ scene_manager.draw_animated_removal(loser, the_clothing)
                    loser "Ugh, look what you've done! Give that back!"
                    "[winner.title] throws the torn garment to [loser.title] and smiles in victory."
                    $ scene_manager.update_actor(winner, emotion = "happy")
                    winner "I hope that teaches you a lesson."
                    $ scene_manager.update_actor(loser, emotion = "sad")
                    $ loser.change_stats(obedience = -5, happiness = -5)
                    loser "Fuck you. Bitch."
                    $ scene_manager.update_actor(loser, position = "walking_away")
                    "[loser.title] grabs her [the_clothing.name] and hurries off to find somewhere private."
                    $ scene_manager.remove_actor(loser)
                    $ winner.change_stats(obedience = -5, happiness = 5)
                    "[winner.title] looks at you, out of breath but obviously a little smug."
                    winner "Sorry sir, I won't let her get out of line like that again."
                    $ scene_manager.update_actor(winner, position = "walking_away")
                    "She smooths her hair back and gets back to work. You decide to do the same."
                else:
                    "After a minute of fighting [winner.title] gets her hands on [loser.title]'s hair and yanks on it hard. [loser.title] yells and struggles, but it's clear she's lost."
                    $ scene_manager.update_actor(loser, emotion = "sad")
                    loser "Fine! Fine, you win!"
                    $ scene_manager.update_actor(winner, emotion = "happy")
                    "[winner.title] pushes [loser.title] away from her and smiles in victory."
                    winner "I hope that teaches you a lesson."
                    $ loser.change_stats(obedience = -5, happiness = -5)
                    loser "Fuck you. Bitch."
                    $ scene_manager.update_actor(loser, position = "walking_away")
                    "[loser.title] storms off to find somewhere private to nurse her wounds."
                    $ scene_manager.remove_actor(loser)
                    $ winner.change_stats(obedience = -5, happiness = 5)
                    $ scene_manager.update_actor(winner, position = "stand2")
                    "[winner.title] looks at you, out of breath but obviously a little smug."
                    winner "Sorry sir, I won't let her get out of line like that again."
                    $ scene_manager.update_actor(winner, position = "walking_away")
                    "She smooths her hair back and gets back to work. You decide to do the same."

            else: #both >= 40
                #Girls start pulling clothing off of each other on purpose until one is naked enough to be very embarrassed, then they give up.
                while the_clothing and loser.outfit.slut_requirement < 80:
                    $ ran_num = renpy.random.randint(0,3)
                    if ran_num == 0:
                        "[winner.title] grabs [loser.title] by the [the_clothing.name] and yanks her around. There's a loud rip and the piece of clothing comes free."
                        $ scene_manager.draw_animated_removal(loser, the_clothing)
                        loser "You bitch!"
                    elif ran_num == 1:
                        "[loser.title] circles around [winner.title], then runs forward yelling and screaming. [winner.title] pushes her to the side, then grabs her by the [the_clothing.name] and tries to pull her to the ground."
                        "The girls struggle until [loser.title]'s [the_clothing.name] comes free and they separate. [winner.title] drops it to the ground."
                        $ scene_manager.draw_animated_removal(loser, the_clothing)
                        loser "You'll pay for that, slut!"
                    elif ran_num == 2:
                        "[winner.title] and [loser.title] collide, screaming profanities at each other."
                        "You aren't sure exactly what happens, but when they separate [winner.title] is holding a piece of fabric that used to be [loser.title]'s [the_clothing.name]."
                        $ scene_manager.draw_animated_removal(loser, the_clothing)
                        loser "Is that all you've got?"
                    else: #ran_num == 3
                        "[loser.title] gets an arm around [winner.title]'s waist and pushes her against a desk. The two grapple for a moment, then [winner.title] grabs [loser.title] by the [the_clothing.name] and pulls until the piece of clothing rips off."
                        $ scene_manager.draw_animated_removal(loser, the_clothing)
                        loser "Fuck, you're going to pay for that!"

                    $ mc.change_locked_clarity(10)
                    $ ran_num = renpy.random.randint(0,2)
                    $ other_clothing = winner.choose_strip_clothing_item()

                    if ran_num == 0: #Doesn't actually return the favour, because she's the loser she only retaliates %66 of the time.
                        "[winner.title] laughs and crouches low."
                        winner "Come on! Come and get it, you cock sucking whore!"
                    elif ran_num == 1:
                        winner "Do you think I'm afraid of you? Come on!"
                        if other_clothing:
                            "[winner.title] rushes forward and grabs at [loser.title]. [loser.title] manages to get the upper hand, grabbing onto [winner.title]'s [other_clothing.name] and whipping her around. With a sharp rip it comes free."
                            $ scene_manager.draw_animated_removal(winner, other_clothing)
                            $ mc.change_locked_clarity(10)
                            winner "Shit, get over here you skank!"

                    elif ran_num == 2:
                        if other_clothing:
                            $ scene_manager.draw_animated_removal(winner, other_clothing)
                            "[winner.title] screams loudly and tries to grab [loser.title] by the waist. [loser.title] is fast enough to get to the side. She grabs [winner.title]'s [other_clothing.name] and yanks on it hard."
                            "[winner.title] struggles for a moment, then manages to slip free of the garment and steps back. [loser.title] drops it to the ground and they square off again."
                            $ mc.change_locked_clarity(10)
                        else:
                            "[winner.title] screams loudly and tries to grab [loser.title] by the waist. [loser.title] is fast enough to get out of the way, and they square off again as the fight continues."

                    $ the_clothing = loser.choose_strip_clothing_item()
                $ other_clothing = None
                $ the_clothing = None
                $ scene_manager.update_actor(loser, emotion = "sad")
                "[loser.title] looks down at herself. She seems to realize for the first time how little she's wearing now."
                loser "Look what you've done! Oh god, I need to... I need to go!"
                if loser.sluttiness > 80 and winner.sluttiness > 80:
                    $ scene_manager.update_actor(loser, position = "walking_away")
                    "[loser.title] turns to hurry away, but [winner.title] swoops in and grabs her from behind."
                    $ scene_manager.update_actor(loser, position = "against_wall")
                    loser "Hey!"
                    winner "You're not going anywhere, not yet!"
                    $ scene_manager.update_actor(winner, position = "stand3", emotion = "happy")
                    "[winner.title] reaches a hand down between [loser.title]'s legs, running her finger over her coworker's pussy."
                    $ loser.change_arousal(5) #The girls arousal gain is the base gain + 10% per the characters skill in that category.
                    loser "Hey... that's not fair! I... ah..."
                    $ scene_manager.update_actor(loser, position = "missionary")
                    "[loser.title] stops fighting almost immediately, leaning against [winner.title] and breathing heavily. You've got a front row seat as [winner.title] starts to finger [loser.title]."
                    $ mc.change_locked_clarity(20)
                    $ loser.change_arousal(15)
                    loser "Oh god... [winner.fname], just... Ah!"
                    "[winner.title] isn't going easy on [loser.title]. She shivers and bucks against [winner.title]."
                    $ loser.change_arousal(25)
                    "[winner.title] speeds up, pumping her fingers in and out of [loser.title]'s exposed cunt. She moans loudly and rolls her hips against [winner.title]'s."
                    $ loser.change_arousal(25)
                    winner "You thought you could get away easy, huh? Well now I'm going to make you cum right here, you dirty little slut!"
                    $ loser.change_arousal(25)
                    "[loser.title] looks right into your eyes. She doesn't look embarrassed - in fact it looks like she's turned on by you watching her get finger banged right in the middle of the office."
                    $ mc.change_locked_clarity(20)
                    loser "I'm going to... I'm going to... AH!"
                    $ loser.change_arousal(25)
                    $ scene_manager.update_actor(loser, emotion = "orgasm")
                    winner "That's it, cum for me slut!"
                    $ loser.have_orgasm()
                    "[loser.title] screams loudly and shivers wildly. She only stays on her feet because [winner.title] is holding her in place."
                    $ loser.change_stats(obedience = -5)
                    $ scene_manager.update_actor(loser, position = "sitting", emotion = "default")
                    "[winner.title] holds [loser.title] up a little longer, then lets her go. [loser.title] stumbles forward on wobbly legs until she finds a chair to collapse into. She pants loudly."
                    $ mc.change_locked_clarity(20)
                    $ winner.change_stats(slut = 1, max_slut = 90, obedience = -5)
                    winner "There we go, that should have sorted her out. I'm sorry about that [winner.mc_title]."
                    mc.name "You did what you had to, I understand."
                    $ scene_manager.update_actor(winner, position = "walking_away")
                    "[winner.title] smiles proudly picks up her clothes and walks off."
                    $ scene_manager.remove_actor(winner)
                    $ scene_manager.update_actor(loser, position = "walking_away")
                    "It takes a few more minutes before [loser.title] is in a state to go anywhere. When she's able to she gathers her things and heads off to get cleaned up."
                else:
                    $ loser.change_stats(slut = 1, max_slut = 80, happiness = -10, obedience = -10)
                    $ scene_manager.update_actor(loser, position = "walking_away")
                    "[loser.title] gathers up what clothes she can from the ground, then hurries away to find somewhere private."
                    $ scene_manager.remove_actor(loser)
                    $ scene_manager.update_actor(winner, emotion = "happy")
                    "[winner.title] watches [loser.title] leave, panting heavily."
                    $ winner.change_stats(happiness = 10, obedience = -10)
                    winner "Hah... I knew I had that..."
                    "[winner.title] takes a look down at herself."
                    winner "I should probably go get cleaned up too. Sorry about all of this [winner.mc_title]."
                    $ scene_manager.update_actor(winner, position = "walking_away")
                    "[winner.title] leaves and you get back to work."
            $ del winner
            $ del loser

        "Punish them for inappropriate behaviour" if office_punishment.is_active():
            mc.name "[person_one.title], [person_two.title], I cannot tolerate that my employees are accusing each other of stealing."
            mc.name "I don't have any choice but to record you both for disciplinary actions later."
            $ person_one.add_infraction(Infraction.inappropriate_behaviour_factory())
            $ person_two.add_infraction(Infraction.inappropriate_behaviour_factory())
            $ scene_manager.update_actor(person_one, emotion = "sad")
            person_one "Really? I..."
            $ scene_manager.update_actor(person_two, emotion = "sad")
            person_two "See what happens when you go around making things up [person_one.fname]. Sorry [person_two.mc_title], we'll get back to work right away."
            person_one "Ugh, whatever. Come on [person_two.fname], let's go."
            $ scene_manager.update_actor(person_one, position = "walking_away")
            $ scene_manager.update_actor(person_two, position = "walking_away")
            "They turn and leave the room together."

        "Have a team building exercise" if willing_to_threesome(person_one, person_two) and mc.energy > 30:
            mc.name "Enough! It is obvious to me that we are spending too much time working against one another, and not enough working as a team."
            $ scene_manager.update_actor(person_one, emotion="sad")
            person_one "But sir..."
            mc.name "Don't \"but sir\" me! It's time for you two to do a team building exercise. On your knees, both of you."
            "They both look at each other, bewildered, but they do what you ask."
            $ scene_manager.update_actor(person_one, position = "blowjob")
            $ scene_manager.update_actor(person_two, position = "blowjob")
            "You unzip your pants and pull your cock out."
            $ mc.change_locked_clarity(30)
            mc.name "Alright, I want you two to cooperate, FOR ONCE, and team up on this."
            "Both girls seem relieved. While unorthodox, you are pretty sure their slutty natures will come out and they'll bond while they blow you."
            call start_threesome(person_one, person_two, start_position = threesome_double_blowjob, position_locked = True) from _team_building_threesome_1
            $ the_report = _return
            if the_report.get("guy orgasms", 0) > 0:
                "You watch as [person_one.title] and [person_two.title] begin to kiss and lick your cum off of each other's faces"
                "This turned out to be a success!"
                $ person_one.change_stats(obedience = 5, happiness = 5)
                $ person_two.change_stats(obedience = 5, happiness = 5)
                mc.name "See what you can do if you just work together? Go on now, get back to work."
                $ scene_manager.update_actor(person_one, position = "walking_away")
                $ scene_manager.update_actor(person_two, position = "walking_away")
                "You watch them both walking off together."
            else:
                "Frustrated, you put your cock away while admonishing them."
                mc.name "If you two can't work together on something as simple as sucking dick, how can you cooperate doing anything else?"
                $ person_one.change_stats(happiness = -5, obedience = 5)
                $ scene_manager.update_actor(person_one, emotion="sad")
                person_one "I'm sorry [person_one.mc_title]. It won't happen again!"
                $ person_two.change_stats(happiness = -5, obedience = 5)
                $ scene_manager.update_actor(person_two, emotion="sad")
                person_two "Understood [person_two.mc_title], there won't be any more problems."
                mc.name "Good to hear. Now get back to work."
                $ scene_manager.update_actor(person_one, position = "walking_away", display_transform = character_right)
                $ scene_manager.update_actor(person_two, position = "walking_away", display_transform = character_center_flipped)

            $ town_relationships.improve_relationship(person_one, person_two)

    python:     # Release variables
        scene_manager.clear_scene()
        the_clothing = None
        del person_one
        del person_two
    return


label cat_fight_pick_winner_enhanced(scene_manager, winner, loser):
    $ loser.change_stats(happiness = -5, obedience = -5)
    mc.name "Enough! [loser.title], I don't want to hear anything about this from you again. Consider this a formal warning."
    $ loser.add_infraction(Infraction.inappropriate_behaviour_factory())
    loser "Wait, but I..."
    mc.name "That's the end of it, now I want both of you to get back to work. Thank you for bringing this to my attention [winner.title]."
    $ winner.change_stats(happiness = 5, obedience = 5)
    winner "My pleasure [winner.mc_title], just trying to keep things orderly around here."
    $ scene_manager.update_actor(winner, position="walking_away")
    "[winner.title] shoots a smug look at [loser.title] then turns around and walks away."
    $ scene_manager.remove_actor(winner)
    $ scene_manager.update_actor(loser, position="walking_away")
    "[loser.title] shakes her head and storms off in the other direction."
    return
