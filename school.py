

class students:
    list1 = []
    def __init__(self,student_name,student_height):
        self.student_name = student_name
        self.student_height = student_height

    def add_to_students_record(self):
        students.list1.append([self.student_name,self.student_height])

    @staticmethod
    def display_students_record():
        if students.list1:
            print("Students_name".center(15),"students_height")
            for i in students.list1:
                print(i[0].center(15),i[1])
        else:
            print("No student data found ")
student1 = students("tharun",5.10)
student2 = students("nani" ,5.11)
student3 = students("sharan",5.12)
student4 = students("hemanth",5.11)
student1.add_to_students_record()
student2.add_to_students_record()
student3.add_to_students_record()
student4.add_to_students_record()


students.display_students_record()
