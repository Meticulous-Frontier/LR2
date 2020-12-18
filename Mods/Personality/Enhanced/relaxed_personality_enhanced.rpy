label relaxed_sex_toy_taboo_break(the_person):
    pass
    return

label relaxed_roleplay_taboo_break(the_person):
    pass
    return

label relaxed_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.sluttiness < 80:
        the_person "Sounds great! Save some energy, we can make it a fun night."
    else:
        the_person "Are you having the same dirty urges as me? Save some energy for me. We can make it a great night!"
    return

label relaxed_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.sluttiness < 80:
        the_person "Mmm, that sounds great! Bring a toothbrush, you can spend the night."
    else:
        the_person "You don't need the wine to seduce me. "
    return


label relaxed_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    "[the_person.title] slowly walks over to you, purposefully exaggerating her hip movements with each step."
    the_person "Thanks... you ready for some fun?"
    return


label relaxed_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Mmm... what do you say we stay in and just cuddle tonight?"
    "She gives you a smirk. You can't help but frown at the thought of just cuddling..."
    the_person "Hah! Oh my god, you should have seen your face..."
    "She sets her wine down on her nightstand."
    the_person "Get over here! I'm ready for some fun!"
    return

label relaxed_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person.char "Oh my god, you're making me cum my brains out... this is amazing..."
    "[the_person.title] lies down in bed and catches her breath."
    the_person.char "I think I can keep going... I'm gonna be sore in the morning though!"
    return


label relaxed_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ahhh, that was nice..."
    "[the_person.title] lies down in bed and catches her breath."
    the_person.char "I'm ready to go again if you are!"
    return

label relaxed_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person.char "Whew, good job. Get some water and let's go for another!"
    "You take some time to catch your breath, drink some water, and wait for your refractory period to pass."
    "You hold [the_person.title] in bed while she caresses you and touches herself, keeping herself ready for you."
    return
