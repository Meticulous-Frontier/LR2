#Designed for the mid game. Your employee model brainstorms marketing ideas with you and comes up with a wet-tshirt contest.
#Requires company model with at least moderate sluttiness (>40)
#Depending on how slutty the company is in general, some girls may come out for fun, others with persuasion, some require a bribe (extra pay)
#Once completed, get a temporary sales boost based on how slutty the girls were who participated.
#Unlocks the wet-shirt scene permanently and MC can run one again once a week if desired.

#Flags
#Use numbers to describe quest flags
#1 Init
#9 Init failes due to lack of company model
#11 You've brainstormed ideas with marketting and come up with the wet t-shirt contest idea.
#19 You've brainstormed ideas with marketing and couldn't come up with anything. (BAD END)
#21 You've talked to HR dept about making sign ups.
#31 HR has reported if girls have signed up or not
#39 Not enough girls signed up so you said heck it
#41 You agree to try and persuade a few girls to do it.
#42 You agree to offer additional pay to a few girls to do it.
#99 For whatever reason you don't have a head model during this process
#101 Wet shirt contest is complete and now unlocked for future use.

#TODO don't forget to add the quest to the list of quests in Side_quests_main.rpy

### The next three functions define the quest progress tracker, init requirements, and how we clean up after quest is done.
init 1 python:
    def setup_quest_wet_tshirt_contest():
        #Use this function to set quest specific variables.
        quest = quest_wet_tshirt_contest()
        contact = mc.business.company_model
        quest.quest_event_dict["target"] = contact.identifier
        quest.quest_event_dict["hr target"] = None
        mc.business.event_triggers_dict["tshirt girls"] = []    #We use mc.business for this because it unlocks for the whole business when this is complete.
        quest.quest_event_dict["start_day"] = 9999
        quest.quest_event_dict["research_day"] = 9999
        quest.quest_event_dict["timeout_day"] = 9999
        quest.set_quest_flag(1)
        contact.add_unique_on_room_enter_event(quest_wet_tshirt_contest_intro)
        game_hints.append(Hint("Marketing Scheme", "There is a strange smell around the office.", "quest_essential_oils().get_quest_flag() <= 1", "quest_essential_oils().get_quest_flag() > 1"))
        game_hints.append(Hint("Marketing Scheme", "Talk to your head researcher about essential oils.", "quest_essential_oils().get_quest_flag() == 11", "quest_essential_oils().get_quest_flag() != 11"))
        game_hints.append(Hint("Marketing Scheme", "Check up on your head researcher.", "quest_essential_oils().get_quest_flag() == 21 and day > quest_essential_oils().quest_event_dict.get('research_day', 0)", "quest_essential_oils().get_quest_flag() != 21"))
        hint_string = "Talk to " + contact.title + " about getting essential oils."
        game_hints.append(Hint("Marketing Scheme", hint_string , "quest_essential_oils().get_quest_flag() == 31", "quest_essential_oils().get_quest_flag() != 31"))
        game_hints.append(Hint("Marketing Scheme", "Talk with Dawn at the mall about bulk purchase of essential oils.", "quest_essential_oils().get_quest_flag() == 41", "quest_essential_oils().get_quest_flag() != 41"))
        return

    def quest_wet_tshirt_contest():
        return quest_director.get_quest("Wet Tshirt Contest")

    def quest_wet_tshirt_contest_tracker():
        quest = quest_wet_tshirt_contest()
        if quest.get_quest_flag() <= 101:    #If company model quits or get fired before quest completion then quest fails
            if mc.business.company_model is None:
                quest.quest_completed()
                return

        return

    def quest_wet_tshirt_contest_start_requirement():
        return False    # NOT YET IMPLEMENTED

        if day < 21:
            return False    # don't start this too soon
        if mc.business.company_model is None:
            return False    # we need a company model
        if mc.business.company_model.sluttiness < 50:
            return False    # she needs to be slutty enough to go along
        return True

    def quest_wet_tshirt_contest_cleanup():
        pass
        # mc.business.remove_mandatory_crisis("quest_essential_oils_abandon_label")
        # person = quest_essential_oils_get_target()
        # if person:
        #     person.remove_on_room_enter_event(quest_essential_oils_intro)
        #     person.remove_on_talk_event(quest_essential_oils_discover_supplier)
        # dawn.remove_on_talk_event(quest_essential_oils_decision)
        # if mc.business.head_researcher:
        #     mc.business.head_researcher.remove_on_talk_event(quest_essential_oils_research_start)
        #     mc.business.head_researcher.remove_on_talk_event(quest_essential_oils_research_end)
        # quest_essential_oils().quest_event_dict.clear()
        return

        ###Declare any requirement functions now
    def quest_wet_tshirt_contest_intro_requirement(the_person):
        if mc.business.is_open_for_business():
            return True
        return False

    def quest_wet_tshirt_contest_hr_talk_requirement(the_person):
        if mc.business.is_open_for_business():
            return True
        return False

        ###Functions unique to the quest


        ###Declare quest actions###

    quest_wet_tshirt_contest_intro = Action("Marketing Scheme", quest_wet_tshirt_contest_intro_requirement, "quest_wet_tshirt_contest_intro_intro_label")

