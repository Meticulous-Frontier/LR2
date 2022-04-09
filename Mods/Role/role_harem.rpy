# Harem Role - girl is accepted into the harem and accepts that she is not the only love interest
# - requires Threesome and love higher than 80
# Things to Consider:
# - can make a harem, lovable, or slavable? currently its lovable as per default and most easiest to implement
# - knows of the others in your harem
# - can have girlfriend and affair roles - when suggested, they may become soley harem, or need to be slowly intergrated
# - girlfriend roles - suggestion to complete, may take time to accept.
# - if affair role - similar to gf role, if they leave SO = harem, continues affair as harem but for the children
# - Harem_Mansion - eventually a place where they all can live together?
# - Dialogs can be done way better than the way I did them XD
#
# ADDED to: \game\general_actions\interaction_actions\chat_actions.rpy
# make_harem_action = Action("Ask her to join your harem", requirement = ask_harem_requirement, effect = "ask_to_join_harem_label",
# menu_tooltip = "Ask her to start an official, polyamorous relationship and be part of your Harem.", priority = 10)
# chat_actions.append(make_harem_action)    
#
#ADDED to: \game\Mods\Screens\enhanced_map_manager.rpy
#ADDED to: \game\Mods\Screens\enhanced_main_choice_display.rpy
#  to show location of harem members
#
#ADDED to: game\game_roles\role_girlfriend.rpy
# - added exception to cousin/aunt role to become _girlfriend_role if they got pregnant so you could eventally add to harem
#
#ADDED to: \game\game_roles\_role_definitions.rpy
#         harem_role, cousin_girlfriend_role, aunt_girlfriend_role using #Sister specific girlfriend role.
# harem_role uses actions here in the role_harem.
# Tried to keep everything tied to this one file.
#
#
#ADDED new graphics - game\Mods\Room\rooms\background_images_replacement.rpy
# gf_token_small_image = im.Scale(Image(get_file_handle("girlfriend.png")), 18, 18)
# renpy.image("gf_token_small", gf_token_small_image)
#
# paramour_token_small_image = im.Scale(Image(get_file_handle("paramour.png")), 18, 18)
# renpy.image("paramour_token_small", paramour_token_small_image)
#
# harem_token_small_image = im.Scale(Image(get_file_handle("harem.png")), 18, 18)
# renpy.image("harem_token_small", harem_token_small_image)
#
#
# ADDED graphics to Mods\Core\images\gui\extra_images\
# = girlfriend.png, harem.png, paramour.png
#
# Would like the GF/Poly/Paramour icons added to the person headers in info ui full view etc.. 48x48 would be nice.
#- game\Mods\Screens\enhanced_person_info_ui.rpy
# I tried, but it shifted around too much, not familiar with the boxes in python
#
# THIS ALLOWS tracking the girlfriend/paramour/poly/tranced/aroused/babymomma around on the map
# Allows to add girlfriend/paramour to polyamorous relationship.
# MUST BE 80+ love, and likes threesomes >0 minimum.
# Must be either GF/Paramour to unlock Polyamory
# if Paramour joins Polyamory, they still are with their BF/husbands and can still leave them and join the poly.
# - this will open up a whole bunch of extra events we can add

