transform transform_one():
    yalign 0.5
    yanchor 0.5
    xalign 1.0
    xanchor 1.0

transform transform_two():
    yalign 0.5
    yanchor 0.5
    xalign 1.0
    xanchor 1.0

init 1 python:
    sexy_opinions_list.append("threesomes")

    def SB_draw_two_person_scene(person_one, person_two, one_position = None, one_emotion = None, one_special_modifier = None, one_pos_x = 1.0, one_pos_y = 1.0, one_scale = 1.0, two_position = None, two_emotion = None, two_special_modifier = None, two_pos_x = 1.0, two_pos_y = 1.0, two_scale = 1.0, lighting = None): #Draw two people.
        #NOTE person two is always drawn second.
        clear_scene()
        renpy.show_screen("SB_two_person_info_ui", person_one, person_two)
        if one_position is None:
            one_position = person_one.idle_pose #Easiest change is to call this and get a random standing posture instead of a specific idle pose. We redraw fairly frequently so she will change position frequently.

        if one_emotion is None:
            one_emotion = person_one.get_emotion()

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        transform_one.xpos = one_pos_x
        transform_one.ypos = one_pos_y
        transform_one.zoom = one_scale

        one_final_image = Flatten(person_one.build_person_displayable(one_position, one_emotion, one_special_modifier, lighting = lighting, background_fill = False))
        renpy.show(person_one.name,at_list=[transform_one, scale_person(person_one.height)],layer="solo",what=one_final_image,tag=person_one.name)

        #Now do person two

        if two_position is None:
            two_position = person_two.idle_pose #Easiest change is to call this and get a random standing posture instead of a specific idle pose. We redraw fairly frequently so she will change position frequently.

        if two_emotion is None:
            two_emotion = person_two.get_emotion()

        transform_two.xpos = two_pos_x
        transform_two.ypos = two_pos_y
        transform_two.zoom = two_scale

        two_final_image = Flatten(person_two.build_person_displayable(two_position, two_emotion, two_special_modifier, lighting = lighting, background_fill = False))
        renpy.show(person_two.name,at_list=[transform_two, scale_person(person_two.height)],layer="solo",what=two_final_image,tag=person_two.name)
        return

