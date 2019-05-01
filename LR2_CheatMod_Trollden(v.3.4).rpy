init python:
    config.overlay_screens = ["keybind"]
    config.console = True # Enables the console, can be set to False.

screen keybind(): # Change the key "" to whatever you want to open / close the cheat menu

    key "z" action [Function(cheat_default_person), ToggleScreen("cm"), Hide("cmmc"), Hide("cmoc"), Hide("cmc"), Hide("cmw")] # Runs the define_a_person function to prevent issues with the_person not being defined, also hides all of the main screens if they are visible.
    key "Z" action [Function(cheat_default_person), ToggleScreen("cm"), Hide("cmmc"), Hide("cmoc"), Hide("cmc"), Hide("cmw")]

init python: # This space is reserved for variables used to display and hide vbox(es) and hbox(es) later on in the code, it was the easiest way for me to do it.
    # The variables that are singled out act as a parent for the cluster below, imagine a tree view. In other words the singled variable has to be true in order for the children to show e.g capp and capph needs to be true for capph to show.

    # Miscellanious - Start

    the_person = None # Intended to prevent the_person is not defined errors
    person_choice = None # Intended to prevent person_choice is not defined errors

    cml = None # Handles the whether the crisis master list should be visible or hidden
    cmlpage = 1 # Defines which page is shown in the crisis master list, defaults to one.

    # Miscellanious - End

    # Other Characters - Start

    capp = None # Shows the_person appearance section and allows the following buttons:

    capph = None # Hair style
    capphc = None # Hair color
    capphcp = 1 # Hair color selection page
    cappf = None # Face
    cappt = None # Tits
    cappb = None # Body
    capps = None # Skin

    cpy = None # Shows the_person personality section and allows the following buttons:

    cpyt = None # Personality Type
    cmlypage = 1 # Tracks pages for the_person's opinions
    cmlyspage = 1 # Tracks pages for the_person's sexy_opinions
    cpyo = None # Personality Opinions
    cpyso = None # Personality Sexy Opinions

    cemp = None # Shows the_person employment section and allows the following buttons:

    # Other Characters - End

    # Business (Company) - Start

    bmm = None # Shows the mc.business section and allows the following buttons:

    bmme = None # Economy
    bmmr = None # Research

    # Business (Company) - End

init python: # This space is reserved for definitions used to simplify the code

    # Definitions - Start

    def cheat_serum_traits(): # Researches all the traits in list_of_traits
        for trait in list_of_traits:
            if trait.tier =< mc.business.research_tier:
                trait.researched = True

    def cheat_default_person(): # Ensures that a person with valid attributes is always set
                                # TODO: Come up with a simular solution that remembers the last person you interacted with, but also replaces whenever a new person is in focus e.g during crisis.
        global the_person       # I want to modify the_person outside of the function
        if the_person == None:
            the_person = lily   # Using the lily pre-made character as it is always present in the world.
        elif the_person == person_choice:
            the_person = person_choice

    def cheat_salary_expectations():

        for people in (mc.business.market_team + mc.business.production_team + mc.business.research_team + mc.business.supply_team + mc.business.hr_team):
            people.salary = people.calculate_base_salary()

    def cheat_salary_pay_raise():

        for people in (mc.business.market_team + mc.business.production_team + mc.business.research_team + mc.business.supply_team + mc.business.hr_team):
            people.salary = (people.calculate_base_salary()) * (1.1)

    def cheat_salary_deduction():

        for people in (mc.business.market_team + mc.business.production_team + mc.business.research_team + mc.business.supply_team + mc.business.hr_team):
            people.salary = (people.calculate_base_salary()) * (0.9)

    def cheat_policies_unlock():

        for policy in (uniform_policies_list + recruitment_policies_list + serum_policies_list + organisation_policies_list):
            if policy not in mc.business.policy_list:
                mc.business.policy_list.append(policy)

        for policy in mc.business.policy_list:
            if policy.on_buy_function is not None:
                policy.on_buy_function(**policy.on_buy_arguments)



