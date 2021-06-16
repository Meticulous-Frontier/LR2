#Note, this role is actually also a class extension.

#########################################################################################
# ----Flight Attendant----
#   Lives in a different city, but is based in your city. She is in town rarely, a certain number of days.
#   No particular hangouts, except the bar in the evening
#   Requires person subclass to keep her "out of town" on days she isn't around. Also disable date function? TODO
#   First event: You fool around in her hotel room.
#   Second event: She stays over at your place.
#   Third event: You offer to let her stay in exchange for "favors". She agrees.
#   Even requirements: Charisma and marketing skill combined.
#   Girl requirements: Since she is a subclass, will have to generate at run time.
#   Other notes: Make random event after third event, whenever she is in town she may ask to come over and spend the night.
#   After stage 6, girl will change to 7 if she is coming over, then back to 6 in the morning.
#
#   Event States:
#   0 - Before first encounter. She is always in town and at the bar until you meet and introduce yourself.
#   1 - Introduced to her
#   2 - After one night stand in her hotel room.
#   3 - She coming over Tonight
#   4 - She has stayed over
#   5 - She is coming over later in exhange for "favors"
#   6 - She has traded sex for a free crash pad
#   7 - She agreed to come over tonight
#
#
#
# Required Labels:
# Get a drink: At the bar only. Chance to give her serum
# Get out of here: Head with her back to her hotel room for a one night stand.
# Sex discussion: Gives you the "boundaries" talk
# My place: Head back to your place for the night.
# Crash pad: She stays at your place. Offers to pay you cheaper rate than hotel, if you seduce her you don't take her money.
# Coming over?: Ask if she needs a place to sleep tonight... for the right price...
# Sexual favors: She arrives at your place to trade favors for a bed to sleep in.
#######################################################################################




init -2 python: #Requirement Declarations#
    def casual_FA_get_a_drink_requirement(person):  #For now this should always return true. May be other conditions not to in the future#
        if person.event_triggers_dict.get("FA_sex_discussion_text_enable", 0) == 1:
            return False
        if mc.charisma + mc.market_skill < 3:   #Average 1.5 skills
            return "Charisma / Marketing skill too low"
        return True

    def casual_FA_get_out_of_here_requirement(person):
        if person.event_triggers_dict.get("FA_progress", 0) == 1:
            if person.event_triggers_dict.get("FA_one_night_avail", 0) == 1:
                return True
            if mc.charisma + mc.market_skill < 6:   #Average 3 skills
                return "Charisma / Marketing skill too low"
            if person.sluttiness < 25:
                return "Requires more sluttiness"
        return False

    def casual_FA_sex_discussion_requirement(person):
        if person.event_triggers_dict.get("FA_sex_discussion_text_enable", 0) == 1:
            return True
        return False

    def casual_FA_my_place_requirement(person):
        if person.event_triggers_dict.get("FA_progress", 0) == 2:
            if mc.charisma + mc.market_skill < 9:   #Average 4.5 skills
                return "Charisma / Marketing skill too low"
            if person.sluttiness < 40:
                return "Requires more sluttiness"
            return True
        if person.event_triggers_dict.get("FA_progress", 0) == 3:
            return "She's already coming over tonight!"
        if person.event_triggers_dict.get("FA_visit", 0) == 1:
            return "She's already coming over tonight!"
        if person.event_triggers_dict.get("FA_progress", 0) == 4:
            if mc.charisma + mc.market_skill < 12:
                return True
        return False

    def casual_FA_crash_pad_requirement(person):
        if time_of_day == 4:
            return True
        return False

    def casual_FA_coming_over_requirement(person):
        if person.event_triggers_dict.get("FA_progress", 0) == 4:
            if mc.charisma + mc.market_skill < 12:
                return False
            if person.sluttiness < 60:
                return "Requires more sluttiness"
            else:
                return True
        if person.event_triggers_dict.get("FA_progress", 0) == 5:
            return "She's already coming over tonight!"
        if person.event_triggers_dict.get("FA_progress", 0) == 6:
            return True
        if person.event_triggers_dict.get("FA_progress", 0) == 7:
            return "She's already coming over tonight!"
        if person.event_triggers_dict.get("FA_visit", 0) == 1:
            return "She's already coming over tonight!"
        return False


    def casual_FA_sexual_favors_requirement(person):
        if time_of_day == 4:
            return True
        return False


#*************Create Casual Flight Attendant Role***********#

init -1 python:
    casual_FA_get_a_drink = Action("Get a drink with her {image=gui/heart/Time_Advance.png}", casual_FA_get_a_drink_requirement, "casual_FA_get_a_drink_label",
        menu_tooltip = "Alcohol loosens lips!")
    casual_FA_get_out_of_here = Action("Drinks to go {image=gui/heart/Time_Advance.png}", casual_FA_get_out_of_here_requirement, "casual_FA_get_out_of_here_label",
        menu_tooltip = "See if she wants to take things somewhere private.")
    casual_FA_sex_discussion = Action("Ask her about the other night... {image=gui/heart/Time_Advance.png}",  casual_FA_sex_discussion_requirement, "casual_FA_sex_discussion_label",
        menu_tooltip = "Make sure it went okay.")
    casual_FA_my_place = Action("Take this back to your place {image=gui/heart/Time_Advance.png}", casual_FA_my_place_requirement, "casual_FA_my_place_label",
        menu_tooltip = "See if she wants to take this to your place")
    casual_FA_coming_over = Action("Come over tonight {image=gui/heart/Time_Advance.png}", casual_FA_coming_over_requirement, "casual_FA_coming_over_label",
        menu_tooltip = "Offer a bed in exchange for favors")
    casual_FA_role = Role(role_name ="Flight Attendant", actions =[casual_FA_get_a_drink, casual_FA_get_out_of_here, casual_FA_sex_discussion, casual_FA_my_place, casual_FA_coming_over], hidden = True)


