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

                                #Key values we want to know about to display our text button.
                                $ title = ""
                                $ return_value = None

                                $ hovered_list = []
                                $ unhovered_list = []
                                $ the_tooltip = None
                                $ extra_args = None

                                $ display = True
                                $ is_sensitive = True

                                if isinstance(item,list): #It's a title/return value pair. Show the title, return the value.
                                    if isinstance(item[0], Action): #It's an action with extra arguments.
                                        $ extra_args = item[1]
                                        $ item = item[0] #Rename item so that this is caught by the action section below.

                                    else: #It's (probably) a title/return string pair. Show the title, return the value
                                        $ title = item[0]
                                        $ return_value = item[1]

                                if isinstance(item,Person): #It's a person. Format it for a person list.
                                    $ title = format_titles(item)
                                    $ return_value = item

                                    if draw_hearts_for_people:
                                        $ title += "\n"
                                        $ title += get_heart_image_list(item)
                                    if person_preview_args is None:
                                        $ person_preview_args = {}
                                    $ hovered_list.append(Function(item.draw_person, **person_preview_args))
                                    $ unhovered_list.append(Function(renpy.scene, "Active"))

                                if isinstance(item,Action):
                                    $ title = ""
                                    $ return_value = item
                                    $ display = False #Default display state for an action is to hide it unless it is enabled or has a disabled slug
                                    if item.is_action_enabled(extra_args):
                                        $ title = item.name
                                        $ display = True

                                    elif item.is_disabled_slug_shown(extra_args):
                                        $ title = item.get_disabled_slug_name(extra_args)
                                        $ display = True

                                    if item.menu_tooltip:
                                        $ the_tooltip = item.menu_tooltip

                                if isinstance(item,basestring): #It's just text. Display the text and return the text.
                                    $ title = item
                                    $ return_value = item

                                if " (tooltip)" in title:
                                    $ the_tooltip = title.split(" (tooltip)",1)[1]
                                    $ title = title.replace(" (tooltip)" + the_tooltip,"")

                                if " (disabled)" in title:
                                    $ title = title.replace(" (disabled)", "")
                                    $ is_sensitive = False

                                if display: #If we haven't encountered any reason to completely hide the item we display it now.
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
