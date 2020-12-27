label stephanie_sex_toy_taboo_break(the_person):
    pass
    return

label stephanie_roleplay_taboo_break(the_person):
    pass
    return

label stephanie_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    the_person "Ohhh, a night with you all to myself? That sounds amazing..."
    "She runs her hand down your chest."
    return

label stephanie_sleepover_herplace_response(the_person): #Spending the night at her place
    if ashley_get_intro_complete(): #We have been introduced to Ashley
        the_person "Sounds good. I'll let Ash know you are coming over so she isn't surprised..."
    else:
        the_person "Wine sounds nice. I'll make sure I have something nice to wear."
        "[the_person.title] gives you a wink."
    return


label stephanie_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    the_person "I was hoping you would like it..."
    "[the_person.possessive_title] slowly walks over to you, her hips swaying enticingly."
    the_person "How do you want me? I'm yours for the night!"
    return


label stephanie_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Mmm, that hits the spot. Nothing like a nice drink to get the night started."
    "[the_person.title] takes a few long sips, draining most of her glass before setting it on the nightstand."
    the_person "I'm ready to get this started. How do you want me?"
    return

label stephanie_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person.char "Oh my god, I've lost count of how many times you've made me cum tonight..."
    "[the_person.title] lies down in bed and catches her breath."
    the_person.char "I think I can keep going... but you might need to be gentle!"
    return


label stephanie_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ahhh, you always make me feel so good..."
    "[the_person.title] lies down in bed and catches her breath."
    the_person.char "I'm ready to go again if you are!"
    return

label stephanie_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person.char "Glad we got that out of your system. Take a minute, then get ready to fuck me for real!"
    "You take some time to catch your breath, drink some water, and wait for your refractory period to pass."
    "You hold [the_person.title] in bed while she caresses you and touches herself, keeping herself ready for you."
    return
