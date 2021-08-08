init 6 python:
    def IT_work_requirement():
        if mc.business.IT_project_in_progress:
            return True
        else:
            return "No active project!"

    IT_work_action = Action("Work on IT development", IT_work_requirement, "IT_work_label")

label IT_work_label():
    "You spend some time working on the current IT Project."
    $ mc.business.IT_increase_project_progress(25, add_to_log = True)
    return
