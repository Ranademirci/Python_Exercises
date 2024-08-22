#kullanıcıdan isim,yaş, eğitim bilgileri alıp ehliyet alabilme durumunu kontrol ediniz.ehliyet alma koşulu en az 18 
#ve eğitim durumu lise ya da üniversite olmalıdır.

a=input("isim:")
b=int(input("yaş:"))
c=input("eğitim durumu:")

if b>=18 and (c=="lise" or c=="üniversite"):
  print("ehliyet alabilir.")
else:
    print("ehliyet alamazsınız.")


#bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
#0-24 ------0
#25-44------1
#45-54------2
#55-69-----3
#80-84------4
#85-100-----5

a=float(input("yazılı1 : "))
b=float(input("yazılı2 : "))
c=float(input("sözlü : "))

ort=(a+b+c)/3
if 0<=ort<=24:
   print(f"ortalamanız:{ort}not :0")
elif 25<=ort<=44:
   print(f"ortalamanız:{ort}not :1")
elif 45<=ort<=54:
   print(f"ortalamanız:{ort}not :2")
elif 55<=ort<=69:
   print(f"ortalamanız:{ort}not :3")
elif 80<=ort<=84:
   print(f"ortalamanız:{ort}not :4")
elif 85<=ort<=100:
   print(f"ortalamanız:{ort}not :5")
else:
   print("yanlış bilgi girdiniz")

#trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#1. bakım ---1. yıl
#2. bakım----2. yıl
#3. bakım ----3. yıl
#süre hesabını alınan gün,ayiyıl bilgisine göre gün bazlı hesaplaynız
#datetime modülü kullanmanız gerekiyo
#(simdi) - (2018/8/1) --gün

import datetime

tarih=(input("aracınız hangi tarihte trafiğe çıktı: (yıl/ay/gün"))
tarih=tarih.split("/")
trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi-trafigeCikis
days=fark.days


if days<=365:
   print("1.servis aralığı")
elif days>365 and days<=365*2:
   print("2. servis aralığı")
elif days>365*2 and days<=365*3:
   print("3. servis aralığı")
else:
   print("hatalı süre")
