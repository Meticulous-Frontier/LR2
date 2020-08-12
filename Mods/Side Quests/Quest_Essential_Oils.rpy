#Designed for the early game. Introduces a serum with great value but high chance of side effect.
#Requires employee with low intelligence
#When entering a room, an employee is diffusing some essential oils
#When you ask, she says they are expensive but that women love them and willing to pay big bucks for them.
#You go to your head researcher to see if they could be added to serum. She promises to research and get back to you.
#Two days later, she says yes, but that you need to be able to buy them in bulk. You go back to your first girl and ask where she got them.
#She says she got them in bulk from Dawn at the mall (naturalist)
#After going to the mall, you meet with dawn. She agrees to sell you a bulk order of essential oils.
#If MC doesn't have enough funds, she offers to set up a payment plan.
#NOTE use mandatory events to force quest progression.

#Flags
#Use numbers to describe quest flags
#1 Init
#11 You've walked in on employee diffusing essential oils.
#19 You told employee to stop being stupid and using the oils.
#21 You've talked to HR about using essential oils to use in serums.
#31 HR says you can, so you go back to original person and ask where she got them.
#41 original target tells you where to get them.
#49 MC decides oils are too expensive, declines to purchase them
#99 If at any point the quest takes too long, MC decides oils are bullshit and to forget about them. Make sure to cleanup!
#101 Dawn agrees to sell MC oils for a straight $500
#102 Dawn agrees to sell MC oils for payment due in 7 days
#If 101 or better gain access to new serum trait, essential oils.

#TODO don't forget to add the quest to the list of quests in Side_quests_main.rpy

### The next three functions define the quest progress tracker, init requirements, and how we clean up after quest is done.
init 1 python:
    def setup_quest_essential_oils():
        #Use this function to set quest specific variables.
        quest_essential_oils.quest_event_dict["target"] = quest_essential_oils_find_employee()
        quest_essential_oils.quest_event_dict["start_day"] = 9999
        quest_essential_oils.quest_event_dict["research_day"] = 9999
        quest_essential_oils.quest_event_dict["timeout_day"] = 9999
        quest_essential_oils.set_quest_flag(1)
        quest_essential_oils_get_target().add_unique_on_room_enter_event(quest_essential_oils_intro)
        game_hints.append(Hint("Essential Oils", "There is a strange smell around the office.", "quest_essential_oils.get_quest_flag() <= 1", "quest_essential_oils.get_quest_flag() > 1"))
        game_hints.append(Hint("Essential Oils Research", "Talk to your head researcher about essential oils.", "quest_essential_oils.get_quest_flag() == 11", "quest_essential_oils.get_quest_flag() != 11"))
        game_hints.append(Hint("Essential Oils Research Checkup", "Check up on your head researcher.", "quest_essential_oils.get_quest_flag() == 21 and day > quest_essential_oils.quest_event_dict.get('research_day', 0)", "quest_essential_oils.get_quest_flag() != 21"))
        hint_string = "Talk to " + quest_essential_oils_get_target().title + " about getting essential oils."
        game_hints.append(Hint("Essential Oils Purchase Research", hint_string , "quest_essential_oils.get_quest_flag() == 31", "quest_essential_oils.get_quest_flag() != 31"))
        game_hints.append(Hint("Essential Oils Purchase", "Talk with Dawn at the mall about bulk purchase of essential oils.", "quest_essential_oils.get_quest_flag() == 41", "quest_essential_oils.get_quest_flag() != 41"))
        return

    def quest_essential_oils_tracker():
        if quest_essential_oils.get_quest_flag() <= 101:    #If head researcher quits or get fired before quest completion then quest fails
            if mc.business.head_researcher == None:
                quest_essential_oils.quest_completed()
                return

        if quest_essential_oils.get_quest_flag() <= 1:
            if quest_essential_oils_get_target() == None:
                the_target = quest_essential_oils_find_employee()
                if the_target == None:
                    quest_essential_oils.quest_completed()
                    return
                quest_essential_oils.quest_event_dict["target"] = the_target
            quest_essential_oils_get_target().add_unique_on_room_enter_event(quest_essential_oils_intro)
        elif quest_essential_oils.get_quest_flag() >= 11 and quest_essential_oils.get_quest_flag() <= 31:
            if quest_essential_oils_get_target() == None:#The quest has started but we fired or the target quit.
                quest_essential_oils.quest_completed()
        return

    def quest_essential_oils_start_requirement():
        if day < 21: # don't start this too soon
            return False
        if mc.business.head_researcher == None:
            return False
        if quest_essential_oils_find_employee() == None:
            return False
        return True

    def quest_essential_oils_cleanup():
        remove_mandatory_crisis_list_action("quest_essential_oils_abandon_label")
        if quest_essential_oils_get_target():
            quest_essential_oils_get_target().remove_on_room_enter_event(quest_essential_oils_intro)
            quest_essential_oils_get_target().remove_on_talk_event(quest_essential_oils_discover_supplier)
        dawn.remove_on_talk_event(quest_essential_oils_decision)
        if mc.business.head_researcher:
            mc.business.head_researcher.remove_on_talk_event(quest_essential_oils_research_start)
            mc.business.head_researcher.remove_on_talk_event(quest_essential_oils_research_end)
        quest_essential_oils.quest_event_dict.clear()
        return

    def quest_essential_oils_get_target():
        return quest_essential_oils.quest_event_dict.get("target", None)

