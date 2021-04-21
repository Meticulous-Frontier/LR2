# Kaya is a new unique character. Kaya starts out working at the coffee shop after Alexia gets hired.
# Kaya is working at the coffee shop to get through college. Her mother was previously supporting her, but has fallen ill and can't afford to anymore.
# Kaya is the daughter of Sakari, who will be introduced later in the story. MC meets Kaya at the coffee shop after she starts working there.
# As MC gets to know Kaya, he learns about her money problems. Working with HR director, MC can start an intern project for college students to work at the company on the weekend.
# Weekend staffing is limited and is limited to Research and production departments (no suppliers open to buy supplies or sell serums, for now no HR? Maybe add HR in the future?)
# Eventually, MC meets Sakari and discovers his father had an affair with her and Kaya is a half sister.
# Kaya and her mother have native american heritage
# Use mod code to have her deny lunch dates due to being at work, require different date time.


init 2 python:
    def kaya_mod_initialization():
        kaya_wardrobe = wardrobe_from_xml("ashley_Wardrobe")
        kaya_base_outfit = Outfit("kaya's base accessories")
        the_eye_shadow = heavy_eye_shadow.get_copy()
        the_eye_shadow.colour = [.26, .14, .21, 0.33]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [1.0, .21, .14, 0.33]
        the_bracelets = colourful_bracelets.get_copy()   #Change this
        the_bracelets.colour = [.71,.4,.85,1.0]
        kaya_base_outfit.add_accessory(the_eye_shadow)
        kaya_base_outfit.add_accessory(the_lipstick)
        kaya_base_outfit.add_accessory(the_bracelets)

        # init kaya role
        kaya_role = Role(role_name ="kaya", actions =[], hidden = True)

        #global kaya_role
        global kaya
        kaya = make_person(name = "Kaya", last_name ="Greene", age = 22, body_type = "thin_body", face_style = "Face_3",  tits="B", height = 0.92, hair_colour="black", hair_style = messy_hair, skin="tan" , \
            eyes = "brown", personality = kaya_personality, name_color = "#228b22", dial_color = "228b22" , starting_wardrobe = kaya_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 7, start_obedience = -18, start_happiness = 88, start_love = 0, \
            relationship = "Single", kids = 0, force_random = True, base_outfit = kaya_base_outfit,
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["taking control", 2, False], ["getting head", 2, False], ["drinking cum", -2, False], ["giving blowjobs", -2, False], ["public sex", 2, False]])

        kaya.generate_home()
        kaya.set_schedule(kaya.home, times = [0,1,2,3,4])
        #kaya.set_schedule(downtown_bar, times = [2,3])
        kaya.home.add_person(kaya)

        kaya.event_triggers_dict["intro_complete"] = False    # True after first talk

        # add appoint
        #office.add_action(HR_director_appointment_action)

        # kaya_intro = Action("kaya_intro",kaya_intro_requirement,"kaya_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        # mc.business.add_mandatory_crisis(kaya_intro) #Add the event here so that it pops when the requirements are met.

        # set relationships
        # town_relationships.update_relationship(kaya, stephanie, "Sister")
        # town_relationships.update_relationship(nora, kaya, "Friend")


        kaya.add_role(kaya_role)
        return


init -2 python:
    def kaya_setup_intro_event_requirement():
        if alexia.is_employee() and day > alexia.event_triggers_dict.get("employed_since", 9999) + 7:
            return True
        return False

    def kaya_intro_requirement(the_person):
        if the_person.location == the_person.downtown:
            return True
        return False

    def kaya_ask_out_requirement(the_person):
        if the_person.location == the_person.downtown and the_person.love > 20:
            #TODO False if we already have a date scheduled for tonight. Maybe make this only non date nights?
            return True
        return False

    def kaya_get_drinks_requirement():
        if time_of_day == 3:
            return True
        return False

    def kaya_add_HR_program_event_requirement():
        if mc.business.hr_director != None and renpy.random.randint(0,5) == 1:
            return True
        return False

    def kaya_HR_start_internship_program_requirement(the_person):
        if the_person.location == the_person.work:
            return True
        return False

    def kaya_meet_lily_at_uni_requirement(the_person):
        if the_person.location == university:
            return True
        return False

    def kaya_lily_study_night_intro_requirement():
        if day%7 == 6 and time_of_day == 4:
            return True
        return False

    def kaya_moving_in_with_mother_intro_requirement():
        if kaya.sluttiness > 40:
            return True
        return False

    def kaya_asks_for_help_moving_requirement(the_person):
        if day >= the_person.event_triggers_dict.get("move_help_day", 9999) and time_of_day != 4:
            return True
        return False

    def kaya_moving_day_requirement():
        if day % 7 == 6:
            return True
        return False

    def kaya_share_the_news_requirement():
        if day >= the_person.event_triggers_dict.get("move_help_day", 9999) and time_of_day == 3 and the_person.location == the_person.downtown:
            return True
        return False

    def kaya_jennifer_confrontation_requirement():
        if willing_to_threesome(kaya, mom):
            return True
        return False


