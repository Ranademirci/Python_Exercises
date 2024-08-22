import math  #math modülünü dahil ettik.bu kütüphaneden yararlanabilirz

value=dir(math)  #math modülü içerisindeki fonksiyonları görmek için ,bileşenleri value içerisine aktardık
value=help(math) #tüm fonksiyonları açıklamalrıyla birlikte verir.ilgili modül içerisindeki dokümanı gösterir.
value=help(math.factorial)#sadece faktoriyel ile alakalı açıklamayı verir
value=math.sqrt(49) #sqrt fonksiyonunu kendimiz yazmamıza gerek kalmadan hazır olanı kullanıyoruz.49 sayısının karekökünü buluruz.
value=math.factorial(5) #faktoriyel hesaplama
value=math.floor(5.9) #aşağı yuvarlar 5 çıktısı gelir
value=math.floor(5.9)#yukarı yuvarlar 6 çıktısı gelir


print(value)

import math as islem #math kütüphaneisne islem adıyla ulaşabilriz artık
value=islem.factorial(5) 


#yöntem 2
from math import* #ilgili kütüohaneden heps,ni import et
value=factorial(5)

from math import factorial,sqrt  #kütüpohane içerisinden 2 foksiyon import ettik.
#import edilmeyen fonksiyonu kullanamayız 


def sqrt(x): #bu sqrt bizim tanımladığımız bir fonksiyon ve import sqrt ettikten sonra aynı isimle fonksiyon oluşturursak ve en son hangisi yazıyosa o çalışır.
    print("x"+str(x))
