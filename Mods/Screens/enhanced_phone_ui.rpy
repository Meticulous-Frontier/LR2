init 2:

    screen phone_hud_ui():
        default phone_up = False
        default start_phone_pos = 1.4
        default end_phone_pos = 1.4
        default ui_xsize = 320
        modal False
        frame:
            background "#1a45a1aa"
            xsize ui_xsize + 20
            ysize 440
            xanchor 1.0
            xalign 0.99
            at phone_slide(start_phone_pos, end_phone_pos)
            frame:
                background None



                null height 5
                viewport:
                    mousewheel True
                    draggable True
                    if len(mc.log_items) > 4:
                        scrollbars "vertical"
                    vbox:
                        for log_item in mc.log_items:
                            if log_item is not None and log_item[0] is not None and log_item[1] is not None: #Minor hack to try and prevent any crashes. In theory log items should always exist.
                                $ fade_time = 5
                                $ time_diff = time.time() - log_item[2]
                                if time_diff > fade_time:
                                    $ time_diff = fade_time

                                frame:
                                    background "#33333388"
                                    xsize ui_xsize
                                    padding (0,0)
                                    text log_item[0] style log_item[1] size 18 xsize ui_xsize first_indent 10 rest_indent 20
                                frame:
                                    background "#ff0000aa"
                                    xsize ui_xsize
                                    ysize 2
                                    yanchor 1.0
                                    yalign 0.95
                                    xpadding 0
                                    ypadding 0
                                    at background_fade(5, time_diff)
                                null height 2
                button:
                    focus_mask None
                    margin [-20, -20]
                    ysize 440
                    action [
                        ToggleScreenVariable("phone_up"),
                        ToggleScreenVariable("end_phone_pos",1.0, 1.4),
                        ToggleScreenVariable("start_phone_pos",1.4, 1.0),
                        ]
