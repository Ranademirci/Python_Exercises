def sayHello(name="user"): #fonksiyonuzmuzu oluşturduk 
    print("hello"+name)

sayHello("Çınar")
sayHello("Ada")
sayHello() #parametre göndermezsek varssayılan olna user bilgisi girilir

def sayHello(name="user"): #fonksiyonuzmuzu oluşturduk 
    return"hello"+name

msg=sayHello("Çınar")
print(msg)

def total(num1,num2):
    return num1+num2
result=total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2024-dogumYili
ageCinar= yasHesapla(2011)
ageAda=yasHesapla(2003)
print(ageCinar,ageAda)

def emekliliğeKaçyılKaldı(dogumYili,isim):
    '''
    DOCSTRING: doğum yılınıza göre emekliliğinize kaç yıl kaldı
    INPUT:doğum yılı
    OUTPUT:hesaplanan yıl bilgisi
    '''
    yas=yasHesapla(dogumYili)
    emeklilik=65-yas
    
    if emeklilik>0:
        print(f"emekliliğinize {emeklilik} yıl kaldı")

    else:
        print("zatene emekli oldunuz")

emekliliğeKaçyılKaldı(1983,"Ali")

print(help(emekliliğeKaçyılKaldı)) #fonksiyon kullanım şekli, hakkında biglilendiri

print(help(list.append))