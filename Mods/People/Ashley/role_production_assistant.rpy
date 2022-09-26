#Production assistant helps MC create serum batches for personal consumption.
#Serum modifiers are unlocked after specific serum traits are researched and master to a specific mastery level to minimize the odds of side effects.
#This role starts initially being filled by Ashley, but if it becomes vacant via the storyline or other means, it can be filled by another girl.

init 1 python:
    #Action List
    mc_serum_intro = Action("Discover MC Serums",mc_serum_intro_requirement,"mc_serum_intro_label")
    mc_serum_timeout = Action("Serums runout",mc_serum_timeout_requirement,"mc_serum_timeout_label")
    mc_serum_review = Action("Review Personal Serums",mc_serum_review_requirement,"mc_serum_review_label", menu_tooltip = "Review your personal serum options, research progress, and refresh your dose.")
    prod_assistant_essential_oils_intro = Action("Essential Oils Intro",prod_assistant_essential_oils_intro_requirement,"prod_assistant_essential_oils_intro_label")
    quest_essential_oils_research_start = Action("Essential Oil Research", quest_essential_oils_research_start_requirement, "quest_essential_oils_research_start_label")
    quest_essential_oils_research_end = Action("Essential Oil Outcome", quest_essential_oils_research_end_requirement, "quest_essential_oils_research_end_label")
    quest_essential_oils_discover_supplier = Action("Find a Supplier", quest_essential_oils_discover_supplier_requirement, "quest_essential_oils_discover_supplier_label")
    quest_essential_oils_decision = Action("Talk to Supplier", quest_essential_oils_decision_requirement, "quest_essential_oils_decision_label")
    prod_assistant_unlock_auras = Action("Unlock Aura Personal Serums",prod_assistant_unlock_auras_requirement,"prod_assistant_unlock_auras_label")
    prod_assistant_unlock_cum = Action("Unlock Cum Personal Serums",prod_assistant_unlock_cum_requirement,"prod_assistant_unlock_cum_label")
    prod_assistant_unlock_physical = Action("Unlock Physical Personal Serums",prod_assistant_unlock_physical_requirement,"prod_assistant_unlock_physical_label")
    prod_assistant_performance_upgrade = Action("Upgrade Performance Serums",prod_assistant_performance_upgrade_requirement,"prod_assistant_performance_upgrade_label")
    prod_assistant_aura_upgrade = Action("Upgrade Aura Serums",prod_assistant_aura_upgrade_requirement,"prod_assistant_aura_upgrade_label")
    prod_assistant_cum_upgrade = Action("Upgrade Cum Serums",prod_assistant_cum_upgrade_requirement,"prod_assistant_cum_upgrade_label")
    prod_assistant_physical_upgrade = Action("Upgrade Physical Serums",prod_assistant_physical_upgrade_requirement,"prod_assistant_physical_upgrade_label")

    #The role
    prod_assistant_role = Role("Production Assistant", [mc_serum_review])