label kaya_setup_intro_event_label():
    $ the_person = kaya
    $ kaya.set_schedule(downtown, times = [2,3])    #TODO make this the coffee shop
    $ kaya.set_schedule(university, days = [0, 1, 2, 3, 4], times = [1])
    $ kaya.add_unique_on_talk_event(kaya_intro)
    return

label kaya_intro_label(the_person):
    "You go to the coffeeshop one afternoon for a pick me up. There's a new girl working there you haven't seen before."
    "She's hot. You flirt with her."
    "Find out her name is Kaya, she's native, a student at the local university."
    "She's cute, you should keep an eye out for her."
    $ the_person.add_unique_on_talk_event(kaya_ask_out)
    return

label kaya_ask_out_label(): #Requires 20 love, substitute for first date.
    "You flirt more with Kaya. She flirst back."
    "We should hang out sometime. She agrees, but cautions work keeps her very busy."
    "Agree to meet her after she gets off work."
    $ mc.business.add_mandatory_crisis(kaya_get_drinks)
    return

label kaya_get_drinks_label():
    "You meet with Kaya after she gets off work. You take her to a local bar."
    "You grab a couple drinks. Chance to serum her."
    "You find out she likes to play pool. You play a round, barely winning."
    "Grab a couple more drinks."
    "Before the next round, Kaya talks about her mother being sick, can't pay for her medications, having to work coffeeshop job to help out."
    "MC gets the idea of the intern program as a way for the company to provide girls with scholarships and some spending money."
    "If shes slutty, she flashes you at a key moment as a distraction."
    "You lose the second round."
    "She's too tired to play another round but asks for a rain check. Asks if you will walk her home."
    "At her apartment door, start making out. When MC starts getting handsy, a door slamming down the hall interrupts."
    "She apologizes, she doesn't want to put out on the first date. Says goodnight to MC."
    "MC has unlocked grabbing drinks with Kaya. He can ask her to grab drinks when she is working at the coffee shop any evening."
    if mc.business.hr_director:
        $ mc.business.hr_director.add_unique_on_talk_event(kaya_HR_start_internship_program)
    return

label kaya_add_HR_program_event_label():
    $ the_person = mc.business.hr_director
    $ the_person.add_unique_on_talk_event(kaya_HR_start_internship_program)
    "Now that you have an HR director, you should talk to her about an internship program for girls like [kaya.title]."
    return

label kaya_HR_start_internship_program_label():
    "You track down your HR director. Have a meeting with her about an internship program."
    "Decide it should happen on the weekends, have it be a half day (slot 1 and 2), in research and production departments."
    "She says as a trial it should probably be kept small, maybe 4 girls max."
    $ kaya.add_unique_on_talk_event(kaya_meet_lily_at_uni)
    return

label kaya_meet_lily_at_uni_label():    #This label starts Kaya and Lily friendship storyline. Requires mid Kaya loev (>40?). REquires scholarship program.
    "You go the university to meet with them there with your offer to have a small internship and scholarship program."
    "If you have rediscovered Nora she is at the meeting, is impressed with your offers, says going forward she can recommend you interns."
    "After you finish, you happen to spot Kaya and say hello."
    "You talk to Kaya about the new internship program. She is impressed and immediately agrees. You assign her to research and development."
    "As you are talking to Kaya, Lily happens to talk by and sees you talking with her. When Lily walks up, Kaya starts to get territorial."
    "She starts to get jealous of you talking to another girl."
    "She's my sister, its not like that (even though it kind of is)."
    "Suddenly she is super friendly with Lily. Find out Lily is taking a class Kaya took last semester."
    "Lily asks if Kaya wants to come over to study some time. Kaya enthusiastically agrees, surprised to find out MC lives with sister and mom."
    "They are now friends."

    $ town_relationships.update_relationship(sister, kaya, "Friend")
    $ mc.business.add_mandatory_crisis(kaya_lily_study_night_intro)
    return

label kaya_lily_study_night_intro_label():
    "Kaya is over studying with Lily. You are in your room and you hear them laughing down the hall. You go to say hello."
    "Kaya and Lily are talking about stuff in her room, you overhear before you knock on the door."
    "You knock, say hello. Kaya says they have become good friends. They've been studying for a while and are just getting ready to take a break."
    "You offer to open a bottle of wine for everyone. Sounds good."
    "You go to the kitchen. Open a bottle of wine. You pour two glasses, one for each girl. Chance to serum them."
    "If you serum Lily's, mom suddenly appears and take the glass of wine and starts to drink it, getting Lily's serum. Doesn't realize you have company."
    "Lily and Kaya appear. Mom is startled."
    "Mom asks about Kaya... says she looks familiar... what's your last name?"
    "Suddenly frowns, turns her back and ignores the rest of the conversation."
    "You pour another glass for Lily. No serum for her. Girls chat for a minute then go back to Lily's room."
    "Mom turns to you, she seems slightly shaken up. She asks you not to get involved with Kaya, but won't explain why."
    "You go to bed confused."
    "From now on, Lily and Kaya study together every sunday night."
    return

