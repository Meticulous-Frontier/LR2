# Changes the tooltip screen to be snappier and aligns the text

init 2:

    screen tooltip_screen():
        zorder 50

        default hovered_enough_time = False
        $ tooltip = GetTooltip()

        if tooltip and __builtin__.len(tooltip) > 0:
            timer 0.3 action SetScreenVariable("hovered_enough_time",True)
            if hovered_enough_time:
                $ mouse_xy = renpy.get_mouse_pos()
                frame:
                    if mouse_xy[1] > 1080/2:
                        xsize 450 xpos mouse_xy[0] ypos mouse_xy[1] yanchor 1.0
                    else:
                        xsize 450 xpos mouse_xy[0] ypos mouse_xy[1]
                    text "[tooltip]":
                        style "serum_text_style"
                        xalign 0.5
        else:
            timer 0.1 action SetScreenVariable("hovered_enough_time", False)
