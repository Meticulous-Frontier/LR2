#Camilla Teamups.

#planned teamups: Alexia is her main teamup. Starts with taking boudoir photos for her hubby, can end up taking them for MC
#If MC corrupts Camilla AND Alexia, have the option to have them both leave their SOs for MC at the same time.
#Alexia explores hotwifey lifestyle during team up. MC and encourage or discourage it.



init 1 python:
    def camilla_alexia_boudoir_intro_setup():   #Use this function to add the appropriate labels to the game for when boudoir photos can begin.
        if mc_business_has_expensive_camera() and alexia_is_model():
            alexia.add_unique_on_room_enter_event(camilla_alexia_boudoir_setup_intro)
        else:
            mc.business.add_mandatory_crisis(camilla_alexia_boudoir_setup_reminder)
        return

    camilla_alexia_boudoir_setup_reminder = Action("Boudoir Reminder", camilla_alexia_boudoir_setup_reminder_requirement, "camilla_alexia_boudoir_setup_reminder_label")
    camilla_alexia_boudoir_setup_intro = Action("Camilla at the bar", camilla_alexia_boudoir_setup_intro_requirement, "camilla_alexia_boudoir_setup_intro_label")


#Requirement Functions
init -1 python:
    def camilla_alexia_boudoir_setup_reminder_requirement():
        if mc_business_has_expensive_camera() and alexia_is_model():
            if time_of_day == 2 and renpy.random.randint(0,100) < 30:
                return True
        return False

    def camilla_alexia_boudoir_setup_intro_requirement(the_person):
        return False



#Labels

label camilla_alexia_boudoir_setup_reminder_label():
    "While working in your office, you start daydreaming about some of your recent sexual adventures."
    "Suddenly, you remember [camilla.possessive_title], and your conversation about taking boudoir photos of her when you helped her pickup out some lingerie."
    "Recently, you purchased a camera and have started taking pictures with [alexia.title]. Maybe you could talk to her about doing them?"
    $ camilla_alexia_boudoir_intro_setup()
    return

label camilla_alexia_boudoir_setup_intro_label(the_person):
    pass
    return




# Teamup wrapper functions
init 2 python:
    def mc_business_has_expensive_camera():
        return mc.business.event_triggers_dict.get("has_expensive_camera",False)

    def alexia_is_model():
        return alexia == mc.business.company_model

    def alexia_has_flirty_ad():
        if alexia_is_model():
            return alexia.event_triggers_dict.get("camera_flirt", False)
        return False

    def alexia_has_underwear_ad():
        if alexia_is_model():
            return alexia.event_triggers_dict.get("camera_flash", False)
        return False

    def alexia_has_nude_ad():
        if alexia_is_model():
            return alexia.event_triggers_dict.get("camera_naked", False)
        return False

    def alexia_has_blowjob_ad():
        if alexia_is_model():
            return alexia.event_triggers_dict.get("camera_suck", False)
        return False

    def alexia_has_sex_ad():
        if alexia_is_model():
            return alexia.event_triggers_dict.get("camera_fuck", False)
        return False
