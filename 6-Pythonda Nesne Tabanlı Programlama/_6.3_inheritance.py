#Inheritance (Kalıtım): Miras alma

#Person => name,lastname,age,eat(),run(),drink()
#Student(Person), Teacher(Person)

class Person():
    def __init__(self,fname,lname):
        self.firsName=fname
        self.lastName=lname
        print("Person Created")

    def who_am_i(self):
        print("Im a person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber=number
        print("Student Created")

    #override
    def who_am_i(self):
        print("ı am a student")

    def sayHello(self):
        print("Hello I am a student")

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname,lname)
        self.branch=branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1=Person("ali","yılmaz")
s1=Student("çınar","turan",1234)
t1=Teacher("serkan","yılmaz","math")

t1.who_am_i()
print(p1.firsName+" "+p1.lastName)
print(s1.firsName+" "+s1.lastName+" "+str(s1.studentNumber))
p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()