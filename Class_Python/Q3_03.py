class grandfather:
    def show_gf(self):
        print("This is grand father class")

class father(grandfather):
    def show_ft(self):
        print("This is father class")

class son(father):
    def show_ch(self):
        print("This is child class")

obj = son()
obj.show_ch()
obj.show_ft()
obj.show_gf()