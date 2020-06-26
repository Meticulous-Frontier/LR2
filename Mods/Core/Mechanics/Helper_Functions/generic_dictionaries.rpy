# Hold dictionaries with various translations
init -1 python:

    def get_work_skills():
        dict_work_skills = {
            "hr_skill": ["Human Resources", "hr_skill"],
            "market_skill": ["Marketing", "market_skill"],
            "research_skill": ["Research & Development", "research_skill"],
            "production_skill": ["Production", "production_skill"],
            "supply_skill": ["Supply Procurement", "supply_skill"]
            }
        return dict_work_skills
    def get_sex_skills():
        dict_sex_skills = {
            "Foreplay": ["Foreplay", "foreplay"],
            "Oral": ["Oral", "oral"],
            "Vaginal": ["Vaginal", "vaginal"],
            "Anal": ["Anal", "anal"]
            }
        return dict_sex_skills
    def get_main_skills():
        dict_main_skills = {
            "int": ["Intelligence", "int"],
            "focus": ["Focus", "focus"],
            "charisma": ["Charisma", "charisma"]
            }
        return dict_main_skills
