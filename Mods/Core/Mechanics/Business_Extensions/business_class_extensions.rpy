init -1 python:
    def get_hr_director(self):
        if not hasattr(self, "_hr_director"):
            self._hr_director = False
        return self._hr_director

    def set_hr_director(self, value):
        self._hr_director = value

    def del_hr_director(self):
        del self._hr_director

    # add follow_mc attribute to person class (without sub-classing)
    Business.hr_director = property(get_hr_director, set_hr_director, del_hr_director, "The company HR director position.")