#        batch_size_increase(increase_amount = 5)
#        add_production_lines(3)
#        increase_max_employee_size(33)

    def cheat_hire_person(): # Takes care of the rudamentary work behind assigning a job to a character when called.
                             # It makes the assumption that the_person.job is set, this is taken care of by a textbutton when called.


        if the_person.job == "Researcher":
            mc.business.add_employee_research(the_person) # Add the_person to the employee overview
            mc.business.r_div.add_person(the_person) # Add the_person to the r_div (research division)
            the_person.set_work([1,2,3], mc.business.r_div) # Set their schedule and work location
            the_person.special_role.append(employee_role) # Append the employee_role to enable corresponding special actions

        elif the_person.job =="Production":
            mc.business.add_employee_production(the_person)
            mc.business.p_div.add_person(the_person)
            the_person.set_work([0,1,2,3,4], mc.business.p_div)
            the_person.special_role.append(employee_role)

        elif the_person.job == "Supply":
            mc.business.add_employee_supply(the_person)
            mc.business.s_div.add_person(the_person)
            the_person.set_work([1,2,3], mc.business.s_div)
            the_person.special_role.append(employee_role)

        elif the_person.job == "Marketing":
            mc.business.add_employee_marketing(the_person)
            mc.business.m_div.add_person(the_person)
            the_person.set_work([1,2,3], mc.business.m_div)
            the_person.special_role.append(employee_role)

        elif the_person.job == "Human Resources":
            mc.business.add_employee_hr(the_person)
            mc.business.h_div.add_person(the_person)
            the_person.set_work([1,2,3], mc.business.h_div)
            the_person.special_role.append(employee_role)

    def cheat_fire_employee(): # Fire a person via the cheat menu, this does not remove them from the world, but changes their schedule to not include the work place.

        if the_person in mc.business.research_team: # Check if they are in this team

            mc.business.research_team.remove(the_person) # Remove them from the division / team
            the_person.set_work(None,None) # Free up their schedule
            the_person.special_role.remove(employee_role) # Remove the special role so they no longer have the "Special Actions..."
            the_person.job = None # Sets their job description to None, could be replaced with e.g "Unemployeed"

        elif the_person in mc.business.production_team:

            mc.business.production_team.remove(the_person)
            the_person.set_work(None,None)
            the_person.special_role.remove(employee_role)
            the_person.job = None

        elif the_person in mc.business.supply_team:

            mc.business.supply_team.remove(the_person)
            the_person.set_work(None,None)
            the_person.special_role.remove(employee_role)
            the_person.job = None

        elif the_person in mc.business.market_team:

            mc.business.market_team.remove(the_person)
            the_person.set_work(None,None)
            the_person.special_role.remove(employee_role)
            the_person.job = None

        elif the_person in mc.business.hr_team:

            mc.business.hr_team.remove(the_person)
            the_person.set_work(None,None)
            the_person.special_role.remove(employee_role)
            the_person.job = None

    def cheat_redraw_hair(): # Call this whenever you have made changes to the hair style or hair color
                             # NOTE:  You can define your own colors here by following the established format.
                             #        It makes the assumption that the_person.hair_colour is set.

        if the_person.hair_colour == "blond":
             the_person.hair_style.colour = [0.84,0.75,0.47,1] # Hair color is in normalized RGB decimal format. [R, G, B, Alpha]

        elif the_person.hair_colour == "brown":
             the_person.hair_style.colour = [0.73,0.43,0.24,1]

        elif the_person.hair_colour == "black":
             the_person.hair_style.colour = [0.1,0.09,0.08,1]

        elif the_person.hair_colour == "red":
             the_person.hair_style.colour = [0.3,0.05,0.05,1]

        elif the_person.hair_colour == "hot pink": # Custom Color
             the_person.hair_style.colour = [1,0.5,0.8,1]

        elif the_person.hair_colour == "sky blue": # Custom Color
             the_person.hair_style.colour = [0.4,0.5,0.9,1]

        elif the_person.hair_colour == "test color 1": # Custom Color
             the_person.hair_style.colour = [0.882, 0.733, 0.580,1]

        elif the_person.hair_colour == "test color 2": # Custom Color
             the_person.hair_style.colour = [0.270, 0.549, 0.274,1]

        elif the_person.hair_colour == "test color 3": # Custom Color
             the_person.hair_style.colour = [0.717, 0.8, 0.8,1]

        elif the_person.hair_colour == "test color 4": # Custom Color
             the_person.hair_style.colour = [0.717, 0.360, 0.839,1]

        the_person.draw_person(the_person.hair_style)

    def cheat_redraw_face(): # Redraws the face with the matching skin colour
        if the_person.face_style == "Face_1": # Variations of Face Style 1
            if the_person.skin == "white":
                 the_person.expression_images = Expression("default","white","Face_1")

            elif the_person.skin == "tan":
                 the_person.expression_images = Expression("default","tan","Face_1")

            elif the_person.skin == "black":
                 the_person.expression_images = Expression("default","black","Face_1")

        elif the_person.face_style == "Face_2": # Variations of Face Style 2
            if the_person.skin == "white":
                 the_person.expression_images = Expression("default","white","Face_2")

            elif the_person.skin == "tan":
                 the_person.expression_images = Expression("default","tan","Face_2")

            elif the_person.skin == "black":
                 the_person.expression_images = Expression("default","black","Face_2")

        elif the_person.face_style == "Face_3": # Variations of Face Style 3
            if the_person.skin == "white":
                 the_person.expression_images = Expression("default","white","Face_3")

            elif the_person.skin == "tan":
                 the_person.expression_images = Expression("default","tan","Face_3")

            elif the_person.skin == "black":
                 the_person.expression_images = Expression("default","black","Face_3")

        elif the_person.face_style == "Face_4": # Variations of Face Style 4
            if the_person.skin == "white":
                 the_person.expression_images = Expression("default","white","Face_4")

            elif the_person.skin == "tan":
                 the_person.expression_images = Expression("default","tan","Face_4")

            elif the_person.skin == "black":
                 the_person.expression_images = Expression("default","black","Face_4")

        elif the_person.face_style == "Face_5": # Variations of Face Style 5
            if the_person.skin == "white":
                 the_person.expression_images = Expression("default","white","Face_5")

            elif the_person.skin == "tan":
                 the_person.expression_images = Expression("default","tan","Face_5")

            elif the_person.skin == "black":
                 the_person.expression_images = Expression("default","black","Face_5")

        elif the_person.face_style == "Face_6": # Variations of Face Style 6
            if the_person.skin == "white":
                 the_person.expression_images = Expression("default","white","Face_6")

            elif the_person.skin == "tan":
                 the_person.expression_images = Expression("default","tan","Face_6")

            elif the_person.skin == "black":
                 the_person.expression_images = Expression("default","black","Face_6")
        the_person.draw_person(the_person.face_style) # Always redraw the face_style

    def cheat_redraw_breasts(): # Redraws the breasts / tits
        the_person.draw_person(the_person.tits)

    def cheat_redraw_body(): # Redraws the body
        the_person.draw_person(the_person.body_type)

    def cheat_redraw_skin(): # Redraws the skin color
        the_person.draw_person(the_person.skin)

    # Definitions - End