init 2 python:  #We use a temporary role to add conversation options to big titty employees to talk them into modeling for the contest.
    emp_with_big_tits_role = Role(role_name ="Big Tit Employee", actions =[], hidden = True)

    def quest_wet_tshirt_contest_add_convo_role():
        for emp in mc.business.get_employee_list():
            if emp.has_large_tits():
                emp.add_role(emp_with_big_tits_role)
        return

    def quest_wet_tshirt_contest_remove_convo_role():
        for emp in mc.business.get_employee_list():
            if emp.has_role(emp_with_big_tits_role):
                emp.remove_role(emp_with_big_tits_role)
        return

    def wet_tshirt_add_contestant(person):
        mc.business.event_triggers_dict["tshirt girls"].append(person)
        return

#Quest Labels. This is the story you want to tell!
label quest_wet_tshirt_contest_intro_init_label():
    $ setup_wet_tshirt_contest_intro_oils()
    return

label quest_wet_tshirt_contest_intro_label(the_person):
    if the_person != mc.business.company_model:
        $ quest_wet_tshirt_contest().set_quest_flag(9)
        return

    $ quest_wet_tshirt_contest().quest_event_dict["start_day"] = day
    "As you walk into your marketing division, your company model spots you and waves you over to her desk."
    $ the_person.draw_person(position = "sitting")
    the_person "Hello [the_person.mc_title], I could use your help with something."
    mc.name "What do you need?"
    the_person "I've been looking into different methods we could use to help market product, but I've kind of hit a wall."
    the_person "As you know, there's been a huge reason rise in live-streaming as a source of marketing potential, but I can't figure out what we could do that would get us the eyeballs we are looking for."
    mc.name "You mean you want to have... some kind of broadcast?"
    the_person "Right. I think we could make a live-stream for our product, and if we targeted the right audience, it would help drive up demand for the product, while being extremely cheap to produce."
    mc.name "Hmm... that's an interesting idea."
    the_person "I just can't figure out what exactly we could stream. Obviously the nature of the product lends itself to certain activities, but for the most possible eyeballs, we need to keep everyone clothed."
    "Hmmm, you think about it for a while."
    mc.name "So, do we want to showcase what the product itself can do? What if we just got a few employees together and had them show some skin?"
    the_person "That would be okay, but honestly kind of boring. Maybe we could have some kind of competition?"
    menu:
        "Wet T-shirt Contest":
            pass
        "Forget it":
            mc.name "I'm sorry, I'm not sure it is a good idea for us to do a live-stream for a pharmaceutical. I appreciate the hard work you put into it though."
            the_person "Aww, really? Okay... I'll try to think of something else."
            #TODO end quest.
            $ quest_wet_tshirt_contest().set_quest_flag(19)
    mc.name "What if we got say 3 employees, and on live-stream we had them do a wet t-shirt contest?"
    mc.name "Everyone would stay clothed, but that would be sexy and help drive demand for serum."
    the_person "Hmmm, that might just work! If you got it set up, I could do some advertising to drive up hype."
    "You consider how to go about setting it up."
    mc.name "Who should we get to be in it? You?"
    the_person "No, I'll need to run the camera and respond in realtime on the stream itself."
    if the_person.has_large_tits():
        mc.name "That's too bad, you've got a great rack..."
        $ the_person.change_happiness(2)
        $ the_person.change_slut(2)
        the_person "Ah, thank you. It would probably be for the best to pick out girls with larger chests in general for this though."
    else:
        the_person "Besides, I'm a little flat chested for what you have in mind. If you really want to drive interest, try to find girls who are a little more blessed in the chest."
    if mc.business.hr_director:
        $ quest.quest_event_dict["hr target"] = mc.business.hr_director.identifier
        the_person "Why don't you talk to the HR director, [mc.business.hr_director.name]? I bet she could help you figure out who would be good for it..."
    else:
        $ contact = get_random_from_list(mc.business.hr_team)
        if contact == None: #No one in HR? We try to just talk to girls directly? Or fail quest?
            the_person "Hmm... I'm not really sure who you would talk to about it to make it happen. Maybe you should just talk to some girls around the office?"
            mc.name "Hmm... maybe..."
            #TODO this
        $ quest.quest_event_dict["hr target"] = contact.identifier
        $ contact.add_unique_on_talk_event(quest_wet_tshirt_contest_hr_talk)
        the_person "Why don't you talk to [contact.name] in HR? I bet she could help you figure out who would be good for it..."
    mc.name "I think I'll do that. Start figuring out a marketing scheme for it, I'll try and make the rest of it happen."
    the_person "Sure thing [the_person.mc_title]!"
    $ quest_wet_tshirt_contest().set_quest_flag(11)

    return

