init 2 python:
    def show_mannequin(demo_outfit):
        renpy.show_transient_screen("mannequin", demo_outfit)
    def hide_mannequin():
        renpy.hide_screen("mannequin")

init 2: # Moved to screen so that it can be refreshed upon changes made in outfit_creator
    screen mannequin(outfit):
        zorder 102
        fixed: #TODO: Move this to it's own screen so it can be shown anywhere
            pos (1450,0)

            add mannequin_average
            if outfit is not None:
                for cloth in outfit.generate_draw_list(None,"stand3"):
                    add cloth
