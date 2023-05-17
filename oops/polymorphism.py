class Student:
    def Name(self):
        print("Student Name")

    # latest method will be considered always , method overloading not possible in this way
    def Name(self, name):
        print(f"Student Name : {name}")

    # Method overloading is possible in this way using None
    def score(self, sub1=None, sub2=None, sub3=None):
        total = 0
        if sub1 != None and sub2 != None and sub3 != None:
            total += sub1+sub2+sub3
        elif sub1 != None and sub2 != None:
            total += sub1+sub2
        else:
            total = sub1
        return total

    # Method Overriding
    def subjects(self):
        print("Common Subject : Maths")


class Student_1(Student):
    def __init__(self, subject):
        self.subject = subject

    # Method Overriding done automatically
    def subjects(self):
        print(f"Common Subject is : {self.subject}")


# parent object
st = Student()
st.Name("Madhu")
print(st.score(10, 20, 30))
print(st.score(30, 40))
print(st.score(50))
st.subjects()

# child object
st1 = Student_1("Physics")
print(st1.score(10, 20, 30))
st1.Name("Rahul")
st1.subjects()