#***************Create Flight Attendant Class************#
init -1 python:
    class Casual_Flight_Attendant(Person):
        def __init__(self):
            self.name = get_random_name()
            self.last_name = get_random_last_name()

            self.title = self.name #Note: We format these down below!
            self.possessive_title = self.name #The way the girl is refered to in relation to you. For example "your sister", "your head researcher", or just their title again.

            self.mc_title = "Stranger"

            self.home = purgatory #The room the character goes to at night. If none a default location is used.
            self.work = None #The room the character goes to for work.
            # self.schedule = {0:self.home,1:self.home,2:self.home,3:self.home,4:self.home} #A character's schedule is a dict of 0,1,2,3,4 (time periods) mapped to locations.
            #If there is a place in the schedule the character will go there. Otherwise they have free time and will do whatever they want.
            self.job = get_random_job() #Probably replace this

            # Relationship and family stuff
            self.relationship = "Single" #Should be Single, Girlfriend, Fiancée, or Married.

            self.SO_name = None #If not single, name of their SO (for guilt purposes or future events).

            self.kids = 0 #If she has kids, how many. (More likely for older characters.


            self.personality = get_random_personality()


            # Loves, likes, dislikes, and hates determine some reactions in conversations, options, etc. Some are just fluff.
            self.opinions = {} #Key is the name of the opinion (see random list), value is a list holding [value, known]. Value ranges from -2 to 2 going from hate to love (things not on the list are assumed 0). Known is a bool saying if the player knows about their opinion.

            self.sexy_opinions = {}
            # We establish random opinions first and will overwrite any that conflict with generated personality opinions.
            for x in __builtin__.range(1,5):
                the_opinion_key = get_random_opinion()
                degree = renpy.random.randint(-2,2)
                if not degree == 0: #ie. ignore 0 value opinions.
                    self.opinions[the_opinion_key] = [degree, False]

            for x in __builtin__.range(1,2):
                the_opinion_key = get_random_sexy_opinion()
                degree = renpy.random.randint(-2,2)
                if not degree == 0: #ie. ignore 0 value opinions.
                    self.sexy_opinions[the_opinion_key] = [degree, False]

            #Now we get our more likely default personality ones.
            for x in __builtin__.range(1,4):
                the_opinion_key, opinion_list = self.personality.generate_default_opinion()
                if the_opinion_key:
                    self.opinions[the_opinion_key] = opinion_list

            for x in __builtin__.range(1,3):
                the_opinion_key, opinion_list = self.personality.generate_default_sexy_opinion()
                if the_opinion_key:
                    self.sexy_opinions[the_opinion_key] = opinion_list



            #TODO: Relationship with other people (List of known people plus relationship with them.)
            FA_font = get_random_font()
            name_color = get_random_readable_color()
            #Using char instead of a string lets us customize the font and colour we are using for the character.
            self.char = Character("???", what_font = FA_font, who_font = FA_font, color = name_color,  what_color = copy.copy(name_color))

            # if title: #Format the given titles, if any, so they appear correctly the first time you meet at person.
            #     self.set_title(title) #The way the girl is refered to by the MC. For example: "Mrs. Whatever", "Lily", or "Mom". Will reset "???" if appropriate
            # else:
            #     self.char.name = self.create_formatted_title("???")
            # if possessive_title:
            #     self.set_possessive_title(possessive_title)

            ## Physical things.
            self.age = renpy.random.randint(18,50)
            self.body_type = get_random_body_type()
            self.tits = get_random_tit()
            self.height = 0.9 + (renpy.random.random()/10) #This is the scale factor for height, with the talest girl being 1.0 and the shortest being 0.8
            #self.body_images = body_images #instance of Clothing class, which uses full body shots.
            self.face_style = get_random_face()
             #instance of the Expression class, which stores facial expressions for different skin colours
            self.hair_colour = generate_hair_colour() #A list of [description, color value], where colour value is a standard RGBA list.
            self.hair_style = get_random_from_list(hair_styles).get_copy()
            self.hair_style.colour = self.hair_colour[1]
            self.skin = get_random_skin()
            self.eyes = get_random_eye()
            #TODO: Tattoos eventually
            if self.skin == "white":
                self.body_images = white_skin
            elif self.skin == "tan":
                self.body_images = tan_skin
            else:
                self.body_images = black_skin

            # self.expression_images = Expression(self.name+"\'s Expression Set", self.skin, self.face_style)

            self.serum_effects = [] #A list of all of the serums we are under the effect of.

            #if not special_role:  #Characters may have a special role that unlocks additional actions. By default this is an empty list.
            self.special_role = []
            # elif isinstance(special_role, Role):
            #     self.special_role = [special_role] #Support handing a non-list special role, in case we forget to wrap it in a list one day.
            # elif isinstance(special_role, list):
            # #     self.special_role = special_role #Otherwise we've handed it a list
            # # else:
            #     self.special_role = []
            #     log_message("Person \"" + name + " " + last_name + "\" was handed an incorrect special role parameter.")


            self.on_room_enter_event_list = [] #Checked when you enter a room with this character. If an event is in this list and enabled it is run (and no other event is until the room is reentered)
            self.on_talk_event_list = [] #Checked when you start to interact with a character. If an event is in this list and enabled it is run (and no other event is until you talk to the character again.)

            self.event_triggers_dict = {} #A dict used to store extra parameters used by events, like how many days has it been since a performance review.
            self.event_triggers_dict["employed_since"] = 0
            self.event_triggers_dict["wants_titlechange"] = False


            skill_cap = 5
            stat_cap = 5

            if recruitment_skill_improvement_policy.is_owned():
                skill_cap += 2

            if recruitment_stat_improvement_policy.is_owned():
                stat_cap += 2

            self.charisma = renpy.random.randint(1,stat_cap) #How likeable the person is. Mainly influences marketing, also determines how well interactions with other characters go. Main stat for HR and sales
            self.int = renpy.random.randint(1,stat_cap) #How smart the person is. Mainly influences research, small bonuses to most tasks. #Main stat for research and production.
            self.focus = renpy.random.randint(1,stat_cap)

            self.charisma_debt = renpy.random.randint(1,stat_cap) #Tracks how far into the negative a characters stats are, for the purposes of serum effects. Effective stats are never lower than 0.
            self.int_debt = renpy.random.randint(1,stat_cap)
            self.focus_debt = renpy.random.randint(1,stat_cap)

            self.charisma_debt = 0 #Tracks how far into the negative a characters stats are, for the purposes of serum effects. Effective stats are never lower than 0.
            self.int_debt = 0
            self.focus_debt = 0

            ##Work Skills##
            #Skills can be trained up over time, but are limited by your raw stats. Ranges from 1 to 5 at start, can go up or down (min 0)
            self.hr_skill = renpy.random.randint(1,skill_cap)
            self.market_skill = renpy.random.randint(1,skill_cap)
            self.research_skill = renpy.random.randint(1,skill_cap)
            self.production_skill = renpy.random.randint(1,skill_cap)
            self.supply_skill = renpy.random.randint(1,skill_cap)

            self.salary = self.calculate_base_salary()

            # self.employed_since = 0 #Default this to 0, it will almost always be overwritten but in case it sneaks through this makes sure that nothing breaks.

            self.idle_pose = get_random_from_list(["stand2","stand3","stand4","stand5"]) #Get a random idle pose that you will use while people are talking to you.

            ##Personality Stats##
            #Things like sugestability, that change over the course of the game when the player interacts with the girl
            self.suggestibility = 0 #How quickly/efficently bleeding temporary sluttiness is turned into core sluttiness.
            self.suggest_bag = [] #This will store a list of ints which are the different suggestion values fighting for control. Only the highest is used, maintained when serums are added and removed.

            self.happiness = 100 #Higher happiness makes a girl less likely to quit and more willing to put up with you pushing her using obedience.
            self.love = 0
            self.sluttiness = 0 + renpy.random.randint(0,20) #How slutty the girl is by default. Higher will have her doing more things just because she wants to or you asked.
            self.core_sluttiness = self.sluttiness #Core sluttiness is the base level of what a girl considers normal. normal "sluttiness" is the more variable version, technically refered to as "temporary slutiness".
            self.obedience = 100 #How likely the girl is to listen to commands. Default is 100 (normal person), lower actively resists commands, higher follows them.

            #Situational modifiers are handled by events. These dicts and related functions provide a convenient way to avoid double contributions. Remember to clear your situational modifiers when you're done with them!!
            self.situational_sluttiness = {} #A dict that stores a "situation" string and the corrisponding amount it is contributing to the girls sluttiness.
            self.situational_obedience = {} #A dictthat stores a "situation" string and a corrisponding amount that it has affected their obedience by.

            ##Sex Stats##
            #These are physical stats about the girl that impact how she behaves in a sex scene. Future values might include things like breast sensitivity, pussy tighness, etc.
            self.arousal = 0 #How actively horny a girl is, and how close she is to orgasm. Generally resets to 0 after orgasming, and decreases over time while not having sex (or having bad sex).

            ##Sex Skills##
            #These represent how skilled a girl is at different kinds of intimacy, ranging from kissing to anal. The higher the skill the closer she'll be able to bring you to orgasm (whether you like it or not!)
            self.sex_skills = {}
            self.sex_skills["Foreplay"] = renpy.random.randint(1,5) #A catch all for everything that goes on before blowjobs, sex, etc. Includes things like kissing and strip teases.
            self.sex_skills["Oral"] = renpy.random.randint(1,5) #The girls skill at giving head.
            self.sex_skills["Vaginal"] = renpy.random.randint(1,5) #The girls skill at different positions that involve vaginal sex.
            self.sex_skills["Anal"] = renpy.random.randint(1,5) #The girls skill at different positions that involve anal sex.

            ## Clothing things.
            self.wardrobe = default_wardrobe.get_random_selection(40) #Note: we overwrote default copy behaviour for wardrobes so they do not have any interference issues with eachother.

            self.planned_outfit = self.wardrobe.decide_on_outfit(self.sluttiness) #planned_outfit is the outfit the girl plans to wear today while not at work. She will change back into it after work or if she gets stripped. Cop0y it in case the outfit is changed during the day.
            self.planned_uniform = None #The uniform the person was planning on wearing for today, so they can return to it if they need to while at work.
            self.outfit = self.planned_outfit.get_copy() #Keep a seperate copy of hte outfit as the one that is being worn.


            ## Conversation things##
            self.sexed_count = 0


        def run_day(self):
            #renpy.say(None,"DEBUG: run day running correctly")
            if day%7 == 3 or renpy.random.randint(0,100) < 50: #If the new day is Friday or random roll is out of town.
                self.home = purgatory
                self.set_schedule(purgatory, times = [0, 1, 2, 3, 4])
            else:
                self.home = downtown_hotel
                self.set_schedule(downtown_bar, days = [4, 5], times = [2, 3])
                self.set_schedule(downtown_hotel, days = [5, 6], times = [4])
            #TODO Find a way to cancel dates made.
            super(Casual_Flight_Attendant, self)
        pass


