class Student:
    def get_data(self):
        self.name = input("Enter Student Name: ")
        self.sap_id = input("Enter SAP ID: ")
        self.phy = float(input("Enter Physics Marks: "))
        self.chem = float(input("Enter Chemistry Marks: "))
        self.maths = float(input("Enter Maths Marks: "))

    def display(self):
        print("\nStudent Details")
        print("Name: ",self.name)
        print("SAP ID: ",self.sap_id)
        print("Physics: ",self.phy)
        print("Chemistry: ",self.chem)
        print("Maths: ",self.maths)

s1 = Student()
s1.get_data()

s1.display()