#Requirement functions
init -1 python:
    def mc_serum_intro_requirement(the_person):
        if mc.business.days_since_event("prod_assistant_advance") > TIER_2_TIME_DELAY:
            if mc.business.is_open_for_business() and mc.is_at_work():
                the_serum = find_in_list(lambda x: x.name == mc_serum_energy_regen.linked_trait, list_of_traits)
                return the_serum.researched
        return False

    def mc_serum_timeout_requirement():
        if mc.business.days_since_event("prod_assistant_advance") > get_mc_serum_duration():
            return True
        return False

    def mc_serum_review_requirement(the_person):
        if mc.business.event_triggers_dict.get("mc_serum_energy_unlocked", False) and mc.business.is_open_for_business():
            return True
        return False

    def prod_assistant_essential_oils_intro_requirement(the_person):
        if mc.business.is_open_for_business() and mc.business.days_since_event("prod_assistant_advance") > TIER_2_TIME_DELAY:
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
                if mc.business.days_since_event("essential_oils_research_start") > TIER_2_TIME_DELAY:
                    return True
        return False

    def quest_essential_oils_discover_supplier_requirement(the_person):
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                return True
        return False

    def quest_essential_oils_decision_requirement(the_person):
        if time_of_day > 0 and time_of_day < 4:
            return True
        return False

    def prod_assistant_unlock_auras_requirement(the_person):
        if mc.business.is_open_for_business():
            if mc.is_at_work() and mc.business.days_since_event("prod_assistant_advance") >= TIER_1_TIME_DELAY:
                return True
        return False

    def prod_assistant_unlock_cum_requirement(the_person):
        if mc.business.is_open_for_business() and the_person.sluttiness > 40:
            if mc.is_at_work() and mc.business.days_since_event("prod_assistant_advance") >= TIER_2_TIME_DELAY:
                return True
        return False

    def prod_assistant_unlock_physical_requirement(the_person):
        if mc.business.is_open_for_business() and the_person.obedience > 140:
            if mc.is_at_work() and mc.business.days_since_event("prod_assistant_advance") >= TIER_2_TIME_DELAY:
                return True
        return False

    def prod_assistant_performance_upgrade_requirement(the_person):
        if mc.business.is_open_for_business() and mc.business.research_tier >= 2:
            if mc.is_at_work() and mc.business.days_since_event("prod_assistant_advance") >= TIER_2_TIME_DELAY and not mc_serum_energy_serum_is_active():
                return True
        return False

    def prod_assistant_aura_upgrade_requirement(the_person):
        if mc.business.is_open_for_business() and mc.business.research_tier >= 2:
            if mc.is_at_work() and mc.business.days_since_event("prod_assistant_advance") >= TIER_2_TIME_DELAY and not mc_serum_aura_serum_is_active():
                return True
        return False

    def prod_assistant_cum_upgrade_requirement(the_person):
        if mc.business.is_open_for_business() and mc.business.research_tier >= 3:
            if mc.is_at_work() and mc.business.days_since_event("prod_assistant_advance") >= TIER_2_TIME_DELAY and not mc_serum_cum_serum_is_active():
                return True
        return False

    def prod_assistant_physical_upgrade_requirement(the_person):
        if mc.business.is_open_for_business() and mc.business.research_tier >= 2:
            if mc.is_at_work() and mc.business.days_since_event("prod_assistant_advance") >= TIER_2_TIME_DELAY and not mc_serum_physical_serum_is_active():
                return True
        return False


