#Production assistant helps MC create serum batches for personal consumption.
#Serum modifiers are unlocked after specific serum traits are researched and master to a specific mastery level to minimize the odds of side effects.
#This role starts initially being filled by Ashley, but if it becomes vacant via the storyline or other means, it can be filled by another girl.

init 1 python:
    #Action List
    mc_serum_intro = Action("Discover MC Serums",mc_serum_intro_requirement,"mc_serum_intro_label")
    mc_serum_timeout = Action("Serums runout",mc_serum_timeout_requirement,"mc_serum_timeout_label")
    mc_serum_review = Action("Review Personal Serums",mc_serum_review_requirement,"mc_serum_review_label", menu_tooltip = "Review your personal serum options, research progress, and refresh your dose.")
    prod_assistant_essential_oils = Action("Essential Oils Intro",prod_assistant_essential_oils_requirement,"prod_assistant_essential_oils_label")
    prod_assistant_unlock_auras = Action("Unlock Aura Personal Serums",prod_assistant_unlock_auras_requirement,"prod_assistant_unlock_auras_label")
    prod_assistant_unlock_cum = Action("Unlock Cum Personal Serums",prod_assistant_unlock_cum_requirement,"prod_assistant_unlock_cum_label")
    prod_assistant_unlock_physical = Action("Unlock Physical Personal Serums",prod_assistant_unlock_physical_requirement,"prod_assistant_unlock_physical_label")
    prod_assistant_energy_upgrade = Action("Upgrade Energy Serums",prod_assistant_energy_upgrade_requirement,"prod_assistant_energy_upgrade_label")
    prod_assistant_aura_upgrade = Action("Upgrade Aura Serums",prod_assistant_aura_upgrade_requirement,"prod_assistant_aura_upgrade_label")
    prod_assistant_cum_upgrade = Action("Upgrade Cum Serums",prod_assistant_cum_upgrade_requirement,"prod_assistant_cum_upgrade_label")
    prod_assistant_physical_upgrade = Action("Upgrade Physical Serums",prod_assistant_physical_upgrade_requirement,"prod_assistant_physical_upgrade_label")

    #The role
    prod_assistant_role = Role("Production Assistant", [mc_serum_review])

#Requirement functions
init -1 python:
    def mc_serum_intro_requirement(the_person):
        return False

    def mc_serum_timeout_requirement():
        return False

    def mc_serum_review_requirement(the_person):
        return True

    def prod_assistant_essential_oils_requirement(the_person):
        return False

    def prod_assistant_unlock_auras_requirement(the_person):

        return False

    def prod_assistant_unlock_cum_requirement(the_person):
        return False

    def prod_assistant_unlock_physical_requirement(the_person):
        return False

    def prod_assistant_energy_upgrade_requirement(the_person):
        return False

    def prod_assistant_aura_upgrade_requirement(the_person):
        return False

    def prod_assistant_cum_upgrade_requirement(the_person):
        return False

    def prod_assistant_physical_upgrade_requirement(the_person):
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
    "As you finish up with your drink, she changes the subject."
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
    the_person "That's too bad. I figured you would say that. But unfortunately, science stops for no man."
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
    $ mc.business.event_triggers_dict["mc_serum_energy_unlocked"] = True
    "You get up and step out of the serum production area."
    "You definitely feel conflicted about what just happened... but you have to admit, the prospect of getting your hands on serums that would enhance your personal performance is tempting."
    "You decide to go along with it for now, but you definitely need to keep a closer eye on [the_person.possessive_title] and her activities."
    return

label mc_serum_timout_label():

    return

label mc_serum_review_label(the_person):
    "In this label, we take a moment to talk about progress we've made on MC related serums."
    "Then we ask MC if he wants to change serum duration or max amount of serums at a time."
    "Then if we have a serum slot available pull up the MC serum screen."
    call screen mc_personal_serum_screen()
    "You have tested the serum screen."
    return

label prod_assistant_essential_oils_intro_label(the_person):
    "Mostly copy paste of the essential oils quest."
    "Tells MC to take these to head researcher to make a serum trait out of it."
    return

label prod_assistant_unlock_auras_label(the_person):
    "In this label, the production assistant has the idea from the essential oils for MC to gain pheremone auras."
    "Convinces MC to give them a try."
    "Unlocks auras in the MC Serum screen."
    $ mc.business.event_triggers_dict["mc_serum_aura_unlocked"] = True
    return

label prod_assistant_unlock_cum_label(the_person):
    "Production assistant has an idea. What if we put a concentrated pheremones into MC's cum."
    "Has a method that should be able to accomplish this."
    "Unlocks cum MC serums."
    $ mc.business.event_triggers_dict["mc_serum_cum_unlocked"] = True
    return

label prod_assistant_unlock_physical_label(the_person):
    "Production assistant comments that some of your serums are now altering many girls physical properties."
    "Asks if MC would be interested in trying some of the beneficial ones."
    "Unlocks physical MC serums."
    $ mc.business.event_triggers_dict["mc_serum_physical_unlocked"] = True
    return

label prod_assistant_energy_upgrade_label(the_person):
    "Use this label to start to process of upgrading energy serums."
    $ mc.business.event_triggers_dict["mc_serum_energy_tier"] = 1
    return

label prod_assistant_aura_upgrade_label(the_person):
    "Use this label to start to process of upgrading aura serums."
    $ mc.business.event_triggers_dict["mc_serum_aura_tier"] = 1
    return

label prod_assistant_cum_upgrade_label(the_person):
    "Use this label to start to process of upgrading cum serums."
    $ mc.business.event_triggers_dict["mc_serum_cum_tier"] = 1
    return

label prod_assistant_physical_upgrade_label(the_person):
    "Use this label to start to process of upgrading physical serums."
    $ mc.business.event_triggers_dict["mc_serum_physical_tier"] = 0
    return