#*************Mandatory Crisis******************#

init 1 python:
    casual_FA_crash_pad = Action("Crash Pad", casual_FA_crash_pad_requirement, "casual_FA_crash_pad_label")

    casual_FA_sexual_favors = Action("Sexual Favors", casual_FA_sexual_favors_requirement, "casual_FA_sexual_favors_label")


#************* Flight Attendant Action Labels *********#

#CSFA00
label casual_FA_get_a_drink_label(the_person):
    if the_person.event_triggers_dict.get("FA_progress", 0) == 0:
        "You decide see if she'll let you buy her a drink."
        mc.name "Hey, can I get you a drink? I'd love to chat and get to know you better."
        the_person "Oh! Sure, I'd love a drink..."
        "You get ready to ask her what she drinks when she continues."
        the_person "But you should now, I don't actually live around here, I actually live in Pittsburgh."
        mc.name "Oh wow, steel city! Hey, tell me what you'd like, I wouldn't mind hearing what you are doing in town!"
        the_person "Okay! I like a Gin Sour, thanks a bunch!"
    elif the_person.event_triggers_dict.get("FA_progress", 0) == 1:
        "Last time you talked to her, she let you buy her a drink and it you had a good time chatting, so you figure you should give it another shot."
        mc.name "Hey, can I get you a drink? I'd love to chat and get to know you better."
        the_person "Ah! Sure! That would be great, [the_person.mc_title]! I have to admit, Gin Sour is like my favorite drink, and they make them so good here..."
        mc.name "You got it. I'll be right back with one."
    else:
        "By this point, you are pretty sure she'll accept an offer to buy her a drink."
        mc.name "Hey, [the_person.title]. I didn't realize you were in town! Can I get you a Gin Sour!"
        "[the_person.title] smiles and nods."
        the_person "That sounds refreshing, [the_person.mc_title]!"
        mc.name "You got it. I'll be right back with one."
    "You head over to the bar and put in your order. It isn't long until you are holding a Gin Sour and a beer."  #TODO pay for her drink
    "You consider for a moment. You could probably slip a serum in her drink without anyone noticing. Do you want to?"

    menu:
        "Give her a serum":
            "You decide to slip one into her drink."
            call give_serum(the_person) from _call_give_serum_CSFA000
        "Don't use serum":
            "You decide just to give her the drink."
    "You go back over to [the_person.title] and hand her the drink."
    mc.name "Why don't we grab a table? I seen one open over there."
    $ the_person.draw_person(position = "sitting")
    "You sit down at the table and start talking with her."
    if the_person.event_triggers_dict.get("FA_progress", 0) == 0:
        mc.name "So, what brings a girl from Pittsburgh here?"
        the_person "Ah, well, I'm in town for work, I guess you could say."
        mc.name "Wow, you work here? That's an awful long way to go for work, isn't it?"
        "[the_person.title] hesitates for a bit."
        the_person "Yeah I suppose it would seem like it, but it honestly isn't that bad."
        mc.name "So what do you do that brings you here?"
        the_person "Well, I'm actually a flight attendant... you know, like in the airlines?"
        mc.name "Wow, that sounds like quite the job!"
        the_person "Yeah, I mean, the pay isn't that great, but the travel benefits are amazing. Last month I took a trip to San Juan and paid nothing for the airfare."
        $ the_person.event_triggers_dict["FA_progress"] = 1
        "You make some small chat with [the_person.title] for a little longer, but soon she stands up."
        $ the_person.draw_person(position = "stand2")
        the_person "Thanks for the drink, [the_person.mc_title], but I'd better get to bed. I have an early flight to operate in the morning, and I HATE working tired."
        "You say goodbye and watch her as she leaves. You wonder if you will see her again."
        call advance_time from _call_advance_casual_FA_drink01
        return

    elif the_person.event_triggers_dict.get("FA_progress", 0) == 1:
        mc.name "So, I'm going to be honest... I'm surprised to see you here again! Do you find yourself in town very often?"
        the_person "Yeah well, I guess I didn't really bring it up last time, but, I'm actually based here. So every time I start a trip, I usually come to town the night before and spend the night."
        mc.name "Oh wow... from Pittsburgh? That's an awfully long drive..."
        the_person "Oh! I don't drive it. With my flight benefits I can fly space available, so if there is an open seat, I'll grab it to get to work!"
        mc.name "What if everything is full?"
        the_person "Honestly? I usually just call in sick. We can get it as an excused absence, but we don't get paid, so I usually just burn sick time."
        mc.name "That's a pretty interesting setup. Do you stay with friends or family in town here?"
        the_person "Well, I used to have a crash pad... A crash pad is like, a bunch of flight attendants go in together and rent out an apartment close to the apartment and share the costs of it."
        mc.name "Used to?"
        "You notice [the_person.title] gives a slight smile before continuing."
        the_person "Yeah, well, I got kicked out."
        mc.name "What for?"
        the_person "Well, it was an all female crash pad, but uhh, I got caught bringing a boy back... We were really quiet but apparently we woke up one of the other flight attendants."
        the_person "Anyway, I haven't been able to find another crash pad yet, so for now I'm staying at the hotel attached to this bar. Its expensive, but at least I have a place to sleep when I'm in town."
        "You nod, understanding. Sounds like a tough predicament to be in."
        the_person "Anyway, I don't really talk about it anymore right now. How about you? What do you do?"
        "You chat with [the_person.title] for a while, talking about what you do for a living. You enjoy flirting and chatting with her."
        $ the_person.draw_person(position = "stand4")
        "After a while, [the_person.title] gets up."
        if mc.charisma + mc.market_skill > 6:   #Average 4.5 skills
            if the_person.sluttiness > 25:
                $ the_person.event_triggers_dict["FA_one_night_avail"] = 1
                "You see her give you the once over."
                the_person "You know... you're pretty cute. Maybe next time you see me here we should take our drinks to go. My room is right upstairs..."
                mc.name "Want to? I could get us both another drink and we could be on our way."
                "She thinks about it for several seconds before responding."
                the_person "I'm sorry... I have to get up really early. The 5:30 am flight isn't gonna work itself! But next time, ask me about it and we'll do it! Okay?"
                return
        the_person "Thanks for the drink, [the_person.mc_title], but I'd better get to bed. I have an early flight to operate in the morning, and I HATE working tired."
        "You say goodbye and watch her as she leaves."
        call advance_time from _call_advance_casual_FA_drink02
        return

    elif the_person.event_triggers_dict.get("FA_progress", 0) == 2:
        "You can see [the_person.title] blush a bit as you approach her."
        the_person "Hey [the_person.mc_title]. Want to chat? I think I need a drink."
    elif the_person.event_triggers_dict.get("FA_progress", 0) == 3:
        the_person "Hey [the_person.mc_title]. Don't worry, I got your address. I really appreciate the offer for a place to stay!"
    elif the_person.event_triggers_dict.get("FA_progress", 0) == 4:
        the_person "Hey [the_person.mc_title]! Want to grab a drink with me? I don't have any plans for tonight, if you wanted to do something later..."
    elif the_person.event_triggers_dict.get("FA_progress", 0) == 5:
        the_person "Hello again [the_person.mc_title]! I can't wait until later..."
    elif the_person.event_triggers_dict.get("FA_progress", 0) == 6:
        the_person "Hey [the_person.mc_title]! Just the man I was hoping to see today!"
    elif the_person.event_triggers_dict.get("FA_progress", 0) == 7:
        the_person "Hey [the_person.mc_title]! Can't wait to see you at your place later. I'm wearing something special for you..."

    return

