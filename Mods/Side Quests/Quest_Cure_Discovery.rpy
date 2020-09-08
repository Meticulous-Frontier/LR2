#Anytime game quest. Available immediately, requires lab leader and at least 1 person in marketing. Gains potency as the game progresses.
#MC and science leader discover cure for some disease.
#At low tier research, discover cure for some obscure disease
#Higher tiers, discover cure for high profile diseases.
#MC realizes he is not equipped to handle production of the drug. Work with marketing to sell patent rights.
#Patent rights sold gives extra cash based on what disease was cured. Should be significant but not OP sum.

# flags
# 1: Quest has been initiated
# 9: If at any point during the quest we fire the head researched. (BAD END)
# 11: Science leader contacts MC, informs him that she stumbled on cure for disease. X
# 18: MC decides to try and keep them all for himself to manufacture small scale.
# 19: MC discovers girl secretly donated drug to large pharma company. (BAD END)
# 21: MC decides to try and sell patent for the drug. Decides to work with someone from marketing.
# 29: After 7 days, if MC hasn't initiated sale with marketing, MC discovers large PHARMA company just announced cure. His cure is worthless (BAD END)
# 31: Talked to marketing about trying to sell patent rights.
# 101: A few days later, marketing returns and gives MC details on selling the patent rights. Payout!

init 1 python:
    def setup_quest_cure_discovery():
        quest_cure_discovery.quest_event_dict["start_day"] = 9999
        quest_cure_discovery.quest_event_dict["cure_tier"] = mc.business.research_tier  #Snapshot quest tier at the beginning.
        quest_cure_discovery.quest_event_dict["disease_name"]  = quest_cure_discovery_disease_name()
        quest_cure_discovery.quest_event_dict["market_contact"] = get_random_from_list(mc.business.market_team)
        quest_cure_discovery.quest_event_dict["market_day"] = 9999
        #TODO add start event
        quest_cure_discovery.set_quest_flag(1)
        mc.business.mandatory_crises_list.append(quest_cure_discovery_intro)
        game_hints.append(Hint("Medical Breakthrough", "Your head researcher has some exciting news.", "quest_cure_discovery.get_quest_flag() <= 1", "quest_cure_discovery.get_quest_flag() > 1"))
        hint_string = "Talk to " + quest_cure_get_market_contact().title + " about selling your medical patent."
        game_hints.append(Hint("Medical Breakthrough", hint_string, "quest_cure_discovery.get_quest_flag() == 21", "quest_cure_discovery.get_quest_flag() != 21"))
        game_hints.append(Hint("Medical Breakthrough", "Wait for your patent rights to sell", "quest_cure_discovery.get_quest_flag() == 31", "quest_cure_discovery.get_quest_flag() != 31"))

        return

    def quest_cure_get_market_contact():
        return quest_cure_discovery.quest_event_dict.get("market_contact", None)

    def quest_cure_set_market_contact(person):
        quest_cure_discovery.quest_event_dict["market_contact"] = person

    def quest_cure_discovery_disease_name():
        if mc.business.research_tier == 0:
            return "Rabies"
        elif mc.business.research_tier == 1:
            return "Dengue fever"
        elif mc.business.research_tier == 2:
            return "Crohn's disease"
        else:
            return "Parkinson's disease"

#Quest defining functions
    def quest_cure_discovery_tracker():

        if quest_cure_discovery.get_quest_flag() <= 101 and quest_cure_discovery.get_quest_flag() > 1:
            if quest_cure_get_market_contact() == None: #We lose our marketing contact
                quest_cure_discovery.quest_completed()

        return

    def quest_cure_discovery_start_requirement():
        if day < 30: # we need to have put in some research for this event to occur
            return False
        if mc.business.head_researcher == None:
            return False
        if __builtin__.len(mc.business.market_team) == 0:
            return False
        return True

    def quest_cure_discovery_cleanup():
        remove_mandatory_crisis_list_action("quest_cure_discovery_intro_label")
        remove_mandatory_crisis_list_action("quest_cure_discovery_market_patent_label")
        remove_mandatory_crisis_list_action("quest_cure_discovery_patent_sold_label")
        remove_mandatory_crisis_list_action("quest_cure_discovery_patent_kept_label")
        remove_mandatory_crisis_list_action("quest_cure_discovery_market_missed_label")
        if quest_cure_get_market_contact():
            quest_cure_get_market_contact().remove_on_talk_event(quest_cure_discovery_market_patent)
        quest_cure_discovery.quest_event_dict.clear()
        return



