# override the default person_choice, to make sure we show back button and sort the people list by name
init 2:
    screen person_choice(people, draw_hearts = False, person_prefix = None, person_suffix = None, show_person_preview = True, person_preview_args = None):
        # create sorted people list (excludes back command which is last item)
        $ sorted_people = sorted(people[:len(people)-1], key = lambda p: p.name)
        # attach back command to sorted people
        $ sorted_people.append(people[len(people)-1])
        style_prefix "choice"
        #We want to have 2 vboxes, seperated so that they are staggered as they go down.
        #if len(items) > 10: #TODO: see if we can have the viewport all the time but only show it as scrollable when there are enough items in it, to simplify this sectio.
        viewport:
            scrollbars "vertical"
            mousewheel True
            child_size (1920, 625 + 125 * (len(sorted_people)//2))
            vbox:
                xalign 0.34
                yalign 0.5
                null height 400
                for i in sorted_people[0::2]:
                    #Check if " (tooltip)" in i.caption, and if it is remove it and everything after it and add it as a tooltip

                    if isinstance(i, Person):
                        $ her_title = format_titles(i)
                        if person_prefix:
                            $ her_title = person_prefix + " " + her_title
                        if person_suffix:
                            $ her_title += " " + person_suffix

                        if draw_hearts: #If we want to draw sluttiness hearts under someone add them to the image list now
                            $ her_title += "\n"
                            $ her_title += get_heart_image_list(i)

                        if person_preview_args is None:
                            $ person_preview_args = {}
                        textbutton her_title:
                            action Return(i)
                            if show_person_preview:
                                hovered Function(i.draw_person, **person_preview_args)
                                unhovered Function(renpy.scene,"Active")
                    else:
                        textbutton i action Return(i)

                    # if " (tooltip)" in i.caption:
                    #     $ the_tooltip = i.caption.split(" (tooltip)",1)[1]
                    # if " (disabled)" in i.caption:
                    #     textbutton i.caption.replace(" (disabled)", "").replace(" (tooltip)" + the_tooltip,"") sensitive False tooltip the_tooltip #Replace the full tooltip bit with nothing.
                    # else:
                    #     textbutton i.caption.replace(" (tooltip)" + the_tooltip,"") action i.action tooltip the_tooltip

            vbox:
                xalign 0.67
                yalign 0.5
                null height 400
                if len(sorted_people)%2 == 0:
                    null height 125 #Add an empty list element to keep the alignment correct if there are an even number of elements in both lists.
                for j in sorted_people[1::2]:
                    if isinstance(j, Person):
                        $ her_title = format_titles(j)
                        if person_prefix:
                            $ her_title = person_prefix + " " + her_title
                        if person_suffix:
                            $ her_title += " " + person_suffix
                        if draw_hearts: #If we want to draw sluttiness hearts under someone add them to the image list now
                            $ her_title += "\n"
                            $ her_title += get_heart_image_list(j)

                        if person_preview_args is None:
                            $ person_preview_args = {}
                        textbutton her_title:
                            action Return(j)
                            if show_person_preview:
                                hovered Function(j.draw_person, **person_preview_args)
                                unhovered Function(renpy.scene,"Active")
                    else:
                        textbutton j action Return(j)

