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
    def mc_serum_intro_requirement():
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


label mc_serum_intro_label():
    "In this label, we go through an introduction process for how MC begins taking serums that are specifically designed for him."
    "The Production assistant provides him with a serum to test that will increase his abilities slightly."
    "We also introduce the possibility of side effects, which are short lived negative stat consequences."
    $ mc.business.event_triggers_dict["mc_serum_energy_unlocked"] = True
    return

label mc_serum_timout_label():
    if mc.business.event_triggers_dict.get("serum_timout_reminder", True):
        if mc.business.prod_assistant:
            "You feel a bit different. Your personal serums have worn off. You should talk to [mc.business.prod_assistant.title] if you want to refresh them."
        else:
            "You feel a bit different. Your personal serums have worn off. However, you no longer have a Production Assistant."
            "You should consider assigning someone new to the position if you want to refresh your personal serums."
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