#CSFA10
label casual_FA_get_out_of_here_label(the_person):
    mc.name "So, wanna grab a couple of drinks and head upstairs?"
    the_person "Yeah... I think I'd like that. This place is too crowded anyway. You know what I drink right?"
    mc.name "Gin Sour, coming right up!"
    "You head over to the bar and put in your order. It isn't long until you are holding a Gin Sour and a beer."  #TODO pay for her drink
    "Do you want to slip a serum in her drink?"
    menu:
        "Give her a serum":
            "You decide to slip one into her drink."
            call give_serum(the_person) from _call_give_serum_CSFA010
        "Don't use serum":
            "You decide just to give her the drink."
    "You spot [the_person.title] by the door and join her. You follow her to the elevator, and soon find yourself in front of her hotel room door."
    #TODO change rooms to hotel#
    the_person "Ok, this will be way quieter than downstairs."
    "[the_person.title] opens her hotel room door and you quickly follow her inside. At first, you weren't sure what she had planned for the evening, but she quickly signalled her intentions."
    $ the_person.draw_person(position = "kissing")
    "She puts one hand on your shoulder and starts leaning into you. At first you lightly brush your lips together, but soon she returns your kiss hungrily."
    "You are savoring the taste of chapstick when she suddenly turns away from you."
    $ the_person.draw_person(position = "back_peek")
    "She grabs the ice bucket and hands it to you."
    the_person "Be a sweetheart and fill this up for me real quick, would you?"
    "You go and quickly fill the ice bucket. You don't run into anyone in the hall, which makes it easier since your cock is rock hard thinking about getting back to the room."
    "When you walk in, you notice the bathroom door is closed and an empty gin sour glass sitting on the table. You set the ice bucket down at the desk and have a seat on the edge of the bed."
    "You wait for a few minutes, and are soon rewarded for your patience when [the_person.title] emerges from the restroom."
    #TODO put her in lingerie
    $ the_person.draw_person(position = "stand2")
    "She emerges in an incredible set of purple lingerie. You start to get up but she quickly stops you, pushing you back onto the bed."
    $ the_person.draw_person (position = "cowgirl")
    "[the_person.possessive_title] pushes you onto your back and straddles your waist. She begins to grind up against you, dry humping your erection."
    "She closes her eyes and moans. You reach up and knead her tits through her bra. She reaches back and undoes the clasp holding her bra on. She leans forward and her bra falls off her shoulders and onto the bed."
    #TODO draw bra strip#
    "Your hands return to her perky tits. They feel soft and supple in your hands. She moans when you pinch her nipples gently."
    $ the_person.change_arousal(10)

    "TODO finish this scene."


    call advance_time from _call_advance_casual_FA_one_night
    return