label kaya_moving_in_with_mother_intro_label(): #This label is called if you ask her to get drinks with you after a few different points in the story. Req 40+ sluttiness
    "You ask Kaya if she wants to go out for drinks tonight. She says no."
    "Her mother's health has been failing, she needs to go take care of her."
    "Implies her mother is likely to die in the near future."
    "Temporarily suspend Kaya's regular events with Lily."
    $ mc.business.add_mandatory_crisis(kaya_asks_for_help_moving)
    $ kaya.event_triggers_dict["move_help_day"] = day + 7
    return

label kaya_asks_for_help_moving_label():    #Timed event after the drink refusal. Something like a week later? Maybe less?
    "When you enter the coffee shop, Kaya spots you and initiates talking. Wants to know if you can do her a favor."
    "Says her mother has been going downhill really fast. Asks if you would be willing to help her move in with her mother this weekend."
    "You agree. She is sad. You try to cheer her up."
    "She says things are really rough right now but she really appreciates you, looks forward to seeing you."
    "Asks you to come over when she gets off work, doesn't want to be alone."
    "You go back to her place."
    "You hook up"
    "Kaya gives MC the option to cover up or not. In her culture, they don't believe in birth control, but won't stop you from wrapping it up if you choose to."
    "If MC chooses raw, Kaya gets knocked up. Also checks pregnancy preferences."
    "You go home"
    $ mc.business.add_mandatory_crisis(kaya_moving_day)
    return

label kaya_moving_day_label():  #Today we meet Sakari, Kaya's mom, and learn Kaya is a half sister.
    "You meet at Kaya's and help her pack up. Takes a while. Optional lets fuck one last time at my place scene. Kaya also gets pregnant if able."
    "Help her move to her mother's."
    "Meet Sakari. She reacts to you oddly. You help her move."
    "While helping her move, you notice a picture. Its your dad with Sakari?"
    "This is suspicious. Later you have the chance to be alone with Sakari and ask her about it."
    "Find out Sakari was your dad's mistress. Kaya is your half sister."
    "IF you fucked her earlier, imagine your cum is still inside your half sister."
    "Sakari asks if you are his son. You admit you are."
    "Sakari admits there was some drama. Never intended to drive a wedge between your parents, but that you should probably leave Kaya alone."
    "Before you can answer, Kaya interrupts the conversation. Doesn't know what was being said."
    "You finish helping Kaya move. Leave the place stunned."
    $ mc.business.add_mandatory_crisis(kaya_share_the_news)
    $ kaya.event_triggers_dict["share_news_day"] = day + 7
    return

label kaya_share_the_news_label():  # Timed event after helping her move.
    "Kaya texts you. Wants to know if you can meet up after she gets off work. IF she's pregnant, she has crazy news for you."
    "You agree to meet up."
    "You meet with her. She invites you into the coffee shop while she closes down, says she's the only one around."
    "When she finishes, you sit with her at a table."
    if kaya.is_pregnant():
        "If she's pregnant, she excitedly tells MC that. Wants to know how MC feels about it."
        "MC tells her how he discovered she is actually his half sister. She is conflicted."
        "In her culture, small tribes sometimes required family members to marry. It's discouraged, but not unheard of."
        "Says she still wants to be with MC and wants to keep the baby. Says she will keep the secret that you are related."
        "Give MC choice. He can agree with her to keep it, or ask her to get rid of it."
        "If MC asks her to get rid of the baby, she is hurt. Asks MC to leave and then leaves the game along with her mother."
    else:
        "MC breaks the news to her that he discovered they are half siblings. She is conflicted."
        "In her culture, small tribes sometimes required family members to marry. It's discouraged, but not unheard of."
        "Says she still wants to be with MC. She offers to keep their relation a secret."
        "Give MC a choice. He can agree or decline. If he declines, Kaya leaves the game."
    "All story after this assume MC sticks with Kaya."
    "If MC sticks with Kaya, she asks if she can be MC's girlfriend, if she isn't already. Agrees to keep your relation secret."
    return

    #TODO find some way to drop a hint here that the best way to continue the storyline is to invite Kaya over for a sleepover date.

label kaya_jennifer_confrontation_label():  #Requires sexual actions taken with Jennifer
    "Make a date with Kaya. Plan it for MC's place."
    "Sneak toward's MC's room, but Jennifer notices."
    "She confronts MC and Kaya. Accuses Kaya of trying to steal her son from her."
    "MC steps in, stops things from getting crazy. Kaya is family, should treat her as such."
    "Ends with reconciliation. Threesome with Kaya and Jennifer."
    return
