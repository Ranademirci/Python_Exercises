#class
class Person:
    #class attributes
    adress="no information"
    #constructor (yapıcı metod)
    def __init__(self,name,year):
       #object attributes
       self.name=name
       self.year=year
       print("init metodu çalisti")

       #methods
    def intro():
        print("hello there")


#object(instance)
p1=Person(name="ali",year="1990")
p2=Person(name="yağmur",year="1995")

#updating
p1.name="ahmet"
p2.aderss="kocaeli"

#accessing object attributes
print(f"p1:  name:  {p1.name} year: {p1.year}  adress:{p1.adress}")
print(f"p2:  name:  {p2.name} year: {p2.year}  adress:{p2.adress}")

print(p1)
print(p2)
print(type(p1))
