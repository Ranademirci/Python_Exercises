liste=["1","2","5a","10b","abc","10","50"]

#1:Liste elemanları içindeki sayısal değerleri bulunuz.
#2: kullanıcı q değerini girmedikçce aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.
#3:Girilen parola içinde türkçe karekter hatası veriniz
#4: faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

#1#
for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue

#2#
while True:
    sayi=input("sayı:")
    if sayi== "q" :
       break
    try:
        result=float(sayi)
        print("girdiğiniz sayı ",result)
    except:
        print("geçersiz sayı")
        continue

#3#
def checkPassword(parola):
   turkce_karekterler="şçğüöıİ"


   for i in parola:
       if i in turkce_karekterler:
          raise TypeError("Parola türkçe karekter içeremez")
       else:
           pass       
   print("geçerli parola")
parola=input("şifre girin: ")
try:
    checkPassword(parola)
except TypeError as err:
    print(err)

#4#
def faktoriyel(x):
    x=int(x)
    if x<0:
        raise ValueError("negatif değer")
    result=1
    for i in range(1,x+1):
        result*=i
    return result

for x in [5,10,20,-3,"10a"]:
    try:
        y=faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)