label mc_serum_intro_label(the_person):
    $ the_person.draw_person()
    "You step into the production lab. As you are walking in, [the_person.possessive_title] is just walking out."
    the_person "Oh hey [the_person.mc_title], great timing. I was just getting coffee... do you want some?"
    mc.name "Oh, sure I could do that."
    the_person "How do you like it?"
    mc.name "Just black is fine."
    the_person "Alright."
    $ clear_scene()
    "She disappears out the door, headed toward the break room. You walk around the production room for a minute, checking up on the serum processing."
    "After you make a round, [the_person.title] reappears with two cups of coffee."
    $ the_person.draw_person()
    the_person "Here we go! Hey, have a few minutes? I wanted to talk to you about something."
    mc.name "Sure."
    $ the_person.draw_person(position = "sitting")
    "You sit down at [the_person.possessive_title]'s desk across from her and start to chat."
    "She talks with you for a while about how she is settling in and how much she appreciates you hiring her."
    "You drink your coffee fairly quickly. It is a nice to take a break from work and you feel re-energized."
    $ mc.change_energy(50)
    $ mc_serum_energy_regen.apply_trait()
    "As you finish up with your coffee, she changes the subject."
    if ashley_on_default_path() and the_person == ashley:
        the_person "So I was talking with Steph about how things are going here at work."
        the_person "She was just gushing all about how her 'boyfriend' built her a special room just for her science work."
    else:
        the_person "So I was talking with the head researcher about how things are going with me settling in here."
        the_person "She was going on and on about the specialized research room you built over in the lab."
    the_person "And of course, as we were talking, I had to ask her the obvious question..."
    the_person "These serums we keep making... they are designed entirely to be used by, and tested on, women."
    the_person "Why not work on similar designs to be used on men?"
    mc.name "Ah, well, there are a number of reasons..."
    the_person "Yeah, yeah I'm sure there are... But I asked her, why don't you ever test any of these serums?"
    the_person "I mean, some of these have some amazing effects..."
    mc.name "Well, I'm the owner of the business, and the business itself is built on marketing the serums to a specific demographic..."
    "[the_person.title] rolls her eyes."
    the_person "Yeah, she gave me a similar excuse. But why not? If we made something here that would be beneficial for you, specifically, why not try it?"
    mc.name "I guess I would certainly consider it, but I wouldn't want that to be the main focus for the employees here."
    the_person "Let me put it this way. If I made a serum, with help from the research department, for you, would you try it?"
    mc.name "I mean, I would need some assurances that some basic safeguards are in place..."
    the_person "Like the safeguards you put in place for the employees you are testing serums on?"
    mc.name "Look. I understand you have some concerns about the way things are done here, but..."
    the_person "So that's a no?"
    mc.name "No."
    "[the_person.possessive_title] shakes her head."
    the_person "That's too bad. I figured you would say that. But fortunately, science stops for no man."
    mc.name "I'm not going to take one..."
    the_person "That's okay! You already have!"
    "... You look down at your empty coffee with a sudden realization. Holy shit, this bitch just used your own tactic against you?"
    the_person "Hey! Don't look at me like that! The coffee has you feeling good, doesn't it? Almost... re-energized?"
    mc.name "I... actually yeah, I do feel like I have more energy."
    "[the_person.title] smiles wide."
    the_person "There, see? All I did was adapt the caffeine infusion trait for your much more manly body."
    the_person "That burst of energy you got from the coffee? I think it should actually last a few days."
    "You are still a bit shocked by the revelation that [the_person.possessive_title] dosed you without your knowledge..."
    mc.name "Okay... we'll see how this one goes, okay?"
    mc.name "But I don't want you to spend all your work time on it, this is just a side project."
    the_person "Yes! Don't worry, this is gonna be great."
    "Yeah. Great... Great for who though?"
    mc.name "Alright. Get back to work, I'm going to do the same."
    the_person "You got it boss!"
    $ clear_scene()
    $ mc.business.add_mandatory_crisis(mc_serum_timeout)
    "You get up and step out of the serum production area."
    "You definitely feel conflicted about what just happened... but you have to admit, the prospect of getting your hands on serums that would enhance your personal performance is tempting."
    "You decide to go along with it for now, but you definitely need to keep a closer eye on [the_person.possessive_title] and her activities."
    $ mc.business.set_event_day("prod_assistant_advance", override = True)
    return

label mc_serum_timeout_label():
    "Something about you feels different. You have... less energy?"
    "The serum that [mc.business.prod_assistant.possessive_title] gave you must have worn off."
    "Maybe you should talk to her about getting another dose? It definitely had a positive effect on you."
    $ mc.business.event_triggers_dict["mc_serum_energy_unlocked"] = True
    $ mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_performance_upgrade)
    $ mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_essential_oils_intro)
    $ mc.business.set_event_day("prod_assistant_advance", override = True)
    return

label mc_serum_review_label(the_person):
    mc.name "I want to discuss my personal serums."
    the_person "Okay, let me see if I have any updated serum formulas."
    call mc_serum_review_upgrades_label(the_person) from _serum_review_upgrades_01
    the_person "The serums themselves have limited duration as well."
    call mc_serum_review_duration_label(the_person) from _serum_review_duration_01
    the_person "We also can only give you so many serums at a time safely."
    call mc_serum_review_quantity_label(the_person) from _serum_review_quantity_01
    the_person "Alright, here are the serums that I have available."
    call screen mc_personal_serum_screen()
    mc.name "Thank you [the_person.title]. Keep up the good work."
    return

