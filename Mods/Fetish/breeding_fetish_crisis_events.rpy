init 2 python:
    def get_breeding_fetish_list():
        return [x for x in known_people_in_the_game() if x.has_breeding_fetish()]

    def get_highly_fertile_breeder():
        return get_random_from_list([x for x in known_people_in_the_game() if x.has_role(breeding_fetish_role) and x.is_highly_fertile()])

    def get_pregnant_breeder():
        return get_random_from_list([x for x in known_people_in_the_game() if x.has_role(breeding_fetish_role) and x.knows_pregnant()])

    def get_family_breeder():
        return get_random_from_list(x for x in known_people_in_the_game() if x.has_breeding_fetish() and x.is_family())

    def breeding_fetish_high_fertility_crisis_requirement():
        if mc_at_home() and time_of_day==4:
            if get_highly_fertile_breeder():
                return True
        return False

    def breeding_fetish_happy_breeder_crisis_requirement():
        if mc_at_home() and time_of_day == 4:
            if get_pregnant_breeder():
                return True
        return False

    def breeding_fetish_family_sleep_crisis_requirement():
        return False #Disable for now
        if mc_at_home() and time_of_day == 4:
            if get_family_breeder():
                return True
        return False

    breeding_fetish_high_fertility_crisis = ActionMod("Breeding fetish desperation", breeding_fetish_high_fertility_crisis_requirement, "breeding_fetish_high_fertility_crisis_label",
        menu_tooltip = "You are visited by a highly fertile breeder.", category = "Fetish", is_crisis = True, crisis_weight = 5)
    breeding_fetish_happy_breeder_crisis = ActionMod("Breeding fetish desperation", breeding_fetish_high_fertility_crisis_requirement, "breeding_fetish_high_fertility_crisis_label",
        menu_tooltip = "You are visited by a highly fertile breeder.", category = "Fetish", is_crisis = True, crisis_weight = 5)
    breeding_fetish_family_sleep_crisis = ActionMod("Familial nighttime breeding", breeding_fetish_family_sleep_crisis_requirement, "breeding_fetish_family_sleep_crisis_label",
        menu_tooltip = "You are visited at night by a thirsty family member.", category = "Fetish", is_crisis = True, crisis_weight = 5)

