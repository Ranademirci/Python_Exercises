#global scope
x="global x"

def function():
    #local scope
    x="local x"
    print(x) #bu fonksiyonun içinde olduğundan fonksiyonda 
    #olan değişkeni verir. eğer fonksiyonunn içinde değişken atamasaydık global olanı verirdi

function()
print(x) #fonksionun dışında olan değişkeni yazdırır.

##################################################################
#global
name="Çınar"
def changeName(new_name):
    #local
    name=new_name
    print(name) #ada

changeName("ada")
print(name) #çınar

##########################################
name="global string"

def greeting():
    name="çınar" #burası yorum satırda olsaydı hello global string çıktısı olurdu.

    def hello():
        #ama burda name="ada" yazsaydı aşağıda hello ada çıkardı.
        print("hello"+name)  #hello çınar
    hello()

greeting()

######################
x=50
def test(x):
    print(f"x {x}") #50 

    x=100
    print(f"changed x to {x}") #100
test(x)
print(x)   #bu 50 çıktısını verir

x=50
def test():
    global x
    print(f"x {x}") #50 

    x=100
    print(f"changed x to {x}") #100
test()
print(x)   #bu 100 çıktısını verir