label mc_serum_review_upgrades_label(the_person):
    $ list_of_upgrades = mc_serum_list_of_upgradable_serums()
    if len(list_of_upgrades) == 0:
        the_person "Looks like we don't have any updated serum formulas right now."
    else:
        python:
            for trait in list_of_upgrades:
                trait.upgrade_with_string(the_person)
                list_of_upgraded_mc_serums.append(trait.name)
    return

label mc_serum_review_duration_label(the_person):
    if get_mc_serum_duration() == 3:
        $ the_serum = find_in_list(lambda x: x.name == "Improved Reagent Purification", list_of_traits)
        if the_serum.mastery_level >= 3.0:
            call prod_assistant_increase_duration_1_label(the_person) from _prod_assist_increase_duration_01
        else:
            the_person "Right now, we expect your serums to last about three days."
            the_person "If we work on researching and mastering duration enhancing traits, I think we could extend this to be longer."
    elif get_mc_serum_duration() == 5:
        $ the_serum = find_in_list(lambda x: x.name == "Low Volatility Reagents", list_of_traits)
        if the_serum.mastery_level >= 3.0:
            call prod_assistant_increase_duration_2_label(the_person) from _prod_assist_increase_duration_02
        else:
            the_person "Right now, we expect your serums to last about five days."
            the_person "If we work on researching and mastering more duration enhancing traits, I think we could extend this to be even longer."
    else:
        the_person "Right now, we expect your serums to last about seven days."
        the_person "I'm not sure they can be extended longer than that safely, but maybe someday I'll be proven wrong."
    return

label mc_serum_review_quantity_label(the_person):
    if mc_serum_max_quantity() == 1:
        $ the_serum = find_in_list(lambda x: x.name == "Improved Serum Production", list_of_traits)
        if the_serum.mastery_level >= 3.0:
            call prod_assistant_increase_production_1_label(the_person) from _prod_assist_increase_production_01
        else:
            the_person "Right now, we can only safely give you one serum at a time."
            the_person "If we work on researching and mastering production traits, we could probably give you more than one serum at the same time."
    elif mc_serum_max_quantity() == 2:
        $ the_serum = find_in_list(lambda x: x.name == "Advanced Serum Production", list_of_traits)
        if the_serum.mastery_level >= 3.0:
            call prod_assistant_increase_production_2_label(the_person) from _prod_assist_increase_production_02
        else:
            the_person "Right now, we can only safely give you two serums at a time."
            the_person "If we work on researching and mastering production traits, we could probably give you more serums at the same time."
    elif mc_serum_max_quantity() == 3:
        $ the_serum = find_in_list(lambda x: x.name == "Futuristic Serum Production", list_of_traits)
        if the_serum.mastery_level >= 3.0:
            call prod_assistant_increase_production_3_label(the_person) from _prod_assist_increase_production_03
        else:
            the_person "Right now, we can safely give you three serums at a time."
            the_person "If we work on researching and mastering production traits, we could probably give you even more serums at the same time."

    else:
        the_person "Right now, we can safely give you four serums at a time."
        the_person "I think this is about the limit of how many serums you can take simultaneously."
    return

