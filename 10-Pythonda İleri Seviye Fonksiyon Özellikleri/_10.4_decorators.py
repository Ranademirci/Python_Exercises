#bir fonksiyona bir özellik eklemek için kullanrıız.

def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper
@my_decorator  #sayHello=my_decorator(sayHello)
def sayHello(name):
    print("hello",name)

def sayGreeting():
    print("greeting")

sayHello("ali") 

import math
import time
def calculate_time(func):
  def inner(*args,**kwargs):
    start=time.time()
    time.sleep(1)
    func(*args,**kwargs)
    finish=time.time()
    print("fonksiyon"+func.__name__+str(finish-start)+ " saniye sürdü.") 
  return inner
@calculate_time
def usalma(a,b):
 print(math.pow(a,b))
  
@calculate_time
def factoriyel(num):
    print(math.factorial(num))


usalma(2,3)
factoriyel(4)