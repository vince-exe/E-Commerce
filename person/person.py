class Person:
    def __init__(self, first_name, last_name, email, psw, id_, money):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.psw = psw
        self.id = id_
        self.money = money

    def get_id(self):
        return self.id

    def get_psw(self):
        return self.psw

    def get_email(self):
        return self.email

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_money(self):
        return self.money

    def add_money(self, money):
        self.money += money

    def remove_money(self, money):
        self.money -= money