label breeding_fetish_high_fertility_crisis_label():
    $ the_person = get_highly_fertile_breeder()
    if the_person == None:
        return
    if the_person.energy < 80:
        $ the_person.energy = 80
    if mc.energy < 80:
        $ mc.energy = 80
    if the_person == mom or the_person == lily:
        "You hear a knock on your door."
        mc.name "Its open!"
        $ the_person.draw_person()
        "Its [the_person.possessive_title!l]. She steps into your room, closes your door, and locks it..."
        mc.name "Something you need tonight [the_person.title]?"
        the_person "Yeah... something like that!"
    else:
        "You get a text on your phone. It's from [the_person.possessive_title!l]."
        $ mc.start_text_convo(the_person)
        the_person "Hey. I need your help with something. I'm on my way over."
        "Hmm, she's inviting herself over? You text her back."
        mc.name "Ok, text me when you get here."
        "A few minutes later, she texts you again."
        the_person "I'm here! Let me in!"
        $ mc.end_text_convo()
        "You go out to your front door and open it."
        $ the_person.draw_person()
        the_person "Hey! Let's go to your room."
        mc.name "Okay... this is a little weird..."
        the_person "I'll explain when we get there..."
        "You quickly lead her back to your room. When you walk in, she closes the bedroom door and locks it."
    the_person "I've been following my cycles on this app... Today it gave me a notification that I am highly fertile!"
    "She comes closer, wrapping her arms around you."
    the_person "You need to cum inside me tonight... I'm not taking no for an answer!"
    if the_person.is_dominant():
        "She pushes you back onto your bed. She seems pretty intent on taking what she wants from you."
        "You watch as she starts to strip down."
        $ the_person.strip_outfit()
        $ the_person.change_arousal(10)
        "She runs a hand down her belly, to her mound and across her slit. You can see moisture already starting to collect there."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.possessive_title] reaches down and pulls your pants off and then climbs up on top of you, your cock at her entrance."
        the_person "Oh god... this is it. I can feel it! Tonight's the night you finally knock me up..."
        "She holds your cock with one hand and slowly starts to sink down onto you. She gasps when your dick parts her labia."
        the_person "Yes! Oh [the_person.mc_title]..."
        "She descends slowly, but finally bottoms out with a sigh. She takes a moment to adjust to your girth before she starts to rock her hips some."
        the_person "Oh god... here we go!"
        call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _highly_fertile_breeding_901
        if the_person.has_creampie_cum():
            the_person "Its inside me! It worked! Don't ask me how I know... I can just feel it!"
            "She rubs her belly and sighs."
            $ become_pregnant(the_person, mc_father = True) #Guaranteed to knock her up
            $ the_person.event_triggers_dict["LastBreedingFetish"] = day
        else:
            "Too tired to continue, [the_person.possessive_title!l] pulls off you a little frustrated."
            the_person "I can't believe it... just... lets make sure we try again soon okay?"

    else:
        mc.name "One knocked up cum slut, coming right up!"
        "You reach down and start to pull her bottoms off."
        $ the_person.strip_outfit(exclude_upper = True)
        "When you finish, you pick her up and throw her down on your bed."
        $ the_person.draw_person(position = "missionary")
        "You pull out your cock and slowly crawl up her body. Soon your cock is at her entrance. You whisper in her ear."
        mc.name "Are you ready for this? Once I knock you up, there's no going back..."
        "She moans and bucks her hips. She wraps her legs around you and pulls you down inside of her forcefully."
        mc.name "Mmm, fuck I guess so!"
        "You start to piston your hips, savoring the highly fertile, bare pussy that is wrapped around you."
        the_person "Give it to me [the_person.mc_title]! Give me a fucking I'll never forget and pour your seed deep!"
        call fuck_person(the_person, start_position = breeding_missionary , private = True, skip_intro = True, position_locked = True) from _highly_fertile_breeding_night_02
        if the_person.has_creampie_cum():
            the_person "Its inside me! I'm pregnant! Don't ask me how I know... I can just feel it!"
            "She rubs her belly and sighs."
            $ become_pregnant(the_person, mc_father = True) #Guaranteed to knock her up
            $ the_person.event_triggers_dict["LastBreedingFetish"] = day
        else:
            "Too tired to continue, [the_person.possessive_title!l] looks up at you little frustrated."
            the_person "I can't believe it... just... lets make sure we try again soon okay?"
        "Finished for now, [the_person.title] excuses herself."
    the_person "I'd better get going..."
    if the_person.has_creampie_cum():
        the_person "It'll be a few days before a test shows a definite positive... but I'm almost positive we just made a baby!"
    else:
        the_person "I'm still going to be fertile for a few days... please try again? Okay? I don't want to wait anymore, I want your baby inside me..."
    $ the_person.review_outfit()
    $ the_person.draw_person(position = "walking_away")


    return

