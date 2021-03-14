init 5 python:
    phone_background = Image(get_file_handle("LR2_Phone_Text_Dark.png"))
    text_bubble_blue = Image(get_file_handle("LR2_Text_Bubble_Blue.png"))
    text_bubble_gray = Image(get_file_handle("LR2_Text_Bubble_Gray.png"))
    text_bubble_yellow = Image(get_file_handle("LR2_Text_Bubble_Yellow.png"))

    def get_phone_history(person):
        display_list = []
        for item in mc.phone.get_message_list(person):
            display_tuple = [item.who, item.what]
            display_list.append(display_tuple)
        return display_list

init 2 style digital_text_2 is text:
    font "Autobusbold-1ynL.ttf"
    color "#ffffffff"
    outlines [(1,"#222222ff",0,0)]
    yanchor 0.5
    yalign 0.5


init 5:
    screen text_message_log(the_person, newest_who = None, newest_what = None):
        default size_x = 600

        fixed:
            xanchor 0.5
            xalign 0.5
            frame:
                background Frame(phone_background, 0,0,0,0)
                xanchor 0.5
                xalign 0.5
                yanchor 1.0
                yalign 1.0
                xsize size_x
                ysize 940

            viewport: #The display for the text, which can be scrolled up and down.
                yalign 0.5
                xalign 0.5
                xoffset 4
                yoffset 404
                xanchor 0.5
                yanchor 1.0
                mousewheel True
                scrollbars "vertical"
                xsize (size_x - 120)
                ysize 656
                yinitial 1.0
                vbox:
                    box_reverse False
                    xanchor 0.5
                    xalign 0.5
                    spacing 10
                    yanchor 1.0
                    yalign 1.0


                    $ display_who = ""
                    $ display_what = ""
                    $ who_align = 0.0
                    $ what_align = 1.0
                    $ display_list = get_phone_history(the_person)
                    if newest_what is not None:
                        $ display_list.append([newest_who, newest_what])

                    for history_item in display_list:
                        $ log_who = history_item[0]
                        $ log_what = history_item[1]

                        frame: #TODO: Add support for system messages (ie. in-phone narration)
                            # background None
                            padding (4,4)
                            if log_who == mc.name:
                                background Frame(text_bubble_blue, 4, 4, 4, 4)
                            elif log_who is None:
                                background Frame(text_bubble_gray, 4, 4, 4, 4)
                            else:
                                background Frame(text_bubble_yellow, 4, 4, 4, 4)

                            hbox:
                                xsize (size_x - 150)
                                if log_who == mc.name:
                                    box_reverse True
                                    $ display_who = mc.name
                                    $ display_what = log_what
                                    $ who_align = 1.0
                                    $ what_align = 0.0
                                elif log_who is None:
                                    $ what_align = 0.5
                                    $ display_who = ""
                                    $ display_what = log_what
                                else:
                                    box_reverse False
                                    $ display_who = mc.having_text_conversation.create_formatted_title(log_who)
                                    $ display_what = log_what
                                    $ who_align = 0.0
                                    $ what_align = 1.0

                                if log_who is not None:
                                    text display_who xsize 75 text_align who_align xalign who_align yalign 0.5 size 18 style "digital_text_2"
                                text display_what xsize (size_x - 225) text_align what_align xalign what_align yalign 0.5 size 18 style "digital_text_2"
