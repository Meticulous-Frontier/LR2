# Kaya is a new unique character. Kaya starts out working at the coffee shop after Alexia gets hired.
# Kaya is working at the coffee shop to get through college. Her mother was previously supporting her, but has fallen ill and can't afford to anymore.
# Kaya is the daughter of Sakari, who will be introduced later in the story. MC meets Kaya at the coffee shop after she starts working there.
# As MC gets to know Kaya, he learns about her money problems. Working with HR director, MC can start an intern project for college students to work at the company on the weekend.
# Weekend staffing is limited and is limited to Research and production departments (no suppliers open to buy supplies or sell serums, for now no HR? Maybe add HR in the future?)
# Eventually, MC meets Sakari and discovers his father had an affair with her and Kaya is a half sister.
# Kaya and her mother have native american heritage
# Use mod code to have her deny lunch dates due to being at work, require different date time.

style kaya_lang:
    outlines [ (absolute(4), "#080", absolute(0), absolute(0)) ]

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
            forced_opinions = [["billiards", 2, False], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["taking control", 2, False], ["getting head", 2, False], ["drinking cum", -2, False], ["giving blowjobs", -2, False], ["public sex", 2, False]])

        kaya.generate_home()
        kaya.set_schedule(kaya.home, times = [0,1,2,3,4])
        kaya.home.add_person(kaya)

        kaya.event_triggers_dict["intro_complete"] = False    # True after first talk
        kaya.event_triggers_dict["can_get_drinks"] = False
        kaya.event_triggers_dict["can_get_barista_quickie"] = False
        kaya.event_triggers_dict["has_moved"] = False
        kaya.event_triggers_dict["has_started_internship"] = False

        # add appoint
        #office.add_action(HR_director_appointment_action)

        # kaya_intro = Action("kaya_intro",kaya_intro_requirement,"kaya_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        mc.business.add_mandatory_crisis(kaya_setup_intro_event) #Add the event here so that it pops when the requirements are met.

        # set relationships
        # town_relationships.update_relationship(kaya, stephanie, "Sister")
        # town_relationships.update_relationship(nora, kaya, "Friend")


        kaya.add_role(kaya_role)
        return


init -2 python:
    def kaya_setup_intro_event_requirement():
        return False    #Disabled for now #test
        if alexia.is_employee() and day > alexia.event_triggers_dict.get("employed_since", 9999) + 7:
            return True
        return False

    def kaya_intro_requirement(the_person):
        if the_person.location == coffee_shop:
            return True
        return False

    def kaya_ask_out_requirement(the_person):
        if the_person.location == coffee_shop and the_person.love > 20 and time_of_day == 3:
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

init 3 python:
    kaya_setup_intro_event = Action("Kaya Setup", kaya_setup_intro_event_requirement, "kaya_setup_intro_event_label")
    kaya_intro = Action("Meet Kaya",kaya_intro_requirement,"kaya_intro_label")
    kaya_ask_out = Action("Ask to get drinks",kaya_ask_out_requirement,"kaya_ask_out_label")

label kaya_setup_intro_event_label():
    $ the_person = kaya
    $ kaya.set_schedule(coffee_shop, days = [0, 1, 2, 3, 4], times = [2,3])    #TODO make this the coffee shop
    $ kaya.set_schedule(university, days = [0, 1, 2, 3, 4], times = [1])
    $ kaya.add_unique_on_talk_event(kaya_intro)
    return