#CSFA20
label casual_FA_sex_discussion_label(the_person):
    "This scene is not yet written."


    call advance_time from _call_advance_casual_FA_sex_discussion
    return

#CSFA30
label casual_FA_my_place_label(the_person):
    "This scene is not yet written."

    call advance_time from _call_advance_casual_FA_my_place
    return

#CSFA40
label casual_FA_crash_pad_label(the_person):
    "This scene is not yet written."

    return

#CSFA50
label casual_FA_coming_over_label(the_person):
    "This scene is not yet written."

    call advance_time from _call_advance_casual_FA_coming_over
    return

#CSFA60
label casual_FA_sexual_favors_label(the_person):
    "This scene is not yet written."

    return


#************* Personality****************# #For now, based on Wild Personality
#
init 1301 python:              #Because Vren Init personality functionns at 1300

    def FA_titles(person):
        valid_titles = []
        valid_titles.append(person.name)

        valid_titles.append("Flygirl")
        if person.sluttiness > 40:
            valid_titles.append("Skyslut")
        if person.sluttiness > 60:
            valid_titles.append("Cock Pit")
        return valid_titles

    def FA_possessive_titles(person):
        valid_possessive_titles = [person.title]

        if person.sluttiness > 60:
            valid_possessive_titles.append("The Skyslut")

        return valid_possessive_titles
    def FA_player_titles(person):
        return mc.name
    FA_personality = Personality("Stewardess", default_prefix = "wild",
    common_likes = ["traveling"],
    common_sexy_likes = ["casual sex"],
    common_dislikes = ["relationships"],
    common_sexy_dislikes = [],
    titles_function = FA_titles, possessive_titles_function = FA_possessive_titles, player_titles_function = FA_player_titles)


#************* Personality labels***************#
#
label FA_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around and looks you up and down."
    #TODO: Have this differ based on personality
    $ the_person.set_title("???")
    the_person "Sorry, I don't live around here, so I'm not sure I can help you..."
    mc.name "I know this sounds crazy, but I saw you and just wanted to say hi and get your name."
    "She laughs and crosses her arms."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person "Yeah? Well I like the confidence, I'll say that. My name's [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    the_person "And what about you, random stranger? What's your name?"
    return
#
label FA_greetings(the_person):
    if the_person.event_triggers_dict.get("FA_progress", 0) == 0:
        the_person "Hello again... it was [the_person.mc_title], right? Is there something I can help you with?"
    if the_person.event_triggers_dict.get("FA_progress", 0) == 1:
        the_person "Hello, [the_person.mc_title], I was just about to get a drink. How are you?"
    if the_person.event_triggers_dict.get("FA_progress", 0) == 2:
        "You can see [the_person.title] blush a bit as you approach her."
        the_person "Hey [the_person.mc_title]. Want to chat? I think I need a drink."
    if the_person.event_triggers_dict.get("FA_progress", 0) == 3:
        the_person "Hey [the_person.mc_title]. Don't worry, I got your address. I really appreciate the offer for a place to stay!"
    if the_person.event_triggers_dict.get("FA_progress", 0) == 4:
        the_person "Hey [the_person.mc_title]! Want to grab a drink with me? I don't have any plans for tonight, if you wanted to do something later..."
    if the_person.event_triggers_dict.get("FA_progress", 0) == 5:
        the_person "Hello again, [the_person.mc_title]! I can't wait until later..."
    if the_person.event_triggers_dict.get("FA_progress", 0) == 6:
        the_person "Hey [the_person.mc_title]! Just the man I was hoping to see today!"
    if the_person.event_triggers_dict.get("FA_progress", 0) == 7:
        the_person "Hey [the_person.mc_title]! Can't wait to see you at your place later. I'm wearing something special for you..."
    else:
        the_person "Hey [the_person.mc_title]."

    return