label SB_threesome_setup_helper(): #This function is designed to help come up with number for threesome positions.
    $ the_person_one = None
    $ the_person_two = None
    $ person_one_position = None
    $ person_two_position = None
    $ person_one_emotion = None
    $ person_two_emotion = None
    $ person_one_pos_x = 1.0
    $ person_one_pos_y = 1.0
    $ person_two_pos_x = 1.0
    $ person_two_pos_y = 1.0
    $ person_one_scale = 1.0
    $ person_two_scale = 1.0
    $ pos_tuple_list = []
    python:
        pos_tuple_list.append(["stand2", "stand2"])
        pos_tuple_list.append(["stand3", "stand3"])
        pos_tuple_list.append(["stand4", "stand4"])
        pos_tuple_list.append(["stand5", "stand5"])
        pos_tuple_list.append(["walking_away", "walking_away"])
        pos_tuple_list.append(["kissing", "kissing"])
        pos_tuple_list.append(["doggy", "doggy"])
        pos_tuple_list.append(["missionary", "missionary"])
        pos_tuple_list.append(["blowjob", "blowjob"])
        pos_tuple_list.append(["against_wall", "against_wall"])
        pos_tuple_list.append(["back_peek", "back_peek"])
        pos_tuple_list.append(["sitting", "sitting"])
        pos_tuple_list.append(["standing_doggy" "standing_doggy"])
        pos_tuple_list.append(["cowgirl", "cowgirl"])
        pos_tuple_list.append(["Leave","Leave"])
    $ SB_menu_choice = None

    # (person_one, person_two, one_position = None, one_emotion = None, one_special_modifier = None, one_pos_x = 1.0, one_pos_y = 1.0, one_scale = 1.0, two_position = None, two_emotion = None, two_special_modifier = None, two_pos_x = 1.0, two_pos_y = 1.0, two_scale = 1.0):

    "Please select person one."
    $ tuple_list = known_people_in_the_game([mc]) + ["Back"]
    call screen person_choice(tuple_list, draw_hearts = True, show_person_preview = False)
    $ the_person_one = _return
    $ del tuple_list

    "Please select person two."
    $ tuple_list = known_people_in_the_game([mc]) + ["Back"]
    call screen person_choice(tuple_list, draw_hearts = True, show_person_preview = False)
    $ the_person_two = _return
    $ del tuple_list

    # for position in ["stand2","stand3","stand4","stand5","walking_away","kissing","doggy","missionary","blowjob","against_wall","back_peek","sitting","standing_doggy","cowgirl"]:
    #     pos_tuple_list.append(position)
    "Please select person one position."
    call SB_select_girl_position() from SB_call_pos_1
    $ person_one_position = _return

    "Please select person two position."
    call SB_select_girl_position() from SB_call_pos_2
    $ person_two_position = _return
    #$ person_two_position = SB_select_girl_position()

    #$ SB_draw_two_person_scene(the_person_one, the_person_two)

    $ SB_draw_two_person_scene(person_one = the_person_one, person_two = the_person_two, one_position = person_one_position, two_position = person_two_position,
    one_pos_x = person_one_pos_x, one_pos_y = person_one_pos_y, one_scale = person_one_scale,
    two_pos_x = person_two_pos_x, two_pos_y = person_two_pos_y, two_scale = person_two_scale)

    while SB_menu_choice != "Finish":

        "What would you like to adjust?"
        menu:
            "Person One X":
                call SB_change_value_amount() from _call_SB_change_value_amount
                $ person_one_pos_x += _return
            "Person One Y":
                call SB_change_value_amount() from _call_SB_change_value_amount_1
                $ person_one_pos_y += _return
            "Person Two X":
                call SB_change_value_amount() from _call_SB_change_value_amount_2
                $ person_two_pos_x += _return
            "Person Two Y":
                call SB_change_value_amount() from _call_SB_change_value_amount_3
                $ person_two_pos_y += _return
            "Person One Scale":
                call SB_change_value_amount() from _call_SB_change_value_amount_4
                $ person_one_scale += _return
            "Person Two Scale":
                call SB_change_value_amount() from _call_SB_change_value_amount_5
                $ person_two_scale += _return
            "Finished":
                $ SB_menu_choice = "Finish"
                pass

        $ SB_draw_two_person_scene(person_one = the_person_one, person_two = the_person_two, one_position = person_one_position, two_position = person_two_position,
        one_pos_x = person_one_pos_x, one_pos_y = person_one_pos_y, one_scale = person_one_scale,
        two_pos_x = person_two_pos_x, two_pos_y = person_two_pos_y, two_scale = person_two_scale)

    $ output_string = 'person one x = ' + str(person_one_pos_x) + ' y = ' + str(person_one_pos_y) + ' scale = ' + str(person_one_scale)

    #$ output_string = ('person one x = ' + str(person_one_pos_x)  + ' y = ' + str(person_one_pos_y) + ' scale = ' + str(person_one_scale) + 'person two x = ' + str(person_two_pos_x) ' y = ' + str(person_two_pos_y) + ' scale = ' + str(person_two_scale))
    mc.name "[output_string]"

    $ output_string = 'person two x = ' + str(person_two_pos_x) + ' y = ' + str(person_two_pos_y) + ' scale = ' + str(person_two_scale)

    mc.name "[output_string]"
    # "Person One X = [one_pos_x]"
    # "Person One Y = [one_pos_y]"
    # "Person One Scale = [one_scale]"
    # "Person Two X = [two_pos_x]"
    # "Person Two Y = [two_pos_x]"
    # "Person Two Scale = [two_scale]"


    return
label SB_change_value_amount():
    "How much do you want to change the value by?"
    menu:
        "+1":
            return 0.01
            pass
        "+10":
            return 0.10
            pass
        "+50":
            return 0.50
            pass
        "-1":
            return -0.01
            pass
        "-10":
            return -0.10
            pass
        "-50":
            return -0.50
            pass
    return 0

label SB_select_girl_position():
    menu:
        "stand2":
            return "stand2"
        "stand3":
            return "stand3"
        "stand4":
            return "stand4"
        "stand5":
            return "stand5"
        "walking_away":
            return "walking_away"
        "kissing":
            return "kissing"
        "doggy":
            return "doggy"
        "missionary":
            return "missionary"
        "blowjob":
            return "blowjob"
        "against_wall":
            return "against_wall"
        "back_peek":
            return "back_peek"
        "sitting":
            return "sitting"
        "standing_doggy":
            return "standing_doggy"
        "cowgirl":
            return "cowgirl"
    return "stand2"  #Default case#