label kaya_intro_label(the_person):
    "Even though it is later in the day, you decide to swing by the coffee-shop for a pick me up."
    $ renpy.show("restaurant", what = restaraunt_background)
    $ the_person.draw_person()
    "When you step inside, there's a new girl working there you haven't seen before."
    "You listen as the person ahead of you orders."
    "?????" "Yes I'd like a tall macchiato with whipped cream."
    the_person "Is that all?"
    "When she talks, there is a slight accent. It's small, and you have trouble placing it."
    "You quickly check behind you. No one in line behind you yet... maybe you can chat with her for a bit?"
    "The person in front of you moves to wait for their drink."
    the_person "Hi, what can I get you?"
    "That accent... where is it from? It's starting to other you..."
    the_person "{=kaya_lang}Kia ora? {/=kaya_lang}(?????)... Do you want to order?"
    "Ah! You zoned out for a second. What was that word?"
    mc.name "Yes, sorry. I was trying to place your accent, but I can't. I'll just take a large coffee, leave room for cream."
    the_person "Okay. Is that all?"
    mc.name "Yeah..."
    "You pay for your coffee, but stand still."
    mc.name "You know, I've been coming here for a while but haven't seen you before. You just get hired?"
    the_person "Yeah, I'm going to school part time at the university, and I picked up this job to help pay tuition."
    mc.name "Ah, good for you. Well, best of luck with your studies. If you are smart as you are beautiful, I'm sure you will do well."
    the_person "Ah, thank you..."
    mc.name "I'm [mc.name]."
    the_person "[the_person.name]."
    mc.name "It's a pleasure to meet you."
    "Right then another employee puts your coffee on the counter and calls your name."
    the_person "Right... sorry, there's someone behind you..."
    "You hear a throat clear behind you. You grab your coffee and move out of the way."
    "Well, the new barista is cute! Maybe you should try to get to know her more..."
    $ the_person.add_unique_on_talk_event(kaya_ask_out)
    $ kaya.event_triggers_dict["intro_complete"] = True
    return

