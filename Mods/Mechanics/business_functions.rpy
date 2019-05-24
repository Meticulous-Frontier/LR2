init -1 python:
    def pay(self, amount, add_to_log = True):
        amount = amount
        self.funds += amount

        if add_to_log:
            if amount >= 0:
                mc.log_event(self.name + " received: " + "$" + str(abs(amount)), "float_text_green")
            else:
                mc.log_event(self.name + " payed: " + "$" + str(abs(amount)), "float_text_green")

        return

    # Add Pay function to business object
    Business.pay = pay
