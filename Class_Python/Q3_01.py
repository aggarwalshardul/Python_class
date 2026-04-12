class Father:
    def show_father(self):
        print("This is father class")

class Son(Father):
    def show_son(self):
        print("This is son class")

obj = Son()
obj.show_son()
obj.show_father()