label SB_test_draw_scene():
    $ SB_draw_two_person_scene(person_one = stephanie, person_two = lily, two_pos_x = 0.7)
    return

label SB_test_draw_scene_two():
    $ SB_draw_two_person_scene(person_one = mom, person_two = lily, one_position = "missionary", one_scale = 0.5, two_position = "doggy",  two_pos_x = 0.95, two_pos_y = 0.7)
    return

label trist_draw_69():
    python:
        scene_manager = Scene()
        scene_manager.add_actor(lily, position = "missionary", display_transform = character_69_bottom, z_order = 0)
        scene_manager.add_actor(mom, position = "cowgirl", display_transform = character_69_on_top, z_order = 1)
        scene_manager.draw_scene() # required for draw with z_order
    return

screen SB_two_person_info_ui(the_person_one, the_person_two): #Used to display stats for a person while you're talking to them.
    layer "solo"
    frame:
        background "gui/topbox.png"
        xsize 1100
        ysize 200
        yalign 0.0
        xalign 0.5
        xanchor 0.5
        hbox:
            xanchor 0.5
            xalign 0.5
            yalign 0.3
            spacing 300
            vbox:
                text the_person_one.name style "menu_text_style" font the_person_one.char.what_args["font"] color the_person_one.char.what_args["color"] size 40
                textbutton "Detailed Information" action Show("person_info_detailed",the_person=the_person_one) style "textbutton_style" text_style "textbutton_text_style"
                if the_person_one.arousal > 0:
                    textbutton "Arousal: [the_person_one.arousal]% (+" + get_red_heart(__builtin__.int(the_person_one.arousal/4)) + ")":
                        ysize 28
                        text_style "menu_text_style"
                        tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will instantly turn temporary sluttiness into core sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider."
                        action NullAction()
                        sensitive True
                else:
                    textbutton "Arousal: 0%":
                        ysize 28
                        text_style "menu_text_style"
                        tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will instantly turn temporary sluttiness into core sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider."
                        action NullAction()
                        sensitive True

                #textbutton "Happiness: [the_person_one.happiness]":
                #    ysize 28
                #    text_style "menu_text_style"
                #    tooltip "The happier a girl the more tolerant she will be of low pay and unpleasant interactions. High or low happiness will return to it's default value over time."
                #    action NullAction()
                #    sensitive True

                #textbutton "Love: [the_person_one.love]":
                #    ysize 28
                #    text_style "menu_text_style"
                #    tooltip "Girls who love you will be more willing to have sex when you're in private (as long as they aren't family) and be more devoted to you. Girls who hate you will have a lower effective sluttiness regardless of the situation."
                #    action NullAction()
                #    sensitive True

                #textbutton "Suggestibility: [the_person_one.suggestibility]%":
                #    ysize 28
                #    text_style "menu_text_style"
                #    tooltip "How likely this character is to increase her core sluttiness. Every time chunk there is a [the_person_one.suggestibility]% chance to change 1 point of temporary sluttiness (" + get_red_heart(5) + ") into core sluttiness (" + get_gold_heart(5) + ") as long as temporary sluttiness is higher."
                #    action NullAction()
                #    sensitive True

                hbox:
                    textbutton "Sluttiness: " + get_heart_image_list(the_person_one):
                        ysize 28
                        text_style "menu_text_style"
                        tooltip "The higher a girls sluttiness the more slutty actions she will consider acceptable and normal. Temporary sluttiness (" + get_red_heart(20) + ") is easier to raise but drops slowly over time. Core sluttiness (" + get_gold_heart(20) + ") is permanent, but only increases slowly unless a girl is suggestible."
                        action NullAction()
                        sensitive True

                    if any(x[0] > 0 or x[0] < 0 for x in the_person_one.situational_sluttiness.itervalues()):
                        textbutton "{image=question_mark_small}":
                            yoffset 6
                            ysize 28
                            tooltip person_info_ui_get_formatted_tooltip(the_person_one)
                            action NullAction()
                            sensitive True

                hbox:
                    textbutton "Obedience: [the_person_one.obedience] - " + get_obedience_plaintext(the_person_one.obedience):
                        ysize 28
                        text_style "menu_text_style"
                        tooltip "Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, and low obedience girls are likely to refuse altogether."
                        action NullAction()
                        sensitive True

                    if any(x[0] > 0 or x[0] < 0 for x in the_person_one.situational_obedience.itervalues()):
                        textbutton "{image=question_mark_small}":
                            yoffset 6
                            ysize 28
                            tooltip person_info_ui_get_formatted_obedience_tooltip(the_person_one)
                            action NullAction()
                            sensitive True

            vbox:
                vbox:
                    text the_person_two.name style "menu_text_style" font the_person_two.char.what_args["font"] color the_person_two.char.what_args["color"] size 40
                    textbutton "Detailed Information" action Show("person_info_detailed",the_person=the_person_two) style "textbutton_style" text_style "textbutton_text_style"
                    if the_person_two.arousal > 0:
                        textbutton "Arousal: [the_person_two.arousal]% (+" + get_red_heart(__builtin__.int(the_person_two.arousal/4)) + ")":
                            ysize 28
                            text_style "menu_text_style"
                            tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will instantly turn temporary sluttiness into core sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider."
                            action NullAction()
                            sensitive True
                    else:
                        textbutton "Arousal: 0%":
                            ysize 28
                            text_style "menu_text_style"
                            tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will instantly turn temporary sluttiness into core sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider."
                            action NullAction()
                            sensitive True

                    #textbutton "Happiness: [the_person_two.happiness]":
                    #    ysize 28
                    #    text_style "menu_text_style"
                    #    tooltip "The happier a girl the more tolerant she will be of low pay and unpleasant interactions. High or low happiness will return to it's default value over time."
                    #    action NullAction()
                    #    sensitive True

                    #textbutton "Love: [the_person_two.love]":
                    #    ysize 28
                    #    text_style "menu_text_style"
                    #    tooltip "Girls who love you will be more willing to have sex when you're in private (as long as they aren't family) and be more devoted to you. Girls who hate you will have a lower effective sluttiness regardless of the situation."
                    #    action NullAction()
                    #    sensitive True

                    #textbutton "Suggestibility: [the_person_two.suggestibility]%":
                    #    ysize 28
                    #    text_style "menu_text_style"
                    #    tooltip "How likely this character is to increase her core sluttiness. Every time chunk there is a [the_person_two.suggestibility]% chance to change 1 point of temporary sluttiness (" + get_red_heart(5) + ") into core sluttiness (" + get_gold_heart(5) + ") as long as temporary sluttiness is higher."
                    #    action NullAction()
                    #    sensitive True

                    hbox:
                        textbutton "Sluttiness: " + get_heart_image_list(the_person_two):
                            ysize 28
                            text_style "menu_text_style"
                            tooltip "The higher a girls sluttiness the more slutty actions she will consider acceptable and normal. Temporary sluttiness (" + get_red_heart(20) + ") is easier to raise but drops slowly over time. Core sluttiness (" + get_gold_heart(20) + ") is permanent, but only increases slowly unless a girl is suggestible."
                            action NullAction()
                            sensitive True

                        if any(x[0] > 0 or x[0] < 0 for x in the_person_two.situational_sluttiness.itervalues()):
                            textbutton "{image=question_mark_small}":
                                yoffset 6
                                ysize 28
                                tooltip person_info_ui_get_formatted_tooltip(the_person_two)
                                action NullAction()
                                sensitive True

                    hbox:
                        textbutton "Obedience: [the_person_two.obedience] - " + get_obedience_plaintext(the_person_two.obedience):
                            ysize 28
                            text_style "menu_text_style"
                            tooltip "Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, and low obedience girls are likely to refuse altogether."
                            action NullAction()
                            sensitive True

                        if any(x[0] > 0 or x[0] < 0 for x in the_person_two.situational_obedience.itervalues()):
                            textbutton "{image=question_mark_small}":
                                yoffset 6
                                ysize 28
                                tooltip person_info_ui_get_formatted_obedience_tooltip(the_person_two)
                                action NullAction()
                                sensitive True