label quest_wet_tshirt_contest_hr_talk_label(the_person):
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. I need to talk to you about something."
    the_person "Okay."
    mc.name "I was talking with [mc.business.company_model.title] in marketing, and we came up with an idea to help drive sales."
    mc.name "We want to host a promotional wet t-shirt contest here with some of the employees. She feels it would help drive up demand."
    #Responses
    if the_person == sarah and the_person.has_large_tits():
        the_person "Oh! That sounds like so much fun! And you want me to be in it?"
        "[the_person.possessive_title] bounces up and down with excitement. You have to admit, she would make a great contestant..."
        mc.name "You certainly can, but I also need your help finding two more volunteers."
        $ wet_tshirt_add_contestant(the_person)
        the_person "Oohhhh I see why you came to talk to me. Hmmm."
    elif the_person.has_large_tits() and the_person.effective_sluttiness("underwear_nudity") >= 40:
        the_person "Oh! And you want me to be in it? [the_person.mc_title] I'm glad you asked. I'd be glad to."
        $ wet_tshirt_add_contestant(the_person)
        mc.name "Right, I want you to be in it... and I am also helping that, being in HR, you could help me find a couple more volunteers."
        the_person "Oooohhhh, I see why you came to talk to me. Hmmm."
    elif the_person.effective_sluttiness() >= 40:
        the_person "Oh! I follow the logic. But ummm, surely you aren't here to ask me to do that, right?"
        mc.name "Being in HR, I was hoping you could help me find the volunteers."
        the_person "Oooohhhh, I see why you came to talk to me. Hmmm."
    elif the_person.effective_sluttiness() <= 15:
        $ the_person.change_happiness(-3)
        the_person "Wow... how... typical? I'm not sure why you came to talk to me though. I'm not doing that."
        mc.name "No, but being in HR, I need your help finding the volunteers."
        "She rolls her eyes hard, but eventually looks over at you."
        the_person "Fine. Let me see..."
    else:
        $ the_person.change_slut(2)
        the_person "That's an interesting idea, for sure... but why come talk to me about it?"
        mc.name "Being in HR, I was hoping you could help me find the volunteers."
        "She seems a bit relieved."
        the_person "Oh! That makes sense. Let me see..."
    the_person "Give me a couple of days and I'll ask around the office. I'll come find you in a couple days and let you know if I can... staff it."
    mc.name "Thanks [the_person.title]. I appreciate it."
    the_person "I'm sure you do..."
    #TODO link next event.
    return

#
# label quest_essential_oils_abandon_label():
#     "It's been over a week now since you started considering adding essential oil as a serum trait. The more you think about it, the dumber it sounds."
#     "You a run a legitimate pharmaceutical business, there's no room for that bullshit around here."
#     "You decide just to scrap the whole idea."
#     $ quest_essential_oils().set_quest_flag(99)
#     $ quest_essential_oils().quest_completed()
#     return
#
# label quest_essential_oils_invoice_label():
#     "You get an invoice to your business for the essential oils you purchased."
#     "You write a check and drop it in the mailbox."
#     $ mc.business.change_funds(-500)
#     $ quest_essential_oils().quest_completed()
#     return
