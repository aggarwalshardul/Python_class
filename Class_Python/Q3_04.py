class parent:
    def show_pr(self):
        print("Parent class")

class child1(parent):
    def show_c1(self):
        print("Child 1 class")

class child2(parent):
    def show_c2(self):
        print("Child 2 class")

obj1 = child1()
obj1.show_c1()
obj1.show_pr()

obj2 = child2()
obj2.show_c2()
obj2.show_pr()