label FA_hookup_rejection(the_person):
    the_person "Your loss! Just thinking about you makes me want to spread my legs, and you could have had some of this..."
    return

label FA_hookup_accept(the_person):
    "This is a test to see if this is working!"
    return


# label FA_sex_responses(the_person):
#     if the_person.arousal < 25:
#         if the_person.sluttiness > 50:
#             the_person "Oh fuck, I never get tired of this feeling!"
#         else:
#             the_person "Oh... Oh fuck me that feels nice..."
#
#     elif the_person.arousal < 50:
#         if the_person.sluttiness > 50:
#             the_person "Mmm, keep going [the_person.mc_title]. Just keep going, that feels perfect."
#         else:
#             the_person "That... That feels so fucking good!"
#
#     elif the_person.arousal < 75:
#         if the_person.sluttiness > 50:
#             the_person "That's right, use me like your dirty little slut!"
#         else:
#             the_person "Does it feel as good for you as it does for me? Mmm, it feels so good!"
#     else:
#         if the_person.sluttiness > 50:
#             if the_person.relationship == "Single":
#                 the_person "Fuck! I'm... You're going to make me cum! I want you to make me cum!"
#             else:
#                 $ so_title = SO_relationship_to_title(the_person.relationship)
#                 the_person "I might have a [so_title], but he doesn't drive me crazy like you do [the_person.mc_title]!"
#                 the_person "Make me cum my brains out! Screw my [so_title], he's not half the man you are!"
#         else:
#             the_person "Don't stop! You're going to make me cum, don't you dare stop!"
#
#     return
#
# label FA_climax_responses(the_person):
#     if the_person.sluttiness > 70:
#         the_person "Ah! More! I'm going to... Ah! Cum! Fuck!"
#         "She closes her eyes and squeals with pleasure."
#     else:
#         the_person "Oh god, I'm going to... Oh fuck me! Ah!"
#     return
#
# label FA_clothing_accept(the_person):
#     if the_person.obedience > 130:
#         the_person "You think it will look good on me? I guess that's all I need to hear then."
#     else:
#         the_person "Hey, thanks. That's a good look, I like it."
#     return
#
label FA_clothing_reject(the_person):
    if the_person.obedience > 130:
        the_person "I don't... I'm sorry, but I really don't think I could get away with wearing something like this. I appreciate the thought though."
    else:
        if the_person.sluttiness > 60:
            the_person "Jesus, you didn't leave much to the imagination, did you? I don't think I can wear this."
        else:
            the_person "Sorry, my bags are already pretty full, you should probably just keep this."
    return
#
label FA_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person "Oh man, I'm a mess. I'll be back in a moment, I'm just going to get cleaned up for you."
    else:
        if the_person.sluttiness > 50:
            the_person "Oh wow, could you imagine if I got on a plane like this? I'd give the poor old captain a heart attack!"
        else:
            the_person "Damn, everything's out of place after that. Wait here a moment, I'm just going to find a mirror and try and look presentable."
    return
#
# label FA_strip_reject(the_person, the_clothing, strip_type = "Full"):
#     if the_person.obedience > 130:
#         the_person "Could we leave that where it is for now, please?"
#     elif the_person.obedience < 70:
#         the_person "No, no, no, I'll decide what comes off and when, okay?"
#     else:
#         the_person "Not yet... get me a little warmed up first, okay?"
#     return
#
# label FA_sex_accept(the_person):
#     if the_person.sluttiness > 70:
#         if the_person.obedience < 70:
#             the_person "Let's do it. Once you've had your fill I have a few ideas we could try out."
#         else:
#             the_person "I was hoping you would suggest that, just thinking about it gets me excited."
#     else:
#         the_person "You want to give it a try? Okay, let's try it."
#     return
#
# label FA_sex_obedience_accept(the_person):
#     if the_person.sluttiness > 70:
#         the_person "God, what have you done to me? I should say no, but... I just want you to use me however you want, [the_person.mc_title]."
#     else:
#         if the_person.obedience > 130:
#             the_person "If that's what you want to do then I will do what you tell me to do."
#         else:
#             the_person "I shouldn't... but if you want to try it out I'm game. Try everything once, right?"
#     return
#
# label FA_sex_gentle_reject(the_person):
#     if the_person.sluttiness > 50:
#         the_person "Not yet [the_person.mc_title], get me warmed up first."
#     else:
#         the_person "Wait, I just... I don't think I'm ready for this. I want to fool around, but let's keep it casual."
#     return
#
# label FA_sex_angry_reject(the_person):
#     if not the_person.relationship == "Single":
#         $ so_title = SO_relationship_to_title(the_person.relationship)
#         the_person "What? I have a [so_title], so you can forget about doing anything like that. Ever."
#         "She glares at you, then walks away."
#     elif the_person.sluttiness < 20:
#         the_person "I'm sorry, what!? No, you've massively misread the situation, get the fuck away from me!"
#         "[the_person.title] glares at you and steps back."
#     else:
#         the_person "What? That's fucking disgusting, I can't believe you'd even suggest that to me!"
#         "[the_person.title] glares at you and steps back."
#     return

label FA_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person "We may not be a mile high right now, but we could always practice for if you ever catch a flight I'm woking."
        else:
            the_person "Right now? Okay, lead the way I guess."
    else:
        if the_person.sluttiness > 60:
            the_person "Thank god, I've been thinking about your cock since my Boston overnight 2 days ago."
            "[the_person.title] takes your hand and leads you off to find some place out of the way."
        elif the_person.sluttiness > 10:
            the_person "I know that look you're giving me, I think I know what you want."
        else:
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes."
    return