init -1 python:
 
   def ask_harem_requirement(the_person):
        #you can convert a girlfriend or affair into a polymorous relationship
        if the_person.love >=80:
            if the_person.get_opinion_score("threesomes") > 0:
                if the_person.has_exact_role(harem_role): #either they are or not
                    return False
                else:
                    if the_person.has_role(affair_role):
                        return True
                    elif the_person.has_exact_role(girlfriend_role):
                        #kept special girlfriend roles for future
                        if the_person.has_role(sister_role) and the_person.event_triggers_dict.get("sister_girlfriend_waiting_for_blessing", False):
                            return false
                        elif the_person.has_role(mother_role) and the_person.event_triggers_dict.get("mom_girlfriend_waiting_for_blessing", False):
                            return false
                        elif the_person.has_role(aunt_role) and not the_person.has_role(aunt_girlfriend_role):
                            return false
                        elif the_person.has_role(cousin_role) and not the_person.has_role(aunt_girlfriend_role):
                            return false
                        else:
                            return True
                    else:
                        return False #not an affair or special girlfriend role
            else:
                return "Requires: 80 Love and positive opinion on Threesomes"
        else:
            if the_person.love < 60:
                return False
            elif the_person.love < 80:
                return "Requires: 80 Love"
            return False #But note that there are still failure conditions in the actual event, but those lead to hints about what do to to stop it.

   def harem_leave_SO_love_calculation(the_person): #Standalone calculation so we can use these values in multiple different events
        love_required = 80 - (the_person.get_opinion_score("cheating on men") * 10) #This should never be lower than the love requirement for her being your girlfriend.
        if the_person.relationship == "Fiancée":
            love_required += 10
        elif the_person.relationship == "Married":
            love_required += 20
        return love_required

   def harem_ask_leave_SO_requirement(the_person):
        if the_person.SO_name !=mc.name:
            love_required = harem_leave_SO_love_calculation(the_person)
            if the_person.love < love_required:
                return "Requires: " + str(love_required) + " Love"
            elif the_person.SO_name == mc.name:
                return False
        else:
            return False
            
   def get_harem_role_actions():
        ask_harem_break_up_action = Action("Break up with her", harem_break_up_requirement, "leave_harem_label", menu_tooltip = "Rip out her heart and stomp on it, will remove her from the Polyamory.")
        ask_harem_leave_SO_action = Action("Ask her to leave her significant other for you", harem_ask_leave_SO_requirement, "harem_ask_leave_SO_label", menu_tooltip = "This affair has been secret long enough! Ask her to leave her significant other and finally make her part of the flock!")
        ask_get_boobjob_action = Action("Ask her to get a boob job\n{color=#ff0000}{size=18}Costs: $7000{/size}{/color}", ask_get_boobjob_requirement, "ask_get_boobjob_label", menu_tooltip = "A little silicone goes a long way. Ask her to get breast enhancement surgery for you.")
        girlfriend_ask_trim_pubes_action = Action("Ask her to trim her pubes", girlfriend_ask_trim_pubes_requirement, "girlfriend_ask_trim_pubes_label", menu_tooltip = "Ask her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.")
        return [ask_get_boobjob_action, girlfriend_ask_trim_pubes_action, ask_harem_leave_SO_action, ask_harem_break_up_action]

   def get_harem_role_dates():
        plan_fuck_date_action = Action("Plan a fuck date at her place", fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = "Pick a night to go over there and spend nothing but \"quality time\" with each other.")
        girlfriend_shopping_date = Action("Go shopping together {image=gui/heart/Time_Advance.png}", shopping_date_requirement, "shopping_date_intro", menu_tooltip = "Take her to the mall and do some shopping together.")
        return [plan_fuck_date_action, girlfriend_shopping_date]

   def harem_break_up_requirement(the_person):
        #Set to only show up if happiness is below 100 or love is below 80, to keep it from popping up all the time
        if the_person.happiness<=100 or the_person.love <=80:
            return True
        else:
            return False


label leave_harem_label(the_person):
    # Stop being in a relationship.
    mc.name "[the_person.title], can we talk?"
    if the_person.happiness > 100:
        the_person "Sure, what's up?"
    else:
        the_person "Oh no, that's never good."

    mc.name "There's no easy way to say this, so I'll just say it: It's not working out."
    $ the_person.draw_person(emotion = "sad")
    #TODO: Add a variant where you've passed below the girlfriend threshold and she feels the same way.
    $ the_person.change_happiness(-(the_person.love - 40)) #TODO: Double check this vs. the girlfriend love threshold.
    "She seems to be in shock for a long moment, before slowly nodding her head."
    the_person "Okay... I don't know what to say."
    $ the_person.change_love(-10)
    mc.name "I'm sorry, but it's just the way things are."
    if the_person.has_role(girlfriend_role): 
       $ the_person.remove_role(girlfriend_role)
    if the_person.has_role(affair_role): 
       $ the_person.remove_role(affair_role)
    # she is not happy and will reset her obedience to 100
    $ the_person.change_stats(love = -20, happiness = -20, obedience = 100 - the_person.obedience)
    # she loses her submissive trait
    $ the_person.update_opinion_with_score("being submissive", 0)
    $ the_person.remove_role(harem_role)
    return
    