#Label requirement functions
    def quest_cure_discovery_intro_requirement():
        if mc.business.is_open_for_business(): #Only trigger if people are in the office.
            return True
        return False

    def quest_cure_discovery_market_patent_requirement(the_person):
        if mc.business.is_open_for_business():
            if the_person.location() == the_person.work:
                return True #Only while she is at work
        return False

    def quest_cure_discovery_patent_sold_requirement():
        if day >= quest_cure_discovery.quest_event_dict.get("market_day", 0) + 3:
            if mc.business.is_open_for_business():
                return True
        return False

    def quest_cure_discovery_patent_kept_requirement():
        if day >= (quest_cure_discovery.quest_event_dict.get("start_day", 9999) + 1):
            if mc.business.is_open_for_business(): # only during office hours and we are at work (dialog depends on it)
                if mc.is_at_work():
                    if time_of_day > 0:
                        return True
        return False

    def quest_cure_discovery_market_missed_requirement():
        if day >= (quest_cure_discovery.quest_event_dict.get("start_day", 9999) + 7) : #One week to talk to marketing
            if time_of_day == 4:
                return True
        return False


    #Action declarations

    quest_cure_discovery_intro = Action("Begin Cure Discovery Quest", quest_cure_discovery_intro_requirement, "quest_cure_discovery_intro_label")
    quest_cure_discovery_market_patent = Action("Attempt to sell patent", quest_cure_discovery_market_patent_requirement, "quest_cure_discovery_market_patent_label")
    quest_cure_discovery_patent_sold = Action("Patent Sold", quest_cure_discovery_patent_sold_requirement, "quest_cure_discovery_patent_sold_label")
    quest_cure_discovery_patent_kept = Action("Patent Stolen", quest_cure_discovery_patent_kept_requirement, "quest_cure_discovery_patent_kept_label")
    quest_cure_discovery_market_missed = Action("Patent Worthless", quest_cure_discovery_market_missed_requirement, "quest_cure_discovery_market_missed_label")

#Quest Labels
label quest_cure_discovery_init_label():
    $ setup_quest_cure_discovery()
    return

