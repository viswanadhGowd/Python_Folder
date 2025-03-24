
class student:
    def __init__(self,student_name):
        self.student_name=student_name
    def get_student_name(self):
        return self.student_name

class teacher(student):
    
    def __init__(self,name,student_name):
        super().__init__(student_name)
        self.name=name
    def get_info(self):
         student_name=self.get_student_name()
         print(student_name)
         return f"teacher name  is {self.name} and student name is {student_name}"

def main():
    t=teacher("Viswanadh", "Raj")
    print(t.get_info())

if __name__ =="__main__":
    main()