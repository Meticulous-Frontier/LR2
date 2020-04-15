# The enhanced version will hide columns that have no actions in them,
# does not work for columns with disabled actions (like special actions)
# but does work for sex positions (when a girl hates anal, the anal column will not be visible)
init 2: # Change name back to main_choice_display once fixed
    screen main_choice_display_2(elements_list): #Elements_list is a list of lists, with each internal list receiving an individual column
        #The first element in a column should be the title, either text or a displayable. After that it should be a tuple of (displayable/text, return_value).

        #[["Title",["Item",Return] ]]

        hbox:
            spacing 10
            xalign 0.518
            yalign 0.2
            xanchor 0.5
            yanchor 0.0
            for count in __builtin__.range(len(elements_list)):
                if len(elements_list[count][1:]) > 0:
                    frame:
                        background "gui/LR2_Main_Choice_Box.png"
                        xsize 380
                        ysize 700
                        $ title_element = elements_list[count][0]
                        if isinstance(title_element, basestring):
                            text title_element xalign 0.5 ypos 45 anchor (0.5,0.5) size 22 style "menu_text_style" xsize 240
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
                                    if item.display: #If we haven't encountered any reason to completely hide the item we display it now.
                                        textbutton item.title:
                                            xsize 360
                                            ysize 80
                                            xalign 0.5
                                            yalign 0.5
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            text_align (0.5,0.5)
                                            if item.display_key:
                                                hovered [Function(show_menu_person, item)]
                                                unhovered [Function(renpy.scene, "Active")]
                                            action Return(item.return_value)
                                            tooltip item.the_tooltip
                                            sensitive item.is_sensitive

                        vbar:
                            value YScrollValue(title_element)
                            xalign 0.99
                            yalign 0.99
                            ysize 585