label harem_ask_leave_SO_label(the_person): #
    # Ask her to leave her significant other. Requires high love (and no negatively impactful opinions).
    # If successful, sets their SO to None (store it for future use in crises if we want), removes the affair role, and gives them the girlfriend role.

    mc.name "[the_person.title] can we talk about something?"
    the_person "You know I've always got five minutes for you."
    $ so_title = SO_relationship_to_title(the_person.relationship)
    mc.name "I want you to leave your [so_title] and join our polymorous completely."
    the_person "[the_person.mc_title]... Do you really mean that?"
    "You nod. She takes a long moment to think, then finally nods back and smiles happily."
    the_person "Okay, I'll do it for you!"
    call transform_affair(the_person) from _call_transform_affair_6
    $ the_person.change_love(10)
    $ the_person.change_obedience(5)
    $ the_person.draw_person(position = "kissing", emotion = "happy")
    "You put your arms around her waist and she kisses you immediately. When you break the kiss she's grinning ear to ear."
    $ the_person.draw_person(emotion = "happy")
    $ ex_title = so_title[:4] #Get's only the first 4 characters of any title for some hesitant-sounding speach.
    the_person "It feels so good to not have to hide anything anymore! I'll break the news to my [ex_title]... My ex-[so_title] later today."
    return
    