label quest_cure_discovery_intro_label():
    $ the_person = mc.business.head_researcher
    $ the_disease = quest_cure_discovery.quest_event_dict.get("disease_name", "Rabies")
    $ quest_cure_discovery.quest_event_dict["start_day"] = day
    if the_person == None:
        return #Bad end
    if mc.location != rd_division:
        "You get a text on your phone. It's from [the_person.possessive_title]."
        the_person.char "Hey, I need to see you in the lab ASAP!"
        "You quickly head to the lab."
        $ mc.change_location(rd_division)
        $ mc.location.show_background()

    $ the_person.draw_person()
    the_person.char "Hey! I need to talk to you about something."
    mc.name "What is it?"
    the_person.char "I was doing some research for a new serum trait. I was testing the effects on some rats in the lab, when I noticed something incredible."
    the_person.char "I had some rats that have [the_disease]. After giving them the serum, they showed no signs of the disease in less than 12 hours!"
    mc.name "That's... interesting?"
    the_person.char "I thought so too, so I ran a bunch more tests. In 99.8 percent of tests I ran, the disease appears to be completely cured!"
    mc.name "Is that something that could be adapted to humans?"
    the_person.char "This would be the first step in researching a cure! I already filed a patent for the business on the formula."
    mc.name "That's great... but could we realistically manufacture that here?"
    "She considers your question for a moment."
    the_person.char "Realistically... not really. Not in the numbers that would be needed to have it available to large numbers of people."
    mc.name "Hmm, that's a shame."
    the_person.char "Maybe you could... I don't know... sell the patent? To a larger pharmaceutical company? One that could make it in the quantity needed to meet worldwide demand?"
    mc.name "That's an interesting idea..."
    menu:
        "Keep the secret for your company":
            mc.name "It might take us some time, but I think we could ramp up production here to meet demand."
            $ the_person.draw_person(emotion = "angry")
            the_person.char "But sir! That would take... months? Or more?"
            mc.name "So?"
            the_person.char "Think of all the people out there, suffering right now. Surely it would be better for us to just sell the rights?"
            mc.name "No, I don't think so."
            $ the_person.change_stats(obedience = -10, love = -10, happiness = -20)
            "She really doesn't like your answer. Hopefully you haven't burned any bridges with your answer?"
            "As you turn to leave, you can hear her muttering something."
            $ del the_disease
            $ quest_cure_discovery.set_quest_flag(18)
            $ mc.business.mandatory_crises_list.append(quest_cure_discovery_patent_kept)
            return
        "Try and sell the patent":
            mc.name "Some cash infusion to the company would be great. That's a great idea, [the_person.title]."
    $ the_target = quest_cure_get_market_contact()
    the_person.char "Personally, I think you should talk to [the_target.name]. You know, over in marketing?"
    mc.name "Oh?"
    if the_target == alexia:
        the_person.char "She's a recent college graduate and seems to have a good handle on things over there. I bet she could manage it!"
        mc.name "Noted. I'm not sure I'll have to time, but I'll talk to her when I can."
    else:
        the_person.char "Yeah, I think she actually has experience doing something similar at a previous job. I bet she could help out!"
        mc.name "Noted. I'm not sure I'll have to time, but I'll talk to her when I can."
    the_person.char "If I were you, I'd get on it, quick! Modern day drug research is extremely fast paced. No telling when another lab might replicate our findings..."
    mc.name "Thank you, [the_person.title], for your research and for bringing this to my attention."
    "So... you should talk to [the_target.possessive_title] about selling your patent rights to the cure for [the_disease]."

    $ del the_disease
    $ quest_cure_set_market_contact(the_target)
    $ del the_target
    $ quest_cure_discovery.set_quest_flag(21)
    $ quest_cure_get_market_contact().add_unique_on_talk_event(quest_cure_discovery_market_patent)
    $ mc.business.mandatory_crises_list.append(quest_cure_discovery_market_missed)
    return

label quest_cure_discovery_market_patent_label(the_person):
    $ the_person.draw_person()
    $ the_disease = quest_cure_discovery.quest_event_dict.get("disease_name", "Rabies")
    mc.name "Hello [the_person.title], do you have a moment?"
    the_person.char "Of course. What can I do for you sir?"
    if the_person == alexia:
        mc.name "We made a big discovery in the research lab, but it is too big for our production department to handle. I was wondering if you could look into selling some patent rights."
        the_person.char "Oh? I think I could handle something like that. What is the patent for?"
        mc.name "Our research department made a discovery related to a possible treatment for [the_disease]."
    else:
        mc.name "Well, I heard that you might have some prior experience working with drug patent rights..."
        the_person.char "Yes sir! At my last job, I worked for a pharmaceutical investment company, buying and selling patent rights to all kinds of different drugs."
        mc.name "Wow, well, that is actually very useful. You see, our research department made a discovery related to a possible treatment for [the_disease]."
    the_person.char "Oh wow! There's currently some preventative drugs for that, but no known cure."
    mc.name "I know. I wish we had the production and testing capabilities here to take it to market, but unfortunately, we just don't."
    the_person.char "Aahhh, I see. So you want me to test the waters and see what I can get for the patent rights to the discovery?"
    mc.name "That's exactly right."
    the_person.char "Okay! I can do that. Give me a couple of days and I'll see what I can find!"
    mc.name "Thank you, [the_person.title]."
    $ quest_cure_set_market_contact(the_person)
    $ quest_cure_discovery.quest_event_dict["market_day"] = day
    $ del the_disease
    $ quest_cure_discovery.set_quest_flag(31)
    $ remove_mandatory_crisis_list_action("quest_cure_discovery_market_missed_label")
    $ mc.business.mandatory_crises_list.append(quest_cure_discovery_patent_sold)
    return

