# Import outfits by Trollden
# Use it as you see fit
# Requires Mod Core by ParadigmShift

init -2 python: # Definitions
    def import_wardrobe(wardrobe, xml_filename): # This is a rewrite of the wardrobe_from_xml function written by Vren.
                                                 # Wardrobe should be who's / what wardrobe you want to import into. e.g for main character it is mc.designed_wardrobe
        wardrobe = wardrobe
        file_path = os.path.abspath(os.path.join(config.basedir, "game"))
        file_path = os.path.join(file_path,"wardrobes")
        file_name = os.path.join(file_path, xml_filename + ".xml")

        if not os.path.isfile(file_name):
            return Wardrobe("xml_filename") #If there is no wardrobe present we return an empty wardrobe with the name of our file.

        wardrobe_tree = ET.parse(file_name)
        tree_root = wardrobe_tree.getroot()

        return_wardrobe = Wardrobe(tree_root.attrib["name"])
        for outfit_element in tree_root.find("FullSets"):

            wardrobe.add_outfit(outfit_from_xml(outfit_element))

        for outfit_element in tree_root.find("UnderwearSets"):

            wardrobe.add_underwear_set(outfit_from_xml(outfit_element))

        for outfit_element in tree_root.find("OverwearSets"):

            wardrobe.add_overwear_set(outfit_from_xml(outfit_element))
        return return_wardrobe

init 2 python:
    def import_wardrobe_requirement():
        return True

    def give_uniform_requirement():
        if strict_uniform_policy.is_owned():
            return True
        else:
            return "Requires: [strict_uniform_policy.name] or higher"

    def import_wardrobe_mod_initialization(self):
        bedroom.actions.append(self.action)
        return
    def give_wardrobe_mod_initialization(self):
        clothing_store.actions.append(self.action)
        return
    def give_uniform_mod_initialization(self):
        office.actions.append(self.action)
        return

    import_wardrobe_action = Mod("Import Wardrobe from XML", import_wardrobe_requirement, "import_wardrobe_label", 
        initialization = import_wardrobe_mod_initialization, menu_tooltip = "Type the name of the XML file to import, case sensitive")

    give_wardrobe_action = Mod("Give Wardrobe from XML", import_wardrobe_requirement, "give_wardrobe_label",
        initialization = give_wardrobe_mod_initialization, menu_tooltip = "Type the name of the XML file to give from, case sensitive")

    give_uniform_action = Mod("Give Uniforms from XML", give_uniform_requirement, "give_uniform_label",
        initialization = give_uniform_mod_initialization, menu_tooltip = "Type the name of the XML file to give from, case sensitive")

label import_wardrobe_label():
    "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import to your wardrobe"
    $ xml_filename = str(renpy.input("Wardrobe to import:"))
    $ import_wardrobe(mc.designed_wardrobe, xml_filename)
    return
#label import_wardrobe_input():
#    pass
label give_wardrobe_label():
    "Select who to give clothes"
    python: # First we select which employee we want

            tuple_list = format_person_list(all_people_in_the_game(), draw_hearts = True) #The list of people to show. e.g mc.location.people
            tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
            person_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

            if person_choice == "Back":
                renpy.jump("game_loop") # Where to go if you hit "Back".
#            else:
#                renpy.say("","You send a shipment of clothes to " + person_choice.name) #Add flavor text to what is about to happen. e.g "You tell the_person to go visit Starbuck for training".
#                renpy.say("", "Delivery has been made")

    call give_wardrobe_input(person_choice)# What to do if "Back" was not the choice taken.
    jump game_loop # Return to the game_loop or a label that will bring you back to the game loop

label give_wardrobe_input(person_choice):

    $ the_person = person_choice
    $ the_person.draw_person()

    "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import to [the_person.name]'s wardrobe"
    $ xml_filename = str(renpy.input("Wardrobe to import:"))

    "Speaker" "You send a shipment of clothes to [the_person.name]"
    "Speaker" "Delivery complete."

    $ import_wardrobe(the_person.wardrobe, xml_filename)
    $renpy.scene("Active")
    return

label give_uniform_label():
    "Speaker" "Choose what division to assign uniforms to"
    menu:
        "All Divisions":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.all_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
        "Marketing Division":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.m_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
        "Production":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.p_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
        "Research Division":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.r_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
        "Supply Division":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.s_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
        "Human Resources Division":
            "Speaker" "Enter the file name e.g Lily_Wardrobe then hit enter to import uniforms"

            $ xml_filename = str(renpy.input("Wardrobe to import:"))
            $ import_wardrobe(mc.business.h_uniform, xml_filename)

            "Speaker" "Uniforms assigned"
            return