label prod_assistant_essential_oils_intro_label(the_person):
    "As you walk into the production area, a very strange mixture of smells enter your nostrils."
    "You are having trouble placing the smell... Is there a chemical leak somewhere!?!"
    "You quickly scan the room. You notice [the_person.title] at a desk... with a strange chemical diffuser sitting next to her?"
    $ the_person.draw_person(position = "sitting")
    "You walk over. The smell is definitely coming from the diffuser."
    mc.name "[the_person.title]... can I ask what you are diffusing into the room?"
    the_person "Oh! Hello [the_person.mc_title]! Yeah I was having some trouble concentrating, so I got out my essential oil diffuser."
    "She can't be serious..."
    the_person "It's my own personal mix of peppermint, rosemary, and lemon oils! Really helps me... Ahhhh ha ha ha ha I'm just kidding."
    the_person "Can you believe that people actually buy this stuff?"
    "You take another whiff... the smell is very confusing. And personally you find it a bit distracting."
    mc.name "Well, I don't think it is a good idea to be diffusing that around here. We have a lot of chemicals we store in the building, and for a minute I thought we had a leak or spill."
    the_person "Oh, yes sir! Don't worry, this batch is almost out anyway. This stuff is so expensive. Actually, you would be surprised how much money people spend on this garbage!"
    "Hmmm... expensive?"
    mc.name "So, this is something people pay a lot of money for? These, essential oils?"
    the_person "Yeah, the whole thing is nuts. I had a shop owner at the mall pawn these off on me as a free sample the other day, but they are crazy expensive."
    the_person "Some people diffuse them, rub them on their skin, even take them orally."
    mc.name "That's interesting. So you can take them orally? And they are perfectly safe?"
    the_person "Yeah, from what I've seen, they don't do a thing if taken orally. Good or bad."
    "You consider this for a moment. Maybe this is something you could use?"
    the_person "You know what you could do? Take some to [mc.business.head_researcher.fname]. I bet she could figure out how to make a serum trait out of them."
    the_person "You could probably use them to help turn a significant profit."
    mc.name "That's a good idea."
    the_person "Here, take these. I was just trying to annoy the other girls with them anyway, but it doesn't seem to be having much of an effect on them."
    $ mc.business.head_researcher.add_unique_on_talk_event(quest_essential_oils_research_start)
    "You take the essential oils from [the_person.title]. You should take them to your head researcher."
    return

label quest_essential_oils_research_start_label(the_person):
    $ the_person.draw_person()
    "You greet your head researcher."
    mc.name "Hello, I have a quick question for you. Have you ever heard of essential oils?"
    the_person "Oh god, don't start with that bullshit..."
    mc.name "Right, well, I was talking to another employee, and apparently there are people out there who will pay big money for them."
    the_person "There's a sucker born every minute, or so I've heard."
    mc.name "So... would it be possible to create a serum trait using essential oils? Not to do anything meaningful, but as a way of driving up the price."
    "[the_person.title] stops and considers what you are saying for a moment."
    the_person "I... think so? I don't know if there's any major negative side effects associated with them. I could look into it the next couple of days and get back to you."
    mc.name "Perfect. Let me know what you find out."
    the_person "Okay. Is there anything else I can do you for you?"
    $ mc.business.head_researcher.add_unique_on_talk_event(quest_essential_oils_research_end)
    $ mc.business.set_event_day("essential_oils_research_start", override = True)
    return

label quest_essential_oils_research_end_label(the_person):
    $ the_person.draw_person()
    the_person "Hey [the_person.mc_title]. Just the man I was hoping to see. I did some research on those essential oils you were asking about."
    mc.name "And?"
    the_person "Well, they are mostly related to placebo effect. People think they work, so they imagine they feel better or whatever else after they use them."
    the_person "Most of them also have some sort of negative side effect, but they are all mostly benign. It wouldn't be too hard to make a serum trait like you were asking."
    mc.name "That's great, that is exactly what I was hoping to hear."
    the_person "Just to give you a heads up though. Some of those oils are hard to extract, and for our company we would need to buy them in pretty bulk sizes..."
    mc.name "Hmm, so I may need to find a supplier."
    the_person "Yup! Sorry, I don't know where you could source this stuff. Here's a list of which ones would be appropriate for us to use."
    mc.name "Thanks, that's exactly what I needed."
    "It was [mc.business.prod_assistant.possessive_title] that suggested it in the beginning. Maybe she can tell you where to get more from?"
    $ mc.business.prod_assistant.add_unique_on_talk_event(quest_essential_oils_discover_supplier)
    return