###Declare any requirement functions now
    def quest_essential_oils_intro_requirement(the_person):
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                return True
        return False

    def quest_essential_oils_research_start_requirement(the_person):
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                return True
        return False

    def quest_essential_oils_research_end_requirement(the_person):
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if day > quest_essential_oils.quest_event_dict.get("research_day", 0):
                    return True
        return False

    def quest_essential_oils_discover_supplier_requirement(the_person):
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                return True
        return False

    def quest_essential_oils_decision_requirement(the_person):
        if time_of_day > 0:
            if time_of_day < 4:
                return True
        return False

    def quest_essential_oils_abandon_requirement():
        if day > quest_essential_oils.quest_event_dict.get("timeout_day", 0):
            if time_of_day == 2:
                return True
        return False

    def add_quest_essential_oils_invoice():
        quest_essential_oils_invoice = Action("Essential Oil Invoice", quest_essential_oils_invoice_requirement, "quest_essential_oils_invoice_label", requirement_args = day + 5)
        mc.business.mandatory_crises_list.append(quest_essential_oils_invoice)
        return

    def quest_essential_oils_invoice_requirement(pay_day):
        if day > pay_day:
            if time_of_day == 2:
                if mc.is_at_work():
                    return True
        return False

###Functions unique to the quest
    def quest_essential_oils_find_employee():
        able_person_list = []
        for person in mc.business.get_employee_list():
            if person.int <= 2 and not quest_director.is_person_blocked(person):
                able_person_list.append(person)
        if __builtin__.len(able_person_list) == 0:
            return None
        return get_random_from_list(able_person_list)

###Declare quest actions###

    quest_essential_oils_intro = Action("Essential Oils", quest_essential_oils_intro_requirement, "quest_essential_oils_intro_label")
    quest_essential_oils_research_start = Action("Essential Oil Research", quest_essential_oils_research_start_requirement, "quest_essential_oils_research_start_label")
    quest_essential_oils_research_end = Action("Essential Oil Outcome", quest_essential_oils_research_end_requirement, "quest_essential_oils_research_end_label")
    quest_essential_oils_discover_supplier = Action("Find a Supplier", quest_essential_oils_discover_supplier_requirement, "quest_essential_oils_discover_supplier_label")
    quest_essential_oils_decision = Action("Talk to Supplier", quest_essential_oils_decision_requirement, "quest_essential_oils_decision_label")
    quest_essential_oils_abandon = Action("Abandon Quest", quest_essential_oils_abandon_requirement, "quest_essential_oils_abandon_label")


#Quest Labels. This is the story you want to tell!
label quest_essential_oils_init_label():
    $ setup_quest_essential_oils()
    return