label ask_to_join_harem_label(the_person):
    #Requires high love, if successful she becomes your girlfriend (which unlocks many other options). Requires high love and her not being in a relationship.
    #Hide this event at low love, show it when it at it's lowest love possibility and let it fail out for specific reasons (thus informing the player WHY it failed out).
    #requires you have to make her a girlfriend/paramour before you can suggest harem
 #General dialogue used for everyone.
    mc.name "[the_person.title], can I talk to you about something important?"
    the_person "Of course. What's on your mind."
    mc.name "I've been thinking about this for a while. I really hope you feel as strongly as I do about us."
    mc.name "I want you to be part of something bigger, we both have alot of love to share."
    mc.name "I want us to be part of a strong and healthy polymorous relationship, do you accept?"
    "[the_person.possessive_title] takes a moment before responding."
    #you are already in a relationship with them, but want to make them accept the harem
    $ convinced = False
    if the_person.relationship=="Single" and not the_person.has_role(girlfriend_role):
        if the_person.get_opinion_score("threesomes") > 0:
            "[the_person.possessive_title] hesitates for a long moment. At long last she nods."
            "[the_person.possessive_title] leans forward and kisses you, putting an arm around your waist and pulling you close. When she breaks the kiss she looks deep into your eyes."
            the_person "Of course! [the_person.mc_title], the more the merrier!"
            the_person "I look forward to seeing our family grow!"
            $ convinced  = True
        else:
            the_person "I'm not ready yet [the_person.mc_title], I really like having you all to myself...."

    elif the_person.has_exact_role(girlfriend_role):
        the_person "Well, we are together already...."
        the_person "And I really like having you all to myself..."
        the_person "Including more into the mix?"
        if the_person.get_opinion_score("threesomes") > 0:
            "[the_person.possessive_title] hesitates for a long moment. At long last she nods."
            "[the_person.possessive_title] leans forward and kisses you, putting an arm around your waist and pulling you close. When she breaks the kiss she looks deep into your eyes."
            the_person "I look forward to seeing our growing family!"
            $ convinced  = True
            $ the_person.remove_role(girlfriend_role)
        else:
            the_person "I'm not ready yet [the_person.mc_title], I really like having you all to myself..."

    elif the_person.has_role(affair_role): #we keep the paramour til she is ready to leave the husband or told to by mc
        the_person "Well technically I'm already in a polymorous relationship, but I am the link."
        the_person "So it does make sense you want something more than what I can offer you..."
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "I mean, I already have a [so_title] and I can't just leave him like this."
        if the_person.get_opinion_score("threesomes") > 0:
            "[the_person.possessive_title] leans forward and kisses you, putting an arm around your waist and pulling you close. When she breaks the kiss she looks deep into your eyes."
            "[the_person.possessive_title] hesitates for a long moment. At long last she nods."
            the_person "I look forward to seeing what I can add to our growing family!"
            $ convinced  = True
            $ the_person.remove_role(girlfriend_role)
        else:
            the_person "I care about you a lot, but it's just not something I could do."
            the_person "Oh [the_person.mc_title], I'm so flattered, but you know that I have a [so_title]."
            if the_person.kids > 0:
                if the_person.kids > 1:
                    the_person "I would never dream of leaving him, and it would devastate our children."
                else:
                    the_person "I would never dream of leaving him, and it would devastate our child."
            else:
                the_person "I would never dream of leaving him."

    elif the_person.has_exact_role(sister_girlfriend_role) or the_person.has_exact_role(cousin_girlfriend_role):
        the_person "[the_person.mc_title], you do make me happy..."
        if the_person.get_opinion_score("threesomes") > 0:
            "She stares deep into your eyes as you take her hands and hold them in yours."
            mc.name "Just be with me [the_person.title]. It's that simple."
            "[the_person.possessive_title] hesitates for a long moment. At long last she nods."
            the_person "Okay, you're right. We've gone this far already..."
            $ convinced  = True
            if person.has_exact_role(sister_girlfriend_role): 
                $ person.remove_role(sister_girlfriend_role)
            if person.has_exact_role(cousin_girlfriend_role): 
                $ person.remove_role(cousin_girlfriend_role)
            if person.has_exact_role(girlfriend_role): 
                $ person.remove_role(girlfriend_role)
        else:
            the_person "I care about you a lot, but it's just not something I could do."
            the_person "Not sure if I'm ready to share you with others."
            mc.name "Remember [the_person.title], it won't be just me and you."
            mc.name "If you change your mind, I'll be here for you."

    elif the_person.has_exact_role(mom_girlfriend_role) or the_person.has_exact_role(aunt_girlfriend_role):
        the_person "A bigger family?"
        the_person "As long as you understand where we stand, I think we can be."
        if the_person.get_opinion_score("threesomes") > 0:
            "[the_person.possessive_title] stares deep into your eyes as you take her hands and hold them in yours."
            mc.name "Just be with me [the_person.title]. It's that simple."
            "[the_person.possessive_title] hesitates for a long moment. At long last she nods."
            the_person "Okay, you're right. We've gone this far already..."
            $ convinced  = True
            if person.has_exact_role(mom_girlfriend_role):
                $ person.remove_role(mom_girlfriend_role)
            if person.has_exact_role(aunt_girlfriend_role): 
                $ person.remove_role(aunt_girlfriend_role)
            if person.has_exact_role(girlfriend_role): 
                $ person.remove_role(girlfriend_role)
        else:
            the_person "I care about you a lot, we are family, that will never change."
            the_person "Adding more, I don't know? I need to think about it.."
    else:
        the_person "[the_person.possessive_title] taps her leg thinking about the pros and cons."
    
    if convinced: 
        # She agrees, you're now in a relationship! Congratulations!
        $ the_person.draw_person(emotion = "happy")
        $ the_person.change_happiness(15)
        $ the_person.change_love(5)
        if the_person.age > 40:
            the_person "Oh I'm so happy to hear you say that! I was worried about our age difference, but I don't want that to stop us!"
        the_person "Oh my god, I'm so happy! Yes, I want to be part of your flock!"
        "She puts her arms around you and pulls you close."
        $ the_person.draw_person(position = "kissing", emotion = "happy")
        $ mc.change_locked_clarity(10)
        "She kisses you, and you kiss her back just as happily."
        $ the_person.add_role(harem_role)
    else:
        the_person "Not sure if I'm ready to share you with others."
        mc.name "Remember [the_person.title], we will never be alone again."
        mc.name "If you change your mind, I'll be here for you."
            
    return
    