label quest_essential_oils_discover_supplier_label(the_person):
    $ the_person.draw_person()
    mc.name "Hello, I have a quick question for you."
    the_person "Yeah [the_person.mc_title]?"
    mc.name "Those oils you had the other day in here. Where did you get them from?"
    the_person "Well, I get mine from over at the mall. I like to hang out there on the weekend sometimes. The one I got is from the weird lifestyle coach lady.."
    mc.name "Do you remember her name?"
    "She thinks about it for a minute."
    the_person "Yes, I'm pretty sure her name is [camilla.fname]. She has a small kiosk setup in the mall itself."
    mc.name "Thank you."
    the_person "Yup! Anything else I can do for you?"
    $ camilla.add_unique_on_talk_event(quest_essential_oils_decision)
    return

label quest_essential_oils_decision_label(the_person):
    $ mc.business.set_event_day("prod_assistant_advance", override = True)
    mc.name "I have an employee who told me she got some essential oils from you. Would you happen to be able to procure a bulk order?"
    the_person "Oh? How big are we talking?"
    mc.name "Well, I am interested in using them in a small run of pharmaceuticals I am developing."
    the_person "Ah, I could set you up with a gallon size for now? A little bit of these things go a long way!"
    mc.name "That sounds good. Here is a list of the ones I need."
    "You hand her the list from your researcher."
    the_person "Okay, I'll need $500 to cover the cost. Do you want to do that up front? Or should I invoice it?"
    mc.name "I'll pay it all now. I have the cash on me."
    the_person "Ok, great!"
    "[the_person.title] takes your information and money."
    $ mc.business.change_funds(-500)
    the_person "I'll make sure it gets delivered out to your business right away!"

    $ clear_scene()
    #$ add_essential_oil_serum_trait()
    $ list_of_traits.append(essential_oil_trait)
    $ mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_unlock_auras)
    if mc.business.head_researcher is None:
        "You now have access to the Essential Oils serum trait. It has a high value, but no positive effects and high chance of a negative side effect."
        # we fired the head researcher, so we don't bother checking in with them.
        return
    "You step away from the kiosk. You give your head researcher a call."
    mc.business.head_researcher "Hello?"
    mc.name "Hey, I've procured an order of essential oils. They should be delivered sometime today."
    mc.business.head_researcher "Okay. If you want to research a new serum that uses them, let me know, we should be able to start developing one ASAP."
    "You hang up the phone. You now have access to the Essential Oils serum trait. It has a high value, but no positive effects and high chance of a negative side effect."
    return

label prod_assistant_unlock_auras_label(the_person):
    "You walk into the production room. When you do, [the_person.possessive_title] notices you and waves you over to her desk."
    $ the_person.draw_person()
    $ mc.business.event_triggers_dict["mc_serum_aura_unlocked"] = True
    the_person "Hey [the_person.mc_title]. I heard about the essential oils. I'm sure they will help out with business profitability!"
    the_person "Dealing with them made me get curious a bit. Would it be possible to replicate the supposed results of essential oils?"
    the_person "Essential oils are obviously umm... shall we say... bogus... but do you know what aren't? Pheremones."
    mc.name "Right, the natural chemicals a person puts out that can act as signal markers to people around them."
    the_person "Exactly. Science has done some studies on their effects on various mammals, but effects on humans are notoriously hard to conduct studies on..."
    the_person "Anyway, with some of the research we've been doing on various pheremones, I think it is possible to make a serum for you that would modify your personal pheremone signature."
    if mc_serum_aura_obedience.get_unlocked():
        the_person "I have a prototype for one that I think might make women near you... how do you say... more obedient."
        mc.name "That does sound useful..."
        the_person "Let me know if you want to give it a try."
        "You have unlocked Personal Aura serums! These serums effect girls around you with every passage of time."
    else:
        the_person "I haven't come up with a prototype yet, but I think with some more research into other traits it might be something worth pursuing."
        mc.name "That does sound useful. Let me know if you come up with something."
        "You have unlocked Personal Aura serums! These serums effect girls around you with every passage of time."
        "Check the serum review screen for information on what to research to enable them!"
    $ mc.business.set_event_day("prod_assistant_advance", override = True)
    $ mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_aura_upgrade)
    $ the_person.add_unique_on_room_enter_event(prod_assistant_unlock_cum)
    return

