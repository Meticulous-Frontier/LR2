# This method is designed to take a list of people and return a time slot that everyone has open. Notably, schedule must be None.
init 2 python:
    def find_opening_in_schedules(people_list, prohibited_days = [], prohibited_times = []): #Returns list of day and time tuples that are available to the people in the list
        list_of_times = []
        for the_day in range(0,7):
            if the_day in prohibited_days:
                continue
            for the_time in range(0,5):
                if the_time in prohibited_times:
                    continue
                list_of_times.append([the_day, the_time])
                for person in people_list:
                    if person.schedule[the_day][the_time] is not None:
                        list_of_times.remove([the_day, the_time])
                        break
        return list_of_times

    def find_random_open_time_in_schedules(people_list): #Returns a random day and time that is open schedule wise for all characters.
        return get_random_from_list(find_opening_in_schedules(people_list))

    def get_current_time_tuple():
        return ([day%7, time_of_day])

    def get_schedule_description(the_time):
        string_one = ""
        string_two = ""
        if the_time[0] == 0:
            string_one = "Monday "
        elif the_time[0] == 1:
            string_one = "Tuesday "
        elif the_time[0] == 2:
            string_one = "Wednesday "
        elif the_time[0] == 3:
            string_one = "Thursday "
        elif the_time[0] == 4:
            string_one = "Friday "
        elif the_time[0] == 5:
            string_one = "Saturday "
        elif the_time[0] == 6:
            string_one = "Sunday "

        if the_time[1] == 0:
            string_two = "early morning"
        elif the_time[1] == 1:
            string_two = "morning"
        elif the_time[1] == 2:
            string_two = "afternoon"
        elif the_time[1] == 3:
            string_two = "evening"
        elif the_time[1] == 4:
            string_two = "night"

        return (string_one + string_two)

    def is_schedule_time(the_time):
        if day%7 == the_time[0] and time_of_day == the_time[1]:
            return True
        return False