#
# label FA_seduction_accept_crowded(the_person):
#     if the_person.relationship == "Single":
#         if the_person.sluttiness < 20:
#             the_person "Alright, let's slip away for a few minutes and you can convince me a little more."
#         elif the_person.sluttiness < 50:
#             the_person "Come on, I know someplace nearby where we can get a few minutes privacy."
#         else:
#             the_person "Oh my god. I hope you aren't planning on making me wait [the_person.mc_title], because I don't know if I can!"
#     else:
#         $ so_title = SO_relationship_to_title(the_person.relationship)
#         if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
#             the_person "Fuck, let's get this party started!"
#             the_person "I hope you don't mind that I've got a [so_title], because I sure as hell don't right now!"
#         else:
#             the_person "God damn it, you're bad for me [the_person.mc_title]... Come on, we need to go somewhere quiet so my [so_title] doesn't find out about this."
#     return
#
# label FA_seduction_accept_alone(the_person):
#     if the_person.relationship == "Single":
#         if the_person.sluttiness < 20:
#             the_person "Well, I think you deserve a chance to impress me."
#         elif the_person.sluttiness < 50:
#             the_person "Mmm, well let's get this party started and see where it goes."
#         else:
#             the_person "Fuck, I'm glad you're as horny as I am right now. Come on, I can't wait any more!"
#     else:
#         $ so_title = SO_relationship_to_title(the_person.relationship)
#         if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
#             the_person "Fuck, you know how to turn me on in ways my [so_title] never can. Come here!"
#         else:
#             the_person "You're such bad news [the_person.mc_title]... I have a [so_title], but all I can ever think of is you!"
#     return
#
label FA_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Sorry [the_person.mc_title], I have to get up early to catch a flight, and I need my rest."
        "[the_person.title] shrugs unapologetically."

    elif the_person.sluttiness < 50:
        the_person "I'll admit it, you're tempting me, but I'm not in the mood to fool around right now. Maybe some other time though, I think we could have a lot of fun together."

    else:
        the_person "Shit, that sounds like a lot of fun [the_person.mc_title], but I'm not feeling it right now. Hang onto that thought and we can fool around some other time."
    return
#
# label FA_flirt_response(the_person):
#     if the_person.obedience > 130:
#         if the_person.sluttiness > 50:
#             the_person "You know that all you have to do is ask and it's all yours."
#         else:
#             the_person "Thank you [the_person.mc_title], I'm glad you're enjoying the view."
#
#     elif not the_person.relationship == "Single":
#         $so_title = SO_relationship_to_title(the_person.relationship)
#         if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
#             the_person "Then why don't you do something about it? Come on, we don't have to tell my [so_title] anything at all, right?"
#             "[the_person.title] winks and spins around, giving you a full look at her body."
#         else:
#             the_person "You're playing with fire [the_person.mc_title]. I've got a [so_title], and I don't think he'd appreciate you flirting with me."
#             mc.name "What about you, do you appreciate it?"
#             "She gives a coy smiles and shrugs."
#             the_person "Maybe I do."
#
#     else:
#         if the_person.sluttiness > 50:
#             the_person "Then why don't you do something about it? Come on, all you have to do is ask."
#             "[the_person.title] smiles at you and spins around, giving you a full look at her body."
#         else:
#             the_person "Well thank you, play your cards right and maybe you'll get to see a little bit more."
#             the_person "You'll have to really impress me though, I have high standards."
#     return
#
# label FA_cum_face(the_person):
#     if the_person.obedience > 130:
#         if the_person.sluttiness > 60:
#             the_person "What do you think? Is this a good look [the_person.mc_title]?"
#             "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
#         else:
#             the_person "I hope you had a good time [the_person.mc_title]. It certainly seems like you did."
#             "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#     else:
#         if the_person.sluttiness > 80:
#             the_person "Mmm that's such a good feeling. Do you think I look cute like this?."
#             "[the_person.title] runs her tongue along her lips, then smiles and laughs."
#         else:
#             the_person "Whew, glad you got that over with. Take a good look while it lasts."
#     return
#
# label FA_cum_mouth(the_person):
#     if the_person.obedience > 130:
#         if the_person.sluttiness > 60:
#             the_person "Mmm, thank you [the_person.mc_title]."
#         else:
#             "[the_person.title]'s face grimaces as she tastes your cum in her mouth."
#             the_person "Ugh. There, all taken care of [the_person.mc_title]."
#     else:
#         if the_person.sluttiness > 80:
#             the_person "Mmm, you taste great [the_person.mc_title]. Was it nice to watch me take your load in my mouth?"
#         else:
#             the_person "Ugh, that's such a... unique taste."
#     return
#
label FA_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Cockpits!", "Holy shit!", "Fucking shit!", "God fucking dammit!", "Son of a bitch!", "Mother fucker!", "Whoah!"])
    the_person "[rando]"
    return

label FA_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "I've got a ton of things I need to get to, could we talk some other time [the_person.mc_title]?"
    else:
        the_person "Hey, I'd love to chat but I have a million things to get done before my report time tomorrow."
    return
