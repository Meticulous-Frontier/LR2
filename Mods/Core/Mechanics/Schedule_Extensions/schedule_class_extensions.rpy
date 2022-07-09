init 2 python:
    def schedule_remove_location(self, location):
        for day_number in range(0, 7):
            for time_number in range(0,5):
                if self.get_destination(specified_day = day_number, specified_time = time_number) == location:
                    self.set_schedule(None, the_days = [day_number], the_times = [time_number])
        return

    Schedule.remove_location = schedule_remove_location