label breeding_fetish_happy_breeder_crisis_label():
    $ the_person = get_pregnant_breeder()
    $ the_person.event_triggers_dict["LastBreedingFetish"] = day
    $ builder = WardrobeBuilder(the_person)
    if the_person == None:
        return
    if the_person.energy < 80:
        $ the_person.energy = 80
    if mc.energy < 80:
        $ mc.energy = 80
    if the_person == mom or the_person == lily:
        "You hear a knock on your door."
        "You stand up and open your door. It's [the_person.title], dressed very nicely..."

        $ the_person.apply_outfit(builder.personalize_outfit(special_fetish_outfit))
        $ the_person.draw_person()
        "Its [the_person.possessive_title!l]. She steps into your room, closes your door, and locks it..."
        mc.name "Something you need tonight [the_person.title]?"
        the_person "Yeah... something like that!"
    else:
        "*Ding Dong*"
        "You're roused from your bed by a ring on your doorbell."
        # make sure we are at the hall
        $ mc.change_location(hall)
        $ mc.location.show_background()
        "You head to your front door and see [the_person.possessive_title!l] standing there... outside... in a very provocative outfit."
        $ the_person.apply_outfit(builder.personalize_outfit(special_fetish_outfit))
        $ the_person.draw_person()
        ###Draw the girl###
        "You quickly open the door and invite her inside."
        "To avoid any situations with [mom.possessive_title] or [lily.possessive_title], you quickly invite her to your room."
        $ mc.change_location(bedroom)
        $ mc.location.show_background()
        "You walk in your room, close the door and lock it."

    $ the_person.draw_person(position="kissing")
    "[the_person.possessive_title] quickly turns and embraces you."
    the_person "Oh, [the_person.mc_title], I'm sorry to just come over without asking like this but, I was at trying to sleep."
    the_person "I kept thinking about the baby growing inside of me and I started getting all worked up..."
    "She stumbles over her words for a second."
    the_person "Oh geeze... I just couldn't stop thinking about how good it feels when you fuck me!"
    "You are hardly surprised. [the_person.possessive_title]'s breeding fetish makes her a cum starved slut..."
    the_person "I just couldn't help it... will you please let me stay here tonight?"
    "[the_person.possessive_title] looks at you with hopeful eyes."
    menu:
        "Accept":  #This begins the sex scene
            "[the_person.possessive_title] walks over to the windows and looks out of it. You see her hips move side to side for a second and the peaks back at you."
            $ the_person.draw_person(position = "back_peek")
            the_person "It so pretty out tonight... Why don't you come over here?"
            "You walk over and stand behind [the_person.possessive_title!l] as she looks by the window."
            ###Sex Scene, standing variant at window###
            "You put your hands on her hips. She sticks her ass out slightly as you line yourself and then gently push your cock inside her."
            call fuck_person(the_person, start_position = SB_facing_wall, start_object = make_window(), skip_intro = True) from _call_fuck_person_preg_breeder_nightscene_01
            "[the_person.possessive_title] walks over to your bed and lays down on her back and takes off any remaining clothing."
            $ the_person.strip_outfit(exclude_feet = False, position = "missionary")
            $ the_person.draw_person(position = "missionary")

            "You join her on the bed. She raises her arm and you lay your head down on her breast."
            "You both catch your breath and just enjoy the warmth of each other's bodies."
            "After a few minutes of cuddling, you reach your hand up and begin to fondle her other breast."
            if the_person.is_lactating():
                "When you squeeze her nipple, some of her milk begins to come out."
                the_person "Oh god, my nipples are so sensitive now that my milk is coming in..."
                the_person "Do you... do you want to taste it?"
                "You turn your head and begin to lick and suck her nipple. With a few aggressive sucking motions, her milk begins to flow."
                if the_person.lactation_sources > 3: #Lots of milk
                    "After a few moments, her milk really begins to flow. There is now a thin but steady stream of the creamy fluid flowing into your mouth."
                    the_person "Ah! Oh baby that's it! aahhhhh..."
                    $ the_person.change_arousal(30)
                    "Her cream is sweet and plentiful. You suckle her for a long while before the flow starts to slow down."
                    the_person "ohhh, [the_person.mc_title] that felt so good. Can you, you know, do the other one too?"
                    mc.name "Mmm, certainly."
                    "You switch sides and begin to suckle again. Almost immediately her milk flows forcefully"
                    the_person "Ahh! Oh my god..."
                    $ the_person.change_arousal(30)
                    "Her cream just keeps flowing. It's a delicious treat that restores some of your energy."
                    $ mc.change_energy(50)
                    $ the_person.change_energy(50)
                else:
                    "Her milk comes out in small amounts as you suckle, her breathing catches with each pull."
                    the_person "Ahhhh... oh [the_person.mc_title] that feels so good..."
                    $ the_person.change_arousal(30)
                    "You manage to squeeze a bit of her cream out. It's a delicious treat that restores some of your energy."
                    $ mc.change_energy(40)
                    $ the_person.change_energy(40)
            else:
                "[the_person.possessive_title] moans and runs her hands through your hair."
                "You turn your head and begin to lick and suck her nipple."
                $ the_person.change_arousal(20)
                the_person "That feels so good [the_person.mc_title]... I can't wait until my milk starts to come in."
                $ mc.change_energy(30)
                $ the_person.change_energy(30)
                "Soon you are getting hard again. It's time for round two."
            "You roll over on top of [the_person.possessive_title!l]. She wraps her arms around you as you slowly sink your cock into her moist cunt."
            ###Sex scene, missionary###
            call fuck_person(the_person, start_position = breeding_missionary, start_object = make_bed(), skip_intro = True) from _call_fuck_person_preg_breeder_nightscene_02

            the_person "Oh god [the_person.mc_title], tonight has been incredible... excuse me for a second."
            $ the_person.draw_person(position = "walking_away")
            ###The girl walking away draw
            "[the_person.possessive_title] excuses herself to your restroom. After a few minutes she comes back. She sits down on the side of the bed."
            $ the_person.draw_person(position = "sitting")
            ###The girl sitting###
            the_person "Why don't... why don't you come sit on the side of the bed? I know you're tired but... I could really go for one more round..."
            "You sit up and move to the side of the bed."
            "[the_person.possessive_title] smiles and gets down on her knees below you."
            ###Draw the girl on knees###
            $ the_person.draw_person(position = "blowjob")
            the_person "I'm sorry [the_person.mc_title]... I just can't help it. It feels so good inside of me..."
            "[the_person.possessive_title] reaches down and starts to stroke your mostly soft cock."
            "Her hands feel good but you can tell its going to take a little more to get you aroused again, after cumming twice already."
            ###IF girl has big tits, ask for a tit fuck
            if the_person.has_large_tits():
                mc.name "Why don't you put it between your tits for a while?"
                "[the_person.possessive_title] smiles up at you."
                the_person "Anything for you, [the_person.mc_title]."
                "[the_person.possessive_title] looks up at you while she scoots closer to you, until her body is up against yours. She uses her hand to point your cock straight up while she moves it in position between her amazingly soft tits."
                "Once in position, she uses her hands to push her tits together, squashing your prick in her heavenly soft tit-flesh."
                "[the_person.possessive_title] starts to move up and down. Now and then when her tits are at the base of your dick she licks the sensitive tip."
                "The view of [the_person.possessive_title!l] on her knees before you, happy with you between her tits is extremely arousing. It isn't long until you are fully erect."

            else:
                mc.name "Why don't you put it in your mouth for a while?"
                "[the_person.possessive_title] smiles up at you."
                the_person "Anything for you, [the_person.mc_title]."
                "[the_person.possessive_title] looks up at you while she scoots closer to you, then lowers her head down and begins to lick and up down your groin."
                "She moves her head to the tip and slowly moves her head up and down your shaft a few times. She pulls off for a second then looks up at you."
                the_person "Mmm, I can taste the remnants of earlier... I can't wait to feel you inside me again..."
                "[the_person.possessive_title] resumes blowing you with vigor."
                "The view of [the_person.possessive_title!l] on her knees before you, happy with your cock in her mouth is extremely arousing. It isn't long until you are fully erect."

            mc.name "Okay [the_person.title], I'm ready. Now bend over and get ready for another round."
            "[the_person.possessive_title] obediently does as you ask and bends over your bed as you stand up and get behind her."
            $ the_person.draw_person(position = "standing_doggy")
            the_person "Come and get it, [the_person.mc_title]... its yours for the taking!"
            "You line yourself up with her soaking wet slit and push yourself in."
            ###Sex Doggy Style###
            call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_floor(), skip_intro = True) from _call_fuck_person_SBV13

            "Exhausted from your night with [the_person.possessive_title!l], you get back up into your bed. [the_person.possessive_title] joins you and you quickly fall asleep, cuddling together."
            "That night, you have many pleasant dreams involving [the_person.possessive_title!l] and sex in all kinds of crazy positions."
        "Refuse":       # allow for player to decide if he wants to induce fetish
            mc.name "I'm sorry [the_person.title], I really need to get some sleep."
            $ the_person.change_obedience(-10)
            $ the_person.change_happiness(-10)
            the_person "Oh! I'm sorry... Maybe tomorrow then?"
            "[the_person.possessive_title] quickly sulks off."
            return # EXIT
        "Too Tired" if mc.energy < 30:
            "[the_person.possessive_title] is surprised by your answer."
            $ the_person.change_obedience(-5)
            $ the_person.change_happiness(-5)
            the_person "Oh! I'm sorry... I didn't think about that. Maybe tomorrow then?"
            "[the_person.possessive_title] quickly sulks off."
            return  # EXIT

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_breeder_02
    call breeder_cowgirl_wakeup_label(the_person) from _breeder_overnight_cowgirl_wakeup__01
    return "Advance Time"

