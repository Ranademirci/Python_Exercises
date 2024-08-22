#gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın

def yazdir(kelime, adet):
  print(kelime*adet)
yazdir("merhaba\n",10)


#kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon
def listeyeCevir(*params):
   liste=[]

   for param in params:
      liste.append(param)
   return liste

result = listeyeCevir(10,20,30,"merhaba")
print(result)

#gönderilen 2 sayı arasındaki tüm asal sayıları bulun

sayı1=int(input("sayı1:"))
sayı2=int(input("sayı2:"))

def asalSayıBul(sayı1,sayı2):
   for sayı in range(sayı1,sayı2+1):
      if sayı>1:
         for i in range(2,sayı):
          if (sayı%i==0):
            break
         else:
            print(sayı)

asalSayıBul(sayı1,sayı2)

#kendisine gönderilen bir sayının tam bölenlerini bir liste  şeklinde döndrünz

def tamBölenleriBul(sayı):
   tamBolenler=[]

   for i in range(2,sayı):
      if sayı %i==0:
         tamBolenler.append(i)
   return tamBolenler

print(tamBölenleriBul(20))