init -1 python:
    SB_list_of_threesomes = []
    class SB_Threesome_Position():
        def __init__(self,name,slut_requirement,slut_cap,position_one_tag, position_two_tag,requires_location,requires_clothing,skill_tag_p1,skill_tag_p2,girl_one_arousal,girl_two_arousal,girl_one_source,girl_two_source,guy_arousal,skill_tag_guy,guy_source,current_girl,connections,intro,scenes,outro,transition_default,
        strip_description, strip_ask_description, orgasm_description, swap_description,
        verb = "fuck" , opinion_tags = None, p1_x = 1.0, p1_y = 1.0, p1_zoom = 1.0, p2_x = 1.0, p2_y = 1.0, p2_zoom = 1.0, can_swap = False, swap_text = ""):
            self.name = name
            self.slut_requirement = slut_requirement #The required slut score of the girl. Obedience will help fill the gap if possible, at a happiness penalty. Value from 0 (almost always possible) to ~100
            self.slut_cap = slut_cap #The maximum sluttiness that this position will have an effect on.
            self.position_one_tag = position_one_tag # The tag used to get the correct position image set
            self.position_two_tag = position_two_tag # The tag used to get the correct position image set
            self.requires_location = requires_location #
            self.requires_clothing = requires_clothing
            self.skill_tag_p1 = skill_tag_p1 #The skill that will provide a bonus to this for girl 1
            self.skill_tag_p2 = skill_tag_p2 #The skill that will provide a bonus to this for girl 2
            self.opinion_tags = opinion_tags #The opinion that will be checked each round.
            self.girl_one_arousal = girl_one_arousal # The base arousal the girl receives from this position.
            self.girl_two_arousal = girl_two_arousal # The base arousal the girl receives from this position.
            self.girl_one_source = girl_one_source  #Who is giving girl 1 pleasure. 0 = MC, 1 = herself, 2 = girl 2
            self.girl_two_source = girl_two_source  #Who is giving girl 2 pleasure. 0 = MC, 1 = girl 1, 2 = herself
            self.guy_arousal = guy_arousal # The base arousal the guy receives from this position.
            self.skill_tag_guy = skill_tag_guy #The skill that will decide how much arousal MC receives.
            self.guy_source = guy_source # Who is giving MC pleasure. 0 = MC, 1 = girl 1, 2 = girl 2
            self.current_girl = current_girl
            self.connections = connections
            self.intro = intro
            self.scenes = scenes
            self.outro = outro
            self.transition_default = transition_default #TODO: add transitions that go between related positions but with different objects. Things like standing sex into fucking her against a window.
            self.transitions = []
            self.strip_description = strip_description
            self.strip_ask_description = strip_ask_description
            self.orgasm_description = orgasm_description
            self.swap_description = swap_description
            self.verb = verb #A verb used to describe the position. "Fuck" is default, and mostly used for sex positions or blowjobs etc. Kiss, Fool around, etc. are also possibilities.

            self.current_modifier = None #We will update this if the position has a special modifier that should be applied, like blowjob.
            self.p1_x = p1_x
            self.p1_y = p1_y
            self.p1_zoom = p1_zoom
            self.p2_x = p2_x
            self.p2_y = p2_y
            self.p2_zoom = p2_zoom
            self.can_swap = can_swap
            self.swap_text = swap_text

        def link_positions(self,other,transition_label): #This is a one way link!
            self.connections.append(other)
            self.transitions.append([other,transition_label])

        def link_positions_two_way(self,other,transition_label_1,transition_label_2): #Link it both ways. Great for adding a modded position without modifying other positions.
            self.link_positions(other,transition_label_1)
            other.link_positions(self,transition_label_2)

        def call_intro(self, the_person_one, the_person_two, the_location, the_object, round, current_girl):
            renpy.call(self.intro,the_person_one, the_person_two, the_location, the_object, round, current_girl)

        def call_taboo_break(self, the_person, the_location, the_object):
            renpy.call(self.taboo_break_description, the_person, the_location, the_object)

        def call_scene(self, the_person_one, the_person_two, the_location, the_object, round, current_girl):
            random_scene = renpy.random.randint(0,__builtin__.len(self.scenes)-1)
            renpy.call(self.scenes[random_scene],the_person_one, the_person_two, the_location, the_object, round, current_girl)

        def call_outro(self, the_person_one, the_person_two, the_location, the_object, round, current_girl):
            renpy.call(self.outro,the_person_one, the_person_two, the_location, the_object, round, current_girl)

        def call_transition(self,the_position, the_person_one, the_person_two, the_location, the_object, round, current_girl):
            transition_scene = self.transition_default
            if renpy.has_label(transition_scene):
                renpy.call(transition_scene, the_person_one, the_person_two, the_location, the_object, round, current_girl)

        def call_strip(self, the_clothing, the_person_one, the_person_two, the_location, the_object, round, current_girl):
            renpy.call(self.strip_description, the_clothing, the_person_one, the_person_two, the_location, the_object, round, current_girl)

        def call_strip_ask(self, the_clothing, the_person, the_location, the_object, round, current_girl):
            renpy.call(self.strip_ask_description, the_clothing, the_person, the_location, the_object, round, current_girl)

        def call_orgasm(self, the_person_one, the_person_two, the_location, the_object, round, current_girl):
            renpy.call(self.orgasm_description, the_person_one, the_person_two, the_location, the_object, round, current_girl)

        def call_swap(self, the_person_one, the_person_two, the_location, the_object, round, current_girl):
            renpy.call(self.swap_description, the_person_one, the_person_two, the_location, the_object, round, current_girl)

        def check_clothing(self, the_person):
            if self.requires_clothing == "Vagina":
                return the_person.outfit.vagina_available()
            elif self.requires_clothing == "Tits":
                return the_person.outfit.tits_available()
            else:
                return True ##If you don't have one of the requirements listed above just let it happen.

        def redraw_scene(self, the_person_one, the_person_two, emotion = None): #redraws the scene, call this when something is modified.
            SB_draw_two_person_scene(person_one = the_person_one, person_two = the_person_two, one_position = self.position_one_tag, two_position = self.position_two_tag, one_pos_x = self.p1_x, one_pos_y = self.p1_y, one_scale = self.p1_zoom, two_pos_x = self.p2_x, two_pos_y = self.p2_y, two_scale = self.p2_zoom,)

        def calc_arousal(self, the_person_one, the_person_two):
            if self.girl_one_source == 0:
                change_amount = self.girl_one_arousal + (self.girl_one_arousal * mc.sex_skills[self.skill_tag_p1] * 0.1) #How much we increase her arousal.
            elif self.girl_one_source == 1:
                change_amount = self.girl_one_arousal + (self.girl_one_arousal * the_person_one.sex_skills[self.skill_tag_p1] * 0.1) #How much we increase her arousal.
            elif self.girl_one_source == 2:
                change_amount = self.girl_one_arousal + (self.girl_one_arousal * the_person_two.sex_skills[self.skill_tag_p1] * 0.1) #How much we increase her arousal.
            if self.opinion_tags:
                for opinion_tag in self.opinion_tags:
                    change_amount += the_person_one.get_opinion_score(opinion_tag) #Add a bonus or penalty if she likes or dislikes the position.
                    the_person_one.discover_opinion(opinion_tag)

            if the_person_one.sluttiness + 1 > self.slut_cap:
                slut_report = "Position Max Reached."
            else:
                slut_report = the_person_one.change_slut_temp(1)
            #SBNOTE Hard to imagine girls being too slutty for Threesomes
            #if the_person.arousal > the_position.slut_cap:
            #    if the_person.sluttiness > the_position.slut_cap: #She's too slutty to find this interesting.
            #        $ mc.log_event(the_person.name + ": Bored by position. Arousal gain halved.", "float_text_red")
            #        $ change_amount = change_amount/2 #Low sluttiness girls can be made to cum by kissing, higher sluttiness girls require more intense positions.
            #        #TODO: add a "sex_bored" dialogue option that can be called, asking for a more intense position.

            the_person_one.change_arousal(change_amount) #The girls arousal gain is the base gain + 10% per the characters skill in that category.

            if self.girl_two_source == 0:
                change_amount = self.girl_two_arousal + (self.girl_two_arousal * mc.sex_skills[self.skill_tag_p2] * 0.1) #How much we increase her arousal.
            elif self.girl_two_source == 1:
                change_amount = self.girl_two_arousal + (self.girl_two_arousal * the_person_one.sex_skills[self.skill_tag_p2] * 0.1) #How much we increase her arousal.
            elif self.girl_two_source == 2:
                change_amount = self.girl_two_arousal + (self.girl_two_arousal * the_person_two.sex_skills[self.skill_tag_p2] * 0.1) #How much we increase her arousal.
            if self.opinion_tags:
                for opinion_tag in self.opinion_tags:
                    change_amount += the_person_two.get_opinion_score(opinion_tag) #Add a bonus or penalty if she likes or dislikes the position.
                    the_person_two.discover_opinion(opinion_tag)

            if the_person_two.sluttiness + 1 > self.slut_cap:
                slut_report = "Position Max Reached."
            else:
                slut_report = the_person_two.change_slut_temp(1)

            the_person_two.change_arousal(change_amount)

            if self.guy_source == 0:
                 mc.change_arousal(self.guy_arousal + (self.guy_arousal * mc.sex_skills[self.skill_tag_guy] * 0.1)) # The same calculation but for the guy
            elif self.guy_source == 1:
                 mc.change_arousal(self.guy_arousal + (self.guy_arousal * the_person_one.sex_skills[self.skill_tag_guy] * 0.1))
            elif self.guy_source == 2:
                 mc.change_arousal(self.guy_arousal + (self.guy_arousal * the_person_two.sex_skills[self.skill_tag_guy] * 0.1))

        def threesome_choose_position(the_person, the_position, the_object):
            tuple_list = []
            tuple_list.append(["Keep going.",the_position])
            #tuple_list.append(["Back off and change positions.","Pull Out"])
            if (mc.arousal > 80): #Only let you finish if you've got a high enough arousal score. #TODO: Add stat that controls how much control you have over this.
                tuple_list.append(["Cum!","Finish"])
            #tuple_list.append(["Strip her down.","Strip"])
            if (the_position.can_swap == True):
                tuple_list.append([the_position.swap_text,"Swap"])
            for position in the_position.connections:
                if the_object.has_trait(position.requires_location):
                    if position.check_clothing(the_person):
                        appended_name = "Change to " + position.name + ".\n{size=18}Max Effect: " + get_red_heart(position.slut_cap) + "\nSuggested Sluttiness: " + get_red_heart(position.slut_requirement) + "{/size}"
                    else:
                        appended_name = "Change to " + position.name + ".\n{size=18}Obstructed by Clothing\nSuggested Sluttiness: " + get_red_heart(position.slut_requirement) + "{/size} (disabled)"
                    tuple_list.append([appended_name,position])
            return renpy.display_menu(tuple_list,True,"Choice")


