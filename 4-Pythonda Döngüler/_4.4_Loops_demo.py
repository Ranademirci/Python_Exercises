#1-100 arasında rasatgele üretilecek bir sayıyı aşağı yukarı ifadeleri 
#buldurmaya çalışın(hak=5)
#"random modülü" için "python random" şeklinde arama yapın
#100 üzerinden puanlama yapın. her soru 20 puan
#hak bilgisini kullanıcıdan alın ve her oru belirtilen can sayısı
#üzerinden hesaplansın.

import random
sayi=random.randint(1,100)
can=int(input("kaç hak kullanmak istersiniz:"))
hak=can
sayac=0
while hak>0 :
    hak-=1
    sayac+=1
    tahmin=int(input("tahmin:"))

    if sayi==tahmin:
        print(f"doğru tahmin!. {sayac} . defada bildiniz.toplam puanınız:{100-((100/can)*(sayac-1))}") #sayac-1 çünkü  bilinen turdan puana kırmamamız lazım.
        break
    elif sayi>tahmin:
        print("yukarı")
    elif sayi<tahmin:
        print("aşağı")
    if hak==0:
        print(f"hakkınız bitti. Tutulan sayı :{sayi}")


