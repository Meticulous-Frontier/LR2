## Mom NTR Crisis Mod by Tristimdorion
# Based on the Pilotus13 Vanilla extension
init -1 python:
    mom_ntr_mod_weight = 5

init 2 python:
    def mom_ntr_mod_requirement():
        if mc_asleep() and day % 7 is not 4: # not on Friday nights
            if mom.sluttiness >=20:
                return True
        return False

    mom_ntr_mod_action = ActionMod("Mom NTR",mom_ntr_mod_requirement,"mom_ntr_mod_action_label",
        menu_tooltip = "At night you hear strange sounds out of [mom.possessive_title]'s bedroom", category = "NTR")
    crisis_list.append([mom_ntr_mod_action, mom_ntr_mod_weight])

label mom_ntr_mod_action_label:
    ## Mom having her private life
    $ the_person = mom
    "Some time late in the night, you're awoken by some noise down the hallway."
    "As it seems to go on and on, you decide to investigate."
    "You drag yourself out of bed and enter the hallway. There is some rustling in [the_person.possessive_title]'s bedroom."
    "The door seems to be not closed. You decide to take a peek."
    ## Now we determine which finising scenes are available depending on traits
    $ finishes = []
    if the_person.get_opinion_score("being covered in cum") > 0 or the_person.get_opinion_score("cum facials") > 0:
        $ finishes.append ("facial")
    if the_person.get_opinion_score("creampies") > 0 or the_person.get_opinion_score("risking getting pregnant") > 0:
        $ finishes.append ("inside")
    if the_person.get_opinion_score("giving blowjobs") > 0 or the_person.get_opinion_score("drinking cum") > 0:
        $ finishes.append ("drink")
    $ finishes.append ("usual")
    ## Submission check for additional lines related to that
    $ submissive = the_person.get_opinion_score("being submissive") > 0
    ## Love of BJ for additional scene at the beginning and maybe some additional scenes/dialog along the way
    $ bj = the_person.get_opinion_score("giving blowjobs") > 0
    ## Determine what type of encounter it is
    if the_person.sluttiness >= 60:
        $ encounter = renpy.random.randint (1,2)
    else:
        $ encounter = 1

    $ change_scene_display(bedroom)
    show screen person_info_ui(the_person)
    $ man_name = get_random_male_name()
    $ wife_name = get_random_name()
    while wife_name is the_person.name: ## Just to avoid stupid duplications
        $ wife_name = get_random_name()

    ## Now determine how many clothes mom will take off
    if the_person.sluttiness < 40:
        $ clothes_number = renpy.random.randint (1,3) ## so it will be random from 1 to 3
    elif the_person.sluttiness < 80:
        $ clothes_number = renpy.random.randint (1,4) ## so it will be random from 1 to 4
    else:
        $ clothes_number = renpy.random.randint (2,4) ## so it will be random from 2 to 4

    $ detected = renpy.random.randint(0,2) == 1 #33% chance of detection.
    ## Now determine how many clothes mom will take off
    if encounter is 1: ## a scene with one man
        if bj:
            $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
            "You take a look inside the room and your eyes widen. You see [the_person.possessive_title] sitting in front of an unknown man, sucking his cock."
            "By the look on man's face you can tell that he is also quite surprised."
            "As they go on, you seem to recognise him. It's [man_name], one of [the_person.title]'s colleagues. You might have seen him on some corporate events."
            man_name "Wow, [the_person.name]! We just arrived and you already have my boy in your mouth. I didn't expect that, to say the least."
            $ the_person.draw_person(position = "blowjob", emotion = "happy")
            "[the_person.possessive_title] takes his dick out of her mouth, look up to [man_name]'s face, while her hand starts jerking him off."
            the_person.char "Well, [man_name]. Two reasons for that. First - you were so nice with me during all the evening that I felt you deserve a little present."
            $ the_person.discover_opinion("giving blowjobs")
            the_person.char "Second - as you might already guessed, I just love to feel man's dick in my mouth."
            man_name "We have been working together for several years now and I had no idea that you were such a cock-sucking slut, [the_person.name]."
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "[the_person.possessive_title] just smiles then gets up embraces and kiss her man passionately."
            "You are unsure what to do here."
        else:
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            show screen person_info_ui(the_person)
            "You see [the_person.possessive_title] embracing some man, kissing him deeply."
            the_person.char "Oh [man_name], you are so nice. I had a wonderful evening!"
            "Now, when you heard the name, you recognize the man. It's [man_name], one of [the_person.possessive_title] colleagues."
            "You are unsure what to do here."
        menu:
            "Keep looking.":
                "You decide to see what they are up to."
                "They go on kissing. After a while [man_name] places his hands on [the_person.possessive_title]'s ass, slightly caressing it."
                if the_person.sluttiness <= 30 or (the_person.get_opinion_score("taking control") > 0 and the_person.sluttiness <= 45):
                    "[the_person.possessive_title] seems to be taken aback by [man_name] actions."
                    the_person.char "No, [man_name]. We are colleagues, we should not cross some lines."
                    the_person.char "It's late. Thanks for the wonderful evening. See you in the office."
                    $ man_aggro = renpy.random.randint(0,2) ##if man is aggresive
                    if man_aggro < 1:
                        man_name "Yes, [the_person.name]. I lost control. Sorry. See you in the office."
                        "You go back to your room and through half-closed door you see [man_name] leaving the house, clearly dissapointed how things went."
                    else:
                        if bj:
                            man_name "What the fuck, [the_person.name]?! You have been flirting aroung me the whole evening, brought me to your room, sucked me off and now thinking of stopping here?"
                        else:
                            man_name "Oh, no, [the_person.name]. You have been flirting aroung me the whole evening, brought me to your room and now thinking of stopping here?"
                        man_name "This will not do! I can't go back with blue balls. You have to do something about it. You just need a little push."
                        $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                        if mom_clothing is None:
                            pass
                        else:
                            man_name "I think you'd be better without [mom_clothing.name]..."
                            $ the_person.draw_animated_removal (mom_clothing, position = "stand3", emotion = "sad")
                            "He takes off [the_person.possessive_title]'s [mom_clothing.name] and throws it on a floor."
                            if submissive:
                                "[the_person.possessive_title] just keep standing there, accepting her fate, while [man_name] undresses her."
                            else:
                                the_person.char "Please, [man_name]. Don't do it. I'm so ashamed..."
                                man_name "Why don't you just shut up, [the_person.name]? It will make life easier for both of us?"
                        if clothes_number >1:
                            $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                            if not mom_clothing is None:
                                the_person.char "Not my [mom_clothing.name]..."
                                $ the_person.draw_animated_removal (mom_clothing, position = "stand3", emotion = "sad")
                                "You watch as [the_person.possessive_title]'s [mom_clothing.name] also being taken off despite her objections."
                                if submissive:
                                    "[the_person.possessive_title] just keep standing there, with blank face while [man_name] undresses her."
                                else:
                                    the_person.char "Please stop, [man_name]. You can't see me like this."
                                    man_name "I can and I will. Didn't I say for you to shut up? Suggest you do it."
                        if clothes_number >2:
                            $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                            if not mom_clothing is None:
                                man_name "You're not going to need this either, [the_person.name]. Trust me."
                                $ the_person.draw_animated_removal (mom_clothing, position = "stand3", emotion = "sad")
                                "[man_name] rips off her [mom_clothing.name], his hands are all over [the_person.title]'s body."
                                if submissive:
                                    "[the_person.possessive_title] just keep standing there, [man_name] can undress her like a doll."
                                else:
                                    the_person.char "No, I beg you, [man_name]. I feel so naked..."
                                    man_name "One more word and it would be even worse. There will be pain involved."
                        if clothes_number >3:
                            $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                            if not mom_clothing is None:
                                $ the_person.draw_animated_removal (mom_clothing, position = "stand3", emotion = "sad")
                                "[man_name] continues even further. Now [the_person.title] is almost naked."
                                if submissive:
                                    "Completely broken, [the_person.possessive_title] does not care what [man_name] will see"
                                else:
                                    "Afraid to anger him further, [the_person.possessive_title] just stands there, sobbing."
                        if bj:
                            man_name "Now it is much better! Just get on your knees, [the_person.name]. You have already done this, so get back to it, you cock-loving whore."
                        else:
                            man_name "Now it is much better! Just get on your knees, [the_person.name]. I know you have dreamed of sucking my cock for a long time."
                        $ the_person.draw_person(position = "blowjob", emotion = "sad")
                        "[the_person.title] can't refuse [man_name]'s force as she obeys him. She gets down on her knees while he lowers his pants and underwear."
                        man_name "That's better. Like the view of my friend? See how big he is because of you? Now start working on it, [the_person.name]!"
                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                        "She can't resist [man_name]'s urging and starts to suck him off."
                        man_name "That's is, bitch! You like to suck my cock, don't you? Just too afraid to declare it in open."
                        man_name "If I knew you are so good at it, I have done it with you long time ago."
                        if bj:
                            "[the_person.possessive_title] keeps sucking [man_name], and he clearly enjoys it. She also seems to get aroused a little."
                        else:
                            "[the_person.possessive_title] keeps sucking [man_name], as he clearly enjoys it."
                        if the_person.outfit.vagina_available():
                            man_name "You are a great cosksucker, [the_person.name]!. Let's find out if you are any good with other stuff. Get on the bed, I'm gonna take you from the back."
                            $ the_person.draw_person(position = "doggy")
                            "[the_person.possessive_title] has lost all will to resist and obeys [man_name]'s orders. She gets on the bed, displaying her ass in front of the [man_name]."
                            man_name "Good girl! You're already soaking wet, bitch. Did you know that?"
                            if submissive:
                                the_person.char "Oh, [man_name], just shut up and fuck me!"
                                the_person.char "I like when a man is rough. You see I'm already wet."
                                the_person.char "So please, [man_name], fuck me hard. Don't stop at anything. Make me scream like a bitch."
                                $ the_person.discover_opinion("being submissive")
                                man_name "No objections here, dear! I will rail you so hard that you'll have trouble walking in the morning."
                            else:
                                the_person.char "No, [man_name], please, don't do it. We are colleagues... Wa can't do this."
                                man_name "My dear [the_person.name], you should have thought on this before flirting with me and taking me here."
                                man_name "Now we are alone, undressed, you are on all fours, I have a rock hard erection and you expect me to stop? You've got another thing coming!"
                            "You see as [man_name] in one thrust enter's [the_person.possessive_title] pussy."
                            if submissive:
                                the_person.char "Fuck, yes! Please, [man_name], fuck me. Fuck me hard!"
                                man_name "You are really a slut, [the_person.name]. Like being railed from behind?"
                                the_person.char "Yes. Yes. Do me! Fuck my pussy, [man_name]!"
                                "For a time being there is silence in a room. Only the wet sounds of [man_name]'s dick going in and out of [the_person.possessive_title] vagina and slapping sounds as their bodies collide can be heard."
                                "[man_name] grabs her hair and pull her upwards."
                                man_name "Like it, [the_person.name]? Do you like it, whore?"
                                the_person.char "Oh yes! Keep doing me, [man_name]. I'm about to cum!"
                                "[man_name] goes on pumping [the_person.possessive_title] and then slaps her ass with a force."
                                the_person.char "Mmmmmm... Yes, slap me. Hit me hard, it turns me on so much! And keep ravaging my pussy with your great dick!"
                                "They keep on fucking for some time and now both appear to be approaching orgasm."
                            else:
                                the_person.char "Oh... Please, [man_name], stop. You cannot rape me like that!"
                                man_name "Shut up, [the_person.name]. No one is taking this as a rape. You wanted this all along."
                                "For a time being there is slilence in a room. Only wet sounds of [man_name]'s dick going in and out of [the_person.possessive_title] vagina and pumping sounds as their bodies collapse."
                                "[man_name] grabs her hair and pull her upwards."
                                man_name "Like it, [the_person.name]? Do you like it, whore?"
                                the_person.char "Please, stop, [man_name]. I beg you to stop..."
                                "[man_name] goes on pumping [the_person.possessive_title] and then slaps her ass with a force."
                                man_name "You will beg to make you cum again and again. You'll see."
                                "They keep on fucking for some time and now [man_name] appears to be approaching orgasm."
                            $ finish = get_random_from_list(finishes)
                            if finish == "facial":
                                "While it seemed rough at the beginning, [the_person.possessive_title] seems to enjoy at least part of it. She gets off his cock and drops to her knees."
                                $ the_person.draw_person(position = "blowjob")
                                the_person.char "Now shower me with your hot jizz. Cover my body with it!"
                                man_name "Want me to cum spray your face, eh, [the_person.name]? Aren't you a slut?"
                                "[man_name] can't hold for much longer and he starts cumming over [the_person.possessive_title]'s body."
                                $ the_person.cum_on_face()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "First he covers [the_person.possessive_title] face with his semen."
                                $ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "But the load is big so the sperm also covers [the_person.possessive_title]'s tits."
                                the_person.char "Now are you happy, [man_name]? See me covered in your love juices?"
                                man_name "You are great, [the_person.name]. I wish I could do it more often."
                                $ the_person.draw_person(position = "stand2", emotion = "happy")
                                "[the_person.possessive_title] get's up and smiles."
                                the_person.char "How about a shower, [man_name]?"
                                "They both go into the bathroom and you decide to get back to your room."
                                if submissive or the_person.sluttiness > 60:
                                    "Some time later at night you awoke again by the screams coming from [the_person.possessive_title]'s room."
                                    the_person.char "Take me with your hard dick, [man_name]. I want to feel it again. I beg you, rape me again!"
                                    man_name "Aren't you a cock-hungry whore, [the_person.name]? Now lay on the table. I want to see your boobs this time, see them jump."
                                    the_person.char "Of course, [man_name]. You can take me however you want. Just keep covering your slut body with your hot sperm."
                                    "It seems that [the_person.possessive_title] now does not wish the encounter to end as her screams and [man_name] moans keep on..."
                            elif finish == "inside":
                                "While it seemed rough at the beginning, [the_person.possessive_title] seems to enjoy at least part of it, as she gets more and more turned on."
                                the_person.char "Please, [man_name], cum inside me. I'm on a pill, so don't worry. I just want to feel your warmth in me."
                                man_name "Well, since it is safe, I'll give you what you want. One cunt full of cum coming right up. Get your pussy ready."
                                $ the_person.cum_in_vagina()
                                $ the_person.draw_person(position = "doggy")
                                "You see [man_name] body shivers as he explodes inside of [the_person.possessive_title]."
                                the_person.char "Yes, yes! Fill me! Drench my pussy in your cum!"
                                "He makes a few more thrusts and with a wet sound takes his cock out of [the_person.possessive_title]'s vagina."
                                "You see some white drops falling to the blankets."
                                man_name "Well, quite a nice view. One cum filled bitch."
                                $ the_person.draw_person(position = "stand2", emotion = "happy")
                                "[the_person.possessive_title] get's up and smiles."
                                the_person.char "No need to be so rough. The last part was really not bad, I agree."
                                the_person.char "How about a shower, [man_name]?"
                                "They both go into the bathroom and you decide to get back to your room."
                                if submissive or the_person.sluttiness > 60:
                                    "Some time later at night you awoke again by the screams coming from the kitchen."
                                    the_person.char "Take me with your hard dick, [man_name]. I want to feel it again. I beg you, rape me again!"
                                    man_name "Aren't you a cock-hungry whore, [the_person.name]? Now lay on the table. I want to see your boobs this time, watch them bounce as I fuck you."
                                    the_person.char "Of course, [man_name]. You can take me however you want. Just keep filling me with your cum!."
                                    "It seems that [the_person.possessive_title] now does not wish the encounter to end as her screams and [man_name] moans keep on..."
                            elif finish == "drink":
                                "While it seemed rough at the beginning, [the_person.possessive_title] seems to enjoy at least part of it. She gets off his cock and drops to her knees."
                                $ the_person.draw_person(position = "blowjob")
                                the_person.char "Now I want you to fill my mouth with your hot jizz."
                                man_name "Not that you are in position of making requests but I like the idea. I can't refuse such a request."
                                man_name "Now open your mouth and say 'Aaaaa'."
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[the_person.possessive_title] opens her mouth wide and [man_name] drives his hard penis into it."
                                "She starts sucking while playing with man's balls."
                                if submissive:
                                    man_name "No slacking off for you, whore!"
                                    "He grabs [the_person.possessive_title]'s head and impales it with his thing."
                                    "It goes all the way inside with man's ball hitting [the_person.title]'s jaw."
                                    man_name "I bet you love being face fucked, [the_person.name]. And today you are my own personal slut."
                                    "[the_person.possessive_title] can't say anything but she makes no intentions to protest against [man_name]'s actions."
                                    "You never expected to see [the_person.possessive_title] being fucked like porn actresses from all those films."
                                "[man_name] can't hold for much longer and he starts cumming into [the_person.possessive_title]'s mouth."
                                $ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "The man just keep on and on and on. Finally he seems to reached his limit."
                                man_name "Wow, that was something. It's like that mouth of yours is meant for sucking cock."
                                $ the_person.draw_person(position = "blowjob")
                                "Saying that, he takes his softening dick out of [the_person.possessive_title]'s mouth."
                                "[the_person.possessive_title] gulps and drinks [man_name]'s cum in one shot but you still see traces of it around her mouth and something is still inside."
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "She looks up at him and smiles."
                                the_person.char "Ah, you taste so good, [man_name]. I hope there be more of it."
                                man_name "You are just a perverted cum-loving slut, [the_person.name]. You know that?"
                                $ the_person.draw_person(position = "stand2", emotion = "happy")
                                "[the_person.possessive_title] get's up and smiles."
                                the_person.char "Well, maybe so... Still, no need for such rude words after such a wonderful final."
                                the_person.char "How about a shower, [man_name]?"
                                "They both go into the bathroom and you decide to get back to your room."
                                if submissive or the_person.sluttiness > 60:
                                    "Some time later at night you awoke again by the screams coming from the kitchen."
                                    the_person.char "Take me with your hard dick, [man_name]. I want to feel it again. I beg you, rape me again!"
                                    man_name "Aren't you a cock-hungry whore, [the_person.name]? Now lay on the table. I want to see your boobs this time, watch them bounce as I fuck you."
                                    the_person.char "Of course, [man_name]. You can take me however you want. Just keep cumming into my mouth."
                                    "It seems that [the_person.possessive_title] now does not wish the encounter to end as her screams and [man_name] moans keep on..."
                                else:
                                    pass
                            elif finish == "usual":
                                if submissive or the_person.sluttiness > 60:
                                    "[the_person.possessive_title] seems to already have several orgasms as her screams are now loud. She clearly don't care or understand that you or Lily may come to investigate."
                                    the_person.char "Yeeeeees! Fuck! Tear me apart, [man_name]! I'm your bitch tonight that need a proper fuck! Do it!"
                                    "The man keeps pumping her and slapping her already red ass. With each slap, [the_person.possessive_title] moans with pleasure."
                                    man_name "Didn't I said that you just a slut, needing a push? I promised to give you a proper one, so you still owe me!"
                                    "[man_name] keeps rimming [the_person.possessive_title] pussy and after a few seconds starts to cum on her ass."
                                    $ the_person.cum_on_ass()
                                    $ the_person.draw_person(position = "doggy")
                                    "His white liquid covers her butt."
                                    man_name "That's it, [the_person.name]. You got what you deserved."
                                    $ the_person.draw_person(position = "kissing", emotion = "happy")
                                    "[the_person.possessive_title] get's up and kisses [man_name] with a passion."
                                    the_person.char "That was really great, [man_name]. I lost count how many orgasms I had. Never had such a good sex. We must do it again sometime."
                                    the_person.char "Now, how about a shower, [man_name]? I'm sweating like a cow."
                                    "They both go into the bathroom and you decide to get back to your room."
                                    "Some time later at night you awoke again by the screams coming from [the_person.possessive_title]'s room."
                                    the_person.char "Take me with your hard dick, [man_name]. I want to feel it again. I beg you, rape me again!"
                                    man_name "Aren't you a cock-hungry whore, [the_person.name]? Now lay on the table. I want to see your boobs this time, see them jump."
                                    the_person.char "Of course, [man_name]. You can take me however you want. Just keep fucking your slutty [the_person.name]."
                                    "It seems that [the_person.possessive_title] now does not wish the encounter to end as her screams and [man_name] moans keep on..."
                                else:
                                    "[man_name] keeps rimming [the_person.possessive_title] pussy and after a few seconds starts to cum on her ass."
                                    $ the_person.cum_on_ass()
                                    $ the_person.draw_person(position = "doggy")
                                    "His white liquid covers her butt."
                                    man_name "That's it, [the_person.name]. You got what you deserved."
                                    $ the_person.draw_person(position = "stand2", emotion = "sad")
                                    "[the_person.possessive_title] get's up. You see tears in her eyes."
                                    the_person.char "Damn, [man_name]! I wish none of this has happened. Now get out of my house. Don't want to see your face anymore!"
                                    $ the_person.draw_person(position = "sitting", emotion = "sad")
                                    "You retreat to your room, while [man_name] collects his clothes and gets dressed."
                                    "[the_person.possessive_title] sits on her bed, sobbing."
                        else:
                            "[the_person.possessive_title] keeps on sucking [man_name] cock, clearly putting him on an edge."
                            $ finish = get_random_from_list(finishes)
                            if finish == "facial":
                                "While it seemed rough at the beginning, [the_person.possessive_title] seems to enjoy at least part of it.She takes his dick out of her mouth and looks up."
                                $ the_person.draw_person(position = "blowjob")
                                the_person.char "Wanna see this pretty face with your sperm on it, [man_name]? Now shower me with your hot jizz. Cover my body with it!"
                                man_name "Want me to cum spray your face, eh, [the_person.name]? Aren't you a slut?"
                                "[man_name] can't hold for much longer and he starts cumming over [the_person.possessive_title]'s body."
                                $ the_person.cum_on_face()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "First he covers [the_person.possessive_title] face with his semen."
                                $ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "But the load is big so the sperm also covers [the_person.possessive_title]'s tits."
                                the_person.char "Now are you happy, [man_name]? See me covered in your love juices?"
                                man_name "You are great, [the_person.name]. I wish I could do it more often."
                                $ the_person.draw_person(position = "stand2", emotion = "happy")
                                "[the_person.possessive_title] get's up and smiles."
                                the_person.char "How about a shower, [man_name]?"
                                "They both go into the bathroom and you decide to get back to your room."
                                if submissive or the_person.sluttiness > 60:
                                    "Some time later at night you awoke again by the noise coming from [the_person.possessive_title]'s room."
                                    the_person.char "Mrmh... Blgrhm..."
                                    man_name "That's it, [the_person.name]. Take it into your slutty mouth!"
                                    "Seems [man_name] liked the idea of face fucking [the_person.possessive_title]. She doesn't seem to object."
                                    "It seems that [the_person.possessive_title] now does not wish the encounter to end as her and [man_name] moans keep on..."
                                else:
                                    pass
                            elif finish == "drink":
                                "While it seemed rough at the beginning, [the_person.possessive_title] seems to enjoy at least part of it. She takes his dick out of her mouth."
                                $ the_person.draw_person(position = "blowjob")
                                the_person.char "Now I want you to fill my mouth with your hot jizz."
                                man_name "Not that you are in position of meking requests but I like the idea. Never can refuse this things."
                                man_name "Now open your mouth and say 'Aaaaaa'."
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[the_person.possessive_title] opens her mouth wide and [man_name] drives his hard penis into it."
                                "She starts sucking while playing with man's balls."
                                if submissive:
                                    man_name "No slacking off for you, whore!"
                                    "He grabs [the_person.possessive_title]'s head and impales it woth his thing."
                                    "It goes all the way inside with man's ball hitting [the_person.title]'s jaw."
                                    man_name "I bet you love being face fucked, [the_person.name]. And today you are my own personal slut."
                                    "[the_person.possessive_title] can't say anything but she makes no intentions to protest against [man_name] actions."
                                    "You never expected to see [the_person.possessive_title] being fucked like porn actresses from all those films."
                                "[man_name] can't hold for much longer and he starts cumming into [the_person.possessive_title]'s mouth."
                                $ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "The man just keep on and on and on. Finally he seems to reached his limit."
                                man_name "Wow, that was something. It's like that mouth of yours is meant for sucking cock."
                                $ the_person.draw_person(position = "blowjob")
                                "Saying that, he takes his softening dick out of [the_person.possessive_title]'s mouth."
                                "[the_person.possessive_title] gulps and drinks [man_name]'s cum in one shot but you still see traces of it around her mouth and something is still inside."
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "She looks up at him and smiles."
                                the_person.char "Ah, you taste so good, [man_name]. I hope there be more of it."
                                man_name "You are just a perverted cum-loving slut, [the_person.name]. You know that?"
                                $ the_person.draw_person(position = "stand2", emotion = "happy")
                                "[the_person.possessive_title] get's up and smiles."
                                the_person.char "Well, maybe so... Still, no need for such rude words after such a wonderful final."
                                the_person.char "How about a shower, [man_name]?"
                                "They both go into the bathroom and you decide to get back to your room."
                                if submissive or the_person.sluttiness > 60:
                                    "Some time later at night you awoke again by the noise coming from [the_person.possessive_title]'s room."
                                    the_person.char "Mrmh... Blgrhm..."
                                    man_name "That's it, [the_person.name]. Take it into your slutty mouth!"
                                    "Seems [man_name] liked the idea of face fucking [the_person.possessive_title]. She doesn't seem to object."
                                    "It seems that [the_person.possessive_title] now does not wish the encounter to end as her and [man_name] moans keep on..."
                            elif finish == "usual":
                                man_name "Oh, yes, [the_person.name]. You suck so good. How about I fill you cute mouth with my sperm?"
                                "She doesn't seem to object, just keep going until [man_name] grins and starts ejaculating into her mouth."
                                $ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                man_name "Oh, fuck! [the_person.name], you really dried me up!"
                                if submissive or the_person.sluttiness > 60:
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "She looks up at him and smiles."
                                    the_person.char "Well, sometimes I don't mind being a little rough with."
                                    the_person.char "Now, how about a shower, [man_name]?"
                                    "They both go into the bathroom and you decide to get back to your room."
                                    "Some time later at night you awoke again by the sounds coming from [the_person.possessive_title]'s room."
                                    the_person.char "Mrmh... Blgrhm..."
                                    man_name "That's it, [the_person.name]. Take it into your slutty mouth!"
                                    "Seems [man_name] liked the idea of face fucking [the_person.possessive_title]. She doesn't seem to object."
                                    "It seems that [the_person.possessive_title] now does not wish the encounter to end as her and [man_name] moans keep on..."
                                else:
                                    $ the_person.draw_person(position = "blowjob", emotion = "sad")
                                    "She looks up at him. You see tears in her eyes."
                                    the_person.char "Damn you, [man_name]! I wish none of this has happened. Now get out of my house. Don't want to see your face anymore!"
                                    "You rush back to your room to avoid being seen."
                else:
                    the_person.char "Oh, [man_name]. You clearly have some plans for tonight, don't you?."
                    if bj:
                        "She strokes his penis a little."
                    else:
                        "She caresses the buldge on his pants."
                    the_person.char "I like those plans, as well as my little friend here. Now let me help you get rid of those clothes."
                    "You see them help each other undress."
                    $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                    if not mom_clothing is None:
                        man_name "I think you'd be better without [mom_clothing.name]..."
                        $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                        "He takes off [the_person.possessive_title]'s [mom_clothing.name] and throws it on a nearby chair."
                    if clothes_number >1:
                        $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                        if not mom_clothing is None:
                            the_person.char "I like the touch of your soft hands, [man_name]."
                            $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                            "You watch as [the_person.possessive_title]'s [mom_clothing.name] also getting off. [man_name]'s hand are softly caressing [the_person.possessive_title] naked skin."
                    if clothes_number >2:
                        $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                        if not mom_clothing is None:
                            the_person.char "Ooooh, [man_name], you are really turning me on with your touches."
                            $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                            "[man_name] takes off her [mom_clothing.name], his hands are all over [the_person.possessive_title]'s body."
                    if clothes_number >3:
                        $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                        if not mom_clothing is None:
                            the_person.char "I don't mind go even more naked, [man_name]. Please, take off my [mom_clothing.name] with that magical hands of yours."
                            $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                            "He grants her wish, caressing now open parts of her body."
                    $ the_person.sluttiness += 2
                    "Now with both of them pretty naked, you clearly see where it will go."
                    the_person.char "Well, I think we are both ready for action. So, let's do it!"
                    menu:
                        "[the_person.possessive_title] lays on the bed..." if the_person.outfit.vagina_available():
                            $ the_person.draw_person(position = "missionary", emotion = "happy")
                            "You see as [the_person.possessive_title] lays on her bed and spreads her legs, inviting [man_name] to enter her."
                            the_person.char "Oh, [man_name], how about you do me the traditional way?"
                            "He quickly drops down his underwear and climbs atop of [the_person.possessive_title], entering her pussy in one go."
                            the_person.char "Oh yes, [man_name]! Do it! I really needed that."
                            "[man_name] speeds up, pumping [the_person.possessive_title] wet vagina and kissing her hard."
                            man_name "God, [the_person.name], you are really tight there!"
                            "[the_person.possessive_title] hands caress [man_name]'s back. Then she breakes the kiss to have some air."
                            the_person.char "Yes! Do me! I like the way you do it! Fuck me further!"
                            if submissive:
                                the_person.char "Harder, I beg you. I love being owned."
                                $ the_person.discover_opinion("being submissive")
                                "[man_name] increases his amplitude. Now with each move he presses [the_person.possessive_title] against the bed, producing heavy squeaking sound."
                            $ arousal_plus = renpy.random.randint (10,50)
                            $ the_person.change_arousal (arousal_plus)
                            menu:
                                "Keep hiding...":
                                    $ hidden = True
                                "Don't hide...":
                                    $ hidden = False

                            if detected or not hidden:
                                "[the_person.possessive_title] turns her head and see that the door is slightly ajar and you standing there."
                                if the_person.sluttiness >=50 or the_person.get_opinion_score("public sex") > 0 or the_person.arousal > 35:
                                    the_person.char "[the_person.mc_title], don't just stay there, come on in. [the_person.possessive_title] will help you relax as well."
                                    "[man_name] does not mind you joining the show as he keeps fucking [the_person.possessive_title]'s pussy."
                                    man_name "Go on, boy. You see she is quite ready for both of us. Aren't you, [the_person.name]?"
                                    the_person.char "I don't mind [the_person.mc_title] seeing me like this. Now, come closer, dear."
                                    "You come close to [the_person.possessive_title] and take your dick out of your pants."
                                    the_person.char "Good boy! Now let [the_person.possessive_title] take care of you."
                                    "She starts stroking your penis while [man_name] keeps driving his dick into her soaking vagina."
                                    the_person.char "Oh, [man_name], please go on. Keep fucking me!"
                                    man_name "Wow, [the_person.name]. You really don't care about your son seeing his [the_person.title] being fucked liked that?" # NOTE: Does this sentence make sense with anything else than "mom" / "mother". Other characters would not use the titles, but for the sake of avoiding mentions of incest title should be used.
                                    the_person.char "The only thing I now care about is your thing inside of me. So keep going, [man_name]!"
                                    while the_person.arousal < 100:
                                        "[man_name] thrusts his dick into [the_person.possessive_title] pussy. It goes in and out with a wet sound. Clearly [the_person.title] is having great time."
                                        the_person.char "Please, [man_name], more. Do me! Do me!"
                                        if submissive:
                                            the_person.char "Harder. Pin me down with that great thing of yours! I want a rough fuck!"
                                        "As she gets more and more turned on, the speed of her hand on your cock also increases."
                                        $ arousal_plus = renpy.random.randint (10,50)
                                        $ the_person.change_arousal (arousal_plus)
                                    "After being fucked by [man_name] for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                                    the_person.char "Oh, God! I'm cumming! Fuck me! Fuck me more! Fuck me a fast as you can, [man_name]!"
                                    "He starts to pump [the_person.possessive_title] with some ferocity, fully buring his dick in her."
                                    $ the_person.draw_person(position = "missionary", emotion = "orgasm")
                                    the_person.char "Yes! Yes! That's it! I love it, [man_name]!"
                                    man_name "Shit, [the_person.name], your pussy is driving me crazy! I think I will come soon!"
                                    $ finish = get_random_from_list(finishes)
                                    if finish == "facial":
                                        the_person.char "Hold it, [man_name]! I have a better idea."
                                        $ the_person.draw_person(position = "blowjob")
                                        "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                                        the_person.char "Would you like to cover my face with your hot cum? I doubt that your wife allows you to do this!"
                                        man_name "No, [wife_name] never allows anything in bed. Sometimes I really hate it!"
                                        the_person.char "Well, thats your chance to try something new, [man_name]!"
                                        "She looks into [man_name]'s eyes while jerking your cocks with both hands."
                                        man_name "I'm cumming [the_person.name]!"
                                        "She leans closer so that [man_name] tip is just in front of her face."
                                        the_person.char "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                        $ the_person.cum_on_face()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[man_name] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                        man_name "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name]!"
                                        "[man_name] clearly liked the idea of doing it with his wife."
                                        the_person.char "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                        man_name "It really turns me on! I feel I can do another round shortly."
                                        the_person.char "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]."
                                        $ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                        the_person.char "Here we go. All finished!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        if submissive or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person.char "Do me again, [man_name]. Fuck me harder! Shower your whore's face again!"
                                            man_name "On your face, slut!"
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "inside":
                                        the_person.char "Yes! Do it, [man_name]! I want you to fill me."
                                        $ the_person.cum_in_vagina()
                                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                                        "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                                        the_person.char "Yes, [man_name]! I want it in me!"
                                        "After few seconds [man_name] gets off [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy."
                                        the_person.char "Wow, [man_name]! You really neded to get some steam off! That was a huge load."
                                        man_name "And you look gorgeous, [the_person.name] lying there, full of my cum. And with your sons cock in hands."
                                        the_person.char "Glad you like it, [man_name]! Now let's finish with [the_person.mc_title]."
                                        $ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                        the_person.char "Here we go. All finished!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the bed and smiles."
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        $ the_person.draw_person(position = "walking_away")
                                        "As [the_person.possessive_title] starts walking towards bathroom, you see several white drops falling on the floor."
                                        "While she walks past [man_name], he places his hand on her butt."
                                        the_person.char "First - the shower. Then we will see, dear."
                                        if submissive  or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.title]'s room."
                                            the_person.char "Do me again, [man_name]. It feels so good to be filled with your semen!"
                                            man_name "Take it all in, [the_person.name]!"
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "drink":
                                        the_person.char "Hold it, [man_name]! I have a better idea."
                                        $ the_person.draw_person(position = "blowjob")
                                        "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                                        the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                        man_name "No, [wife_name] never allows anything in bed, she is so prudish and boring at times."
                                        the_person.char "Well, thats your chance to try something new, [man_name]!"
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "She looks into [man_name]'s eyes while sucking him off. One of her hands is working on you in meantime."
                                        man_name "I'm gonna cum, [the_person.name]!"
                                        "She just keep on going at steady pace."
                                        the_person.char "Mmmmmm... Mmmm.. Uh."
                                        $ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "[man_name] shrugs and starts filling her mouth with his load."
                                        man_name "Oh, yes! Get it, [wife_name]!"
                                        "[man_name] clearly liked the idea of doing it with his wife."
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                                        the_person.char "Liked that, [man_name]? [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                        man_name "It really turned me on! I feel I can do another round shortly."
                                        the_person.char "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]. I want to drink his stuff too."
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "With that she takes your cock with her hot lips."
                                        man_name "Never thought you are such cum drinking fan, [the_person.name]!"
                                        $ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up mouth around your dick and in few seconds you cum inside. She retreats back and gulps."
                                        the_person.char "Here we go. Double sweet load."
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        if submissive  or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person.char "Fuck me again, [man_name]. Take me however you wish. Just let me taste your sweet cum again, I beg you!"
                                            man_name "Suck it, bitch, or no sweets for you!"
                                            the_person.char "Mhhmhmh..."
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "usual":
                                        "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                                        "[the_person.possessive_title] closes the tip with her hand so that no sperm would be split around."
                                        man_name "Ow, fuck! That was great!"
                                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                                        the_person.char "Indeed, [man_name]! It was great! Best fuck I had in some time! Now let's finish with [the_person.mc_title]."
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum in her arms."
                                        the_person.char "Here we go. All finished!"
                                        man_name "I don't believe it, [the_person.name]. You just let your son watch us fuck and then jerked him off!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the bed and smiles."
                                        the_person.char "Didn't that turn you on, [the_person.mc_title]?"
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        if submissive  or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person.char "Take me again, [man_name]. Bang me with your amazing big thing!"
                                            man_name "Turn around, [the_person.name]. I want you from behind."
                                            the_person.char "Oh, [man_name]! I'm cumming again. Slap my ass! Harder!"
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                else:
                                    $ the_person.happiness -= 5
                                    $ the_person.draw_person(position = "missionary", emotion = "angry")
                                    the_person.char "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get beck to your room now!"
                                    "You go back to your bedroom accompanied by bed sqeaking from [the_person.possessive_title]'s room as [man_name] keeps doing her."
                            else:
                                while the_person.arousal < 100:
                                        "[man_name] thrusts his dick into [the_person.possessive_title] pussy. It goes in and out with a wet sound. Clearly [the_person.title] is having great time."
                                        the_person.char "Please, [man_name], more. Do me! Do me! Fuck me! Fuck [the_person.name]!"
                                        if submissive:
                                            the_person.char "Harder! Slam your dick in me, [man_name]. I love being fucked roughly!"
                                        else:
                                            pass
                                        "As she gets more and more turned on, her screams get louder and louder."
                                        $ arousal_plus = renpy.random.randint (10,50)
                                        $ the_person.change_arousal (arousal_plus)
                                "After being fucked by [man_name] for quite some time, [the_person.possessive_title] seems to be close to orgasm."
                                the_person.char "Oh, God! I'm cumming! Fuck me! Fuck me more! Fuck me at full speed, [man_name]!"
                                "He starts to pump [the_person.possessive_title] with some ferocity, fully buring his dick in her."
                                $ the_person.draw_person(position = "missionary", emotion = "orgasm")
                                the_person.char "Yes! Yes! That's it! I love you, [man_name]!"
                                man_name "Shit, [the_person.name], your pussy is driving me crazy! I think I will come soon!"
                                $ finish = get_random_from_list(finishes)
                                if finish == "facial":
                                    the_person.char "Hold it, [man_name]! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                                    the_person.char "Would you like to cover my face with your hot cum? I doubt that your wife allows you to do this!"
                                    man_name "No, [wife_name] never allows anything in bed. Sometimes I really hate it!"
                                    the_person.char "Well, thats your chance to try something new, [man_name]!"
                                    "She looks into [man_name]'s eyes while jerking him with both hands."
                                    man_name "I'm cumming [the_person.name]!"
                                    "She leans closer so that [man_name] tip is just in front of her eyes."
                                    the_person.char "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                    $ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name]!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    $ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                    the_person.char "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                    man_name "It really turns me on! I feel I can do another round shortly."
                                    the_person.char "We will discuss it later, [man_name]. First - a shower. I need to wash off it before it dries."
                                    $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                    "You see them walking away to bathroom. Some white drops fall on the floor."
                                    "[man_name]'s hand is on [the_person.title]'s ass, but she does not object. As they close the door, you see that [the_person.possessive_title] caresses his balls while his dick shows signs of returning to life."
                                    if submissive  or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Do me again, [man_name]. Fuck me harder! Shower your whore's face again!"
                                        man_name "On your face, slut!"
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "inside":
                                    the_person.char "Yes! Do it, [man_name]! I want you to fill me."
                                    $ the_person.cum_in_vagina()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                                    the_person.char "Yes, [man_name]! I want it in me!"
                                    "After few seconds [man_name] gets off [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy."
                                    the_person.char "Wow, [man_name]! You really neded to get some steam off! That was a huge load."
                                    man_name "And you look gorgeous, [the_person.name] lying there, full of my cum. I wish my wife would allow this."
                                    the_person.char "Glad you like it, [man_name]! Want a better picture?"
                                    "[the_person.possessive_title] spreads her legs even further, offering a full view of her cum-drenched pussy."
                                    the_person.char "Here we go. Remember the view next time you fuck your wife."
                                    $ the_person.draw_person(position = "back_peek", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and heads towards bathroom. [man_name] slaps her ass."
                                    the_person.char "Now I need to take a bath. Then we will see"
                                    $ the_person.draw_person(position = "walking_away")
                                    "As [the_person.possessive_title] walks towards bathroom, you see several white drops falling on the floor."
                                    if submissive or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Do me again, [man_name]. It feels so good to be filled with your semen!"
                                        man_name "Take it all in, [the_person.name]!"
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person.char "Hold it, [man_name]! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                                    the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                    man_name "No, [wife_name] never allows anything in bed, she is so prudent and boring at times."
                                    the_person.char "Well, thats your chance to try something new, [man_name]!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name]'s eyes while sucking him off."
                                    man_name "I'm gonna cum, [the_person.name]!"
                                    "She just keep on going at steady pace."
                                    the_person.char "Mmmmmm... Mmmm.. Uh."
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name] shrugs and starts filling her mouth with his load."
                                    man_name "Oh, yes! Get it, [wife_name]!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                    the_person.char "Liked that, [man_name]? [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name "It really turned me on! I feel I can do another round shortly."
                                    the_person.char "We will discuss it later, [man_name]. First - a shower. I got sweaty with all of that."
                                    $ the_person.draw_person(position = "walking_away")
                                    "You see them walking away to bathroom."
                                    "[man_name]'s hand is on [the_person.possessive_title]'s ass, but she does not object. As they close the door, you see that [the_person.title] caresses his balls while his dick shows signs of returning to life."
                                    if submissive or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Fuck me again, [man_name]. Take me however you wish. Just let me taste your sweet cum again, I beg you!"
                                        man_name "Suck it, bitch, or no sweets for you!"
                                        the_person.char "Mhhmhmh..."
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                                    "[the_person.possessive_title] closes the tip with her hand so that no sperm would be split around."
                                    man_name "Ow, fuck! That was great!"
                                    the_person.char "Indeed, [man_name]! It was great!"
                                    if submissive:
                                         the_person.char "I guess you like when a girl allows you to be rough, don't you? I too like feel owned by a man while he fucks me."
                                         man_name "Yes, it is a wonderful feeling. I really turns me on. Wish I could do it with my wife..."
                                    man_name "Thanks, [the_person.name]. I really needed that."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person.char "Didn't that event paid off, dear?"
                                    the_person.char "Now go to bath, [man_name]. I will join you shortly."
                                    if submissive  or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Take me again, [man_name]. Bang me with your amazing big thing!"
                                        man_name "Turn around, [the_person.name]. I want you from behind."
                                        the_person.char "Oh, [man_name]! I'm cumming again. Slap my ass! Harder!"
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                        "[the_person.possessive_title] poses next to bed..." if the_person.outfit.vagina_available():
                            $ the_person.draw_person(position = "standing_doggy")
                            "You see as [the_person.possessive_title] turns back and poses on her bed spreading her legs, inviting [man_name] to enter her from behind."
                            the_person.char "All the evening you seemed to be interested in my ass."
                            the_person.char "How about we do something while you can enjoy the view?"
                            "He quickly drops down his underwear and comes to [the_person.possessive_title], entering her pussy in one go."
                            the_person.char "Oh yes, [man_name]! Do it! I really needed that."
                            "[man_name] speeds up, pumping [the_person.possessive_title] wet vagina while plaing with her tits."
                            "[the_person.title] hand is working on her clit while she is being railed from behind."
                            the_person.char "Yes! Do me! I like the way you do it!"
                            if submissive:
                                the_person.char "Harder! Smash your body up my ass! I want you to be rough with [the_person.name]. You own me today!"
                                $ the_person.discover_opinion("being submissive")
                            else:
                                pass
                            $ arousal_plus = renpy.random.randint (10,50)
                            $ the_person.change_arousal (arousal_plus)
                            "[man_name] caresses [the_person.title]'s ass."
                            man_name "You ass is so great, [the_person.name]! I wish I could do this more often."
                            the_person.char "Who knows, [man_name]. If you do good now, then... So come on,nail me with your dick."
                            menu:
                                "Keep hiding...":
                                    $ hidden = True
                                "Don't hide...":
                                    $ hidden = False
                            if detected or not hidden:
                                "In a mirror next to the bed [the_person.possessive_title] sees that the door is slightly ajar and you standing there."
                                if the_person.sluttiness >=50 or the_person.get_opinion_score("public sex") > 0 or the_person.arousal > 35:
                                    the_person.char "[the_person.mc_title], don't just stay there, come on in. [the_person.possessive_title] will help you relax as well."
                                    man_name "Holy cow, [the_person.name]. You'll let your son watch you being fucked?"
                                    the_person.char "I don't mind [the_person.mc_title] seeing me like this. Now, come closer, [the_person.mc_title]."
                                    "You lay down on bed in front of [the_person.possessive_title] and take your dick out of your pants."
                                    the_person.char "Good boy! Now let [the_person.possessive_title] take care of you."
                                    "She starts sucking your penis while [man_name] keeps driving his dick into her soaking vagina."
                                    "[the_person.possessive_title] takes your cock out of her mouth and turns back to [man_name]."
                                    the_person.char "Oh, [man_name], please go on. Keep fucking me! Your hand feel so good on my ass."
                                    man_name "Sure, [the_person.name]. You really look lovely from this position."
                                    the_person.char "Enjoy the view. But don't forget - you must do good if wish to have this again. So keep going, [man_name]!"
                                    while the_person.arousal < 100:
                                        "[man_name] thrusts his dick into [the_person.possessive_title] pussy. With each move [the_person.possessive_title] moans. Clearly she is having great time."
                                        the_person.char "Please, [man_name], more. Do me! Do me!"
                                        if submissive:
                                            the_person.char "Slap my ass, [man_name]. Your [the_person.name] has been a bad girl and needs spanking!"
                                            "[man_name] does as she requests and slaps her buttocks. [the_person.possessive_title] moans while sucking you."
                                        else:
                                            pass
                                        "As she gets more and more turned on, the speed of her lips on your cock also increases."
                                        $ arousal_plus = renpy.random.randint (10,50)
                                        $ the_person.change_arousal (arousal_plus)
                                    "After being fucked by [man_name] for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                                    the_person.char "Oh, God! I'm cumming! Fuck me! Fuck me more! Fuck me as fast as you can, [man_name]!"
                                    "He starts to pump [the_person.possessive_title] with some ferocity, his balls slam into her clit. And there is a loud sound as he slaps into her ass."
                                    the_person.char "Yes! Yes! That's it! I love it, [man_name]!"
                                    if submissive:
                                        the_person.char "You own me tonight, Master [man_name]!"
                                    else:
                                        pass
                                    man_name "Shit, [the_person.name], your pussy is driving me crazy! I think I will come soon!"
                                    $ finish = get_random_from_list(finishes)
                                    if finish == "facial":
                                        the_person.char "Hold it, [man_name]! I have a better idea."
                                        $ the_person.draw_person(position = "blowjob")
                                        "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                                        the_person.char "Would you like to cover my face with your hot cum? I doubt that your wife allows you to do this!"
                                        man_name "No, [wife_name] never allows anything in bed. Sometimes I really hate it! Never had a blowjob from her.."
                                        the_person.char "Well, thats your chance to try something new, [man_name]!"
                                        "She looks into [man_name]'s eyes while jerking your cocks with both hands."
                                        man_name "I'm cumming [the_person.name]!"
                                        "She leans closer so that [man_name] tip is just in front of her eyes."
                                        the_person.char "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                        $ the_person.cum_on_face()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[man_name] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                        man_name "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name]!"
                                        "[man_name] clearly liked the idea of doing it with his wife."
                                        the_person.char "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                        man_name "It really turns me on! I feel I can do another round shortly."
                                        the_person.char "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]."
                                        $ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                        the_person.char "Here we go. All finished!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        "As you turn to leave, you see [man_name]'s balls being caressed by [the_person.possessive_title] and his thing starting to rise."
                                        if submissive or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person.char "Do me again, [man_name]. Fuck me harder! Shower your whore's face again!"
                                            man_name "On your face, slut!"
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "inside":
                                        the_person.char "Yes! Do it, [man_name]! I want you to fill me."
                                        $ the_person.cum_in_vagina()
                                        $ the_person.draw_person(position = "standing_doggy")
                                        "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title], while grabbing her ass with both hands."
                                        the_person.char "Yes, [man_name]! I want it in me!"
                                        "After few seconds [man_name] gets off from [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy down her legs."
                                        the_person.char "Wow, [man_name]! You really neded to get some steam off! That was a huge load."
                                        man_name "And you look gorgeous, [the_person.name], posing there, full of my cum. And with your son cock in hands."
                                        the_person.char "Glad you like it, [man_name]! Now let's finish with [the_person.mc_title]."
                                        "[the_person.possessive_title] lowers her head, taking your dick back into her mouth."
                                        $ the_person.cum_in_mouth()
                                        "[the_person.possessive_title] speeds up her lips around your dick and in few seconds you cum in her mouth."
                                        the_person.char "Here we go. All finished!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the bed and smiles."
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        $ the_person.draw_person(position = "walking_away")
                                        "As [the_person.possessive_title] starts walking towards bathroom, you see several white drops falling on the floor."
                                        "While she walks past [man_name], he places his hand on her butt."
                                        if submissive or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person.char "Do me again, [man_name]. It feels so good to be filled with your semen!"
                                            man_name "Take it all in, [the_person.name]!"
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "drink":
                                        the_person.char "Hold it, [man_name]! I have a better idea."
                                        $ the_person.draw_person(position = "blowjob")
                                        "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] turns around and gets on her knees in front of [man_name] cock."
                                        the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                        man_name "No, [wife_name] never allows anything in bed. Even take her from behind, like I did you."
                                        the_person.char "Well, that's your chance to try something new, [man_name]!"
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "She looks into [man_name]'s eyes while sucking him off."
                                        man_name "I'm gonna cum, [the_person.name]!"
                                        "She just keep on going at steady pace."
                                        the_person.char "Mmmmmm... Mmmm.. Uh."
                                        $ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "[man_name] shrugs and starts filling her mouth with his load."
                                        man_name "Oh, yes! Get it, [wife_name]!"
                                        "[man_name] clearly liked the idea of doing it with his wife."
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                        the_person.char "Liked that, [man_name]? [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                        man_name "It really turned me on! I feel I can do another round shortly."
                                        the_person.char "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]. I want to drink his stuff too."
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "With that she takes your cock with her hot lips."
                                        man_name "Never thought you are such cum drinking fan, [the_person.name]!"
                                        $ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up mouth around your dick and in few seconds you cum inside. She moves her head back and gulps."
                                        the_person.char "Here we go. Double sweet load."
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        if submissive or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person.char "Fuck me again, [man_name]. Take me however you wish. Just let me taste your sweet cum again, I beg you!"
                                            man_name "Suck it, bitch, or no sweets for you!"
                                            the_person.char "Mhhmhmh..."
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "usual":
                                        $ the_person.draw_person(position = "standing_doggy")
                                        "[man_name] pulls out his cock and starts stroking it with [the_person.possessive_title]'s buttocks."
                                        "She reaches out and help him with her hand. And when he starts to cum, covers the tip so that he explodes in her hand."
                                        man_name "Ow, fuck! That was great!"
                                        the_person.char "Indeed, [man_name]! It was great! Best fuck I had in some time! Now let's finish with [the_person.mc_title]."
                                        "[the_person.possessive_title] begin to jerk you off fast. You cannot hold for long an finish in her hand."
                                        the_person.char "Here we go. All finished!"
                                        man_name "I don't believe it, [the_person.name]. You just let your son watch us fuck and then sucked him off!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the bed and smiles."
                                        the_person.char "Didn't that turn you on, [the_person.mc_title]?"
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        if submissive  or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person.char "Take me again, [man_name]. Bang me with your amazing big thing!"
                                            man_name "Turn around, [the_person.name]. I want you from behind."
                                            the_person.char "Oh, [man_name]! I'm cumming again. Slap my ass! Harder!"
                                            "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                else:
                                    $ the_person.happiness -= 5
                                    $ the_person.draw_person(position = "back_peek", emotion = "angry")
                                    the_person.char "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get beck to your room now!"
                                    "You go back to your bedroom accompanied by bed sqeaking from [the_person.possessive_title]'s room as [man_name] keeps doing her."
                            else:
                                while the_person.arousal < 100:
                                    "[man_name] thrusts his dick into [the_person.possessive_title] pussy. As he slaps her ass, she moans."
                                    the_person.char "Please, [man_name], more. Do me!"
                                    if submissive:
                                        the_person.char "Fuck me like a dog! I wanna be your bitch tonight. Fuck your whore [the_person.name]."
                                    else:
                                        pass
                                    "As she gets more and more turned on, her screams get louder and louder."
                                    $ arousal_plus = renpy.random.randint (10,50)
                                    $ the_person.change_arousal (arousal_plus)
                                "After being fucked by [man_name] for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                                the_person.char "Oh, God! I'm cumming! Fuck me! Fuck me more! Fuck me as hard as you can, [man_name]!"
                                "He starts to pump [the_person.possessive_title] with some ferocity, fully buring his dick in her. His balls smash against [the_person.title]'s pussy."
                                the_person.char "Yes! Yes! That's it! I love this, [man_name]!"
                                man_name "Shit, [the_person.name], your pussy is driving me crazy! I think I will come soon!"
                                $ finish = get_random_from_list(finishes)
                                if finish == "facial":
                                    the_person.char "Hold it, [man_name]! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes him backwards. You see [the_person.title]'s juices dripping on the floor. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                                    the_person.char "Would you like to cover my face with your hot cum? I doubt that your wife allows you to do this!"
                                    man_name "No, [wife_name] never allows anything in bed. I wish I could fuck her just like I did you."
                                    the_person.char "Well, that's your chance to try something new, [man_name]!"
                                    "She looks into [man_name]'s eyes while jerking him with both hands."
                                    man_name "I'm cumming [the_person.name]!"
                                    "She leans closer so that [man_name] tip is just in front of her eyes."
                                    the_person.char "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                    $ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name]!"
                                    "[the_person.possessive_title] decides to back up his play."
                                    the_person.char "Yes, dear. Cover my bitchy face with your cum. I'm sorry that didn't allow that before."
                                    the_person.char "Cover your dearest [wife_name]'s face with semen. I really want it!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    $ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                    the_person.char "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                    man_name "It really turns me on! I feel I can do another round shortly."
                                    the_person.char "We will discuss it later, [man_name]. First - a shower. I need to wash off it before it dries."
                                    $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                    "You see them walking away to bathroom. Some white drops fall on the floor."
                                    "[man_name]'s hand is on [the_person.possessive_title]'s ass, but she does not object. As they close the door, you see that [the_person.title] caresses his balls while his dick shows signs of returning to life."
                                    if submissive or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Do me again, [man_name]. Fuck me harder! Shower your whore's face again!"
                                        man_name "On your face, slut!"
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "inside":
                                    the_person.char "Yes! Do it, [man_name]! I want you to fill me."
                                    $ the_person.cum_in_vagina()
                                    "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title], grabbing her ass with both hands."
                                    the_person.char "Yes, [man_name]! I want it in me!"
                                    "After few seconds [man_name] gets off from [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.possessive_title]'s pussy over her legs."
                                    the_person.char "Wow, [man_name]! You really neded to get some steam off! That was a huge load."
                                    man_name "And you look gorgeous, [the_person.name] standing there, full of my cum. I wish my wife would allow this."
                                    the_person.char "Glad you like it, [man_name]! Want a better picture?"
                                    $ the_person.draw_person(position = "doggy")
                                    "[the_person.possessive_title] bends even further, offering a full view of her cum-drenched pussy."
                                    the_person.char "Here we go. Remember the view next time you fuck your wife."
                                    $ the_person.draw_person(position = "back_peek", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and heads towards bathroom. [man_name] slaps her ass."
                                    the_person.char "Now I need to take a bath. Then we will see"
                                    $ the_person.draw_person(position = "walking_away")
                                    "As [the_person.possessive_title] walks towards bathroom, you see several white drops falling on the floor."
                                    if submissive  or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Do me again, [man_name]. It feels so good to be filled with your semen!"
                                        man_name "Take it all in, [the_person.name]!"
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person.char "Hold it, [man_name]! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] turns around and gets on her knees in front of [man_name] cock."
                                    the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                    man_name "No, [wife_name] never allows anything in bed. Even take her from behind, like I did you."
                                    the_person.char "Well, that's your chance to try something new, [man_name]!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name]'s eyes while sucking him off."
                                    man_name "I'm gonna cum, [the_person.name]!"
                                    "She just keep on going at steady pace."
                                    the_person.char "Mmmmmm... Mmmm.. Uh."
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name] shrugs and starts filling her mouth with his load."
                                    man_name "Oh, yes! Get it, [wife_name]!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                    the_person.char "Liked that, [man_name]? [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name "It really turned me on! I feel I can do another round shortly."
                                    the_person.char "We will discuss it later, [man_name]!"
                                    the_person.char "What a sweet load."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person.char "Now go to shower. I will join you shortly."
                                    if submissive or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Fuck me again, [man_name]. Take me however you wish. Just let me taste your sweet cum again, I beg you!"
                                        man_name "Suck it, bitch, or no sweets for you!"
                                        the_person.char "Mhhmhmh..."
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    $ the_person.draw_person(position = "standing_doggy")
                                    "[man_name] pulls out his cock and starts stroking it with [the_person.possessive_title]'s buttocks."
                                    "She reaches out and help him with her hand. And when he starts to cum, covers the tip so that he explodes in her hand."
                                    man_name "Ow, fuck! That was great! I really like having a woman from behind."
                                    the_person.char "Indeed, [man_name]! It was great! Best fuck I had in some time!"
                                    man_name "Thanks, [the_person.name]. I really needed that."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person.char "Didn't that event paid off, dear?"
                                    the_person.char "Now go to bath, [man_name]. I will join you shortly."
                                    if submissive  or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Take me again, [man_name]. Bang me with your amazing big thing!"
                                        man_name "Turn around, [the_person.name]. I want you from behind."
                                        the_person.char "Oh, [man_name]! I'm cumming again. Slap my ass! Harder!"
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                        "[the_person.possessive_title] gets on her knees...":
                            $ the_person.draw_person(position = "blowjob")
                            "You see as [the_person.possessive_title] gets on her knees, taking down [man_name]'s underwear."
                            "His erected dick is right in front of [the_person.possessive_title]'s face."
                            the_person.char "Hello there, sweetie. How about we have some fun together?"
                            $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                            "[the_person.possessive_title] takes his cock in her mouth and starts sucking."
                            "[man_name] paces his hands on her head slighty regulating the speed."
                            man_name "It feels great, [the_person.name]. I like the way you do it!"
                            $ arousal_plus = renpy.random.randint (10,50)
                            $ the_person.change_arousal (arousal_plus)
                            "[the_person.possessive_title] takes [man_name]'s dick out of her mouth, looks at his eyes."
                            the_person.char "I really like it, [man_name]. It feels great in my mouth."
                            "Then she get's back to suck it."
                            menu:
                                "Keep hiding...":
                                    $ hidden = True
                                "Don't hide...":
                                    $ hidden = False
                            if detected or not hidden:
                                "[the_person.possessive_title] turns her head a little and see that the door is slightly ajar and you standing there."
                                if the_person.sluttiness >=50 or the_person.get_opinion_score("public sex") > 0 or the_person.arousal > 35:
                                    "[the_person.possessive_title] takes [man_name]'s dick out of her mouth."
                                    the_person.char "[the_person.mc_title], don't just stay there, come on in. [the_person.possessive_title] will help you relax as well."
                                    man_name "Shit, [the_person.name]. Your son sees you sucking a guy off, and you don't mind?"
                                    "[the_person.possessive_title] doesn't bother to answer as she goes back to sucking him."
                                    "You come close to [the_person.possessive_title] and take your dick out of your pants."
                                    "She starts stroking you while [man_name] keeps driving his dick into her mouth."
                                    while the_person.arousal < 100:
                                        "[the_person.possessive_title] keeps sucking his dick. You notice that she is rubbing her clit with her free hand."
                                        man_name "Oh, thats great, [the_person.name]! You are great at sucking cocks."
                                        if submissive:
                                            "[the_person.possessive_title] grabs [man_name]'s ass and impales her mouth on his cock. His ball hit [the_person.possessive_title]'s jaw."
                                            man_name "Ow, that feels so good, [the_person.name]!"
                                        else:
                                            pass
                                        "As she gets more and more turned on, her moans get louder and louder."
                                        $ arousal_plus = renpy.random.randint (10,50)
                                        $ the_person.change_arousal (arousal_plus)
                                    "[the_person.possessive_title] takes guys cock out and looks up."
                                    the_person.char "Oh. I get so turned on with a cock im my mouth. I'm cumming!"
                                    "She get's back to his dick as her body shivers with orgasm."
                                    man_name "Oh, [the_person.name], your toungue is driving me crazy! I think I will come soon!"
                                    $ finish = get_random_from_list(finishes)
                                    if finish == "facial":
                                        "She takes his dick out of her mouth."
                                        the_person.char "Would you like to cover my face with your hot cum? I doubt that your wife allows you to do this!"
                                        man_name "No, [wife_name] never allows anything in bed. I wish I could make her blow me."
                                        the_person.char "Well, that's your chance to try something new, [man_name]!"
                                        "She looks into [man_name]'s eyes while jerking him with both hands."
                                        man_name "I'm cumming [the_person.name]!"
                                        "She leans closer so that [man_name] tip is just in front of her eyes."
                                        the_person.char "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                        $ the_person.cum_on_face()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[man_name] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                        man_name "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name]!"
                                        "[the_person.possessive_title] decides to back up his play."
                                        the_person.char "Yes, dear. Cover my bitchy face with your cum. I'm sorry that didn't allow that before."
                                        the_person.char "Cover your dearest [wife_name]'s face with semen. I really want it!"
                                        "[man_name] clearly liked the idea of doing it with his wife."
                                        the_person.char "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                        man_name "It really turns me on! I feel I can do another round shortly."
                                        the_person.char "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]."
                                        $ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                        the_person.char "Here we go. All finished!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        "As you turn to leave, you see [man_name]'s balls being caressed by [the_person.possessive_title] and his thing starting to rise."
                                        if submissive or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by incomprehensive loud blabbering from [the_person.possessive_title]'s room."
                                            the_person.char "Mrmh... Blgrhm..."
                                            man_name "That's it, [wife_name]. My bitch want a shower?"
                                            the_person.char "Oh, yes, Master! Cover my face with your blessing!"
                                            "Seems [man_name] liked the idea of roleplaying with face-fucking [the_person.possessive_title]. She doesn't seem to object."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "drink":
                                        the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                        man_name "No, [wife_name] never blows me. It pisses me off, now that I know how good it is."
                                        the_person.char "Well, that's your chance to try something new, [man_name]!"
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "She looks into [man_name]'s eyes while sucking him off. Her hand keeps jerking you in meantime."
                                        man_name "I'm gonna cum, [the_person.name]!"
                                        "She just keep on going at steady pace."
                                        the_person.char "Mmmmmm... Mmmm.. Uh."
                                        $ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "[man_name] shrugs and starts filling her mouth with his load."
                                        man_name "Oh, yes! Get it, [wife_name]!"
                                        "[man_name] clearly liked the idea of doing it with his wife."
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                        the_person.char "Liked that, [man_name]? [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                        man_name "It really turned me on! I feel I can do another round shortly."
                                        the_person.char "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]. I want to drink his stuff too."
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "With that she takes your cock with her hot lips."
                                        man_name "Never thought you are such cum drinking fan, [the_person.name]!"
                                        $ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up mouth around your dick and in few seconds you cum inside. She moves her head back and gulps."
                                        the_person.char "Here we go. Double sweet load."
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        if submissive or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by incomprehensive loud blabbering from [the_person.possessive_title]'s room."
                                            the_person.char "Mrmh... Blgrhm..."
                                            man_name "That's it, [wife_name]. Take it into your slutty mouth! Like the taste. whore?"
                                            "Seems [man_name] liked the idea of roleplaying with feeding [the_person.possessive_title]. She doesn't seem to object."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "usual":
                                        "[the_person.possessive_title] take his penis out of her mouth and looks up at him."
                                        the_person.char "Yes! Please cum on my breast. It's easier to clean than the furniture around."
                                        man_name "As you wish!"
                                        $ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[man_name] starts grinning as he ejaculates to [the_person.possessive_title]'s large boobs."
                                        man_name "Ow, fuck! That was great!"
                                        "[the_person.possessive_title] looks up at him and smiles."
                                        the_person.char "Indeed, [man_name]! Now let's finish with [the_person.mc_title]."
                                        $ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you also cum on [the_person.title]'s tits."
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person.char "Now go to your room, [the_person.mc_title]. Me and [man_name] need to take a bath."
                                        "You go back to your bedroom accompanied by shower sounds from [the_person.possessive_title]'s room."
                                else:
                                    $ the_person.happiness -= 5
                                    $ the_person.draw_person(position = "blowjob", emotion = "angry")
                                    the_person.char "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get back to your room now!"
                                    "You go back to your bedroom accompanied by bed sqeaking from [the_person.possessive_title]'s room as she keeps sucking [man_name]'s dick."
                            else:
                                while the_person.arousal < 100:
                                    "[the_person.possessive_title] keeps sucking his dick. You notice that she is rubbing her clit with a free hand."
                                    man_name "Oh, thats great, [the_person.name]! Your mouth is so sweet and nice."
                                    if submissive:
                                        "[the_person.possessive_title] grabs [man_name]'s ass and impales her mouth on his cock. His ball hit [the_person.possessive_title]'s jaw."
                                        man_name "Ow, that feels so good, [the_person.name]!"
                                    else:
                                        pass
                                    "As she gets more and more turned on, her moans get louder and louder."
                                    $ arousal_plus = renpy.random.randint (10,50)
                                    $ the_person.change_arousal (arousal_plus)
                                "[the_person.possessive_title] takes guys cock out and looks up."
                                the_person.char "Oh. I get so turned on with a cock im my mouth. I'm cumming!"
                                "She get's back to his dick as her body shivers with orgasm."
                                $ finish = get_random_from_list(finishes)
                                if finish == "facial":
                                    "She takes his dick out of her mouth."
                                    the_person.char "Would you like to cover my face with your hot cum? I doubt that your wife allows you to do this!"
                                    man_name "No, [wife_name] never do anything like that. I wish I could make her blow me."
                                    the_person.char "Well, that's your chance to try something new, [man_name]!"
                                    "She looks into [man_name]'s eyes while jerking him with both hands."
                                    man_name "I'm cumming [the_person.name]!"
                                    "She leans closer so that [man_name] tip is just in front of her eyes."
                                    the_person.char "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                    $ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name]!"
                                    "[the_person.possessive_title] decides to back up his play."
                                    the_person.char "Yes, dear. Cover my bitchy face with your cum. I'm sorry I didn't let you before."
                                    the_person.char "Cover your dearest [wife_name]'s face with semen. I really want it!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    $ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                    the_person.char "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                    man_name "It really turns me on! I feel I can do another round shortly."
                                    the_person.char "We will discuss it later, [man_name]! Now I need a shower."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person.char "Now we need to take a bath."
                                    "As you turn to leave, you see [man_name]'s balls being caressed by [the_person.possessive_title] and his thing starting to rise."
                                    if submissive or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by incomprehensive loud blabbering from [the_person.possessive_title]'s room."
                                        the_person.char "Mrmh... Blgrhm..."
                                        man_name "That's it, [wife_name]. You look great with this."
                                        "Seems [man_name] liked the idea of roleplaying with cumming on [the_person.possessive_title]. She doesn't seem to object."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                    man_name "No, [wife_name] never blows me. It pisses me off, now that I know how good it is."
                                    the_person.char "Well, that's your chance to try something new, [man_name]!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name]'s eyes while sucking him off."
                                    man_name "I'm gonna cum, [the_person.name]!"
                                    "She just keep on going at steady pace."
                                    the_person.char "Mmmmmm... Mmmm.. Uh."
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name] shrugs and starts filling her mouth with his load."
                                    man_name "Oh, yes! Get it, [wife_name]!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                    the_person.char "Liked that, [man_name]? [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name "It really turned me on! I feel I can do another round shortly."
                                    the_person.char "What a sweet load. As for another round, we will see..."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person.char "Now go to shower. I will join you shortly."
                                    if submissive or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by incomprehensive loud blabbering from [the_person.possessive_title]'s room."
                                        the_person.char "Mrmh... Blgrhm..."
                                        man_name "That's it, [wife_name]. A proper wife should like her man taste!"
                                        "Seems [man_name] liked the idea of roleplaying with feeding [the_person.possessive_title]. She doesn't seem to object."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    "[the_person.possessive_title] take his penis out of her mouth and looks up at him."
                                    the_person.char "Yes! Please cum on my breasts. It's easier to clean than the furniture."
                                    man_name "As you wish!"
                                    $ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name] starts grinning as he ejaculates to [the_person.possessive_title]'s large boobs."
                                    man_name "Ow, fuck! That was great!"
                                    "[the_person.possessive_title] looks up at him and smiles."
                                    the_person.char "Indeed, [man_name]! You did great!"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person.char "I really like the taste of big john, [man_name]."
                                    the_person.char "Now go the bathroom, I will join shortly."
                                    "You go back to your bedroom accompanied by shower sounds from [the_person.possessive_title]'s room."
            "Get back to bed.":
                "You decide that it is wrong to interfere into [the_person.possessive_title]'s private life so you go back to your room to sleep."
    elif encounter is 2: ##For a scene with 2 men
        $ man_name2 = get_random_male_name()
        while man_name is man_name2: ## Just to make sure that names don't match or it will look stupid
            $ man_name2 = get_random_male_name()
        $ wife_name2 = get_random_name()
        while wife_name2 is (the_person.char or wife_name): ## Just to avoid stupid duplications
            $ wife_name2 = get_random_name()

        ## let's create wives names here, just not to insert that in every scene it is required
        if bj:
            $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
            "You take a look inside the room and your eyes widen. You see two men sitting on a bed with their cocks out of their pants."
            "[the_person.possessive_title] is on her knees in front of them, sucking one cock and jerking the other."
            "By the look on men's faces you can tell that them are also quite surprised. One of them is clearly not very comfortable with the situation."
            $ the_person.draw_person(position = "blowjob", emotion="happy")
            "[the_person.possessive_title] notices that. She stops sucking the other man and looks to the confused one with a broad smile."
            the_person.char "Oh, relax, [man_name]. The event was great, you men were so nice. Why not let the fun continue?"
            man_name "Well, you have a point there. [man_name2], did you expect that when we agreed to drive [the_person.name] home, she will thank us this way?"
            man_name2 "I could only dream of [the_person.name] sucking my boy. We worked together for so many years and now..."
            $ the_person.discover_opinion("giving blowjobs")
            the_person.char "And for all those years, [man_name2], you never knew how I dreamed of your cock in my mouth. I just like sucking men off so much..."
            man_name "Wow. I had no idea that you is cock-sucking slut, [the_person.name]. Dreamed of my cock too?"
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "[the_person.possessive_title] just smiles then gets up, embraces and kisses [man_name] passionately."
            "It seems that [the_person.title] is having fun with her colleagues, [man_name] and [man_name2]."
            "You are unsure what to do here."
        else:
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "You see [the_person.possessive_title] embracing two men, kissing them deeply."
            the_person.char "Oh guys, you are so nice. I had a wonderful evening! Thanks for driving me home, [man_name]."
            man_name "Not a problem, [the_person.name]. I'm glad that [man_name2] joined us."
            man_name2 "I live in this district too, so you actually did me a favor as well."
            "As you open the door a little more, you recognize them . It's [man_name] and [man_name2], [the_person.possessive_title] colleagues."
            "You are unsure what to do here."
        menu:
            "Keep looking.":
                "You decide to see what they are up to."
                "They go on kissing. After a while [man_name] places his hands on [the_person.possessive_title]'s ass, slightly caressing it, while [man_name2] is fondling her tits."
                the_person.char "Oh, [man_name]. You clearly have some plans for tonight, don't you?."
                if bj:
                    "She strokes their cocks a little."
                else:
                    "She caresses their crotches."
                the_person.char "I like that plan, as well as your little friends there. How about we get more comfortable by getting rid of those clothes?"
                $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                if not mom_clothing is None:
                    $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                    man_name "That's a nice [mom_clothing.name] you have, [the_person.name]. I wonder how you will look without it."
                    "He takes off [the_person.possessive_title]'s [mom_clothing.name] and throws it on a nearby chair."
                if clothes_number >1:
                    $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                    if not mom_clothing is None:
                        the_person.char "I like the touch of your soft hands, [man_name]."
                        $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                        man_name2 "Let me help you too. Your [mom_clothing.name] need to go off, don't you agree?"
                if clothes_number >2:
                    $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                    if not mom_clothing is None:
                        the_person.char "Ooooh, [man_name2], you are really turning me on with your touches."
                        $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                        if the_person.outfit.vagina_available():
                            "[man_name] takes off her [mom_clothing.name], while [man_name2] plays with her open pussy."
                        else:
                            "[man_name] takes off her [mom_clothing.name], while [man_name2] and [the_person.possessive_title] kiss passionately."
                if clothes_number >3:
                    $ mom_clothing = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True, exclude_feet = True)
                    if not mom_clothing is None:
                        the_person.char "I don't mind go even more naked, guys. Who would like to take my [mom_clothing.name] next?"
                        $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                        if the_person.outfit.vagina_available():
                            "[man_name2] grants her wish, while [man_name] fingers her open pussy."
                        else:
                            "[man_name2] grants her wish, while [the_person.possessive_title] caresses [man_name2]'s crouch."
                $ the_person.sluttiness += 2
                "Now with all of them pretty naked, you clearly see where it will go."
                the_person.char "Oh, guys, I feel so horny around you. Let's have some fun!"
                menu:
                    "[the_person.title] lays on the table..." if the_person.outfit.vagina_available():
                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                        "You see as [the_person.possessive_title] lays on her table and spreads her legs, smiling broadely."
                        the_person.char "Alright, who's wanna be the first to bang your colleague?"
                        man_name "I've been in the company longer than any of you, so it would only be fair that I go first."
                        "He comes up to the table, kneels in front of it and starts licking [the_person.possessive_title]'s pussy."
                        $ arousal_plus = renpy.random.randint (5,20)
                        $ the_person.change_arousal (arousal_plus)
                        the_person.char "Oh yes, [man_name]! It feels so great."
                        "[man_name] kisses her clit than stands up."
                        man_name "One big dick for [the_person.name] coming right up!"
                        "In one powerful move he enters [the_person.possessive_title]. She rolls her eyes and moans."
                        the_person.char "Ahhh, fuck! That feels so good, [man_name]!"
                        "[man_name2] comes up to the table, stroking his dick."
                        man_name2 "How about you take care of me as well while I wait for my turn?"
                        the_person.char "Sure, [man_name2]. How about some helping hand?"
                        "She grabs his cock and starts stroking him while being pumped by [man_name]."
                        while the_person.arousal < 60:
                            "[man_name] moves his dick in [the_person.possessive_title] pussy. It goes in and out with a wet sound. Clearly [the_person.title] is having great time."
                            the_person.char "Please, [man_name], more. Bang me like you always wanted!"
                            if submissive:
                                the_person.char "Harder. I want a rough fuck! Nail me more!"
                            "As she gets more and more turned on, the speed of her hand on [man_name2]'s cock also increases."
                            $ arousal_plus = renpy.random.randint (10,50)
                            $ the_person.change_arousal (arousal_plus)
                        the_person.char "Oh, [man_name], you are so great, but I want to feel [man_name2] inside too!"
                        man_name "Oh, [the_person.name]... I hope you will take care of me in a meantime."
                        "[man_name] takes his cock out off her. You see [the_person.possessive_title]'s juices flowing out of her. She is clearly enjoying this."
                        menu:
                            "Keep hiding...":
                                $ hidden = True
                            "Don't hide...":
                                $ hidden = False
                        if detected or not hidden:
                            "While the men are changing positions, [the_person.possessive_title] turns her head and see that the door is slightly ajar and you standing there."
                            if the_person.sluttiness >=70 or the_person.get_opinion_score("public sex") > 0:
                                the_person.char "[the_person.mc_title], don't just stay there, come on in. [the_person.possessive_title] will help you relax as well."
                                man_name "Wow, [the_person.name]! Having two men at once, and now letting your son see it..."
                                the_person.char "My house, my rules. So, come on closer. I will help you let it go."
                                "You and [man_name] come to the table from both sides and [the_person.possessive_title] starts stroking your dicks."
                                "[man_name2] clearly has no objections of you joining the show as he puts his rock-hard cock into woman wet pussy."
                                the_person.char "Yes! It is so good!"
                                while the_person.arousal < 100:
                                    "[man_name2] keeps doing [the_person.possessive_title]. His hip are smashing into [the_person.possessive_title]'s."
                                    the_person.char "Yes, [man_name2]! Fuck me more. I feel so good now."
                                    if submissive:
                                        the_person.char "Rougher! Do me harder! Fuck my brains out, I beg you!"
                                    else:
                                        pass
                                    "As she gets more and more turned on, she strokes your dicks faster and faster."
                                    $ arousal_plus = renpy.random.randint (10,50)
                                    $ the_person.change_arousal (arousal_plus)
                                "After being fucked by [man_name2] for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                                the_person.char "Oh, God! I'm cumming! Fuck me! Fuck me more! Do me more, [man_name2]!"
                                "He starts to pump [the_person.possessive_title] real fast, his balls are smashing against [the_person.title]'s ass."
                                $ the_person.draw_person(position = "missionary", emotion = "orgasm")
                                the_person.char "Yes! Yes! That's it! I love you guys!"
                                man_name2 "Shit, [the_person.name], your pussy is driving me crazy! I think I will come soon!"
                                man_name "Same here, man."
                                $ finish = get_random_from_list(finishes)
                                if finish == "facial":
                                    the_person.char "Hold it, giys! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes [man_name2] backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name2] cock."
                                    the_person.char "[man_name], [the_person.mc_title], come here!"
                                    "Both of you come closer. Now [the_person.possessive_title] is on her knees with three erected dicks in front of her."
                                    the_person.char "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                    man_name "No, [wife_name] would never suggest anything like that..."
                                    man_name2 "I once proposed this to [wife_name2]. She called me a pervert who is watching too much porn."
                                    the_person.char "Well, now you can try the stuff from those movies yourselves!"
                                    "She looks into [man_name2]'s eyes while jerking your and [man_name]'s cocks with both hands. [man_name2] is jerking his member pointing into [the_person.title]'s face."
                                    man_name2 "I'm cumming [the_person.name]!"
                                    "She leans closer so that [man_name2] tip is just in front of her eyes."
                                    the_person.char "Do it, [man_name2]! Cover me! Imagine that's your wife, if you like."
                                    $ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name2 "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name2]!"
                                    "[man_name2] clearly liked the idea of doing it with his wife."
                                    the_person.char "Liked that, [man_name2]? Seeing a girl on her knees with your sperm over her face?"
                                    man_name2 "It really turns me on! I feel I can do another round shortly."
                                    the_person.char "We will discuss it later, [man_name]! Now let's finish with others."
                                    $ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] speeds up her hand around [man_name] dick and in few seconds he cums on her tits."
                                    the_person.char "Two out, one to go!"
                                    $ the_person.cum_on_stomach()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "Seeing [the_person.possessive_title] covered in cum is show enough and you start to ejaculate. You finish on [the_person.title]'s tits and there is so much of jizz so it starts falling on her belly."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person.char "Now go to your room, [the_person.mc_title]. Me and the boys need to take a bath."
                                    if submissive or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... More, please, do me more!"
                                        man_name2 "Now I want to take this bitch from behind. Get on all fours, [the_person.name]."
                                        "It seems that men are planning to fuck [the_person.possessive_title] all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and men's laughter from [the_person.possessive_title]'s room."
                                elif finish == "inside":
                                    the_person.char "Yes! Do it, [man_name2]! I want you to fill me."
                                    $ the_person.cum_in_vagina()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "After a few hard thrusts, [man_name2] starts spilling his semen into [the_person.possessive_title]."
                                    the_person.char "Yes, [man_name2]! I want it in me!"
                                    "After few seconds [man_name2] gets away [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy."
                                    the_person.char "Wow, [man_name2]! You really neded to get some steam off! That was a huge load."
                                    man_name2 "And you look gorgeous, [the_person.name] lying there, full of my cum. And with two cocks in hands."
                                    the_person.char "Glad you like it, [man_name2]! Now [man_name], fill me up!"
                                    "[man_name] comes to [the_person.possessive_title]'s vagina and starts doing her again. As he is well aroused, after a few frictions he grins."
                                    the_person.char "Cum in me! Give it all to me!"
                                    $ the_person.cum_in_vagina()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "After a few final trusts, [man_name] pulls out. You see even more sperm flowing out."
                                    $ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                    the_person.char "Here we go. All finished!"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person.char "Now go to your room, [the_person.mc_title]. Me and guys need to take a bath."
                                    $ the_person.draw_person(position = "walking_away")
                                    "As [the_person.possessive_title] starts walking towards bathroom, you see several white drops falling on the floor."
                                    "While she walks past [man_name], he places his hand on her butt."
                                    the_person.char "First - the shower. Then we will see, dear."
                                    man_name2 "Wait for me!"
                                    if submissive  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... Fill me with cum!"
                                        man_name2 "Oh, [the_person.name], I'm gonna fill you so much that it will come from your ears!"
                                        "It seems that men are planning to fuck [the_person.possessive_title] all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and bed sqeaking from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person.char "Hold it, [man_name]! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name2] cock."
                                    the_person.char "[man_name], [the_person.mc_title], come here!"
                                    "Both of you come closer. Now [the_person.possessive_title] is on her knees with three erected dicks in front of her."
                                    the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                    man_name2 "No, [wife_name2] never allows anything other than missionary with a condom, she is so prudent and boring at times."
                                    man_name "I asked [wife_name] once for a bj. She tried but it was awful and she called it disgusting..."
                                    the_person.char "Well, thats your chance to try something new, guys!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name2]'s eyes while sucking him off. Her hands are working on two other dicks in meantime."
                                    man_name2 "I'm gonna cum, [the_person.name]!"
                                    "She just keep on going at steady pace."
                                    the_person.char "Mmmmmm... Mmmm.. Uh."
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name2] shrugs and starts filling her mouth with his load."
                                    man_name2 "Oh, yes! Get it, [wife_name2]!"
                                    "[man_name2] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                                    the_person.char "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name2 "It really turned me on! I feel I can do another round shortly."
                                    the_person.char "We will discuss it later, [man_name2]! Now let's finish with [man_name]. I want to drink his stuff too."
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "With that she takes his cock with her hot lips."
                                    man_name2 "Never thought you are such cum drinking fan, [the_person.name]!"
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] speeds up mouth around [man_name]'s dick and in few seconds he cums inside. She retreats back and gulps."
                                    the_person.char "Here we go. Double sweet load. Now for [the_person.mc_title]."
                                    man_name "Well, her mouth is really something."
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] take you dick in her mouth and in a short time you also explode inside."
                                    "She retreats back and gulps."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person.char "Now go to your room, [the_person.mc_title]. Me and guys need to take a bath."
                                    if submissive  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... Let me drink your cum!"
                                        man_name2 "Open up your mouth, slut!  You gonna be feed with some hot stuff!"
                                        "It seems that men are planning to fuck [the_person.possessive_title] all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and gulping sounds from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    $ the_person.cum_on_stomach()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "[man_name2] pulls out his cock and finishes on [the_person.possessive_title] belly."
                                    man_name2 "Ow, fuck! That was great!"
                                    the_person.char "Indeed, [man_name2]! It was great! Best fuck I had in some time! Now let's finish with others."
                                    $ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "[the_person.possessive_title] speeds up her hand around your dicks and in few seconds you both cum on her tits."
                                    the_person.char "Here we go. All finished!"
                                    man_name "I don't believe it, [the_person.name]. You just let your son watch us fuck and then jerked him off!"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person.char "Didn't that turn you on, [the_person.mc_title]?"
                                    the_person.char "Now go to your room, [the_person.mc_title]. Me and colleagues need to take a bath."
                                    "You go back to your bedroom accompanied by shower sounds from [the_person.possessive_title]'s room."
                            else:
                                $ the_person.happiness -= 5
                                $ the_person.draw_person(position = "missionary", emotion = "angry")
                                the_person.char "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get beck to your room now!"
                                "You go back to your bedroom accompanied by bed sqeaking from [the_person.possessive_title]'s room as men keep doing her."
                        else:
                            while the_person.arousal < 100:
                                    "[man_name2] puts his dick into [the_person.possessive_title] pussy. By the look on [the_person.title]'s face she is clearly having great time."
                                    "While being pumped by [man_name2], she grabs [man_name] cock and strokes him."
                                    the_person.char "Please, [man_name2], more. Fuck me! Fuck your [the_person.name]!"
                                    if submissive:
                                        the_person.char "Harder! Slam your dick in me, [man_name2]. I love being fucked roughly!"
                                    "As she gets more and more turned on, her screams get louder and louder."
                                    $ arousal_plus = renpy.random.randint (10,50)
                                    $ the_person.change_arousal (arousal_plus)
                            "After being fucked by [man_name2] for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                            the_person.char "Oh, God! I'm cumming! Fuck me! Keep doing this, [man_name2]!"
                            "He starts to pump [the_person.possessive_title] faster and faster, fully buring his dick in her."
                            $ the_person.draw_person(position = "missionary", emotion = "orgasm")
                            the_person.char "Yes! Yes! That's it! You made me cum, [man_name2]!"
                            man_name2 "Shit, [the_person.name], your pussy is driving me crazy! I think I will come soon!"
                            man_name "Me too!"
                            $ finish = get_random_from_list(finishes)
                            if finish == "facial":
                                the_person.char "Hold it, guys! I have a better idea."
                                $ the_person.draw_person(position = "blowjob")
                                "She pushes [man_name2] backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name2] cock."
                                the_person.char "Come here, [man_name]."
                                "He comes over. Now [the_person.possessive_title] is sitting on the floor with two dicks up to her face."
                                the_person.char "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                man_name2 "No, [wife_name2] is not into lewd stuff. It's so boring. I wish to see [wife_name2] in sperm, just like in those movies."
                                man_name "I once came on [wife_name] belly. She called me a prevert and didn't spoke to me for a week!"
                                the_person.char "Well, thats your chance to try something new, guys! Just like the movies."
                                "She looks into [man_name2]'s eyes while jerking him with both hands."
                                man_name2 "I'm cumming [the_person.name]!"
                                "She leans closer so that [man_name2] tip is just in front of her eyes."
                                the_person.char "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                $ the_person.cum_on_face()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                man_name2 "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name2]!"
                                "[man_name] clearly liked the idea of doing it with his wife."
                                man_name "Shit, that's hot! I'm cumming too!"
                                $ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "Second load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                the_person.char "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                man_name "It really turns me on! I feel I can do another round shortly."
                                the_person.char "We will discuss it later, guys. First - a shower. I need to wash off it before it dries."
                                $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                "You see them walking away to bathroom. Some white drops fall on the floor."
                                "Both men hands are on [the_person.title]'s ass, but she does not object. As they close the door, you see that [the_person.possessive_title] caresses their balls while dicks show signs of returning to life."
                                if submissive  or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person.char "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... More, please, do me more!"
                                    man_name "On your face, [wife_name]! Looking good bitch!"
                                    man_name2 "And this is for you, [wife_name2]! Aren't you a slut?"
                                    "It seems the guys liked role-playing with [the_person.possessive_title] as their fuck doll."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans and bed sqeaks from [the_person.possessive_title]'s room."
                            elif finish == "inside":
                                the_person.char "Yes! Do it, [man_name2]! I want you to fill me."
                                $ the_person.cum_in_vagina()
                                $ the_person.draw_person(position = "missionary", emotion = "happy")
                                "After a few hard thrusts, [man_name2] starts spilling his semen into [the_person.possessive_title]."
                                the_person.char "Yes, [man_name2]! I want it in me!"
                                "After few seconds [man_name2] gets off [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy."
                                the_person.char "Wow, [man_name2]! You really neded to get some steam off! That was a huge load."
                                man_name "And you look gorgeous, [the_person.name] lying there, full of my cum. I wish my wife would allow this."
                                the_person.char "Glad you like it, [man_name2]! Want a better picture?"
                                "[the_person.possessive_title] spreads her legs even further, offering a full view of her cum-drenched pussy."
                                the_person.char "Here we go. Remember the view next time you fuck your wife. Now [man_name], come here and fill me as well!"
                                "He comes over, enter's [the_person.possessive_title] pussy and after a few moves starts to grin."
                                $ the_person.cum_in_vagina()
                                $ the_person.draw_person(position = "missionary", emotion = "happy")
                                the_person.char "Yes! Inside. Fill me!"
                                "After [man_name] finshes, he pulls out. [the_person.possessive_title] is laying on the table with white liquid flows out of her."
                                $ the_person.draw_person(position = "back_peek", emotion = "happy")
                                "[the_person.possessive_title] stands up from the bed and heads towards bathroom. [man_name] slaps her ass."
                                the_person.char "Now I need to take a bath. Then we will see"
                                $ the_person.draw_person(position = "walking_away")
                                "As [the_person.possessive_title] walks towards bathroom, you see several white drops falling on the floor."
                                if submissive or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person.char "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... Cum in me! I want to be filled."
                                    man_name2 "Spread wide and receive my load as well!"
                                    "Seems that men just foun out a warm and comfortable place for them, as they seem to do [the_person.possessive_title] all night long."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "drink":
                                the_person.char "Hold it, [man_name2]! I have a better idea."
                                $ the_person.draw_person(position = "blowjob")
                                "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name2] cock."
                                the_person.char "Come here, [man_name]."
                                "He comes over. Now [the_person.possessive_title] is sitting on the floor with two dicks up to her face."
                                the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                man_name2 "No, [wife_name2] hates oral sex. It is so frustrating."
                                man_name "I once asked [wife_name] for a blowjob. She said if I ever ask this again she will file a divorce!"
                                the_person.char "Well, thats your chance to experience the feeling, guys!"
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "She looks into [man_name2]'s eyes while sucking him off."
                                man_name2 "I'm gonna cum, [the_person.name]!"
                                "She just keep on going at steady pace."
                                the_person.char "Mmmmmm... Mmmm.. Uh."
                                $ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[man_name2] shrugs and starts filling her mouth with his load."
                                man_name "Oh, yes! Get it, [wife_name2]!"
                                "[man_name2] clearly liked the idea of doing it with his wife."
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                the_person.char "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                man_name "It really turned me on! I feel I can do another round shortly."
                                the_person.char "We will discuss it later, [man_name2]. First - I need to taste [man_name]."
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "She puts another dick int oher mouth and sucks it off."
                                man_name "This is so great. I can't hold much longer!"
                                $ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[man_name] comes into [the_person.possessive_title]'s mouth and pulls his cock away. You see her mouth is full of cum. Then she gulpes it and stands up."
                                $ the_person.draw_person(position = "walking_away")
                                "You see them walking away to bathroom."
                                "[man_name]'s hand is on [the_person.title]'s ass, and [man_name2] caresses her between the legs, but she does not object. As they enter bathroom, men's dicks show signs of returning to life."
                                if submissive or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person.char "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... Give it to me! I want to drink it all!"
                                    man_name2 "Like the taste, bitch? Aren't you a cum-gulping whore, [the_person.name]?"
                                    "It seems [the_person.possessive_title]'s mouth gonna keep them awake for a while..."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "usual":
                                $ the_person.cum_on_stomach()
                                $ the_person.draw_person(position = "missionary", emotion = "happy")
                                "[man_name2] pulls out his cock and finishes on [the_person.possessive_title] belly."
                                man_name2 "Ow, fuck! That was great!"
                                the_person.char "Indeed, [man_name2]! It was great!"
                                if submissive:
                                     the_person.char "I guess you like when a girl allows you to be rough, don't you? I too like how it feels being owned by a man while he fucks me."
                                     man_name2 "Yes, it is a wonderful feeling. It really turns me on. Wish I could do this with my wife..."
                                man_name2 "Thanks, [the_person.name]. I really needed that."
                                man_name "I'm cumming too!"
                                $ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "missionary", emotion = "happy")
                                "After being stroked for so long, he finally cums on [the_person.possessive_title]'s tits."
                                $ the_person.draw_person(position = "stand2", emotion = "happy")
                                "[the_person.possessive_title] stands up from the bed and smiles."
                                the_person.char "Didn't that event paid off, dear?"
                                the_person.char "Now go to bath, guys. I will join you shortly."
                                "You go back to your bedroom accompanied by shower sounds from [the_person.possessive_title]'s room."
                    "[the_person.title] shows on the bed..." if the_person.outfit.vagina_available() and (the_person.sluttiness > 70 or the_person.get_opinion_score("anal sex") > 0):
                        the_person.char "Alright, I have an idea of how we all can have fun. Please, [man_name], lie on the bed."
                        "The man does so. From where you stand you can see how hard he is."
                        $ the_person.draw_person(position = "doggy")
                        "[the_person.possessive_title] gets over him and puts his cock inside."
                        the_person.char "Oh, you have a wonderful thing here, [man_name]. Now, [man_name2], how about you stick your instrument in my ass? There is some lubricant in mddle drawer."
                        man_name2 "Shit, [the_person.name]... I could only dream of anal. And you butt is so sweet."
                        "He comes up to the table, takes a tube of lubricant, pours some on his dick, then fingers [the_person.possessive_title]'s ass with it."
                        the_person.char "Thanks, [man_name2]. I'm ready. Put it in me."
                        $ arousal_plus = renpy.random.randint (5,20)
                        $ the_person.change_arousal (arousal_plus)
                        "[man_name2] comes from behind and starts to slowly push against [the_person.possessive_title]'s ass."
                        the_person.char "Keep going, [man_name2]. It feels so pleasant."
                        "The man is now fully inside [the_person.possessive_title]'s ass."
                        the_person.char "Ahhh, fuck! That feels so good, guys!"
                        "Men start to slowly move. [the_person.possessive_title] kiss [man_name] with a passion, while [man_name2] is caressing her buttocks."
                        the_person.char "Ohh, guys! You make me feel so good!"
                        if submissive:
                            the_person.char "Harder! Nail me with your cocks. I want you to be rough with your [the_person.name]. I'm your fuck toy today!"
                            $ the_person.discover_opinion("being submissive")
                        else:
                            pass
                        "You just can't believe your eyes - [the_person.possessive_title] gets screwed by two men at once!"
                        menu:
                            "Keep hiding...":
                                $ hidden = True
                            "Don't hide...":
                                $ hidden = False
                        if detected or not hidden:
                            if the_person.sluttiness >=70 or the_person.get_opinion_score("public sex") > 0:
                                "[the_person.possessive_title] raises her head and in the mirror next to bed sees that the door is slightly ajar and you standing there."
                                the_person.char "[the_person.mc_title], don't just stay there, come on in. [the_person.possessive_title] will help you relax as well."
                                man_name2 "Wow, [the_person.name]! Two of us not enough for you?"
                                if submissive:
                                    the_person.char "I want two of you to fuck me real hard so that I would scream like mad. I don't want to wake Lily so I need something to shut my mouth."
                                    man_name "Wanna a rough fuck, [the_person.name]? Can do!"
                                else:
                                    the_person.char "My house, my rules. So, come on [the_person.mc_title]. I will help you relax."
                                "You stand on the bed in front of [the_person.possessive_title] and she starts sucking your dick."
                                "The guys go on doing [the_person.possessive_title]'s two holes at once."
                                the_person.char "Mhhhh.... Ohmmmm..."
                                while the_person.arousal < 100:
                                    "[man_name2] and [man_name] keep fucking [the_person.possessive_title] two ways."
                                    the_person.char "Mhmhmmmmh..."
                                    "Your cock in [the_person.possessive_title]'s mouth prevents her from saying anything, she can only moan. On her face you see a mixture of pain and pleasure."
                                    if submissive:
                                        "She pulls her head away from you."
                                        the_person.char "Oh God! Fuck me! Fuck! Fuck!"
                                        "Afraid that she would wake up Lily, you grab her head and impale her wide open mouth on your dick."
                                        "It seems to turn her on even more."
                                    else:
                                        pass
                                    "As she gets more and more turned on, she sucks your dick faster and faster."
                                    $ arousal_plus = renpy.random.randint (10,50)
                                    $ the_person.change_arousal (arousal_plus)
                                "After being fucked by three of you for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                                the_person.char "Oh, God! I'm cumming! Fuck me! Fuck me more! Fill my holes!"
                                "Both men start to pump [the_person.possessive_title] real fast, their bodies slamming into her."
                                the_person.char "Aaaaaahhh...! Fuuuuuuck! Cumming!"
                                "Both men don't stop there, they keep on going. [the_person.possessive_title] seems to have reached multiple orgasms."
                                the_person.char "Yeah! More! Harder! Fuck me! Screw me! Rip me apart!"
                                man_name2 "Shit, [the_person.name], your ass is so tight! I think I will come soon!"
                                man_name "Same here, man."
                                $ finish = get_random_from_list(finishes)
                                if finish == "facial":
                                    the_person.char "Hold it, giys! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes away from man's crouches. With a wet sound their dicks leaves her holes. [the_person.possessive_title] gets on her knees on the bed."
                                    the_person.char "[man_name], [man_name2], [the_person.mc_title], come here!"
                                    "Three of you come closer. Now [the_person.possessive_title] is on her knees with three erected dicks in front of her."
                                    the_person.char "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                    man_name "No, [wife_name] would never suggest anything like that..."
                                    man_name2 "I once proposed this to [wife_name2]. She called me a pervert who is watching too much porn."
                                    the_person.char "Well, now you can try the stuff from those movies yourselves!"
                                    "She looks into [man_name2]'s eyes while jerking your and [man_name]'s cocks with both hands. [man_name2] is jerking his member pointing into [the_person.title]'s face."
                                    man_name2 "I'm cumming [the_person.name]!"
                                    "She leans closer so that [man_name2] tip is just in front of her eyes."
                                    the_person.char "Do it, [man_name2]! Cover me! Imagine that's your wife, if you like."
                                    $ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name2 "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name2]!"
                                    "[man_name2] clearly liked the idea of doing it with his wife."
                                    the_person.char "Liked that, [man_name2]? Seeing a girl on her knees with your sperm over her face?"
                                    man_name "It really turns me on! I feel I can do another round shortly."
                                    the_person.char "We will discuss it later, [man_name]! Now let's finish with others."
                                    $ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] speeds up her hand around [man_name] dick and in few seconds he cums on her tits."
                                    the_person.char "Two out, one to go!"
                                    $ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "Seeing [the_person.possessive_title] covered in cum is show enough and you start to ejaculate. You finish on [the_person.title]'s tits and there is so much of jizz so it starts falling on her belly."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person.char "Now go to your room, [the_person.mc_title]. Me and the boys need to take a bath."
                                    if submissive or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Do me again, [man_name]. Take my ass!"
                                        man_name "We are out of lubricant, so suck me for a while,[the_person.name]."
                                        the_person.char "Sure, come here. Ahhh, [man_name2], keep doing me! I like it from behind."
                                        "It seems that men are planning to fuck [the_person.possessive_title] all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and men's laughter from [the_person.possessive_title]'s room."
                                elif finish == "inside":
                                    the_person.char "Yes! Do it, [man_name]! I want you to fill me."
                                    $ the_person.cum_in_vagina()
                                    $ the_person.draw_person(position = "doggy")
                                    "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                                    the_person.char "Yes, [man_name]! I want it in me!"
                                    "After few seconds [man_name] gets away [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy."
                                    the_person.char "Wow, [man_name]! You really neded to get some steam off! That was a huge load."
                                    man_name "And you look gorgeous, [the_person.name] lying there, full of my cum, being nailed in the ass."
                                    the_person.char "Glad you like it, [man_name]! Now [man_name2], fill me up!"
                                    "[man_name2] takes his cock from her ass and puts it into [the_person.possessive_title]'s vagina and starts doing her. As he is well aroused, after a few frictions he grins."
                                    the_person.char "Cum in me! Give it all to me!"
                                    $ the_person.cum_in_vagina()
                                    $ the_person.draw_person(position = "doggy")
                                    "After a few final trusts, [man_name2] pulls out. You see even more sperm flowing out."
                                    $ the_person.cum_on_tits()
                                    "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                    the_person.char "Here we go. All finished!"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person.char "Now go to your room, [the_person.mc_title]. Me and guys need to take a bath."
                                    $ the_person.draw_person(position = "walking_away")
                                    "As [the_person.possessive_title] starts walking towards bathroom, you see several white drops falling on the floor."
                                    "While she walks past [man_name], he places his hand on her butt."
                                    the_person.char "First - the shower. Then we will see, dear."
                                    man_name2 "Wait for me!"
                                    if submissive  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Do me again, guys. Fuck me more! Ahhh... Fill me with cum!"
                                        man_name2 "Oh, [the_person.name], now we will fill both your holes!"
                                        "It seems that men are planning to fuck [the_person.possessive_title]'s holes all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and bed sqeaking from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person.char "Hold it, guys! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes away from them. With a wet sound their dicks leaves her pussy and anus. [the_person.possessive_title] gets on her knees on the bed."
                                    the_person.char "[man_name], [man_name2], [the_person.mc_title], come here!"
                                    "Three of you come closer. Now [the_person.possessive_title] is on her knees with three erected dicks in front of her."
                                    the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                    man_name2 "No, [wife_name2] never allows anything other than missionary with a condom, she is so prudent and boring at times."
                                    man_name "I asked [wife_name] once for a bj. She tried but it was awful and she called it disgusting..."
                                    the_person.char "Well, thats your chance to try something new, guys!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name2]'s eyes while sucking him off. Her hands are working on two other dicks in meantime."
                                    man_name2 "I'm gonna cum, [the_person.name]!"
                                    "She just keep on going at steady pace."
                                    the_person.char "Mmmmmm... Mmmm.. Uh."
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name2] shrugs and starts filling her mouth with his load."
                                    man_name2 "Oh, yes! Get it, [wife_name2]!"
                                    "[man_name2] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                                    the_person.char "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name2 "It really turned me on! I feel I can do another round shortly."
                                    the_person.char "We will discuss it later, [man_name2]! Now let's finish with [man_name]. I want to drink his stuff too."
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "With that she takes his cock with her hot lips."
                                    man_name2 "Never thought you are such cum drinking fan, [the_person.name]!"
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] speeds up mouth around [man_name]'s dick and in few seconds he cums inside. She retreats back and gulps."
                                    the_person.char "Here we go. Double sweet load. Now for [the_person.mc_title]."
                                    man_name "Well, her mouth is really something. I wish [wife_name] could do the same!"
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] take you dick in her mouth and in a short time you also explode inside."
                                    "She retreats back and gulps."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person.char "Now go to your room, [the_person.mc_title]. Me and guys need to take a bath."
                                    if submissive  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Take me again, guys. Fuck me however you want! My ass and pussy are all yours! Just let me drink your semen!"
                                        man_name2 "Open up your mouth, slut!  You gonna be feed with some hot stuff!"
                                        man_name "Can you take two loads at once, [the_person.name]?"
                                        "It seems that men are planning to use [the_person.possessive_title] as cum dump all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and guliong sounds from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    $ the_person.cum_on_stomach()
                                    "[man_name] pulls out his cock and finishes on [the_person.possessive_title] belly."
                                    man_name "Ow, fuck! That was great!"
                                    the_person.char "Indeed, [man_name]! It was great! Best fuck I had in some time! Now let's finish with others."
                                    $ the_person.cum_on_ass()
                                    $ the_person.draw_person(position = "doggy")
                                    "[man_name2] grabs her butt and speeds up. In few seconds he cums on her ass."
                                    $ the_person.cum_on_tits()
                                    "Aroused by the view you cum on [the_person.possessive_title]'s tits."
                                    the_person.char "Here we go. All finished!"
                                    man_name "I don't believe it, [the_person.name]. You just let your son watch us fuck you two ways and then sucked him off!"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person.char "Didn't that turn you on, [the_person.mc_title]?"
                                    the_person.char "Now go to your room, [the_person.mc_title]. Me and colleagues need to take a bath."
                                    if submissive  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Take me again, guys, please. I really liked your hard things in me at once!"
                                        man_name2 "You are sex hungry slut, [the_person.name]."
                                        man_name "Let me take your ass this time."
                                        "It seems that men are planning to have some more fun with [the_person.possessive_title]..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and guliong sounds from [the_person.possessive_title]'s room."
                            else:
                                $ the_person.happiness -= 5
                                the_person.char "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get beck to your room now!"
                                "You go back to your bedroom accompanied by bed sqeaking from [the_person.possessive_title]'s room as men keep doing her."
                        else:
                            "The guys go on doing [the_person.possessive_title]'s two holes at once."
                            the_person.char "Ow, it is so good! More!"
                            while the_person.arousal < 100:
                                "[man_name2] and [man_name] keep fucking [the_person.possessive_title] two ways."
                                the_person.char "More, please. Fuck me more!"
                                if submissive:
                                    the_person.char "Harder! Rip me apart! Take me roughly!"
                                else:
                                    pass
                                "As she gets more and more turned on, her screams get louder and louder."
                                $ arousal_plus = renpy.random.randint (10,50)
                                $ the_person.change_arousal (arousal_plus)
                            "After being fucked by two men at once for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                            the_person.char "Oh, God! I'm cumming! Fuck me! Fuck me more! Fill my holes!"
                            "Men start to pump [the_person.possessive_title] real fast, their bodies slamming into her."
                            the_person.char "Aaaaaahhh...! Fuuuuuuck! Cumming!"
                            "Guys do not stop there, they keep on going. [the_person.possessive_title] seems to have reached multiple orgasms."
                            the_person.char "Yeah! More! More! Fuck me! Do me!"
                            man_name2 "Shit, [the_person.name], your ass is so tight! I think I will come soon!"
                            man_name "Same here, man."
                            $ finish = get_random_from_list(finishes)
                            if finish == "facial":
                                the_person.char "Hold it, guys! I have a better idea."
                                $ the_person.draw_person(position = "blowjob")
                                "She pushes them backwards. [the_person.possessive_title] gets on her knees on the bed. Men come up to her, stroking their cocks."
                                the_person.char "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                man_name2 "No, [wife_name2] is not into lewd stuff. It's so boring. I wish to see [wife_name2] in sperm, just like in those movies."
                                man_name "I once came on [wife_name] belly. She called me a prevert and didn't spoke to me for a week!"
                                the_person.char "Well, thats your chance to try something new, guys! Just like the movies."
                                "She looks into [man_name2]'s eyes while jerking him with both hands."
                                man_name2 "I'm cumming [the_person.name]!"
                                "She leans closer so that [man_name2] tip is just in front of her eyes."
                                the_person.char "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                $ the_person.cum_on_face()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                man_name2 "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name2]!"
                                "[man_name] clearly liked the idea of doing it with his wife."
                                man_name "Shit, that's hot! I'm cumming too!"
                                $ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "Second load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                the_person.char "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                man_name "It really turns me on! I feel I can do another round shortly."
                                the_person.char "We will discuss it later, guys. First - a shower. I need to wash off it before it dries."
                                $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                "You see them walking away to bathroom. Some white drops fall on the floor."
                                "Both men hands are on [the_person.possessive_title]'s ass, but she does not object. As they close the door, you see that [the_person.title] caresses their balls while dicks show signs of returning to life."
                                if submissive  or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person.char "Do me again, [man_name]. Fuck me any way you want! Harder! And spray it all over me!"
                                    man_name "On your face, [wife_name]! Looking good bitch!"
                                    man_name2 "And this is for you, [wife_name2]! Aren't you a slut?"
                                    "It seems the guys liked role-playing with [the_person.possessive_title] as their fuck doll."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans and bed sqeaks from [the_person.possessive_title]'s room."
                            elif finish == "inside":
                                the_person.char "Yes! Do it, [man_name]! I want you to fill me."
                                $ the_person.cum_in_vagina()
                                $ the_person.draw_person(position = "doggy")
                                "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                                the_person.char "Yes, [man_name]! I want it in me!"
                                "After few seconds [man_name] gets away [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy."
                                the_person.char "Wow, [man_name]! You really neded to get some steam off! That was a huge load."
                                man_name "And you look gorgeous, [the_person.name] lying there, full of my cum, being nailed in the ass."
                                the_person.char "Glad you like it, [man_name]! Now [man_name2], fill me up!"
                                "[man_name2] takes his cock from her ass and puts it into [the_person.possessive_title]'s vagina and starts doing her. As he is well aroused, after a few frictions he grins."
                                the_person.char "Cum in me! Give it all to me!"
                                $ the_person.cum_in_vagina()
                                $ the_person.draw_person(position = "doggy")
                                "After a few final trusts, [man_name2] pulls out. You see even more sperm flowing out."
                                $ the_person.draw_person(position = "back_peek", emotion = "happy")
                                "[the_person.possessive_title] stands up from the bed and heads towards bathroom. [man_name] slaps her ass."
                                the_person.char "Now I need to take a bath. Then we will see on having more fun."
                                $ the_person.draw_person(position = "walking_away")
                                "As [the_person.possessive_title] walks towards bathroom, you see several white drops falling on the floor."
                                if submissive or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person.char "Take me again, guys. Fuck me hard! Use my holes to your pleasure. Cum in me! I want to be filled."
                                    man_name2 "Spread wide and receive my load as well!"
                                    man_name "Oh, [the_person.name], now we will fill both your holes!"
                                    "Seems that both men liked to fill [the_person.possessive_title] with sperm, as they seem to do [the_person.possessive_title] all night long."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "drink":
                                the_person.char "Hold it, [man_name2]! I have a better idea."
                                $ the_person.draw_person(position = "blowjob")
                                "She pushes away from them. With a wet sound their dicks leaves her pussy and anus. [the_person.possessive_title] gets on her knees on the bed."
                                the_person.char "[man_name], [man_name2], come here!"
                                "Both of them come closer. Now [the_person.possessive_title] is on her knees with two hard dicks in front of her."
                                the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                man_name2 "No, [wife_name2] never allows anything other than missionary with a condom, she is so prudent and boring at times."
                                man_name "I asked [wife_name] once for a bj. She tried but it was awful and she called it disgusting..."
                                the_person.char "Well, thats your chance to try something new, guys!"
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "She looks into [man_name2]'s eyes while sucking him off. Her hands are working on [man_name]'s dick in meantime."
                                man_name2 "I'm gonna cum, [the_person.name]!"
                                "She just keep on going at steady pace."
                                the_person.char "Mmmmmm... Mmmm.. Uh."
                                $ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[man_name2] shrugs and starts filling her mouth with his load."
                                man_name2 "Oh, yes! Get it, [wife_name2]!"
                                "[man_name2] clearly liked the idea of doing it with his wife."
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                                the_person.char "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                man_name "It really turned me on! I feel I can do another round shortly."
                                the_person.char "We will discuss it later, [man_name2]! Now let's finish with [man_name]. I want to drink his stuff too."
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "With that she takes his cock with her hot lips."
                                man_name2 "Never thought you are such cum drinking fan, [the_person.name]!"
                                $ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "[the_person.possessive_title] speeds up mouth around [man_name]'s dick and in few seconds he cums inside. She retreats back and gulps. With a happy smile she gets up."
                                $ the_person.draw_person(position = "walking_away")
                                the_person.char "Such a sweet taste. Now for a bath."
                                "You see them walking away to bathroom."
                                "[man_name]'s hand is on [the_person.title]'s ass, and [man_name2] caresses her between the legs, but she does not object. As they enter bathroom, men's dicks show signs of returning to life."
                                if submissive or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person.char "Take my ass again, [man_name2]. Fuck me more! Ahhh... Give it to me! I want to drink it all!"
                                    man_name2 "Like the taste, bitch? Aren't you a cum-gulping whore, [the_person.name]?"
                                    "It seems [the_person.possessive_title]'s mouth gonna keep them awake for a while..."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "usual":
                                $ the_person.cum_on_stomach()
                                "[man_name] pulls out his cock and finishes on [the_person.possessive_title] belly."
                                man_name "Ow, fuck! That was great!"
                                the_person.char "Indeed, [man_name]! It was great! I also liked having you two in me."
                                if submissive:
                                     the_person.char "I guess I just like being used this way. I  like feel owned by men whilethey fuck me."
                                     man_name "Yes, it is a wonderful feeling. I really turns me on. Wish I could do it with my wife..."
                                man_name "Thanks, [the_person.name]. I really needed that."
                                man_name2 "I'm cumming too!"
                                $ the_person.cum_on_ass()
                                $ the_person.draw_person(position = "doggy")
                                "[man_name2] takes his dick out of [the_person.possessive_title]'s ass and covers it with his liquid."
                                $ the_person.draw_person(position = "stand2", emotion = "happy")
                                "[the_person.possessive_title] stands up from the bed and smiles."
                                the_person.char "Didn't that event went great?"
                                the_person.char "Now go to bath, guys. I will join you shortly."
                                if submissive  or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person.char "Take me again, guys, please. I really liked your hard things in me at once!"
                                    man_name2 "You are sex hungry slut, [the_person.name]."
                                    man_name "Let me take your ass this time."
                                    "It seems that men are planning to have some more fun with [the_person.possessive_title]..."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                    "[the_person.title] gets on her knees":
                        $ the_person.draw_person(position = "blowjob")
                        "You see as [the_person.possessive_title] gets on her knees, taking down [man_name]'s underwear."
                        "His erected dick is right in front of [the_person.possessive_title]'s face."
                        the_person.char "Hello there, sweetie. How about we have some fun together?"
                        "[man_name2] also drops his pants and come to her."
                        $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                        "[the_person.possessive_title] takes the cock in her mouth and starts sucking."
                        "[man_name] places his hands on her head slighty regulating the speed."
                        man_name "It feels great, [the_person.name]. I like the way you do it!"
                        man_name2 "How about giving me some pleasure too?"
                        "[the_person.possessive_title] begins to suck [man_name2]'s cock, while jerking [man_name]."
                        $ arousal_plus = renpy.random.randint (10,50)
                        $ the_person.change_arousal (arousal_plus)
                        menu:
                            "Keep hiding...":
                                $ hidden = True
                            "Don't hide...":
                                $ hidden = False
                        if detected or not hidden:
                            "[the_person.possessive_title] turns her head and sees that the door is slightly ajar and you standing there."
                            if the_person.sluttiness >=70 or the_person.get_opinion_score("public sex") > 0:
                                "[the_person.possessive_title] takes [man_name2]'s dick out of her mouth."
                                the_person.char "[the_person.mc_title], don't just stay there, come on in. [the_person.possessive_title] will help you relax as well."
                                "Both [man_name] and [man_name2] don't mind you joining the show as [the_person.possessive_title] goes back to sucking them."
                                "You come close to [the_person.possessive_title] and take your dick out of your pants."
                                "She starts stroking you along with [man_name] while [man_name2] keeps driving his dick into her mouth."
                                man_name2 "Oh, [the_person.name], your toungue is driving me crazy! I think I will come soon!"
                                $ finish = get_random_from_list(finishes)
                                if finish == "facial":
                                    the_person.char "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                    man_name2 "No, [wife_name2] is not into lewd stuff. It's so boring. I wish to see [wife_name2] covered in sperm, just like in the movies."
                                    man_name "I once came on [wife_name] belly. She called me a pervert and didn't speak to me for a week!"
                                    the_person.char "Well, this is your chance to try something new, guys! Just like the movies."
                                    "She looks into [man_name2]'s eyes while jerking him with both hands."
                                    man_name2 "I'm cumming [the_person.name]!"
                                    "She leans closer so that [man_name2] tip is just in front of her eyes."
                                    the_person.char "Do it, [man_name]! Cover me! Imagine it is your wife, if you like."
                                    $ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name2 "Oh, yes! Get it, you bitch! Get that jizz all over your slutty face, [wife_name2]!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    man_name "Shit, that's hot! I'm cumming too!"
                                    $ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "Second load is so huge that it spills from [the_person.possessive_title]'s face onto her breasts."
                                    the_person.char "Two out, one to go!"
                                    $ the_person.cum_on_stomach()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "Seeing [the_person.possessive_title] covered in cum is enough of a show and you too start to ejaculate. You finish on [the_person.possessive_title]'s tits and there's so much jizz it starts falling onto her belly."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person.char "Now go to your room, [the_person.mc_title]. Me and the boys need to take a bath."
                                    $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                    "You see them walking away to the bathroom followed by some white drops dripping towards the floor."
                                    "Both men have their hands on [the_person.possessive_title]'s ass, but she does not object. As they close the door, you see that [the_person.title] caresses their balls while their dicks show signs of returning to life."
                                    if submissive  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Oh, you are naughty guys! Want some more? Well, why not? As long as you promise to cum on me."
                                        man_name "On your face, [wife_name]! Looking good bitch!"
                                        man_name2 "And this is for you, [wife_name2]! Aren't you a slut?"
                                        "It seems the guys liked role-playing with [the_person.possessive_title] as their sperm dump."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and bed squeaks from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person.char "I want to taste your hot cum. I don't think your wife lets you do this!"
                                    man_name2 "No, [wife_name2] never allows anything other than missionary with a condom, she is so prude and boring at times."
                                    man_name "I asked [wife_name] once for a BJ. She tried but it was awful and she called it disgusting..."
                                    the_person.char "Well, this is your chance to try something new, guys!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name2]'s eyes while sucking him off. Her hands are working on two other dicks in meantime."
                                    man_name2 "I'm gonna cum, [the_person.name]!"
                                    "She keeps on going at steady pace."
                                    the_person.char "Mmmmmm... Mmmm.. Uh."
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name2] shrugs and starts filling her mouth with his load."
                                    man_name2 "Oh, yes! Get it, [wife_name2]!"
                                    "[man_name2] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                                    the_person.char "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name2 "It really turned me on! I feel I can do another round shortly."
                                    the_person.char "We will discuss it later, [man_name2]! Now let's finish with [man_name]. I want to drink his stuff too."
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "With that she takes his cock with her hot lips."
                                    man_name2 "Never thought you were such a cumdump, [the_person.name]!"
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] speeds up mouth around [man_name]'s dick and in few seconds he cums inside. She retreats back and gulps."
                                    the_person.char "Here we go. Double sweet load. Now for [the_person.mc_title]."
                                    man_name "Well, her mouth is really something."
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] take you dick in her mouth and in a short time you also explode inside."
                                    "She moves back and gulps."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person.char "Now go to your room, [the_person.mc_title]. Me and guys need to take a bath."
                                    if submissive  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person.char "Want more of my mouth? Well, okay if you let me drink your cum!"
                                        man_name2 "Open up your mouth, slut!  You gonna be feed with some hot stuff!"
                                        "It seems that men are planning to cum in [the_person.possessive_title]'s mouth all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and gulping sounds from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    "[the_person.possessive_title] takes [man_name2]'s cock out of her mouth and starts jerking him off, while you and [man_name] are helping yourselves."
                                    man_name2 "Ow, fuck! That feels great!"
                                    "As he starts to cum, [the_person.possessive_title] closes the tip with her hand so he finishes in it."
                                    man_name "Now help me too!"
                                    "[man_name2] places his instrument into [the_person.possessive_title]'s hand and she starts moving it. In few moments he cums in her hand."
                                    the_person.char "OK, now for you. [the_person.mc_title]."
                                    "You also explode into her hand."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person.char "Didn't that event went great?"
                                    the_person.char "Now go to bath, guys. I will join you shortly."
                                    if submissive  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        man_name2 "How about another blowjob, [the_person.name]?"
                                        man_name "I would not mind as well."
                                        "It seems that men are planning to have some more fun with [the_person.possessive_title]..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            else:
                                $ the_person.happiness -= 5
                                $ the_person.draw_person(position = "blowjob", emotion = "angry")
                                the_person.char "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get beck to your room now!"
                                "You go back to your bedroom accompanied by bed sqeaking from [the_person.possessive_title]'s room as she keeps sucking both [man_name]'s and [man_name2]'s dicks."
                        else:
                            man_name2 "Oh, [the_person.name], your toungue is driving me crazy! I think I will come soon!"
                            $ finish = get_random_from_list(finishes)
                            if finish == "facial":
                                the_person.char "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                man_name2 "No, [wife_name2] is not into lewd stuff. It's so boring. I wish to see [wife_name2] in sperm, just like in those movies."
                                man_name "I once came on [wife_name] belly. She called me a prevert and didn't spoke to me for a week!"
                                the_person.char "Well, thats your chance to try something new, guys! Just like the movies."
                                "She looks into [man_name2]'s eyes while jerking him with both hands."
                                man_name2 "I'm cumming [the_person.name]!"
                                "She leans closer so that [man_name2] tip is just in front of her eyes."
                                the_person.char "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                $ the_person.cum_on_face()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                man_name2 "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name2]!"
                                "[man_name] clearly liked the idea of doing it with his wife."
                                man_name "Shit, that's hot! I'm cumming too!"
                                $ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "Second load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                the_person.char "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                man_name "It really turns me on! I feel I can do another round shortly."
                                the_person.char "We will discuss it later, guys. First - a shower. I need to wash off it before it dries."
                                $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                "You see them walking away to bathroom. Some white drops fall on the floor."
                                "Both men have their hands on [the_person.possessive_title]'s ass, but she does not object. As they close the door, you see that [the_person.title] caresses their balls while dicks show signs of returning to life."
                                if submissive  or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by talk from [the_person.possessive_title]'s room."
                                    the_person.char "Oh, you are naughty gyus! Want some more? Well, why not? As long as you promise to cum on me."
                                    man_name "On your face, [wife_name]! Looking good bitch!"
                                    man_name2 "And this is for you, [wife_name2]! Aren't you a slut?"
                                    "It seems the guys liked role-playing with [the_person.possessive_title] as their sperm dump."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans and bed sqeaks from [the_person.possessive_title]'s room."
                            elif finish == "drink":
                                the_person.char "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                man_name2 "No, [wife_name2] hates oral sex. It is so frustrating."
                                man_name "I once asked [wife_name] for a blowjob. She said if I ever ask this again she will file a divorce!"
                                the_person.char "Well, thats your chance to experience the feeling, guys!"
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "She looks into [man_name2]'s eyes while sucking him off."
                                man_name2 "I'm gonna cum, [the_person.name]!"
                                "She just keep on going at steady pace."
                                the_person.char "Mmmmmm... Mmmm.. Uh."
                                $ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[man_name2] shrugs and starts filling her mouth with his load."
                                man_name "Oh, yes! Get it, [wife_name2]!"
                                "[man_name2] clearly liked the idea of doing it with his wife."
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                the_person.char "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                man_name "It really turned me on! I feel I can do another round shortly."
                                the_person.char "We will discuss it later, [man_name2]. First - I need to taste [man_name]."
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "She puts another dick int oher mouth and sucks it off."
                                man_name "This is so great. I can't hold much longer!"
                                $ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[man_name] comes into [the_person.possessive_title]'s mouth and pulls his cock away. You see her mouth is full of cum. Then she gulpes it and stands up."
                                $ the_person.draw_person(position = "walking_away")
                                "You see them walking away to bathroom."
                                "[man_name]'s hand is on [the_person.possessive_title]'s ass, and [man_name2] caresses her between the legs, but she does not object. As they enter bathroom, men's dicks show signs of returning to life."
                                if submissive or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person.char "Want more of my mouth? Well, okay if you let me drink your cum!"
                                    man_name2 "Open up your mouth, slut!  You gonna be feed with some hot stuff!"
                                    "It seems that men are planning to cum in [the_person.possessive_title]'s mouth all the night..."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "usual":
                                "[the_person.possessive_title] takes [man_name2]'s cock out of her mouth and starts jerking him off, while [man_name] is caressing her boobs."
                                man_name2 "Ow, fuck! That feels great!"
                                "As he starts to cum, [the_person.possessive_title] closes the tip with her hand so he finishes in it."
                                man_name "Now help me too!"
                                "[man_name2] places his instrument into [the_person.possessive_title]'s hand and she starts moving it. In few moments he cums in her hand."
                                "[the_person.possessive_title] stands up from the bed and smiles."
                                the_person.char "Didn't that event went great?"
                                the_person.char "Now go to bath, guys. I will join you shortly."
                                if submissive  or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    man_name2 "How about another blowjob, [the_person.name]?"
                                    man_name "I would not mind as well."
                                    "It seems that men are planning to have some more fun with [the_person.possessive_title]..."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            "Get back to bed.":
                "You decide that it is wrong to interfere into [the_person.possessive_title]'s private life so you go back to your room to sleep."
    hide screen person_info_ui
    $ the_person.sluttiness += 5
    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.
    $ change_scene_display(mc.location)
    $ renpy.scene("Active")
    return
