class Father:
    def show_father(self):
        print("This is father class")
class Mothter:
    def show_mother(self):
        print("This is mother class")

class child(Father,Mothter):
    def show_child(self):
        print("Child class")

obj = child()
obj.show_child()
obj.show_father()
obj.show_mother()