label breeding_fetish_family_sleep_crisis_label():
    $ the_person = get_family_breeder()
    if the_person = None:
        return
    $ builder = WardrobeBuilder(the_person)
    if the_person == lily:

        $ mc.change_location(bedroom)
        $ mc.location.show_background()

        "Before going to bed, you hear a knock on your door. You hear [the_person.possessive_title!l] from the other side of the door."
        the_person "Hey [the_person.mc_title], you still up? I was just wondering if I could come in for a bit?"
        "You invite her in. You immediately start to get aroused when you see what she is wearing."
        $ the_person.apply_outfit(builder.personalize_outfit(special_fetish_blue_outfit))
        $ the_person.draw_person()
        the_person "So... I was wondering... is it okay if I sleep in here with you again tonight?"
        menu:
            "Not tonight":
                mc.name "Sorry [the_person.title]... I had a long day and I'm pretty wore out... maybe tomorrow?"
                "She is clearly disappointed."
                the_person "Whatever [the_person.mc_title]... see you in the morning I guess?"
                "You head for bed, looking forward to a restful night's sleep."
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(-5)
                return
            "Strip first":
                $ the_person.event_triggers_dict["LastVaginalFetish"] = day
                mc.name "That sounds good [the_person.title]... why don't you give me a show before we go to bed?"
                "[the_person.possessive_title] smiles at you."
                the_person "Aww, does my [the_person.mc_title] wanna see his [the_person.title] get naked for him? What a pervert!"
                "[the_person.possessive_title] winks at you before beginning her routine."
                call free_strip_scene(the_person) from _free_strip_scene_701
                mc.name "Damn [the_person.title], you are really getting good at that."
                "[the_person.possessive_title] bites her lip, glancing down at your bulge. Her cheeks are flushed and rosy."
                the_person "Hey... if you want to I could... you know... take care of that tent you are sporting there [the_person.mc_title]."
                the_person "I've come to really love the way it feels when you spurt inside of me..."
                "You stand up and embrace her, your dick straining against your clothes, eager to begin another incestuous tryst with [the_person.possessive_title!l]."


        "You kiss [the_person.possessive_title!l] along her neck and ear. She shivers at the sensation and then whispers in your ear."
        $ the_person.change_arousal(20)
        the_person "Throw me down on your bed, [the_person.mc_title]. I want to feel your weight on top of me while you fuck my brains out!"
        "You roughly pick up [the_person.possessive_title!l] and carry her over to the bed. You throw her down and quickly jump on top of her."
        "[the_person.possessive_title] spreads her legs wide, giving you easy access. She sighs as you sink your cock into her greedy cunt."
        call fuck_person(the_person, start_position = breeding_missionary, start_object = make_bed(), skip_intro = True) from _call_fuck_person_lily_breeding_overnight

        "After you finish your rutting, you and [the_person.possessive_title!l] get under the covers of your bed."
        "Spooning behind [the_person.possessive_title!l], you drift off to a wonderful night's sleep. Her body heat and the feeling of her naked skin against yours give you very pleasant dreams."

        call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_SBV070
        call SB_cowgirl_wakeup_label(the_person) from _SB_cowgirl_wakeup_label_SBV070
        return "Advance Time"