label kaya_ask_out_label(the_person): #Requires 20 love, substitute for first date.
    $ kaya.event_triggers_dict["can_get_drinks"] = True
    "You step into the coffee shop. You wonder if [the_person.title] is working. It is almost closing time."
    $ renpy.show("restaurant", what = restaraunt_background)
    $ the_person.draw_person()
    "Sure enough, as you step inside, there she is. You've been getting to know her more lately, and you feel ready to ask her out."
    "When you step up to the counter, she smiles at you."
    $ the_person.draw_person( emotion = "happy")
    the_person "Good evening [the_person.mc_title]. What can I get you?"
    mc.name "I'll take a small coffee with room for cream... and I'd was hoping to ask you something."
    the_person "Okay, I can do that... and what is the question?"
    mc.name "I was ahhh, wondering if you were doing anything after you got off work today?"
    the_person "No, I don't have any plans. You umm... have any particular reason for asking?"
    mc.name "I know a good bar around the corner... I thought maybe we could get a drink?"
    the_person "Oh! I... you seem pretty nice... yeah I guess I could do that!"
    mc.name "Great! Tell you what, I'll take my coffee out to the patio... whenever you get off, I'll walk you over there?"
    the_person "Okay... don't worry I get off soon!"
    $ clear_scene()
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "You step outside and sit down, sipping your coffee."
    "You spend some time on your phone, and follow up on a couple of work emails while you wait. It's a pretty pleasant evening."
    "Pretty soon you hear [the_person.possessive_title] clear her throat nearby. You look up from your phone."
    $ the_person.draw_person()
    mc.name "Ah, you're right, that was quick!"
    the_person "Yes... hey... I need to be honest about something..."
    mc.name "Oh? Did you change your mind? It's quite alright..."
    the_person "No, I'd still like to go and hang out, but I won't be able to have any drinks."
    mc.name "Ah, you don't drink?"
    the_person "No, it's not that, I'm just... with school and some other stuff going on... money is just really tight right now..."
    mc.name "Oh! Why don't you let me pick up the tab tonight?"
    the_person "I couldn't let you..."
    mc.name "Just pretend like I left a 20 in your tip jar, and you wanted to treat yourself."
    the_person "I suppose... just a couple, okay?"
    mc.name "Great! Let's go."
    "You stand up, making sure to throw your coffee cup away and leave the table clean. You start to walk with [the_person.title] a couple blocks to the bar."
    the_person "So... sorry if I'm like... misreading this... but... is this like... a date?"
    "She seems to be in tune with your intentions."
    mc.name "Well [the_person.title], I'm certainly interested in getting to know you better! And I have to say I like what little I know about you so far..."
    mc.name "I can hardly think a better way of learning more about you than a date!"
    $ the_person.change_love(2)
    the_person "Ahhh... I'm glad to know I wasn't mistaken."
    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()
    "Soon, you arrive at the bar. You point her to a high top you spot that looks open."
    mc.name "Hey, if you want to go grab that table, what is your drink of choice?"
    the_person "Oh, umm, let me walk up with you instead, I want to see if they have any specials."
    mc.name "Okay. With company as pretty as you we'll probably getting served faster anyway!"
    $ the_person.change_happiness(3)
    "She smiles and accepts your compliment. You walk up to the bar with her. Soon the bartender comes over."
    "?????" "Hey there. Never see you around here before, what can I get you?"
    the_person "Hi! Are you running any specials tonight?"
    "?????" "Well, we got domestic beers for $2, some imports for $3, and rail drinks for $4."
    the_person "Ah, can I get a rum and coke please?"
    "You wonder if she's just trying to be considerate? You would hardly expected a girl like her to order that as a first choice..."
    "You must have given her a funny look."
    the_person "What? You seem like a nice guy, I just want to be a cheap date!"
    "Ah, so she must be very budget conscious. You suppose there are certainly worse personality traits to have!"
    "You order yourself an old fashioned, something to sip on while you chat."
    "Once you have your drinks, you look around. The table you were looking at is full... looks like everything is full..."
    the_person "Ah! Look! An open pool table! Let's play!"
    $ the_person.discover_opinion("billiards")
    "[the_person.possessive_title] gets really excited. She must really enjoy billiards?"
    "She takes a sip of her drink, then sets it down on the side of the pool table. You do the same."
    mc.name "So tell me, cheap date, what happens to be your actual favorite cocktail?"
    the_person "Why so interested? Trying to get me drunk?"
    mc.name "Honestly, I feel like a person's favorite drink says a lot about them."
    the_person "Is that so?"
    mc.name "Absolutely. I know I'm dealing with immature college girls when I get when the answer is some ridiculous drink like 'sex on the beach'."
    the_person "Ha! Yeah I suppose."
    "[the_person.title] pulls some quarters out of her purse and puts them in the table. She pays the cost of a game and you hear the billiard balls fall into the gully."
    mc.name "But you... you seem much too practical for something like that. You seem like the type that would enjoy finer spirits."
    "[the_person.possessive_title] is pulling the balls from the gully and setting them on the table. She looks at you and smirks."
    the_person "Ah, is that so?"
    mc.name "Indeed. And the fact that you don't deny it tells me I'm right."
    the_person "You sure seem pretty confident in yourself there, mister! Tell you what. Let's play a round, and if you win, I'll tell you favorite drink. Okay?"
    mc.name "Ah, whose confident now? Placing a wager on a billiards game!"
    "She chuckles and rolls her eyes mockingly."
    the_person "Disclosing my favorite drink hardly seems like a major wager. Maybe I intend to lose, so you can learn my secret? You're the one buying the drinks, remember?"
    the_person "Tell you what, if I win, I'll even allow you a guess, and I'll tell you if you're right or not."
    mc.name "That seems more than fair. If I can't get it right, I think I can get close."
    "She picks up her drink and takes a long sip. Then grabs her pole."
    the_person "Here, rack these up, will you?"
    call play_billiards(the_person) from _kaya_first_billiards_01
    if _return: #You won
        the_person "Wow, I'm impressed! Do you play much?"
        mc.name "Not particularly. But It's a game of angles, and math has always been a strong subject for me."
        the_person "I see."
        mc.name "Now, about our wager?"
        the_person "Okay okay. If you really want to know..."
        the_person "My favorite cocktail is a Manhattan with an orange twist."
    else:
        mc.name "Wow, you are very good at pool! That was very impressive."
        the_person "Thank you. I love to play. It is a good exercise for your dexterity and your brain."
        mc.name "I agree. Now, about the wager..."
        the_person "Yes, this should be interesting. Go ahead, think about it and guess my favorite drink."
        "It is clear to you so far that [the_person.possessive_title] is intelligent and practical. However, even though she is strapped for money right now, you get the feeling things haven't always been this way for her."
        "Rum is too simple a spirit for her to favor. She probably favors gin or whiskey."
        "Something about her dark skin has you guessing it might be a darker spirit too, so you decide to guess a classic whiskey cocktail."
        menu:
            "Whiskey sour":
                pass
            "Highball":
                pass
            "John Collins":
                pass
        the_person "Wow. I admit, I was thinking that you were pretty full of shit, but that's actually really close! Close enough for me anyway!"
        mc.name "Oh?"
        the_person "My favorite cocktail is definitely a Manhattan with an orange twist."
    mc.name "Ah, a bold drink indeed. I was definitely thinking something whiskey inspired, but I would not have guessed that."
    the_person "Yeah. Sometimes I'll have one, but to make a good one it requires good whiskey. The ones you get with more affordable varieties just aren't as good."
    mc.name "Yes, a quality of many heavy whiskey drinks I think. Well, we seem to be ready for another round?"
    the_person "I umm... I'm kind of out of quarters..."
    mc.name "Here, let me go get us a couple more drinks and some quarters. I'm not quite ready to say goodbye for the evening yet."
    $ the_person.change_love(2)
    the_person "I suppose I could stay out for a bit longer."
    $ mc.business.add_mandatory_crisis(kaya_get_drinks)
    $ kaya.event_triggers_dict["bar_date"] = True
    $ clear_scene()
    "You walk back up to the bartender. You order yourself another old fashioned and a top shelf manhattan with an orange twist for [the_person.title]."
    "When he brings you the drinks, you ask for change for a dollar to play another round of pool. When he goes to make change for you, you look down at the drinks..."
    "You could probably slip a serum into her drink if you do it quickly..."
    call give_serum(the_person) from _call_give_kaya_serum_bar_01
    "You walk back to the pool table. She smirks when she sees your drink for her."
    the_person "Ah, so you ARE trying to get me drunk then? Ahhh, {=kaya_lang}koretake {/=kaya_lang}(?????)."
    mc.name "As... what now?"
    the_person "Ah... sorry... as you might have guessed, English isn't my first language."
    "She takes a sip from her drink."
    the_person "My mom thought it was important for me to learn my native tongue first, even though no one really speaks it anymore."
    the_person "Sometimes I still find myself using words from it by accident."
    mc.name "Ah, I see. So what language is your first language?"
    the_person "Well, my family and I are natives... from before white colonization here."
    mc.name "That's very interesting! I'm not sure I've ever met a native."
    the_person "Well, to be honest, there aren't many of us left, and even fewer off of reservations."
    "You take a moment to think about it. You take the coins from the bartender and walk around the pool table, starting up another game."
    the_person "We playing for anything this time? It's kinda fun when there are stakes..."
    mc.name "Sounds good to me. I set the stakes last match, how about you set them for this one?"
    the_person "Hmmm... okay. How about, if I win, you have to walk me home?"
    mc.name "You know I was planning to offer to do that anyway, right?"
    the_person "Probably, but now you'll HAVE to!"
    mc.name "Ah. Well, in that case, if I win, you have to let me take you out for drinks again another time."
    the_person "Free drinks? Deal. I might have to lose on purpose!"
    call play_billiards(the_person) from _kaya_first_billiards_02
    if _return: #You won
        the_person "Oh no! Now I have to subject myself to another night of free drinks and billiards!"
        mc.name "The horror!"
        the_person "Guess I'll just have to walk myself home now, dreading the day the mysterious stranger shows up at the coffee-shop and demands my presence again!"

    else:
        the_person "Well, I won! But... I still think you should have to take me out for drinks again some time."
        mc.name "Too bad you didn't make that your wager then."
        "At first she looks at you, a bit startled, thinking you mean you don't want to, but then realizes you are teasing her"
        the_person "Guess you'll just have to walk me home and we'll go our separate ways then."
    "The teasing between you two has definitely become playful. You are really enjoying her company."
    the_person "But uh... we're doing both... right?"
    mc.name "Of course."
    "You both finish off what is left of your drinks, then leave the bar together."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "You step out on to the sidewalk and start to walk [the_person.possessive_title] home. Sensing a connection with her, you hold out your hand and she takes it."
    mc.name "So, you're going to class at the university, right?"
    the_person "That's right."
    mc.name "What are you studying?"
    the_person "I'm majoring in biology, but I'm hoping once I graduate to get into med school..."
    mc.name "Wow. So you want to be a doctor?"
    the_person "Yeah... something like that..."
    "She is quiet for a little bit, before she resumes."
    the_person "I know this might sound silly, but my mother is really the last family I have left. She's always had some recurring health issues, but lately they've been getting worse I think."
    the_person "It sucks... I know I'll never finish school in time to do anything for her... but I think I want to get into research. You know? Learn how to help other people. People like her."
    mc.name "She must be a great woman for you to look up to her like that."
    the_person "Yeah. She really is. She inspires me every day."
    mc.name "I can understand that. Did I tell you I run a pharmaceutical company? We do our own research and development, although not for any major medical illnesses."
    the_person "Really? That's pretty interesting. You're a very interesting man [the_person.mc_title]."
    "You walk in silence a bit longer with [the_person.title]."
    "Soon you walk up to the steps of run down apartment building. This must be where she is living."
    the_person "Hey, I just want to say, it's been a long time since I had a night like this to just relax and have fun. I had a great time... please come back and see me at the coffeshop, okay?"
    mc.name "Your charm is difficult to resist. And the coffee is good too."
    $ the_person.draw_person(position = "kissing")
    "[the_person.title] holds her arms out for a hug, and you draw her close. She is looking up at you, and feeling right, you kiss her."
    "She responds immediately and starts kissing you back. Her mouth opens and your tongues intertwine in a passionate kiss."
    "Your hands start to roam around [the_person.possessive_title]'s back. She gives a little moan when you hand wanders down to her ass, but reaches back and moves your hand back up."
    $ the_person.change_arousal(15)
    $ the_person.break_taboo("kissing")
    "You keep making out for several more seconds until [the_person.title] breaks it off and then steps back."
    $ the_person.draw_person()
    the_person "God you are hot..."
    mc.name "Can I umm... come up?"
    the_person "Oh... I'm sorry... this was just a first date! I couldn't possibly after just once..."
    mc.name "That's okay. I'm sorry I didn't mean to make you uncomfortable."
    the_person "It didn't at all. We umm... we just need to get to know each other better. Okay?"
    mc.name "Sounds great. I'll see you around?"
    the_person "Bye!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and starts to walk up the starts to the apartment building."
    "Wow, what a busy night! You feel like you have a connection with [the_person.title]. She definitely seems eager too..."
    return