label quest_essential_oils_intro_label(the_person):
    $ the_person = quest_essential_oils_get_target()
    if the_person is None:
        # Abort, something went wrong
        return

    # lock selected person out of other quests
    $ quest_director.add_unavailable_person(the_person)
    $ quest_essential_oils.quest_event_dict["start_day"] = day
    "As you walk into one of the business rooms, a very strange mixture of smells enter your nostrils."
    "You are having trouble placing the smell... Is there a chemical leak somewhere!?!"
    "You quickly scan the room. You notice [the_person.title] at a desk... with a strange chemical diffuser sitting next to her?"
    $ the_person.draw_person(position = "sitting")
    "You walk over. The smell is definitely coming from the diffuser."
    mc.name "[the_person.title]... can I ask what you are diffusing into the room?"
    the_person.char "Oh! Hello [the_person.mc_title]! Yeah I was having some trouble concentrating, so I got out my essential oil diffuser."
    the_person.char "It's my own personal mix of peppermint, rosemary, and lemon oils! Really helps me focus on the task at hand!"
    "You take another whiff... the smell is very confusing. And personally you find it a bit distracting."
    mc.name "Well, I don't think it is a good idea to be diffusing that around here. We have a lot of chemicals we store in the building, and for a minute I thought we had a leak or spill."
    the_person.char "Oh, yes sir! Don't worry, this batch is almost out anyway. This stuff is so expensive, I can't diffuse it often anyway."
    "Hmmm.... expensive?"
    mc.name "So, this is something people pay a lot of money for? These, essential oils?"
    the_person.char "Oh yes! You can use them for all sorts of things. Tummy aches, headaches, concentration, memory. Diffusers are good, but you can also apply them to the skin or even orally."
    menu:
        "Ask about taking the oils orally":
            mc.name "That's interesting. So you can take them orally? And they help with all that stuff?"
            the_person.char "Oh yeah! I've been using them for a while and definitely notice a difference."
            "You consider this for a moment. It's no secret that [the_person.title] isn't the brightest... but maybe this is something you could use?"
            "You wonder if you could somehow make a serum trait that uses the essential oils to help drive up the price. Surely if you advertised it was made with essential oils you could sell it for more?"
            "You should talk to your head researcher and see what she thinks about it."
            $ quest_essential_oils.quest_event_dict["timeout_day"] = day + 7
            $ quest_essential_oils.set_quest_flag(11)
            $ mc.business.head_researcher.add_unique_on_talk_event(quest_essential_oils_research_start)
            $ mc.business.mandatory_crises_list.append(quest_essential_oils_abandon)
        "Tell her to knock it off and leave it at home":
            mc.name "Well don't bring them back. This could have triggered an evacuation."
            the_person.char "Oh my... yes sir, I'll leave it at home from now on."
            $ quest_essential_oils.set_quest_flag(19)
            $ quest_essential_oils.quest_completed()
    "You say goodbye to [the_person.title]."
    return

label quest_essential_oils_research_start_label(the_person):
    $ the_person.draw_person()
    "You greet your head researcher."
    mc.name "Hello, I have a quick question for you. Have you ever heard of essential oils?"
    the_person.char "Oh god, don't start with that bullshit..."
    mc.name "Right, well, I was talking to another employee, and apparently there are people out there who will pay big money for them."
    the_person.char "There's a sucker born every minute, or so I've heard."
    mc.name "So... would it be possible to create a serum trait using essential oils? Not to do anything meaningful, but as a way of driving up the price."
    "[the_person.title] stops and considers what you are saying for a moment."
    the_person.char "I... think so? I don't know if theres any major negative side effects associated with them. I could look into it the next couple of days and get back to you."
    mc.name "Perfect. Let me know what you find out."
    the_person.char "Okay. Is there anything else I can do you for you?"
    $ quest_essential_oils.quest_event_dict["timeout_day"] = day + 7
    $ quest_essential_oils.quest_event_dict["research_day"] = day + 2
    $ mc.business.head_researcher.add_unique_on_talk_event(quest_essential_oils_research_end)
    $ quest_essential_oils.set_quest_flag(21)
    return

label quest_essential_oils_research_end_label(the_person):
    $ the_person.draw_person()
    the_person.char "Hey [the_person.mc_title]. Just the man I was hoping to see. I did some research on those essential oils you were asking about."
    mc.name "And?"
    the_person.char "Well, they are mostly related to placebo effect. People think they work, so they imagine they feel better or whatever else after they use them."
    the_person.char "Most of them also have some sort of negative side effect, but they are all mostly benign. It wouldn't be too hard to make a serum trait like you were asking."
    mc.name "That's great, that is exactly what I was hoping to hear."
    the_person.char "Just to give you a heads up though. Some of those oils are hard to extract, and for our company we would need to buy them in pretty bulk sizes..."
    mc.name "Hmm, so I may need to find a supplier."
    the_person.char "Yup! Sorry, I don't know where you could source this stuff. Here's a list of which ones would be appropriate for us to use."
    mc.name "Thanks, that's exactly what I needed."
    $ oil_target = quest_essential_oils_get_target()
    "You think back. It was [oil_target.title] that had some in the first place. Maybe you could ask her where she gets hers from?"
    $ oil_target.add_unique_on_talk_event(quest_essential_oils_discover_supplier)
    $ del oil_target
    $ quest_essential_oils.set_quest_flag(31)
    return

