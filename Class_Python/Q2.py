class Student:
    def __init__(self,name,sap_id,phy,chem,maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def display(self):
        print("Student details")
        print("Name: ",self.name)
        print("SAP ID: ",self.sap_id)
        print("Physics: ",self.phy)
        print("Chemistry: ",self.chem)
        print("Maths: ",self.maths)

    def find_marks_percentage(self):

        total = self.phy + self.chem + self.maths
        percentage = total/3
        return percentage
    
    def result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            return "Pass"
        else:
            return "fail"
        
def class_average(student_list):
    total_percentage = 0
    for student in student_list:
        total_percentage += student.find_marks_percentage()
    avg = total_percentage/len(student_list)
    return avg


n = int(input("Enter number of students: "))
students = []


for i in range(n):
    print(f"\n Enter details for Student {i+1}")
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = float(input("Enter Physics marks: "))
    chem = float(input("Enter Chemistry marks: "))
    maths = float(input("Enter Maths makrs: "))

    s = Student(name,sap_id,phy,chem,maths)
    students.append(s)