label SB_threesome_description(the_person_one, the_person_two, the_position, the_object, round, private = True, girl_in_charge = False, current_girl = 1):
    #NOTE: the private variable decides if you are in private or not relative to the location you are in. If True other people in the room do not get a chance to interact.
    #"Hey, this is a debug line."
    ##Describe the current round

    ## FIRST ROUND EXCLUSIVE STUFF ##
    if round == 0: ##First round means to play the intro.
        $ the_position.call_intro(the_person_one, the_person_two, mc.location, the_object, round, current_girl)
        $ the_position.redraw_scene(the_person_one, the_person_two)

    ## ONCE WE HAVE DONE FIRST ROUND CHECKS WE GO HERE ##
    $ the_position.call_scene(the_person_one, the_person_two, mc.location, the_object, round, current_girl) #HERE IS WHERE THE SCENE SCRIPT IS CALLED
    #$ mc.listener_system.fire_event("sex_event", the_person = the_person, the_position = the_position, the_object = the_object) #TODO Figure out what the fuck this does

    $ the_position.calc_arousal(the_person_one, the_person_two)

    if the_person_one.arousal >= 100 or the_person_two.arousal >= 100:
        $ the_position.call_orgasm(the_person_one, the_person_two,mc.location, the_object, round, current_girl)

    if the_person_one.arousal >= 100:
        #She's climaxing.
        #$ the_person.call_dialogue("climax_responses") #We now use a position specific orgasm part of the scene.
        #$ the_position.redraw_scene(the_person,emotion="orgasm")
        $ mc.listener_system.fire_event("girl_climax", the_person = the_person_one, the_position = the_position, the_object = the_object)
        #
        $ the_position.current_modifier = None
        if the_person_one.sluttiness > the_person_one.core_sluttiness and the_person_one.core_sluttiness < the_position.slut_cap:
            $ the_person_one.change_slut_core(1)
            $ the_person_one.change_slut_temp(-1)
        $the_person_one.change_happiness(2) #Orgasms are good, right?
    if the_person_two.arousal >= 100:
        #She's climaxing.
        #$ the_person.call_dialogue("climax_responses") #We now use a position specific orgasm part of the scene.
        #$ the_position.redraw_scene(the_person,emotion="orgasm")
        $ mc.listener_system.fire_event("girl_climax", the_person = the_person_two, the_position = the_position, the_object = the_object)
        #
        $ the_position.current_modifier = None
        if the_person_two.sluttiness > the_person_two.core_sluttiness and the_person_two.core_sluttiness < the_position.slut_cap:
            $ the_person_two.change_slut_core(1)
            $ the_person_two.change_slut_temp(-1)
        $the_person_two.change_happiness(2) #Orgasms are good, right?


    ## IF OTHER PEOPLE ARE AROUND SEE WHAT THEY THINK ##
    #Implement this later#
    #if not private:
    #    $ other_people = [person for person in mc.location.people if person is not the_person] #Build a list with all the _other_ people in the room other than the one we're fucking.
    #    $ watcher = get_random_from_list(other_people) #Get a random person from the people in the area, if there are any.
    #    if watcher:
    #        # NOTE: the dialogue here often draws the person talking with various emotions or positions, so we redraw the scene after we call them.
    #        $ watcher.call_dialogue("sex_watch", the_sex_person = the_person, the_position = the_position) #Get the watcher's reaction to the people having sex. This might include dialogue calls from other personalities as well!
    #        $ the_position.redraw_scene(the_person)
    #        $ the_person.call_dialogue("being_watched", the_watcher = watcher, the_position = the_position) #Call her response to the person watching her.
    #        $ the_person.change_arousal(the_person.get_opinion_score("public sex"))
    #        $ the_person.discover_opinion("public sex")

    #Same with this#
    #$ strip_chance = the_person.effective_sluttiness() - the_person.outfit.slut_requirement
    #$ the_clothing = the_person.outfit.remove_random_any(exclude_feet = True, do_not_remove = True)
    #if renpy.random.randint(0,100) < strip_chance and the_clothing:
    #    $ ask_chance = renpy.random.randint(0,100)
    #    if ask_chance < the_person.obedience - the_person.arousal:
    #        $ the_position.call_strip_ask(the_person, the_clothing, mc.location, the_object, round)
    #    else:
    #        $ the_position.call_strip(the_person, the_clothing, mc.location, the_object, round) #If a girl's outfit is less slutty than she is currently feeling (with arousal factored in) she will want to strip stuff off.

    #TODO: This is where we check to see if a girl seizes initative during an encounter.
    #TODO: This is where a girl might request a different position (and be happy if you follow through)

    ##Ask how you want to keep fucking her or find out how she keeps fucking you##
    $ position_choice = "Keep Going" #Default value just to make sure scope is correct.
    python:
        if (mc.arousal >= 100):
            "You're past your limit, you have no choice but to cum!"
            position_choice = "Finish"
        else:
            if girl_in_charge:
                renpy.say("",the_person_one.name +  " is taking the lead. She keeps " + the_position.verb + "ing you.")
                position_choice = the_position
                #TODO: this is where we perform any changes for the girl.
            else:
                position_choice = threesome_choose_position(the_person_one, the_position, the_object)

    if position_choice == "Finish":
        $ the_position.current_modifier = None
        $ the_position.call_outro(the_person_one, the_person_two, mc.location, the_object, round, current_girl)
        $ mc.reset_arousal()
        # TODO: have you finishing bump her arousal up so you might both cum at once.

    #elif position_choice == "Strip":
    #    call strip_menu(the_person) from _call_strip_menu
    #    $ the_position.redraw_scene(the_person)
    #    call sex_description(the_person, the_position, the_object, round+1, private = private) from _call_sex_description_1

    #elif position_choice == "Pull Out": #Also how you leave if you don't want to fuck till you cum.
    #    $ the_position.current_modifier = None
    #    call fuck_person(the_person) from _call_fuck_person_2
    elif position_choice == "Swap":
        $ the_position.call_swap(the_person_one, the_person_two, mc.location, the_object, round, current_girl)
        if current_girl == 1:
            $ current_girl = 2
        else:
            $ current_girl = 1
        call SB_threesome_description(the_person_one, the_person_two, the_position, the_object, round+1, private = private, girl_in_charge = girl_in_charge, current_girl = current_girl) from _call_SB_threesome_description_3
    else:

        call SB_threesome_description(the_person_one, the_person_two, position_choice, the_object, round+1, private = private, girl_in_charge = girl_in_charge, current_girl = current_girl) from _call_SB_threesome_description_2

    return