label quest_essential_oils_discover_supplier_label(the_person):
    $ the_person.draw_person()
    mc.name "Hello, I have a quick question for you."
    the_person.char "Yeah [the_person.mc_title]?"
    mc.name "Those oils you had the other day in here. Where did you get them from?"
    the_person.char "Oh! Looking to get some too?"
    mc.name "Yes, something like that."
    the_person.char "Well, I get mine from over at the mall. There's a nice lady over there who sells them. One of those, lifestyle coach, naturalist type people."
    mc.name "Do you remember her name?"
    "She thinks about it for a minute."
    the_person.char "Yes, I'm pretty sure her name is [dawn.name]. She has a small kiosk setup in the mall itself."
    mc.name "Thank you."
    the_person.char "Yup! Anything else I can do for you?"
    $ dawn.add_unique_on_talk_event(quest_essential_oils_decision)
    $ quest_essential_oils.set_quest_flag(41)
    return

label quest_essential_oils_decision_label(the_person):
    mc.name "I have an employee who told me she got some essential oils from you. Would you happen to be able to procure a bulk order?"
    the_person.char "Oh? How big are we talking?"
    mc.name "Well, I am interested in using them in a small run of pharmaceuticals I am developing."
    the_person.char "Ah, I could set you up with a gallon size for now? A little bit of these things go a long way!"
    mc.name "That sounds good. Here is a list of the ones I need."
    "You hand her the list from your researcher."
    the_person.char "Okay, I'll need $500 to cover the cost. Do you want to do that up front? Or should I invoice it?"
    menu:
        "Pay it up front":
            mc.name "I'll pay it all now. I have the cash on me."
            the_person.char "Ok, great!"
            "[the_person.title] takes your information and money."
            $ mc.business.change_funds(-500)
            the_person.char "I'll make sure it gets delivered out to your business right away!"
            $ quest_essential_oils.set_quest_flag(101)
            $ quest_essential_oils.quest_completed()
        "Invoice":
            mc.name "I don't have that amount of money on me. Could you please invoice my business?"
            the_person.char "Sure, I can do that. Accounts to be payable in no less than one week, of course."
            "[the_person.title] takes your information."
            the_person.char "I'll make sure it gets delivered out to your business right away!"
            $ quest_essential_oils.set_quest_flag(102)
            $ add_quest_essential_oils_invoice()
        "Too pricey":
            mc.name "Wow... $500? You know what, this was a mistake. I'm sorry to bother you."
            the_person.char "Okay, your loss!"
            $ quest_essential_oils.set_quest_flag(49)
            $ quest_essential_oils.quest_completed()
            return
    $ clear_scene()
    #$ add_essential_oil_serum_trait()
    $ list_of_traits.append(essential_oil_trait)
    $ quest_essential_oils_cleanup()
    if mc.business.head_researcher is None:
        # we fired the head researcher, so we don't bother checking in with them.
        return
    "You step away from the kiosk. You give your head researcher a call."
    mc.business.head_researcher.char "Hello?"
    mc.name "Hey, I've procured an order of essential oils. They should be delivered sometime today."
    mc.business.head_researcher.char "Okay. If you want to research a new serum that uses them, let me know, we should be able to start developing one ASAP."
    "You hang up the phone. You now have access to the Essential Oils serum trait. It has a high value, but no positive effects and high chance of a negative side effect."
    return

label quest_essential_oils_abandon_label():
    "It's been over a week now since you started considering adding essential oil as a serum trait. The more you think about it, the dumber it sounds."
    "You a run a legitimate pharmaceutical business, theres no room for that bullshit around here."
    "You decide just to scrap the whole idea."
    $ quest_essential_oils.set_quest_flag(99)
    $ quest_essential_oils.quest_completed()
    return

label quest_essential_oils_invoice_label():
    "You get an invoice to your business for the essential oils you purchased."
    "You write a check and drop it in the mailbox."
    $ mc.business.change_funds(-500)
    $ quest_essential_oils.quest_completed()
    return


init python:
    def essential_oil_function_on_apply(the_person, add_to_log):
        the_person.change_happiness(5)
        return

    def essential_oil_function_on_remove(the_person, add_to_log):
        the_person.change_happiness(-5)
        return


    essential_oil_trait = SerumTrait(name = "Essential Oils",
            desc = "Pleasant smell and texture adds greatly to the value of the serum. High chance of negative side effect.",
            positive_slug = "+$50 Value, +5 Happiness",
            negative_slug = "+20 Serum Research",
            value_added = 50,
            research_added = 20,
    #     slots_added = a_number,
    #     production_added = a_number,
    #     duration_added = a_number,
            base_side_effect_chance = 150,
            on_apply = essential_oil_function_on_apply,
            on_remove = essential_oil_function_on_remove,
    #     on_turn = ovulation_function_on_turn,
    #     on_day = a_function,
    #     requires = [list_of_other_traits],
            tier = 0,
            start_researched =  True,
            research_needed = 1500,
    #     exclude_tags = [list_of_other_tags],
    #     is_side_effect = a_bool)
        )
