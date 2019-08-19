init 2:
    screen main_choice_display(elements_list, draw_hearts_for_people = True, person_preview_args = None): #Elements_list is a list of lists, with each internal list recieving an individual column
        #The first element in a column should be the title, either text or a displayable. After that it should be a tuple of (displayable/text, return_value).

        #[["Title",["Item",Return] ]]

        hbox:
            spacing 10
            xalign 0.518
            yalign 0.2
            xanchor 0.5
            yanchor 0.0
            for count in __builtin__.range(len(elements_list)):
                frame:
                    background "gui/LR2_Main_Choice_Box.png"
                    xsize 380
                    ysize 700
                    $ title_element = elements_list[count][0]
                    if isinstance(title_element, basestring):
                        text title_element xalign 0.5 ypos 45 anchor (0.5,0.5) size 26 style "menu_text_style" xsize 200
                    else:
                        add title_element xalign 0.5 ypos 45 anchor (0.5,0.5)


                    $ column_elements = elements_list[count][1:]
                    viewport id title_element:
                        #scrollbars "vertical" #But if we aren't on a PC we need to make sure the player can scroll since they won't have a mouse wheel.

                        mousewheel True
                        xalign 0.5
                        xanchor 0.5
                        yanchor 0.0

                        ypos 99
                        xsize 360
                        ysize 588
                        vbox:
                            for item in column_elements:

                                python:
                                    #Key values we want to know about to display our text button.
                                    title = ""
                                    return_value = None

                                    hovered_list = []
                                    unhovered_list = []
                                    the_tooltip = None
                                    extra_args = None

                                    display = True
                                    is_sensitive = True

                                    quick_buttons = None

                                    if isinstance(item,list): #It's a title/return value pair. Show the title, return the value.
                                        if isinstance(item[0], Action): #It's an action with extra arguments.
                                            extra_args = item[1]
                                            item = item[0] #Rename item so that this is caught by the action section below.

                                        else: #It's (probably) a title/return string pair. Show the title, return the value
                                            title = item[0]
                                            return_value = item[1]

                                    if isinstance(item,Person): #It's a person. Format it for a person list.
                                        title = format_titles(item)
                                        return_value = item

                                        if draw_hearts_for_people:
                                            title += "\n"
                                            title += get_heart_image_list(item)
                                        if person_preview_args is None:
                                            person_preview_args = {}
                                        hovered_list.append(Function(item.draw_person, **person_preview_args))
                                        unhovered_list.append(Function(renpy.scene, "Active"))
                                        quick_buttons = []
                                        if mc.business.get_employee_title(item) != "None":
                                            if move_employee_requirement(item) == True and len(quick_buttons) < 3:
                                                quick_buttons.append(["Mods/images/icons/organigram.png", Action("Move her to a new division", requirement = move_employee_requirement, effect = "move_employee_label", args = item, requirement_args = item,
                                                                     menu_tooltip = "Move her to a new division, where her skills might be put to better use.")])
                                        if seduce_requirement(item) == True and len(quick_buttons) < 3:
                                            quick_buttons.append(["Mods/images/icons/seduce.png", Action("Try to seduce her.", requirement = seduce_requirement, effect = "seduce_label", args = item, requirement_args = item,
                                                                 menu_tooltip = "Try and seduce her right here and now. Love, sluttiness, obedience, and your own charisma all play a factor in how likely she is to be seduced.")])
                                        if serum_give_requirement(item) == True and len(quick_buttons) < 3:
                                            quick_buttons.append(["Mods/images/icons/serum.png", Action("Try to give her a dose of serum.", requirement = serum_give_requirement, effect = "serum_give_label", args = item, requirement_args = item,
                                                                 menu_tooltip = "Demand she take a dose, ask her politely, or just try and slip it into something she'll drink. Failure may result in her trusting you less or being immediately unhappy.")])
                                        if small_talk_requirement(item) == True and len(quick_buttons) < 3:
                                            quick_buttons.append(["Mods/images/icons/talk.png", Action("Make small talk. {image=gui/heart/Time_Advance.png}", requirement = small_talk_requirement, effect = "small_talk_person",
                                                                 args=item, requirement_args=item, menu_tooltip = "A pleasant chat about your likes and dislikes. A good way to get to know someone and the first step to building a lasting relationship. Provides a chance to study the effects of active serum traits and raise their mastery level.")])

                                    if isinstance(item,Action):
                                        title = ""
                                        return_value = item
                                        display = False #Default display state for an action is to hide it unless it is enabled or has a disabled slug
                                        if item.is_action_enabled(extra_args):
                                            title = item.name
                                            display = True

                                        elif item.is_disabled_slug_shown(extra_args):
                                            title = item.get_disabled_slug_name(extra_args)
                                            display = True

                                        if item.menu_tooltip:
                                            the_tooltip = item.menu_tooltip

                                    if isinstance(item,basestring): #It's just text. Display the text and return the text.
                                        title = item
                                        return_value = item

                                    if " (tooltip)" in title:
                                        the_tooltip = title.split(" (tooltip)",1)[1]
                                        title = title.replace(" (tooltip)" + the_tooltip,"")

                                    if " (disabled)" in title:
                                        title = title.replace(" (disabled)", "")
                                        is_sensitive = False

                                if display: #If we haven't encountered any reason to completely hide the item we display it now.
                                    if isinstance(quick_buttons, list):
                                        hbox:
                                            spacing 6
                                            xsize 360
                                            ysize 100
                                            textbutton title:
                                                xsize 320
                                                ysize 100
                                                xalign 0.5
                                                yalign 0.0
                                                xanchor 0.5
                                                yanchor 0.0
                                                style "textbutton_style"
                                                text_size 18
                                                text_style "textbutton_text_style"
                                                text_align (0.5,0.5)
                                                hovered hovered_list
                                                unhovered unhovered_list
                                                action Return(return_value)
                                                tooltip the_tooltip
                                                sensitive is_sensitive
                                            vbox:
                                                spacing 2
                                                for qb in quick_buttons:
                                                    imagebutton:
                                                        xysize (32, 32)
                                                        xalign 0.5
                                                        yalign 0.0
                                                        idle qb[0]
                                                        focus_mask qb[0]
                                                        action Return(qb[1])
                                    else:
                                        textbutton title:
                                            xsize 360
                                            ysize 100
                                            xalign 0.5
                                            yalign 0.0
                                            xanchor 0.5
                                            yanchor 0.0
                                            style "textbutton_style"
                                            text_size 18
                                            text_style "textbutton_text_style"
                                            text_align (0.5,0.5)
                                            hovered hovered_list
                                            unhovered unhovered_list
                                            action Return(return_value)
                                            tooltip the_tooltip
                                            sensitive is_sensitive


                    vbar:
                        value YScrollValue(title_element)
                        xalign 0.99
                        yalign 0.99
                        ysize 585
