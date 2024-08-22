#girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
a=float(input("sayı:"))
print(f"girdiğiniz sayı {a} ,0 ile 100 arasındadır:{(a>0) and (a<100)}" )

#kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız.
#ortalama 50 ve üsütndeyse geçti değilse kaldı yazsın
#ortalama 50 olsa bile final notu en az 50 olmalıdır
#final 70 ise ortalamanın önemi olmasın

a=float(input("vize notu 1:"))
b=float(input("vize notu 2:"))
c=float(input("final notu:"))
ort= (((a+b)/2)*6/10)+(c*4/10)
print(f"öğrencinin ortalaması: {ort} , geçme durumu {ort>=50 or c>=70}")


#kişinin ad kilo boy bilgilerini alıp kilo endeksi hesaplayınız.
#formül= (kilo/boy uzunluğunun karesi)
#0-18.4 -----zayıf
#18.5-24.9-------normal
#25.0-29.9-------fazla kilolu
#30.0-34.0----obez

ad=(input("adınız:"))
kilo=float(input("kilo:"))
boy=float(input("boy:"))
formül=kilo/(boy**2)
zayıf=(formül>=0) and (formül<=18.4)
normal=(formül>=18.5) and (formül<=24.9)
fazla_kilo=(formül>=25) and (formül<=29.9)
obez=(formül>=30) and (formül<=34)

print(f"{ad} isimli kişinin kilo indeksi :{formül} kilo durumu zayıf:{zayıf}")
print(f"{ad} isimli kişinin kilo indeksi :{formül} kilo durumu normal:{normal}")
print(f"{ad} isimli kişinin kilo indeksi :{formül} kilo durumu fazla kilolu:{fazla_kilo}")
print(f"{ad} isimli kişinin kilo indeksi :{formül} kilo durumu obez:{obez}")