#
# label FA_sex_strip(the_person):
#     if the_person.sluttiness < 20:
#         if the_person.arousal < 50:
#             the_person "One sec, I want to take something off."
#         else:
#             the_person "Ah, I'm wearing way too much right now. One sec!"
#
#     elif the_person.sluttiness < 60:
#         if the_person.arousal < 50:
#             the_person "Why do I bother wearing all this?"
#         else:
#             the_person "Wait, I want to get a little more naked for you."
#
#     else:
#         if the_person.arousal < 50:
#             the_person "Give me a second, I'm going to strip something off just. For. You."
#         else:
#             the_person "Ugh, let me get this off. I want to feel you pressed against every inch of me!"
#     return
#
# label FA_sex_watch(the_person, the_sex_person, the_position):
#     if the_person.sluttiness < the_position.slut_requirement - 20:
#         $ the_person.draw_person(emotion = "angry")
#         the_person "Ugh, jesus you two. Get a room or something, nobody wants to see this."
#         $ the_person.change_obedience(-2)
#         $ the_person.change_happiness(-1)
#         "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.sluttiness < the_position.slut_requirement - 10:
#         $ the_person.draw_person()
#         the_person "Could you two at least keep it down? This is fucking ridiculous."
#         $ the_person.change_happiness(-1)
#         "[the_person.title] tries to avert her gaze and ignore you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.sluttiness < the_position.slut_requirement:
#         $ the_person.draw_person()
#         the_person "You're certainly feeling bold today [the_sex_person.name]. At least it looks like you're having a good time..."
#         $ change_report = the_person.change_slut_temp(1)
#         "[the_person.title] watches for a moment, then turns away while you and [the_sex_person.name] keep [the_position.verb]."
#
#     elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
#         $ the_person.draw_person()
#         the_person "Oh wow that's hot. You don't mind if I watch, do you?"
#         $ change_report = the_person.change_slut_temp(2)
#         "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."
#
#     else:
#         $ the_person.draw_person(emotion = "happy")
#         the_person "Come on [the_person.mc_title], [the_sex_person.name] is going to fall asleep at this rate! You're going to have to give her a little more than that."
#         "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
#     return
#
# label FA_being_watched(the_person, the_watcher, the_position):
#     if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #They agree you should give it to her harder
#         the_person "Come on [the_person.mc_title], be rough with me. I can handle it!"
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."
#
#     elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's super slutty and doesn't care what people think.
#         the_person "I bet she just wishes she was the one being [the_position.verb]ed you."
#
#     elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #She's super slutty and encourages the watcher to be slutty.
#         the_person "Oh god, you need to get a little of this yourself, [the_watcher.name]!"
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."
#
#     elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #She's into it and encouraged by the slut watching her.
#         the_person "[the_watcher.name], I'm giving him all I can right now. Any more and he's going to break me!"
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."
#
#     elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's into it but shamed by the prude watching her.
#         the_person "Fuck, maybe we should go somewhere a little quieter..."
#         $ the_person.change_arousal(-1)
#         $ the_person.change_slut_temp(-1)
#         "[the_person.title] seems uncomfortable with [the_watcher.name] nearby."
#
#     else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #They're both into it but not fanatical about it.
#         the_person "Ah, now this is a party! Maybe when he's done you can tap in and take a turn [the_watcher.name]!"
#         $ the_person.change_arousal(1)
#         $ the_person.change_slut_temp(1)
#         "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.name] around."
#
#     return
#
# label FA_work_enter_greeting(the_person):
#     if the_person.happiness < 80:
#         "[the_person.title] glances at you when you enter the room. She scoffs and turns back to her work."
#
#     elif the_person.happiness > 130:
#         if the_person.sluttiness > 40:
#             the_person "Hey [the_person.mc_title], down here for business or pleasure?"
#             "The smile she gives you tells you which one she's hoping for."
#         else:
#             "[the_person.title] looks up from her work and smiles at you when you enter the room."
#             the_person "Hey [the_person.mc_title], it's nice to have you stop by. Let me know if you need anything!"
#
#     else:
#         if the_person.sluttiness > 60:
#             "[the_person.title] walks over to you when you come into the room."
#             the_person "Just the person I was hoping would stop by. I'm here if you need anything."
#             "She winks and slides a hand down your chest, stomach, and finally your crotch."
#             the_person "Anything at all."
#         else:
#             the_person "Hey [the_person.mc_title]. Need anything?"
#     return
#
# label FA_date_seduction(the_person):
#     if the_person.relationship == "Single":
#         if the_person.sluttiness > the_person.love:
#             if the_person.sluttiness > 40:
#                 the_person "I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you. Want to come back to my place and find out what they are?"
#             else:
#                 the_person "You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead?"
#         else:
#             if the_person.love > 40:
#                 the_person "Tonight's been amazing [the_person.mc_title], I just don't want to say goodbye. Do you want to come back to my place and have a few drinks?"
#             else:
#                 the_person "This might be crazy, but I had a great time tonight and you make me a little crazy. Do you want to come back to my place and see where things go?"
#     else:
#         $ so_title = SO_relationship_to_title(the_person.relationship)
#         if the_person.sluttiness > the_person.love:
#             if the_person.sluttiness > 40:
#                 the_person "I've had a blast [the_person.mc_title], but I'm not done with you yet. Want to come back to my place?"
#                 the_person "My [so_title] won't be home until morning, so we would have plenty of time."
#             else:
#                 the_person "This might be crazy, but do you want to come back to have another drink with me?"
#                 the_person "My [so_title] is stuck at work and I don't want to be left all alone."
#         else:
#             if the_person.love > 40:
#                 the_person "You're making me feel crazy [the_person.mc_title]. Do you want to come have a drink at my place?"
#                 the_person "My [so_title] won't be home until morning, and we have a big bed you could help me warm up."
#             else:
#                 the_person "This is crazy, but would you want to have one last drink at my place? My [so_title] won't be home until morning..."
#     return
#
# label FA_sex_end_early(the_person):
#     if the_person.sluttiness > 50:
#         if the_person.love > 40:
#             if the_person.arousal > 60:
#                 the_person "You're really done? Fuck [the_person.mc_title], I'm still so horny..."
#             else:
#                 the_person "That's all you wanted? I was prepared to do so much more to you..."
#         else:
#             if the_person.arousal > 60:
#                 the_person "Fuck, I'm so horny... you're sure you're finished?"
#             else:
#                 the_person "That was a little bit of fun, I suppose."
#
#     else:
#         if the_person.love > 40:
#             if the_person.arousal > 60:
#                 the_person "[the_person.mc_title], you got me so turned on..."
#             else:
#                 the_person "I hope you had a good time."
#         else:
#             if the_person.arousal > 60:
#                 the_person "Oh god, that was intense..."
#             else:
#                 the_person "Done? Good, nice and quick."
#     return
#
#
# label FA_sex_take_control (the_person):
#     if the_person.arousal > 60:
#         the_person "Oh hell no, you can't just get me wet and then walk away!"
#     else:
#         the_person "Are you getting bored already? Get back here, we aren't done yet!"
#     return
#
# label FA_sex_beg_finish(the_person):
#     "Wait [the_person.mc_title], I'm going to cum soon and I just really need this... I'll do anything for you, just let me cum!"
#     return
#
# ## Role Specific Section ##
# label FA_improved_serum_unlock(the_person):
#     mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
#     the_person "Okay, how can I help?"
#     mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
#     "[the_person.title] smiles mischievously."
#     the_person "Well, I've got an idea in mind. It's risky, but I think it could really push our research to a new level."
#     mc.name "Go on, I'm interested."
#     the_person "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
#     the_person "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
#     return
#