label breeder_cowgirl_wakeup_label(the_person):
    "All night long, you have sexy dreams centered around [the_person.possessive_title!l]."
    "She's on her knees, sucking you off expertly. Later, shes on her back while you pin her to the bed. Sometime later, shes on her hands and knees, taking your cock from behind like a pro."
    "When morning comes, you feel a stirring in your loins again as you start to slowly wake up. This time, however, there are some very pleasant sensations coming from your crotch."

    $ the_person.apply_outfit(special_fetish_nude_outfit)
    $ the_person.draw_person(position = "cowgirl")
    $ the_person.change_arousal(35)
    $ mc.arousal = 25

    "You slowly open your eyes and discover that [the_person.possessive_title!l] is on top of you, riding you in the cowgirl position."
    "You reach up and grab her amazing ass cheeks. [the_person.possessive_title] looks in your eyes when she feels your hands on her."
    the_person "Good morning [the_person.mc_title]... Sorry but when I woke up I noticed you were hard so... I figured you wouldn't mind if I hopped on for a bit..."
    "[the_person.possessive_title] moans during one slow stroke."
    "You decide to lay back and enjoy the ride"
    # call fuck_person(the_person, start_position = cowgirl, start_object = make_bed(), skip_intro = True, girl_in_charge = True) from _call_sex_description_SBV50
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, start_object = make_bed(), skip_intro = True) from _call_sex_description_breeder_wakeup__01
    mc.name "Oh god what a wakeup. I think I'm gonna go back to sleep for a bit. Thanks!"
    if the_person is mom:
        "[the_person.possessive_title] looks at you and smiles."
        the_person "Oh, anything for you honey. Well, I'd better go get ready for the day!"
    elif the_person is starbuck:
        "[the_person.possessive_title] giggles for a second then says goodbye."
        the_person "Yeah well, just don't tell my other customers about this, I can't make house calls for everyone!"
    else:
        "[the_person.title] looks at you and winks."
        the_person "Anytime [the_person.mc_title]! I'd better go get ready!"
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "stand3")
    "You fall back asleep. When you wake up, [the_person.possessive_title!l] has left."
    $ clear_scene()
    "Looks like you slept in!"
    return