label kaya_get_drinks_label(the_person):  #Repeatable date night with Kaya
    mc.name "How about a couple drinks tonight?"
    the_person "Sounds great! It's almost closing time, and I'm solo tonight. If you want to just grab a seat while I close up, we can walk over together."

    "You meet with Kaya after she gets off work. You take her to a local bar."
    "You grab a couple drinks. Chance to serum her."
    "You find out she likes to play pool. You play a round, barely winning."
    "Grab a couple more drinks."
    "Before the next round, Kaya talks about her mother being sick, can't pay for her medications, having to work coffee-shop job to help out."
    "MC gets the idea of the intern program as a way for the company to provide girls with scholarships and some spending money."
    "If shes slutty, she flashes you at a key moment as a distraction."
    "You lose the second round."
    "She's too tired to play another round but asks for a rain check. Asks if you will walk her home."
    "At her apartment door, start making out. When MC starts getting handsy, a door slamming down the hall interrupts."
    "She apologizes, she doesn't want to put out on the first date. Says goodnight to MC."
    "MC has unlocked grabbing drinks with Kaya. He can ask her to grab drinks when she is working at the coffee shop any evening."
    if mc.business.hr_director:
        $ mc.business.hr_director.add_unique_on_talk_event(kaya_HR_start_internship_program)
    else:
        $ mc.business.add_mandatory_crisis(kaya_add_HR_program_event)
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