label quest_cure_discovery_patent_sold_label():
    $ the_disease = quest_cure_discovery.quest_event_dict.get("disease_name", "Rabies")
    $ the_person = quest_cure_get_market_contact()
    if the_person == None:
        return
    #TODO test to make sure market contact still works for us.
    "You get a text message from [the_person.title]."
    the_person.char "Hey there! I just got some good news on that patent you have for [the_disease]."
    mc.name "Glad to hear it. What is the news?"
    if quest_cure_discovery.quest_event_dict.get("cure_tier", 0) == 0:
        the_person.char "Well, [the_disease] has very few cases annually, so the prospects of a lucrative deal for the patent rights were pretty slim."
        the_person.char "After negotiating, I was able to sell them for $1500. I hope that is okay."
        $ mc.business.funds += 1500
        mc.name "I understand. That is still very helpful. Thank you [the_person.title]."
    elif quest_cure_discovery.quest_event_dict.get("cure_tier", 0) == 1:
        the_person.char "Well, [the_disease] really only propagates in poor, tropical areas, due to the way it spreads."
        the_person.char "While the good this drug can do is great, the profit potential is pretty low. I was only able to sell it for $3500. I hope that is okay."
        $ mc.business.funds += 3500
        mc.name "Thank you [the_person.title], I just hope the drug can be put to good use."
    elif quest_cure_discovery.quest_event_dict.get("cure_tier", 0) == 2:
        the_person.char "[the_disease] is widespread in the developed world. However, because this treatment has only been shown effective in rats, the over all effectiveness is unknown."
        the_person.char "After negotiating, I was able to sell the patent for $15000. I hope that is okay."
        $ mc.business.funds += 15000
        mc.name "That is still a considerable sum. Thank you [the_person.title]."
    elif quest_cure_discovery.quest_event_dict.get("cure_tier", 0) >= 3:
        the_person.char "[the_disease] is widespread in older populations. However, because this treatment has only been shown effective in rats, the over all effectiveness is unknown."
        the_person.char "After negotiating, I was able to sell the patent for $50000. I hope that is okay."
        $ mc.business.funds += 50000
        mc.name "That is still a significant sum. Thank you [the_person.title]."
    "The patent is sold! And you made a little extra money for the business."
    $ del the_disease
    $ quest_cure_discovery.set_quest_flag(101)
    $ quest_cure_discovery.quest_completed()
    return

#Bad Ends and paths

