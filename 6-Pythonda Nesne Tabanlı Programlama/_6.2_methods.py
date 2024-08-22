#class
class Person:
    #class attributes
    adress="no information"

    #constructor (yapıcı metod)
    def __init__(self,name,year):
       #object attributes
       self.name=name
       self.year=year
      

       #methods
    def intro(self):
        print("hello there . I am ",+self.name)

    def calculateAge(self):
        return 2019-self.year

#object(instance)
p1=Person(name="ali",year="1990")
p2=Person(name="yağmur",year="1995")

p1.intro()
p2.intro()

print(f"adım: {p1.name}yaşım: {p1.calculateAge()}")
print(f"adım: {p2.name}yaşım: {p2.calculateAge()}")


class Circle:
    #Class object attribute
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    #methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)

c1=Circle() #yaricap=1
c2=Circle(5)
print(f"c1: alan={c1.alan_hesapla()} çevre={c1.cevre_hesapla()}")
print(f"c2: alan={c2.alan_hesapla()} çevre={c2.cevre_hesapla()}")