label kaya_meet_lily_at_uni_label():    #This label starts Kaya and Lily friendship storyline. Requires mid Kaya love (>40?). REquires scholarship program.
    "You go the university to meet with them there with your offer to have a small internship and scholarship program."
    "If you have rediscovered Nora she is at the meeting, is impressed with your offers, says going forward she can recommend you interns."
    "After you finish, you happen to spot Kaya and say hello."
    "You talk to Kaya about the new internship program. She is impressed and immediately agrees. You assign her to research and development."
    "As you are talking to Kaya, Lily happens to talk by and sees you talking with her. When Lily walks up, Kaya starts to get territorial."
    "She starts to get jealous of you talking to another girl."
    "She's my sister, it's not like that (even though it kind of is)."
    "Suddenly she is super friendly with Lily. Find out Lily is taking a class Kaya took last semester."
    "Lily asks if Kaya wants to come over to study some time. Kaya enthusiastically agrees, surprised to find out MC lives with sister and mom."
    "They are now friends."

    $ town_relationships.update_relationship(sister, kaya, "Friend")
    $ mc.business.add_mandatory_crisis(kaya_lily_study_night_intro)
    $ kaya.event_triggers_dict["has_started_internship"] = False
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
    "While helping her move, you notice a picture. It's your dad with Sakari?"
    "This is suspicious. Later you have the chance to be alone with Sakari and ask her about it."
    "Find out Sakari was your dad's mistress. Kaya is your half sister."
    "IF you fucked her earlier, imagine your cum is still inside your half sister."
    "Sakari asks if you are his son. You admit you are."
    "Sakari admits there was some drama. Never intended to drive a wedge between your parents, but that you should probably leave Kaya alone."
    "Before you can answer, Kaya interrupts the conversation. Doesn't know what was being said."
    "You finish helping Kaya move. Leave the place stunned."
    $ mc.business.add_mandatory_crisis(kaya_share_the_news)
    $ kaya.event_triggers_dict["share_news_day"] = day + 7
    $ kaya.event_triggers_dict["has_moved"] = False
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



label play_billiards(the_person, skill_offset = 0): #MC can play billiards.
    $ the_person.draw_person()
    "[the_person.title] grabs a pool stick and starts to chalk the end while you rack the billiard balls."
    "Once you've got them nice and tight, you nod to her."
    mc.name "Go ahead, you can break."
    menu:
        "Play the game":
            pass
        "Simulate the game":
            pass

    return

init 2 python:
    def calc_pool_ball_sink_chance(skill = 0, difficulty = 0):
        if renpy.random.randint(0,100) < min((50 + (skill * 5) ) - (difficulty * 10), 90):
            return True
        return False


init 3 python:      #Use this section to make wrappers for determining where we are in relation to Kaya's major story events

    def kaya_has_finished_intro():
        return kaya.event_triggers_dict.get("intro_complete", False)   # True after first talk

    def kaya_can_get_drinks():
        return kaya.event_triggers_dict.get("can_get_drinks", False)

    def kaya_can_get_work_quickie():
        return kaya.event_triggers_dict.get("can_get_barista_quickie", False)

    def kaya_has_started_internship():
        return kaya.event_triggers_dict.get("has_moved", False)

    def kaya_has_moved():
        return kaya.event_triggers_dict.get("has_started_internship", False)