# Styles - Start

init -2 style cheatbutton_style: # Cheat Button Style
    background "#000080"
    insensitive_background "#222222"
    hover_background "#aaaaaa"

init -2 style cheattext_style: # Cheat Text Style
    text_align 0.5
    size 14
    color "#dddddd"
    outlines [(2,"#222222",0,0)]

# Styles - End

# Screens - Start
# NOTE: This is the main part of the cheat and handles everything from frames, boxes, buttons, positions and toggling of variables. It will be cluttered, so keep it consistent.

screen cm(): # Overlaps the screen "screen goal_hud_ui():" in script.rpy
                    # Textbuttons are bound to an action (left click) and an alternate (right click) that increases or decreases value(s)
                    # Tooltips are text that show when hovering the button

    zorder 49 # Keep zorder below 50 to allow tooltips to properly display
    frame:
        background "Goal_Frame_1.png"
        yalign 0.5
        xsize 260
        ysize 250
        vbox:
            spacing -5
            textbutton "Cheat Menu" action [ToggleScreen("cm"), Hide("cmmc"), Hide("cmoc"), Hide("cmc"), Hide("cmw")] style "textbutton_style" text_style "textbutton_text_style" xsize 245 text_xalign 0.5 tooltip "Hides the cheat menu"

            textbutton "Main Character" action [ToggleScreen("cmmc"), Hide("cmoc"), Hide("cmc"), Hide("cmw")] style "textbutton_style" text_style "textbutton_text_style" xsize 245 tooltip "Cheats for the main character"

            textbutton "Edit: [the_person.name]" action [ToggleScreen("cmoc"), Hide("cmmc"), Hide("cmc"), Hide("cmw")] style "textbutton_style" text_style "textbutton_text_style" xsize 245 tooltip "Cheats for other characters"

            textbutton "Company" action [ToggleScreen("cmc"), Hide("cmoc"), Hide("cmmc"), Hide("cmw")] style "textbutton_style" text_style "textbutton_text_style" xsize 245

            textbutton "World" action [ToggleScreen("cmw"), Hide("cmoc"), Hide("cmmc"), Hide("cmc")] style "textbutton_style" text_style "textbutton_text_style" xsize 245

