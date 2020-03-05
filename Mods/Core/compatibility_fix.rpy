init -100 python:
    # Fix compatibility of save games.

    def move_followers_action_requirement():
        return
    def change_location_action_requirements():
        return

init -1 python:
    # override some of the default settings to improve performance
    config.image_cache_size = 12
    config.image_cache_size_mb = 1024
    config.predict_statements = 16