
init 1:
    default persistent.hud_alpha = 1
    default persistent.say_window_alpha = 1
    default persistent.show_portrait = True

init 2:
    screen say(who, what):
        default show_phone = False #If True the phone is shown. If having a text conversation with "who" then that message is displayed on the phone. The say window has priority on displaying dialogue.
        default show_say_window = True #If True the say window is shown. If also showing the phone this will be on top, and is for narration or dialogue with other characters.

        if hasattr(store,"mc"):
            if mc.having_text_conversation is not None:
                $ show_phone = True
                if who is None: #Narration is always shown in the normal say window
                    $ show_say_window = True
                elif mc.text_conversation_paused: #And dialogue can be shown as normal by setting this to True
                    $ show_say_window = True
                else: #Otherwise we're talking via text, don't show the menu.
                    $ show_say_window = False

        if show_phone:
            if show_say_window:
                use text_message_log(mc.having_text_conversation) #We're displaying narration or non-texting dialogue, so just display the history
            else:
                use text_message_log(mc.having_text_conversation, who, what) #Pass it the current message to display it

            window: #NOTE: This whole section is invisible, but is needed to satisfy Ren'py's need to have something with the "what" id.
                at transform:
                    alpha 0.0
                xalign 2.5 #Just shove it all off the screen, in case it renders not-invisible at some point
                id "window"
                background None
                text what id "what"
                if who is not None:
                    window:
                        text who id "who"

        if show_say_window:
            window:
                style_prefix "say"
                id "window"
                # if vren_test is not None:
                #     text vren_test id "what"
                # else:
                text what id "what"
                background Transform("gui/textbox.png", alpha=persistent.say_window_alpha, xalign=0.5, yalign=1.0)

                if who is not None:
                    window:
                        style "namebox"
                        text who id "who" xoffset 80

                    if persistent.show_portrait and "portrait_say" in globals() and isinstance(portrait_say, renpy.display.core.Displayable):
                        imagebutton:
                            idle portrait_say at character_portrait_say()

        #     # If there's a side image, display it above the text. Do not display
        #     # on the phone variant - there's no room.
        #     if not renpy.variant("small"):
        #         add SideImage() xalign 0.0 yalign 1.0