label quest_cure_discovery_patent_kept_label():
    $ the_person = mc.business.head_researcher
    $ the_disease = quest_cure_discovery.quest_event_dict.get("disease_name", "Rabies")
    $ quest_cure_discovery.set_quest_flag(19)
    "You get a notification on your phone and you check it. It's from the Red Cross?"
    "Red Cross""Thank you for donating your patent for [the_disease]!"
    "Red Cross""With this donation, we promise we will work to the best of our abilities to get this cure into the hands of everyone who needs it, worldwide."
    "Donated? What the hell? You didn't donate that!"
    if the_person == None:
        "Suddenly, you realize what must have happened. After clearing out her desk, the old head researcher must have donated the patent she discovered!"
        "Well, maybe you should have considered selling the patent. Either way, that business opportunity is now gone."
        $del the_disease
        $ quest_cure_discovery.quest_completed()
        return
    else:
        "Suddenly, you realize what must have happened. [the_person.title], not happy with your intention to keep the patent, must have secretly donated the rights to it."
    "You call her up."
    the_person.char "Hello?"
    mc.name "Hey. So, I'm guessing you're the one I have to thank for the email I got this morning from the Red Cross?"
    "There is silence on the other end. You think you hear an expletive whispered."
    the_person.char "I'm not going to lie... yes, that was me. You have to understand! This could help a lot of people!"
    "She sounds very sincere. It's hard to be mad, and maybe this is something that really COULD help a lot of people."
    the_person.char "Please don't fire me, I love working here, but I just couldn't sit by while something that could help people..."
    menu:
        "Fire her":
            mc.name "Clean out your desk. I can't have someone undermining me as my head researcher. You're fired."
            "Stunned silence on the other end of the call. Finally she speaks up."
            the_person.char "I understand. I'll be out before the end of the day."
            $ mc.business.remove_employee(the_person)
        "It's okay":
            mc.name "It's okay, [the_person.title]. I'm sorry I didn't make that move right from the start. You did the right thing."
            "She sounds relieved."
            the_person.char "Oh [the_person.mc_title], I knew you were a reasonable man! I'll make it up to you, I promise!"
            if the_person.effective_sluttiness() > 50: #MC can push for make up sex.
                mc.name "I think I know how you can make it up to me. Come to my office."
                the_person.char "Yes sir!"
                #TODO change background to office
                $ the_person.draw_person()
                "You hear a knock. You look up and see [the_person.possessive_title]"
                the_person.char "You wanted to see me?"
                mc.name "Yes. Come in, and lock the door behind you."
                the_person.char "Oh my..."
                "[the_person.title] does as you ask. Her voice takes on a sultry tone."
                the_person.char "So, did you have something in mind? How I can make all this up to you?"
                mc.name "I do, come around here and get on your knees."
                the_person.char "Oh god, yes [the_person.mc_title]."
                $ the_person.draw_person(position = "blowjob")
                "You pull your dick out of your pants and put it right on her face."
                mc.name "You know what to do."
                "You could let her just give you a blowjob, but if you push things a little rougher, it would really drive the point home, but her admiration for you would probably decrease."
                "[the_person.title] opens her mouth and takes the tip of your cock in her hot mouth. She gives you a few strokes as you rapidly harden in her mouth."
                call fuck_person(the_person, start_position = blowjob, skip_intro = True, position_locked = True, ignore_taboo = True) from _quest_cure_sex_path_01
                $ the_report = _return
                if skull_fuck in the_report.get("positions_used", []):  #You really roughed her up
                    "[the_person.possessive_title] mascara is running from tears caused by being gagged when you roughly fucked her throat."
                    mc.name "I know that this story had a happy ending, with the patent going to the Red Cross, but remember, this is my business. Don't do things behind my back again."
                    $ the_person.change_stats(obedience = 50, love = -10, slut_temp = 20, slut_core = 10)
                    "Her voice is trembling as she responds."
                    the_person.char "Yes... yes sir..."
                elif deepthroat in the_report.get("positions_used", []):  #She took it deep.
                    "[the_person.possessive_title] is recovering from taking your cock deep down her throat."
                    mc.name "I know this story had a happy ending, with the patent going to the Red Cross, but please don't do things behind my back like that again."
                    $ the_person.change_stats(obedience = 20, slut_temp = 10, slut_core = 5)
                    the_person.char "Yes sir, it won't happen again!"
                else: #Just a BJ
                    "[the_person.possessive_title] licks her lips, she seems to have enjoyed getting on her knees for you."
                    mc.name "Thank you for doing the right thing, but please let me know before you take actions like that again."
                    $ the_person.change_stats(love = 20, slut_temp = 5, slut_core = 5)
                    the_person.char "Yes sir."
                mc.name "That'll be all for now."
                $ the_person.draw_person(position = "walking_away")
                "Well, you may have missed a financial opportunity, but at least you got a blowjob out of it!"
            else:
                mc.name "I'm sure you will. Please try to let me know before you take actions like that in the future though."
                $ the_person.change_stats(obedience = 20, love = 20, happiness = 20) #Net gain to stats because MC still took a good path in the end.
                the_person.char "Of course sir."
                "You say goodbye and hang up the phone."
                "Well, you may have missed out on a financial opportunity, but it sounds like you've gained some consideration from [the_person.title] in the process."
    $ del the_disease
    $ quest_cure_discovery.quest_completed()
    return

label quest_cure_discovery_market_missed_label():
    $ the_disease = quest_cure_discovery.quest_event_dict.get("disease_name", "Rabies")
    "Before headed for bed, you check on the latest news on your computer. A headline catches your attention."
    "NEWS""BREAKING NEWS: Scientists at BIOFIRM announce possible cure for [the_disease]."
    "Wait a minute... isn't that the disease your head researcher recently found a possible cure for?"
    "FUCK, she was right. You probably should have moved on those patent rights faster!"
    #TODO remove on talk event to market target.
    $ del the_disease
    $ quest_cure_discovery.set_quest_flag(29)
    $ quest_cure_discovery.quest_completed()
    return
