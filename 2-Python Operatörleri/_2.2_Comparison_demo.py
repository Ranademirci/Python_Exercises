#Girilen 2 sayıdan hangisi büyüktür?
'''
a=int(input("Birinci sayı:"))
b=int(input("İkinci sayı:"))
result=(a>b)
print(f"{a},{b} den büyüktür {result}")

#Kullanıcıdan 2 vize (%60) 1 final(%40) notunu alıp ortalama hesaplayınız. Bu ortalamanın 50 den yukardaysa geçti yazsın.
a=float(input("vize notu 1:"))
b=float(input("vize notu2:"))
c=float(input("final notu:"))
ort= (((a+b)/2)*6/10)+(c*4/10)
print(f"ortalamanız:{ort} dersten geçme durumu:{ort>=50}")

#Girilen sayının tek mi çift mi olduğunu yazınız
a=int(input("sayı:"))
print(f"girilen sayı tek sayıdır: {a%2!=0}")

#girilen sayının negatif pozitif olma durumu
a=int(input("sayı:"))
print(f"girilen sayı 0 dan büyük olma durumu: {a>0}")

'''

#parola ve email bilgi isteyip doğruluğunu kontrol ettiriniz(email:rana@gmail.com)(parola:123)
email="aaa@gmail.com"
parola="123"
a=str(input("email:")).lower() #girilen emailin hepsini küçük harfe çevirir bu sebeple kullanıcı için büyük küçük harf önemsiz olur.
b=str(input("parola:"))
print(f"girilen email doğru mu:{email==a} ve girilen parola doğru mu: {parola==b}")



