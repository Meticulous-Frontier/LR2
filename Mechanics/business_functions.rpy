init -1 python:
    def pay(self, amount, add_to_log = True):
        amount = amount
        self.funds += amount

        if add_to_log:
            mc.log_event(self.name + ": " + "$" + str(amount), "float_text_green")

        return

    Business.pay = pay
