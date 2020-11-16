# special class that implements Say class char override behaviour from VREN
init -10 python:
    def custom_execute(self):

        renpy.ast.next_node(self.next)
        renpy.ast.statement_name("say")

        try:

            renpy.game.context().say_attributes = self.attributes
            renpy.game.context().temporary_attributes = self.temporary_attributes

            who = renpy.ast.eval_who(self.who, self.who_fast)

            if not (
                    (who is None) or
                    callable(who) or
                    isinstance(who, basestring) or
                    isinstance(who, renpy.store.Person)):

                raise Exception("Sayer %s is not a function or string." % self.who.encode("utf-8"))

            what = self.what
            if isinstance(who, renpy.store.Person): #Vren: Catches people objects and modifies anything they are saying.
                what = who.personalise_text(what)
                who = who.char # Vren: Set the character properly so it can manage all other aspects of the say command; text colour, ect.

            if renpy.config.say_menu_text_filter:
                what = renpy.config.say_menu_text_filter(what)  # E1102

            renpy.store._last_raw_what = what

            if self.arguments is not None:
                args, kwargs = self.arguments.evaluate()
            else:
                args = tuple()
                kwargs = dict()

            kwargs.setdefault("interact", self.interact)

            if getattr(who, "record_say", True):
                renpy.store._last_say_who = self.who
                renpy.store._last_say_what = what
                renpy.store._last_say_args = args
                renpy.store._last_say_kwargs = kwargs

            renpy.ast.say_menu_with(self.with_, renpy.game.interface.set_transition)
            renpy.exports.say(who, what, *args, **kwargs)

        finally:
            renpy.game.context().say_attributes = None
            renpy.game.context().temporary_attributes = None

    renpy.ast.Say.execute = custom_execute

    def custom_predict(self):
        old_attributes = renpy.game.context().say_attributes
        old_temporary_attributes = renpy.game.context().temporary_attributes

        try:
            renpy.game.context().say_attributes = self.attributes

            who = renpy.ast.eval_who(self.who, self.who_fast)

            def predict_with(trans):
                renpy.display.predict.displayable(trans(old_widget=None, new_widget=None))

            renpy.ast.say_menu_with(self.with_, predict_with)

            what = self.what
            if isinstance(who, renpy.store.Person): #Vren: Catches people objects and modifies anything they are saying.
                what = who.personalise_text(what)
                who = who.char # Vren: Set the character properly so it can manage all other aspects of the say command; text colour, ect.
            if renpy.config.say_menu_text_filter:
                what = renpy.config.say_menu_text_filter(what)

            renpy.exports.predict_say(who, what)

        finally:
            renpy.game.context().say_attributes = old_attributes
            renpy.game.context().temporary_attributes = old_temporary_attributes

        return [ self.next ]

    renpy.ast.Say.predict = custom_predict