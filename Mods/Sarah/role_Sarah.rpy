# ****Sarah profile****
# Personality type: Outgoing, extrovert.
# Background: Childhood friend. Moved away when you were kids but recently moved back to pursue a job that didn't work out. Now selling solar panels door to door, knocks on your door randomly.
#   Has a great HR resume.
#   After first chance meeting, unlocks the HR Supervisor organization policy that unlocks the role and increases maximum company size by 1.
#   After unlocking the policy, the player calls Sarah and hires her.
#   First level corruption:
#   Second level corruption: You catch her stealing breast enhancing serums. Option to forbid her, allow her, or encourage her.
#
#
# Required labels:
# INTRO
# Hire
# Story part one: She catches you in the office on Saturday, invites you out for drinks. She ends up at your place
# Story part two: Catch her swiping breast enhancement serums on friday
# Following monday, observe the results
# Story part three: Help her seduce another employee
#
# Intro: mandatory event, in the AM knocks on MC home selling solar panels.
# Hiring: mandatory event. Call up Sarah and hire her for the HR position.

init 2 python:

    #Sarah ACTIONS




    def Sarah_mod_initialization(): #Add actionmod as argument#

        Sarah_wardrobe = wardrobe_from_xml("Sarah_Wardrobe")

        Sarah_home = Room("Sarah's home", "Sarah's home", [], apartment_background, [],[],[],False,[0.5,0.5], visible = False, hide_in_known_house_map = False)
        Sarah_home.add_object(make_wall())
        Sarah_home.add_object(make_floor())
        Sarah_home.add_object(make_bed())
        Sarah_home.add_object(make_window())

        #Sarah_home.link_locations_two_way(downtown)
        list_of_places.append(Sarah_home)

        # init Sarah role
        Sarah_role = Role(role_name ="Childhood Friend", actions =[])

        #global Sarah_role
        global sarah
        sarah = create_random_person(name = "Sarah", last_name ="Cooper", age = 20, body_type = "thin_body", face_style = "Face_3", tits = "A", height = 0.90, hair_colour = "brown", hair_style = short_hair, skin="white",\
            eyes = "blue", personality = Sarah_personality, name_color = "#9400D3", dial_color = "#9400D3", starting_wardrobe = None, \
            stat_array = [4,3,3], skill_array = [5,3,2,1,1], sex_array = [1,2,3,1], start_sluttiness = 3, start_obedience = 0, start_happiness = 102, start_love = 3, \
            title = "Sarah", possessive_title = "Your childhood friend",mc_title = mc.name, relationship = "Single", kids = 0)

        sarah.schedule[1] = mall #Testing
        sarah.schedule[2] = mall
        sarah.schedule[3] = mall

        sarah.home = Sarah_home

        sarah.home.add_person(sarah)

        Sarah_intro = Action("Sarah_intro",Sarah_intro_requirement,"Sarah_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        mc.business.mandatory_crises_list.append(Sarah_intro) #Add the event here so that it pops when the requirements are met.
        return


init -1 python:
    def Sarah_intro_requirement():
        if day > 14:
            if mc_at_home():
                if time_of_day < 4:
                    return True
        return False

    def Sarah_hire_requirement():
        if HR_director_creation_policy.is_owned():
            return True
        return False

    def  Sarah_new_tits_requirement():
        if time_of_day == 1:
            if day%7 == 0:  #Monday
                return True
        return False

    def  Sarah_epic_tits_requirement():
        if time_of_day == 1:
            if day%7 == 0:  #Monday
                return True
        return False


label Sarah_intro_label():
    $ the_person = sarah
    "*DING DONG*"
    "You hear the doorbell ring. You don't remember expecting anyone? You go and answer it."
    $ the_person.draw_person()
    "Standing at your door is a cute brunette, fairly short, and strikingly familiar..."
    "She appears to be holding some kind of clipboard. A door to door salewoman? Do those still exist?"
    the_person.char "Hello sir, I am [the_person.title], with Metropolis Power and Light, I was just wondering if you had ever thought about installing solar panels..."
    "She begins talking about the benefits and tax credits associated with solar panels, but you have a hard time listening."
    "This girl... she look so familiar! Where do you know her from!?!"
    the_person.char "...with even 50% coverage of the roof you can expect a considerable reduction in your electric bill..."
    "What did she say her name was again? [the_person.title]? Suddenly you get a flash of a memory from a long time again. You quickly interrupt her."
    mc.name "I'm sorry, you said your name was [the_person.title]? Is your name [the_person.title] [the_person.last_name]?"
    "She immediately stops her sales pitch."
    the_person.char "That's right... do... do I know your from somewhere?"
    "Faint memories come flooding back to you. When you were growing up, your dad and his best friend got married around the same time and had kids!"
    "You used to spend a lot of time with your dad and his friend, and his friend's daughter, who was just a few years younger than you!"
    "You aren't sure what happened, but one day the other family moved away, to another city, and you never saw them again."
    mc.name "Your dad, he was friends with my dad! I remember when our dad's used to hang out, we spent a lot of time together!"
    "She looks shocked, but you can see she is also starting to remember..."
    the_person.char "Wait, I think I remember... Mr. [mc.last_name]? So you must be... is it really [mc.name]???"
    "You quickly nod!"
    $ the_person.draw_person(emotion = "happy")
    the_person.char "Oh my god! I don't believe it! You and your dad used to come over every week! And even though I was a few years younger than you, you would be so nice to me!"
    "You don't really remember going out of your way to be nice, but it was also a long time ago."
    $ the_person.draw_person(position = "kissing")
    "Without warning, [the_person.name] throw herself at you and gives you a big hug."
    the_person.char "I never would have thought in a million years I would run into you again!"
    $ the_person.draw_person(position = "stand2", emotion = "happy")
    mc.name "Dad told me your family had to move away from work. What brings you back to town?"
    $ the_person.draw_person(position = "stand2", emotion = "sad")
    the_person.char "Ahh... well, I had just finished my degree and landed an internship at a company in town here. It was a great company, or so I thought..."
    "She clears her throat and continues."
    the_person.char "The director there told me if the internship went well it could become a full time position. I worked my ASS off at that place, for 6 months! And I was bartending in the evenings to make ends meet..."
    the_person.char "... well, when my six months was up, he said, sorry, that wasn't good enough. We are terminating you."
    $ the_person.draw_person(position = "stand2", emotion = "angry")
    the_person.char "I found out later, they hired some dumb bimbo for my position. I made some friends at the company, they are pretty sure the director is banging her in the office every day!"
    $ the_person.draw_person(position = "stand2", emotion = "sad")
    "[the_person.possessive_title] looks down at the ground. It looks like she is about to cry."
    mc.name "That really sucks. I'm sorry to hear that. What were you interning for, anyway?"
    $ the_person.draw_person(position = "stand3")
    "The change of topic helps her keep her composure."
    the_person.char "Well, I just finished up my degree in Sociology, and I was interning for a Human Resources position..."
    "Human Resources? That might actually be fairly useful."
    the_person.char "... I was really hoping to eventually move up to HR director there. I love working with other people, and the small business atmosphere was great!"
    "HR director? You've never heard of such a position."
    mc.name "So, what kind of work would you do as an HR director that is different from a regular HR position?"
    the_person.char "Well, I would be in charge of the direction of the company in general, as far as work values, help with compan morale..."
    "She goes on to list multiple duties, aspects of running a small business that you had honestly never considered before."
    "When she finishes, you consider things for a moment. It would be REALLY handy to have someone around like this. She already has some work experience, and is young and ready to prove herself."
    "But, before you hire her, you would need to set up the HR director position at the company. Alternatively, you could still setup the new position, but hire someone else to fill the position."
    menu:
        "Offer to hire her":
            mc.name "So, as it turns out, I just recently started a new business making small run pharmaceuticals. You seem pretty knowledgable, would you consider running the HR department?"
            "[the_person.title] is caught completely off gaurd by your offer."
            the_person.char "Wait, so, you run a small business? I mean, I would love to, but I can't afford to do another unpaid internship right now."
            mc.name "I didn't say it was unpaid, this would definitely be a paid position."
            $ the_person.draw_person(position = "stand3", emotion = "happy")
            $ the_person.change_happiness(5)
            $ the_person.change_love(5)
            the_person.char "That would be... incredible! I don't know what to say! I can't wait to get started!"
            mc.name "I'll have to get your phone number. I'll need to set up the position before I can officially hire you, and that might take a few days."
            the_person.char "Oh! Of course, here..."
            "You quickly exchange phone numbers with [the_person.title]."
            mc.name "I'll be in touch with you soon I think."
            the_person.char "This is great, [the_person.mc_title], you won't regret this, I promise!"
            "You say goodbye to her, and she goes to keep selling solar panels until you get back to her after creating the HR director position."
            "In order to hire [the_person.title], you will need to create a new HR Director position via the policy menu."
            $ Sarah_hire = Action("Sarah hire",Sarah_hire_requirement,"Sarah_hire_label")
            $ mc.business.mandatory_crises_list.append(Sarah_hire) #Add the event here so that it pops when the requirements are met.
        "Don't offer to hire her":
            "You decide maybe down the line you could make a new HR director position, but you decide the [the_person.title] is probably not the best fit for it."
            mc.name "I'm sorry it didn't work out, I hope you are able to find something in your field."
            the_person.char "Thanks... well, it was good seeing you. I'd better keep at it."
            "You say goodbye to [the_person.title]. If you want to hire an HR director, you will need to create the position via the policy menu."
            #TODO figure out a way to delete sarah and remove her from the game.


    if HR_director_creation_policy not in organisation_policies_list:       #Hopefully by testint to see if it is already there we can avoid any issues in the future with mod compatability.... *shrug*
        $ organisation_policies_list.append(HR_director_creation_policy)

    return

label Sarah_hire_label():
    $ the_person = sarah
    "After creating the new HR Director position, you call up [the_person.title]. She answers and says hello."
    mc.name "Hey, I just wanted to let you know, I have the details finalized for an HR Director position."
    the_person.char "That sounds great! When can I get started?"
    mc.name "Tomorrow morning. I'll text the address after this call. We will go over your role and responsibilities when you get there."
    the_person.char "Yes! I'm so glad to finally be done selling solar panels. I'll see you in the morning!"
    "You hang up the phone. You quickly text [the_person.title] the adress of your business."
    #TODO Hire Sarah officially here?
    $ HR_director_initial_hire = Action("Hire HR Director",HR_director_initial_hire_requirement,"HR_director_initial_hire_label", args = the_person) #Set the trigger day for the next monday. Monday is day%7 == 0
    $ mc.business.mandatory_crises_list.append(HR_director_initial_hire) #Add the event here so that it pops when the requirements are met.

    return

label Sarah_catch_stealing_label():
    $ the_person = sarah
    "As you walk to halls of your company, getting ready to pack things up for the weekend, you notice [the_person.title] sneaking out of the research division."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]... what brings you to research on a late Friday evening?"
    "She looks down at the ground and mutters for a second, trying to think of something. It is clear she is hiding something."
    the_person.char "Hey [the_person.mc_title]! I was just, well, [stephanie.name] had something for me that umm, I asked her for help with and so I was just grabbing it before I left for the weekend!"
    "With one hand behind her back, it doesn't appear she wants you to know what is it that she has."
    mc.name "Is that so? That's awfully nice of her. What is she helping with? Can I see it?"
    if the_person.obedience > 120:
        "Realizing that you need to know what she was doing in there, she lowers her head and brings her hand forward. In it are several glass vials with some prototype serum labeled 'T+'"
        the_person.char "I'm sorry... I know I shouldn't... distract the research staff but, when you told me on Monday that we had come up with a breast enhancement serum, I immediately knew I had to get some I just..."
    else:
        the_person.char "Oh, don't worry about it, it is just between me and her!"
        "You furrow your brow. Hopefully you can convince her to come clean with whatever it is that she is doing."
        mc.name "I'm sure it is fine, but you ARE coming out of a research on a Friday, after everyone has left for the weekend. Let me see what you have."
        "Realing that you aren't going to back down, she slowly brings her hand forward. In it are several glass vials with some prototype serum labeled 'T+'"
        the_person.char "Don't be mad! When you told me on Monday that we had come up with a breast enhancement serum, I knew I had to get my hands on one of the prototypes..."
    mc.name "It okay. I didn't realize that was something you would be interested in. If you had asked me, I would have seen it arranged without having to sneak around!"
    $ the_person.change_happiness(5)
    $ the_person.change_love(3)
    $ the_person.draw_person(emotion = "happy")
    "She is very relieved to hear that."
    the_person.char "Oh! Thank you [the_persom.mc_title]! I'm sorry, I won't be sneaky like that again. I just... you now I've always had such a small chest and I've always been really self concious about it."
    the_person.char "I've thought about getting implants before but... surgery seems so extreme for a cosmetic issue."
    mc.name "So, how many are you planning to take?"
    the_person.char "Oh, well, research says we don't know for sure how effectice they are... I figure I'll just take one each day until I go up a few cup sizes."
    the_person.char "I've already ordered new bras and everything. I'm going to keep a careful record of how many I take and when, and then take measurements over the weekend."
    "[stephanie.name] is going to stop by this weekend to help document everything, she said it would be good for research..."
    "You think about it for a moment. You picture [the_person.title] for a moment with some nice 'C' cup tits... but then you can't help but imagine if she went crazy with it and took more."
    menu:
        "Sounds like a good plan":
            mc.name "You should definitely take it slow. I mean, worst case scenario, you can just take more later if you need to."
        "You should take them all":
            "[the_person.title] looks up at you, a bit surprised."
            the_person.char "Wh... what? I mean, I've always dreamed of having huge tits but... I mean I can always take more later, right?"
            mc.name "Fortune favors the bold, [the_person.title]. I don't think you will regret it if you do it."
            the_person.char "But... I've already bought all new bras and lingerie... I don't have the money right now to do that all over again!"
            menu:
                "Buy her new bras ($300)":
                    $ mc.business.funds += -300
                    mc.name "I'll consider it an investment, from the business. It is the least we can do if you are willing to test the new serum prototypes."
                    the_person.char "Oh... that's very generous! I mean, I supposed if you're willing to do that. I can probably return a bunch of the other ones too."
                    "She stands there for a few moments, considering her options."
                    the_person.char "Ok! I'll do it! Oh god I'm so excited. I'm going to go straight home and take a few before bedtime."
                    mc.name "Sounds good. I'll look forward to seeing... all of you... on Monday."
                    "She blushes and nods."
                    the_person.char "Alright, see you Monday!"
                    $ Sarah_epic_tits = Action("Sarah epic tits",Sarah_epic_tits_requirement,"Sarah_epic_tits_label")
                    $ mc.business.mandatory_crises_list.append(Sarah_epic_tits) #Add the event here so that it pops when the requirements are met.
                    return
                "Stop wearing bras":
                    #TODO make new function to iterate through her wardrobe and remove the bra from every outfit.
                    if the_person.sluttiness > 40:
                        $ the_person.draw_person(position = "stand4", emotion = "happy")
                        the_person.char "Oh! Well that's an idea. Funny, why hadn't I thought of that?"
                        #TODO if based on if she has a uniform
                        # the_person.char "If I do that... Are you going to relax the dress code a bit? That's fine as long as I don't have to wear bras to work anymore..."
                        # mc.name "I will definitely look into it, if it helps you make up your mind."
                        "She stands there for a few moments, considering her options."
                        the_person.char "Ok! I'll do it! Oh god I'm so excited. I'm going to go straight home and take a few before bedtime."
                        mc.name "Sounds good. I'll look forward to seeing... all of you... on Monday."
                        "She blushes and nods."
                        the_person.char "Alright, see you Monday!"
                        $ Sarah_epic_tits = Action("Sarah epic tits",Sarah_epic_tits_requirement,"Sarah_epic_tits_label")
                        $ mc.business.mandatory_crises_list.append(Sarah_epic_tits) #Add the event here so that it pops when the requirements are met.
                        return
                    else:
                        the_person.char "I just... I don't think I can do that right now. I'm sorry [the_person.mc_title]!"
                        mc.name "It fine, I just want you to be happy with your body."
                        the_person.char "Right. I mean, I can always take more later if I need to."

                "You're right":
                    mc.name "I just want you to be happy with your body."
                    "[the_person.title] looks a bit relieved."
                    the_person.char "Thanks [the_person.mc_title]."
    mc.name "Alright, you be careful this weekend. I'll look forward to seeing... all of you... on Monday."
    "She blushes and nods."
    the_person.char "Alright, see you Monday!"
    $ Sarah_new_tits = Action("Sarah new tits",Sarah_new_tits_requirement,"Sarah_new_tits_label")
    $ mc.business.mandatory_crises_list.append(Sarah_new_tits) #Add the event here so that it pops when the requirements are met.

    return

