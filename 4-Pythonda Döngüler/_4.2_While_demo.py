sayilar=[1,3,5,7,9,12,19,21]
#sayılar listesini while ile ekrana yazdırın
i=0
while i < (len( sayilar)):
   print(sayilar[i])
   i+=1

#başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#tek sayıları ekrana yazdırın

a=int(input("başlangıç sayısı:"))
b=int(input("bitiş sayısı"))
i=a
while i<=b:
   if (i%2!=0):
      print(i)
   i+=1

#1-100 arasındaki sayıları azalan şekilde yazdırın
i=100
while i>0:
   print(i)
   i-=1

#kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
numbers=[]
i=0
while i<5:
   sayı=int(input("sayı:"))
   numbers.append(sayı)
   i+=1
numbers.sort()   
print(numbers)

#kullanıcdan aldığınız sınırsız ürün bilgisini ürünler listesi
#içinde saklayın
#ürün sayısını kullanıcıya sorun
#dictionary listesi yapısı (name,price) şeklinde olsun
#ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

urunler=[]
adet=int(input("kaç ürün eklemek istiyosunuz"))
i=0
while (i<adet):
   name=input("ürün ismi:")
   price= input("ürün fiyatı:")
   urunler.append({
      "name":name,
      "price":price
   })
   i+=1
for urun in urunler:
   print(f"ürün adı :{urun["name"]} , ürün fiyatı: {urun["price"]}  ")
   