screen cmmc():
    zorder 49
    frame: # top frame
        background im.Scale("Goal_Frame_1.png", 900, 195) # Scales the image to a size fitting the frame it is contained within
        xsize 900
        ysize 195
        yalign 0.225
        xalign 0.5
        hbox:
            xalign 0.08
            vbox: # Main stats

                textbutton "Name: [mc.name]" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                textbutton "Main Stats" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

                textbutton "Charisma: [mc.charisma]" action SetField(mc,"charisma", mc.charisma + 1) alternate SetField(mc,"charisma", mc.charisma - 1)  style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Intelligence: [mc.int]" action SetField(mc,"int", mc.int + 1) alternate SetField(mc,"int", mc.int - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Focus: [mc.focus]" action SetField(mc,"focus", mc.focus + 1) alternate SetField(mc,"focus", mc.focus - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Stamina: [mc.current_stamina]" action [SetField(mc,"max_stamina", mc.max_stamina + 1), SetField(mc,"current_stamina", mc.max_stamina + 1)] alternate [SetField(mc,"max_stamina", mc.max_stamina - 1), SetField(mc,"current_stamina", mc.max_stamina - 1)] style "cheatbutton_style" text_style "cheattext_style" xsize 220

            vbox: # Work skills
                textbutton "Work Skills" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

                textbutton "Human Resources: [mc.hr_skill]" action SetField(mc,"hr_skill", mc.hr_skill + 1) alternate SetField(mc,"hr_skill", mc.hr_skill - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Marketing: [mc.market_skill]" action SetField(mc,"market_skill", mc.market_skill + 1) alternate SetField(mc,"market_skill", mc.market_skill - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Research: [mc.research_skill]" action SetField(mc,"research_skill", mc.research_skill + 1) alternate SetField(mc,"research_skill", mc.research_skill - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Production: [mc.production_skill]" action SetField(mc,"production_skill", mc.production_skill + 1) alternate SetField(mc,"production_skill", mc.production_skill - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Supply Procurement: [mc.supply_skill]" action SetField(mc,"supply_skill", mc.supply_skill + 1) alternate SetField(mc,"supply_skill", mc.supply_skill - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220

            vbox: # Sex skills
                textbutton "Sex Skills" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

                textbutton "Foreplay: [mc.sex_skills[Foreplay]]" action SetDict(mc.sex_skills, "Foreplay", mc.sex_skills["Foreplay"] + 1) alternate SetDict(mc.sex_skills, "Foreplay", mc.sex_skills["Foreplay"] - 1)  style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Oral: [mc.sex_skills[Oral]]" action SetDict(mc.sex_skills, "Oral", mc.sex_skills["Oral"] + 1) alternate SetDict(mc.sex_skills, "Oral", mc.sex_skills["Oral"] - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Vaginal: [mc.sex_skills[Vaginal]]" action SetDict(mc.sex_skills, "Vaginal", mc.sex_skills["Vaginal"] + 1) alternate SetDict(mc.sex_skills, "Vaginal", mc.sex_skills["Vaginal"] - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Anal: [mc.sex_skills[Anal]]" action SetDict(mc.sex_skills, "Anal", mc.sex_skills["Anal"] + 1) alternate SetDict(mc.sex_skills, "Anal", mc.sex_skills["Anal"] - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Arousal: [mc.arousal]" action SetField(mc,"arousal", mc.arousal + 50) alternate SetField(mc,"arousal", mc.arousal - 50) style "cheatbutton_style" text_style "cheattext_style" xsize 220

screen cmoc():
    zorder 49
    frame: # Top Frame
        background im.Scale("Goal_Frame_1.png", 900, 195) # Scales the image to a size fitting the frame it is contained within
        xsize 900
        ysize 195
        yalign 0.225
        xalign 0.5
        hbox:
            xalign 0.08
            vbox: # the_person main stats

                textbutton "Name: [the_person.name]" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                textbutton "Main Stats" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

                textbutton "Charisma: [the_person.charisma]" action SetField(the_person,"charisma", the_person.charisma + 1) alternate SetField(the_person,"charisma", the_person.charisma - 1)  style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Intelligence: [the_person.int]" action SetField(the_person,"int", the_person.int + 1) alternate SetField(the_person,"int", the_person.int - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Focus: [the_person.focus]" action SetField(the_person,"focus", the_person.focus + 1) alternate SetField(the_person,"focus", the_person.focus - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                #textbutton "Stamina: [the_person.current_stamina]" action [SetField(the_person,"max_stamina", the_person.max_stamina + 1), SetField(the_person,"current_stamina", the_person.max_stamina + 1)] alternate [SetField(the_person,"max_stamina", the_person.max_stamina - 1), SetField(the_person,"current_stamina", the_person.max_stamina - 1)] style "cheatbutton_style" text_style "cheattext_style" xsize 220

            vbox: # the_person work skills
                textbutton "Work Skills" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

                textbutton "Human Resources: [the_person.hr_skill]" action SetField(the_person,"hr_skill", the_person.hr_skill + 1) alternate SetField(the_person,"hr_skill", the_person.hr_skill - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Marketing: [the_person.market_skill]" action SetField(the_person,"market_skill", the_person.market_skill + 1) alternate SetField(the_person,"market_skill", the_person.market_skill - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Research: [the_person.research_skill]" action SetField(the_person,"research_skill", the_person.research_skill + 1) alternate SetField(the_person,"research_skill", the_person.research_skill - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Production: [the_person.production_skill]" action SetField(the_person,"production_skill", the_person.production_skill + 1) alternate SetField(the_person,"production_skill", the_person.production_skill - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Supply Procurement: [the_person.supply_skill]" action SetField(the_person,"supply_skill", the_person.supply_skill + 1) alternate SetField(the_person,"supply_skill", the_person.supply_skill - 1) style "cheatbutton_style" text_style "cheattext_style" xsize 220

            vbox: # the_person sex skills
                textbutton "Sex Skills" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

                textbutton "Foreplay: [the_person.sex_skills[Foreplay]]" action SetDict(the_person.sex_skills, "Foreplay", the_person.sex_skills["Foreplay"] +1) alternate SetDict(the_person.sex_skills, "Foreplay", the_person.sex_skills["Foreplay"] -1)  style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Oral: [the_person.sex_skills[Oral]]" action SetDict(the_person.sex_skills, "Oral", the_person.sex_skills["Oral"] +1) alternate SetDict(the_person.sex_skills, "Oral", the_person.sex_skills["Oral"] -1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Vaginal: [the_person.sex_skills[Vaginal]]" action SetDict(the_person.sex_skills, "Vaginal", the_person.sex_skills["Vaginal"] +1) alternate SetDict(the_person.sex_skills, "Vaginal", the_person.sex_skills["Vaginal"] -1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Anal: [the_person.sex_skills[Anal]]" action SetDict(the_person.sex_skills, "Anal", the_person.sex_skills["Anal"] +1) alternate SetDict(the_person.sex_skills, "Anal", the_person.sex_skills["Anal"] -1) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Arousal: [the_person.arousal]" action SetField(the_person,"arousal", the_person.arousal + 25) alternate SetField(the_person,"arousal", the_person.arousal - 25) style "cheatbutton_style" text_style "cheattext_style" xsize 220

            vbox: # the_person relations
                textbutton "Relations" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

                textbutton "Happiness: [the_person.happiness]" action SetField(the_person, "happiness", the_person.happiness + 10) alternate SetField(the_person, "happiness", the_person.happiness - 10) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Love: [the_person.love]" action SetField(the_person, "love", the_person.love + 10) alternate SetField(the_person, "love", the_person.love - 10) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Suggestibility: [the_person.suggestibility]" action SetField(the_person, "suggestibility", the_person.suggestibility + 50) alternate SetField(the_person, "suggestibility", the_person.suggestibility - 50) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Sluttiness: [the_person.sluttiness]" action SetField(the_person, "sluttiness", the_person.sluttiness + 10) alternate SetField(the_person, "sluttiness", the_person.sluttiness - 10) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Core Sluttiness: [the_person.core_sluttiness]" action SetField(the_person, "core_sluttiness", the_person.core_sluttiness + 10) alternate SetField(the_person, "core_sluttiness", the_person.core_sluttiness - 10) style "cheatbutton_style" text_style "cheattext_style" xsize 220
                textbutton "Obedience: [the_person.obedience]" action SetField(the_person, "obedience", the_person.obedience + 25) alternate SetField(the_person, "obedience", the_person.obedience - 25) style "cheatbutton_style" text_style "cheattext_style" xsize 220

    frame: # Bottom frame
        background im.Scale("Goal_Frame_1.png", 1165, 200) # Scales the image to a size fitting the frame it is contained within
        xsize 1165
        ysize 200
        yalign 1.0
        xalign 0.529
        hbox:
            xalign 0.029
            vbox: # Bottom frame menu

                textbutton "Appearance" action ToggleVariable("capp") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

                textbutton "Personality" action ToggleVariable("cpy") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

                textbutton "Employment" action ToggleVariable("cemp") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

            if cemp: # Employment options
                hbox:
                    vbox:
                        textbutton "Job: [the_person.job]" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Set Marketing" action [SetField(the_person, "job", "Marketing"), Function(cheat_hire_person)] alternate [Function(cheat_fire_employee)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Set Production" action [SetField(the_person, "job", "Production"), Function(cheat_hire_person)] alternate [Function(cheat_fire_employee)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                    vbox:
                        textbutton "Set Research" action [SetField(the_person, "job", "Researcher"), Function(cheat_hire_person)] alternate [Function(cheat_fire_employee)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Set Supply" action [SetField(the_person, "job", "Supply"), Function(cheat_hire_person)] alternate [Function(cheat_fire_employee)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Set HR" action [SetField(the_person, "job", "Human Resources"), Function(cheat_hire_person)] alternate [Function(cheat_fire_employee)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

            if capp: # Appearance sections
                vbox:

                    textbutton "Hair Styles" action ToggleVariable("capph") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 # Expands to hairstyles
                    textbutton "Hair Color" action ToggleVariable("capphc") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 # Expands to hair color
                    textbutton "Face" action ToggleVariable("cappf") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 # Expands to faces
                    textbutton "Breasts" action ToggleVariable("cappt") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 # Expands to breasts
                    textbutton "Body" action ToggleVariable("cappb") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 # Expands to body
                    textbutton "Skin Color" action ToggleVariable("capps") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 # Expands to skin color

            if capp and capph: # Hair Style Options
                hbox:
                    vbox: # Column 1

                        textbutton "Short Hair" action [SetField(the_person,"hair_style", short_hair), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Ponytail" action [SetField(the_person,"hair_style", ponytail), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Messy Ponytail" action [SetField(the_person,"hair_style", messy_ponytail), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Messy Short Hair" action [SetField(the_person,"hair_style", messy_short_hair), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Messy Long Hair" action [SetField(the_person,"hair_style", messy_hair), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Shaved Side Hair" action [SetField(the_person,"hair_style", shaved_side_hair), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                    vbox: # Column 2

                        textbutton "Twin Ponytails" action [SetField(the_person,"hair_style", twintail), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Long Hair" action [SetField(the_person,"hair_style", long_hair), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Bow Hair" action [SetField(the_person,"hair_style", bow_hair), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

            if capp and capphc: # Hair Color Options
                hbox:
                    vbox: # Column 1, reserved for vanilla hair colors
                        textbutton "Blond Color" action [SetField(the_person,"hair_colour", "blond"), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Brown Color" action [SetField(the_person,"hair_colour", "brown"), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Black Color" action [SetField(the_person,"hair_colour", "black"), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Red Color" action [SetField(the_person,"hair_colour", "red"), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                    vbox: # Column 2,  reserved for custom hair colors
                        textbutton "Hot Pink Color" action [SetField(the_person,"hair_colour", "hot pink"), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Sky Blue Color" action [SetField(the_person,"hair_colour", "sky blue"), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Test Color 1" action [SetField(the_person,"hair_colour", "test color 1"), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Test Color 2" action [SetField(the_person,"hair_colour", "test color 2"), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Test Color 3" action [SetField(the_person,"hair_colour", "test color 3"), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Test Color 4" action [SetField(the_person,"hair_colour", "test color 4"), Function(cheat_redraw_hair)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

            if capp and cappf: # Face Type Options
                hbox:
                    vbox: # Column 1
                        textbutton "Face Type 1" action [SetField(the_person,"face_style", "Face_1"), Function(cheat_redraw_face)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Face Type 2" action [SetField(the_person,"face_style", "Face_2"), Function(cheat_redraw_face)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Face Type 3" action [SetField(the_person,"face_style", "Face_3"), Function(cheat_redraw_face)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                    vbox: # Column 2
                        textbutton "Face Type 4" action [SetField(the_person,"face_style", "Face_4"), Function(cheat_redraw_face)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Face Type 5" action [SetField(the_person,"face_style", "Face_5"), Function(cheat_redraw_face)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Face Type 6" action [SetField(the_person,"face_style", "Face_6"), Function(cheat_redraw_face)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

            if capp and cappt: # Breast Size Options
                hbox:
                    vbox: # Column 1
                        textbutton "A Cups" action [SetField(the_person,"tits", "A"), Function(cheat_redraw_breasts)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "AA Cups" action [SetField(the_person,"tits", "AA"), Function(cheat_redraw_breasts)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "B Cups" action [SetField(the_person,"tits", "B"), Function(cheat_redraw_breasts)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "C Cups" action [SetField(the_person,"tits", "C"), Function(cheat_redraw_breasts)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "D Cups" action [SetField(the_person,"tits", "D"), Function(cheat_redraw_breasts)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "DD Cups" action [SetField(the_person,"tits", "DD"), Function(cheat_redraw_breasts)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                    vbox: # Column 2
                        textbutton "DDD Cups" action [SetField(the_person,"tits", "DDD"), Function(cheat_redraw_breasts)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "E Cups" action [SetField(the_person,"tits", "E"), Function(cheat_redraw_breasts)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "F Cups" action [SetField(the_person,"tits", "F"), Function(cheat_redraw_breasts)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "FF Cups" action [SetField(the_person,"tits", "FF"), Function(cheat_redraw_breasts)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

            if capp and cappb: # Body Type Options
                hbox:
                    vbox: # Column 1
                        textbutton "Thin Body" action [SetField(the_person,"body_type", "thin_body"), Function(cheat_redraw_body)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Standard Body" action [SetField(the_person,"body_type", "standard_body"), Function(cheat_redraw_body)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Curvy Body" action [SetField(the_person,"body_type", "curvy_body"), Function(cheat_redraw_body)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                    vbox: # Column 2, unused
                        pass

            if capp and capps: # Skin Color Options
                hbox:
                    vbox: # Column 1
                        textbutton "White Skin" action [SetField(the_person,"body_images", white_skin), SetField(the_person,"skin", "white"), Function(cheat_redraw_skin)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Tan Skin" action [SetField(the_person,"body_images", tan_skin), SetField(the_person,"skin", "tan"), Function(cheat_redraw_skin)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                        textbutton "Black Skin" action [SetField(the_person,"body_images", black_skin), SetField(the_person,"skin", "black"), Function(cheat_redraw_skin)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                    vbox: # Column 2, unused
                        pass

            if cpy: # Personality Related Options
                vbox:
                    textbutton "Personality Type" action ToggleVariable("cpyt") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 # Expands to hairstyles
                    textbutton "Opinions" action ToggleVariable("cpyo") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Not implemented, sorry" # Expands to opinions
                    textbutton "Sexy Opinions" action ToggleVariable("cpyso") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Not implemented, sorry" # Expands to sexy opinions

                    textbutton "Next Page: [cmlypage]" action [If(cmlypage == 3, true = SetVariable("cmlypage", cmlypage - 2), false = SetVariable("cmlypage", cmlypage + 1))] alternate [If(cmlypage == 1, true = SetVariable("cmlypage", cmlypage + 2), false = SetVariable("cmlypage", cmlypage - 1))] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Shift through pages"

#            if cpy and cpyo: # the_person.opinions
#                hbox:
#                    if cmlypage == 1:
#                        vbox:
#                            textbutton "skirts [the_person.opinions["skirts"]]" action NullAction() style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip ""
#
#                        vbox:
#                            pass
#                    if cmlypage == 2:
#                        vbox:
#                            pass
#
#                    if cmlypage == 3:
#                        vbox:
#                            pass
#
#            if cpy and cpyso: # the_person.sexy_opinions
#                hbox:
#                    vbox:
#                        pass




            if cpy and cpyt: # Personality Type selection
                hbox:
                    vbox:
                        textbutton "Current: [the_person.personality.personality_type_prefix]" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 250
                        textbutton "Relaxed Personality" action [SetField(the_person,"personality", relaxed_personality)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 250
                        textbutton "Reserved Personality" action [SetField(the_person,"personality", reserved_personality)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 250
                        textbutton "Wild Personality" action [SetField(the_person,"personality", wild_personality)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 250
                        textbutton "Bimbo Personality" action [SetField(the_person,"personality", bimbo_personality)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 250
                        textbutton "Stephanie's Personality" action [SetField(the_person,"personality", stephanie_personality)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 250
                    vbox:
                        textbutton "Sister's Personality" action [SetField(the_person,"personality", lily_personality)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 250
                        textbutton "Mom's Personality" action [SetField(the_person,"personality", mom_personality)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 250

screen cmc(): # Cheats for business / company
    zorder 49
    frame: # Top Frame
        background im.Scale("Goal_Frame_1.png", 900, 195) # Scales the image to a size fitting the frame it is contained within
        xsize 900
        ysize 195
        yalign 0.225
        xalign 0.5
        hbox:
            xalign 0.02
            vbox:
                textbutton "Funds: $[mc.business.funds]" action SetField(mc.business, "funds", mc.business.funds + 10000) alternate SetField(mc.business, "funds", mc.business.funds - 10000)  style "cheatbutton_style" text_style "textbutton_text_style" xsize 230
                textbutton "Supplies: [mc.business.supply_count]" action SetField(mc.business, "supply_count", mc.business.supply_count + 10000) alternate SetField(mc.business, "supply_count", mc.business.supply_count - 10000)  style "cheatbutton_style" text_style "textbutton_text_style" xsize 230
                textbutton "Effectivity: [mc.business.team_effectiveness]" action [SetField(mc.business, "team_effectiveness", mc.business.team_effectiveness + 100), SetField(mc.business, "effectiveness_cap", mc.business.team_effectiveness + 100)] alternate [SetField(mc.business, "team_effectiveness", mc.business.team_effectiveness - 100), SetField(mc.business, "effectiveness_cap", mc.business.team_effectiveness - 100)]  style "cheatbutton_style" text_style "textbutton_text_style" xsize 230
                textbutton "Marketability: [mc.business.marketability]" action SetField(mc.business, "marketability", mc.business.marketability + 100) alternate SetField(mc.business, "marketability", mc.business.marketability - 100)  style "cheatbutton_style" text_style "textbutton_text_style" xsize 230
    frame: # Bottom frame
        background im.Scale("Goal_Frame_1.png", 1165, 200) # Scales the image to a size fitting the frame it is contained within
        xsize 1165
        ysize 200
        yalign 1.0
        xalign 0.529
        hbox:
            xalign 0.029
            vbox:
                textbutton "Economy" action ToggleVariable("bmme") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Economical Management"
                textbutton "Research" action ToggleVariable("bmmr") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Unlock Traits, Skip Requirements"
        # Options for the company's economy

            if bmme:
                hbox:
                    vbox: # Column 1
                        textbutton "Salary" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Manage all of your employees' salary"

                        textbutton "Give 10% salary raise" action Function(cheat_salary_pay_raise) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Give all your employees a 10% salary raise"
                        textbutton "Deduct 10% in salary" action Function(cheat_salary_deduction) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Deduct 10% from all your employees' salary"
                        textbutton "Satisfy salary expectations" action Function(cheat_salary_expectations) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Give all your employees the salary they expect based on their skills"
                    vbox: # Column 2
                        textbutton "Policies" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Policy Management"
                        textbutton "Unlock all policies" action Function(cheat_policies_unlock) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Unlock all company policies"

                        pass


            if bmmr:# Research and Serum options
                hbox:
                    vbox:
                        textbutton "Research Tier: [mc.business.research_tier]" action SetField(mc.business, "research_tier", mc.business.research_tier + 1) alternate SetField(mc.business, "research_tier", mc.business.research_tier - 1) style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "If set to 3 or higher you unlock the requirement to research advanced serums"
                        textbutton "Unlock all traits" action Function(cheat_serum_traits) style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Unlocks all traits in your current or lower research tier without the need to research them"
screen cmw(): # Cheats affecting the general world
    zorder 49
    frame: # Top Frame
        background im.Scale("Goal_Frame_1.png", 900, 195) # Scales the image to a size fitting the frame it is contained within
        xsize 900
        ysize 195
        yalign 0.225
        xalign 0.5
        hbox:
            xalign 0.08
            vbox:
                textbutton day_names[day%7] action SetVariable("day", day + 1) alternate SetVariable("day", day - 1)  style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                textbutton time_names[time_of_day] action If(time_of_day == 4, true = SetVariable("time_of_day", time_of_day - 4), false = SetVariable("time_of_day", time_of_day + 1)) alternate If(time_of_day == 0, true = SetVariable("time_of_day", time_of_day + 4), false = SetVariable("time_of_day", time_of_day - 1)) style "cheatbutton_style" text_style "textbutton_text_style" xsize 220
                textbutton "End Day" action [SetVariable("time_of_day", 4), Call("advance_time", from_current=True)] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220

    frame: # Bottom frame
        background im.Scale("Goal_Frame_1.png", 1165, 200) # Scales the image to a size fitting the frame it is contained within
        xsize 1165
        ysize 200
        yalign 1.0
        xalign 0.529
        hbox:
            xalign 0.029
            vbox:
                # List a maximum of four columns with a max of six buttons each.
                textbutton "Crisis & Events" action ToggleVariable("cml") style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "List of crisis and events"

                if cml:
                    $ total_pages = 3 
                    textbutton "Next Page: [cmlpage]" action [If(cmlpage == total_pages, true = SetVariable("cmlpage", cmlpage - total_pages + 1), false = SetVariable("cmlpage", cmlpage + 1))] alternate [If(cmlpage == 1, true = SetVariable("cmlpage", cmlpage + total_pages - 1), false = SetVariable("cmlpage", cmlpage - 1))] style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Shift through pages"

            if cml == True and cmlpage == 1: # Page 1 Work Related Crisis Events
                vbox:
                    textbutton "Work Crisis" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Crisis in your company"

                    textbutton "Broken AC" action Call("broken_AC_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "broken_AC_crisis_label"
                    textbutton "Get Drink" action Call("get_drink_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "get_drink_crisis_label"
                    textbutton "No Uniform" action Call("no_uniform_punishment_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "no_uniform_punishment_label"
                    textbutton "Office Flirt" action Call("office_flirt_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "office_flirt_label"
                    textbutton "Training Seminar" action Call("special_training_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "special_training_crisis_label"

                vbox:
                    textbutton "Lab Accident" action Call("lab_accident_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "lab_accident_crisis_label"
                    textbutton "Production Accident" action Call("production_accident_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "production_accident_crisis_label"
                    textbutton "Water Spill" action Call("water_spill_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "water_spill_crisis_label"
                    textbutton "Employee Quit" action Call("quitting_crisis_label", the_person) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "quitting_crisis_label"
                    textbutton "Investor Call" action Call("invest_opportunity_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "invest_opportunity_crisis_label"
                    textbutton "Investor Visit" action Call("invest_rep_visit_label", get_random_male_name()) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "invest_rep_visit_label"

                vbox: # Column 3
                    textbutton "Work Chat" action Call("work_chat_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "work_chat_crisis_label"
                    textbutton "Cat Fight" action Call("cat_fight_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "cat_fight_crisis_label"
                    textbutton "Cat Fight Pick Winner" action Call("cat_fight_pick_winner", get_random_from_list(mc.location.people), get_random_from_list(mc.location.people)) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "cat_fight_pick_winner"
                    textbutton "Research Reminder" action Call("research_reminder_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "research_reminder_crisis_label"
                    #textbutton "Serum Creation" action Call("serum_creation_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "serum_creation_crisis_label"
                    #textbutton "" action Call("") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip ""
                vbox: # Column 4
                    #textbutton "Serum Improve Unlock" action Call("improved_serum_unlock_label", mc.business.head_researcher) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip ""
                    textbutton "Serum Tier 2" action Call("advanced_serum_stage_2_label", mc.business.head_researcher) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip ""
                    textbutton "Serum Tier 3" action Call("futuristic_serum_stage_2_label", mc.business.head_researcher) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip ""
                    #textbutton "Serum Stage 3" action Call("advanced_serum_stage_3_label", mc.business.head_researcher) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip ""
                    #textbutton "" action Call("") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip ""

            if cml == True and cmlpage == 2: # Page 2 Crisis events that happen at the player character's home
                vbox:
                     textbutton "Home Crisis" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip ""

                     textbutton "Mom Outfit Help" action Call("mom_outfit_help_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "mom_outfit_help_crisis_label"
                     textbutton "Mom Night Surprise" action Call("mom_lingerie_surprise_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "mom_lingerie_surprise_label"
                     textbutton "Sister Underwear" action Call("lily_new_underwear_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "lily_new_underwear_crisis_label"
                     textbutton "Employee Fuck" action Call("home_fuck_crisis_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "home_fuck_crisis_label"
                     #textbutton "" action Call("") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip ""
                vbox:
                    textbutton "Sister Intro" action Call("sister_intro_crisis_label", the_person) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip ""
                    textbutton "Sister Serum Test Deal" action Call("sister_reintro_label", the_person) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "sister_reintro_label"
                    textbutton "Sister Serum Test" action Call("sister_serum_test_label", the_person) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "sister_serum_test_label"
                    textbutton "Sister Strip Deal" action Call("sister_strip_intro_label", the_person) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "sister_strip_intro_label"
                    textbutton "Sister Strip Deal 2" action Call("sister_strip_intro_label", the_person) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "sister_strip_intro_label"
                    textbutton "Sister Strip" action Call("sister_strip_label", the_person) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "sister_strip_label"
                    #textbutton "" action Call("") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip ""
                vbox: # Column 3
                    textbutton "Mom Financial" action Call("mom_weekly_pay_label", mom) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "mom_weekly_pay_label"
                    textbutton "Mom Make Dinner" action Call("mom_offer_make_dinner_label", mom) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "mom_offer_make_dinner_label"
                    textbutton "Mom's Selfie" action Call("mom_selfie_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "mom_selfie_label"
                    textbutton "Mom Morning Surprise" action Call("mom_morning_surprise_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "mom_morning_surprise_label"
                    textbutton "Sister Morning Encounter" action Call("lily_morning_encounter_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "lily_morning_encounter_label"
                    textbutton "Family Breakfast" action Call("family_morning_breakfast_label") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "family_morning_breakfast_label"

            if cml == True and cmlpage == 3: # Page 3 unspecific events in the world
                vbox:
                    textbutton "Misc Crisis" action NullAction() style "cheatbutton_style" text_style "textbutton_text_style" xsize 220 tooltip ""

                    textbutton "Pay to Strip" action Call("pay_strip_scene", the_person) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "pay_strip_scene"
                    textbutton "Dinner Date" action Call("dinner_date", the_person) style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "dinner_date"
                    textbutton "Mom NTR" action Call("mom_ntr_action_description") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Mom NTR Event"
                    textbutton "Sister NTR" action Call("sister_ntr_action_description") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Sister NTR Event"
                    textbutton "Shower Scenes" action Call("shower_action_description") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Shower Spy Event"

                vbox:
                    textbutton "Sister Phone" action Call("sister_phone_action_description") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Your sister sends messages to your phone"
                    textbutton "Town Walk" action Call("town_walk_action_description") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Taking an afternoon stroll through town"
                    textbutton "Going to the Gym" action Call("select_person_for_gym") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Give an employee a training session at the gym"
                    textbutton "Business Meeting" action Call("business_meeting_action") style "cheatbutton_style" text_style "cheattext_style" xsize 220 tooltip "Taking an afternoon stroll through town"
                    
            # if cml == True and cmlpage == 4: # Page 4

            # if cml == True and cmlpage == 5: # Page 5 If you want to add additional pages modify the "Next Page" text button as well!

# Screens - End