label Sarah_epic_tits_label():
    $ the_person = sarah
    $ sarah.tits = "F"
    $ the_person.change_slut_core(10)
    $ the_person.change_slut_temp(10)
    call Sarah_tits_reveal_label() from Sarah_epic_tits_call_1
    return

label Sarah_new_tits_label():
    $ the_person = sarah
    $ sarah.tits = "D"
    $ the_person.change_slut_core(5)
    $ the_person.change_slut_temp(5)
    call Sarah_tits_reveal_label() from Sarah_new_tits_call_1
    return

label Sarah_tits_reveal_label():
    $ the_person = sarah
    $ the_person.draw_person()
    "[the_person.title] steps confidently into your office."
    the_person.char "Good morning [the_person.mc_title]! Ready for our Monday meeting?"
    "Your jaw drops when you look up."
    mc.name "Wow, [the_person.title], you are awfully perky this morning!"
    "She laughs at you and smiles."
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    the_person.char "Thank you [the_person.mc_title]. I'm sorry again about being sneaky about the whole thing. I really appreciate you letting me do this!"
    "You notice she turns and closes your office door... and then locks it."
    if the_person.outfit.tits_available():
        "[the_person.title] takes a breast in her hand, enjoying the weight of it."
        the_person.char "It is incredible. So much better than a implant, and they've gotten more sensitive too."
        "Her hand begins to idly pinch one of her nipples."
        $ the_person.change_arousal(15)
        the_person.char "Mmm. Go ahead and touch them. I want to feel your hands one me!"

    else:
        the_person.char "Do you want to give them a closer look? I mean, you are the man who made this all possible..."
        "You quickly agree."
        while not the_person.outfit.tits_available():    #If covered up, have her take her top off
            $ the_clothing = the_person.outfit.get_upper_ordered()[-1]
            "[the_person.possessive_title] takes off her [the_clothing.name]"
            $ the_person.draw_animated_removal(the_clothing)
        "Her chest now bare before you, [the_person.title] takes a breast in her hand, enjoying the weight."
        the_person.char "Go ahead and touch them. These are so much better than implants, I can't believe how good they feel. And they are so sensitive too..."
    "With both hands your reach and cup her considerable chest. The skin is soft and pliable in your hands."
    $ the_person.change_arousal(15)
    the_person.char "Mmmmmm. Don't be shy! Play with them a bit. It feels so goooood..."
    "You begin to knead her chest a bit rougher now. She gasps as you struggle to get all of her pleasant titflesh in your hands."
    $ the_person.change_arousal(15)
    the_person.char "Oh god, you are getting me so hot..."
    "Her knees buckle for a second when you start to play with her nipples. You pinch and roll them in your fingers."
    $ the_person.change_arousal(15)
    the_person.char "Ah! Stop! God that feels amazing. But theres something else I want to try..."
    mc.name "Oh? What is that?"
    the_person.char "Well, I've tried this a couple times before but to be honest my chest was so small I don't think it was very good for the guy but... I want your cock between my tits!"
    mc.name "That sounds hot. Lets do it!"
    "You turn your chair to the side and [the_person.title] gets on her knees in front of you."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] eagerly begins opening your pants. She pulls out your cock and gives it a few gentle strokes."
    the_person.char "I can't believe I'm finally doing this. This all feels like a dream!"
    "She looks up at you from her knees. She looks you right in the eyes as she leans foward and slides your cock between her pillowy tits."
    "With both hands holding her breasts together, she slowly starts to move her pillowy flesh up and down your erection."
    call sex_description(the_person, SB_Titfuck_Kneeling, make_floor(), round = 1, private = True, girl_in_charge = True) from _call_sex_description_sarah_tits_reveal_1
    if the_person.arousal > 100: #She finished!
        the_person.char "Oh my god, I came so hard... I can't believe it. That felt so good! I need to do that again soon!"
        if the_person.get_opinion_score("showing her tits") < 2:
            $ the_person.sexy_opinions["showing her tits"] = [2, True]
            "[the_person.title] now loves showing her tits!"
    else:
        the_person.char "Mmm that was so hot. I can't wait to try that again..."
        if the_person.get_opinion_score("showing her tits") < 1:
            $ the_person.sexy_opinions["showing her tits"] = [1, True]
            "[the_person.title] now likes showing her tits!"
    the_person.char "Okay... let me go get cleaned up... then I'll come back and we can start our regular Monday meeting!"
    $ the_person.draw_person(position = "walking_away")
    "She gets up and leaves the room. You smile to yourself, thinking about how good her new tits felt around your cock."
    $ the_person.reset_arousal()
    $ the_person.review_outfit(show_review_message = False)

    return
