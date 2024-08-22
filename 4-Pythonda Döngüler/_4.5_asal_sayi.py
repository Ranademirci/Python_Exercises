#girilen bir sayının asal olup olmadığını bulun
##asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.


sayi=int(input("sayı girin:"))
asalmi=True
if sayi==1: #özel bir durum
    print(" 1 sayısı asal değildir.")

for i in range(2,sayi):
    if sayi%i==0:
       asalmi=False
       print(f"girdiğiniz sayı asal olma durumu: {asalmi}")
       break
else:
    print(f"Girdiğiniz sayının asal olma durumu :{asalmi}")

    