label prod_assistant_unlock_cum_label(the_person):
    "Production assistant has an idea. What if we put a concentrated pheremones into MC's cum."
    "Has a method that should be able to accomplish this."
    "Unlocks cum MC serums."
    $ mc.business.event_triggers_dict["mc_serum_cum_unlocked"] = True
    $ mc.business.set_event_day("prod_assistant_advance", override = True)
    $ mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_cum_upgrade)
    $ the_person.add_unique_on_room_enter_event(prod_assistant_unlock_physical)
    return

label prod_assistant_unlock_physical_label(the_person):
    "Production assistant comments that some of your serums are now altering many girls physical properties."
    "Asks if MC would be interested in trying some of the beneficial ones."
    "Unlocks physical MC serums."
    $ mc.business.event_triggers_dict["mc_serum_physical_unlocked"] = True
    $ mc.business.prod_assistant.add_unique_on_room_enter_event(prod_assistant_physical_upgrade)
    $ mc.business.set_event_day("prod_assistant_advance", override = True)
    return

label prod_assistant_performance_upgrade_label(the_person):
    "Use this label to start to process of upgrading performance serums."
    "In this label, the production assistant discusses recent progression with performance related serums."
    "All performance related serums increase in tier by 1 after this label."
    $ mc.business.event_triggers_dict["mc_serum_energy_tier"] = 1
    $ mc.business.set_event_day("prod_assistant_advance", override = True)
    return

label prod_assistant_aura_upgrade_label(the_person):
    "Use this label to start to process of upgrading aura serums."
    "In this label, the production assistant discusses recent progression with aura related serums."
    "All aura related serums increase in tier by 1 after this label."
    $ mc.business.event_triggers_dict["mc_serum_aura_tier"] = 1
    $ mc.business.set_event_day("prod_assistant_advance", override = True)
    return

label prod_assistant_cum_upgrade_label(the_person):
    "Use this label to start to process of upgrading cum serums."
    "In this label, the production assistant discusses recent progression with cum related serums."
    "All performance related serums increase in tier by 1 after this label."
    $ mc.business.event_triggers_dict["mc_serum_cum_tier"] = 1
    $ mc.business.set_event_day("prod_assistant_advance", override = True)
    return

label prod_assistant_physical_upgrade_label(the_person):
    "Use this label to start to process of upgrading physical serums."
    "In this label, the production assistant discusses recent progression with physical related serums."
    "All physical related serums increase in tier by 1 after this label."
    $ mc.business.event_triggers_dict["mc_serum_physical_tier"] = 0
    $ mc.business.set_event_day("prod_assistant_advance", override = True)
    return

label prod_assistant_increase_duration_1_label(the_person):
    "This is an outline label."
    "In this label, [the_person.title] explains that after research, the serums she gives MC now last an additional 2 days, total of 5 days."
    $ mc.business.event_triggers_dict["mc_serum_duration"] = 5
    return

label prod_assistant_increase_duration_2_label(the_person):
    "This is an outline label."
    "In this label, [the_person.title] explains that after research, the serums she gives MC now last an additional 2 days, total of 7 days."
    $ mc.business.event_triggers_dict["mc_serum_duration"] = 7
    return

label prod_assistant_increase_production_1_label(the_person):
    "This is an outline label."
    "In this label, [the_person.title] explains that after research, MC can now take 2 serums at the same time."
    $ mc.business.event_triggers_dict["mc_serum_max_quant"] = 2
    return

label prod_assistant_increase_production_2_label(the_person):
    "This is an outline label."
    "In this label, [the_person.title] explains that after research, MC can now take 3 serums at the same time."
    $ mc.business.event_triggers_dict["mc_serum_max_quant"] = 3
    return

label prod_assistant_increase_production_3_label(the_person):
    "This is an outline label."
    "In this label, [the_person.title] explains that after research, MC can now take 4 serums at the same time."
    $ mc.business.event_triggers_dict["mc_serum_max_quant"] = 4
    return
