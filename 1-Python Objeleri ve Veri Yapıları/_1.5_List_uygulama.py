names=["Ali","Yağmur","Hakan","Deniz"]
years=[1998,2000,1998,1987]

#Cenk ismini listenin sonuna ekleyin
names.append("Cenk")
print(names)

#sena değerini listenin başına ekleyin
names.insert(0,"sena")
print(names)

#deniz ismini listeden silin
names.remove("Deniz")
print(names)

#Hakan değerinin indexini bulun
index=names.index("Hakan")
print(index)

#Ali listenin bir elemanı mı
result= "Ali" in names
#index= names.index("Ali")     #bu şekilde de ali isminin indexi 0 dan büyük çıkarsa demekki listede ali değeri var ama -1 çıkarsa listede ali değerinin olmadığı anlaşılır
#print(index)
print(result)

#names liste elemanlarını ters çevirin
names.reverse()

print(names)

#names listesini alfabetik sıraya göre sırala
names.sort()
print(names)

#years listeisni rakamsal büyüklüğe göre sırala
years.sort()
print(years)

#str="Chevrolet,Dacia" karakter dizisini listeye çevirniz.
str="Chevrolet,Dacia"
result=str.split(",")
print(result)

#years dizisinin en büyük ve en küçük elemanı nedir?
min=min(years)
max=max(years)
print(min)
print(max)

#years dizisinde kaç tane 1998 değeri vardır
sayi=years.count(1998)
print(sayi)

#years dizisinşn tüm elemanlarını siliniz
years.clear()
print(years)

#kullanıcıdan alcağınız 3 tane marka bilgisini bir listede saklayın
marka1=(input("marka1:"))
marka2=(input("marka2:"))
marka3=(input("marka3:"))
list=marka1+" "+marka2+" "+marka3
print(list)
        
        #veya markalar diye boş liste oluşturursun ve 
        #kullanıcıdan aldığın değeri listenin sonuna eklersin
markalar=[]
marka=input("marka: ")
markalar.append(marka)
marka=input("marka: ")
markalar.append(marka)
marka=input("marka: ")
markalar.append(marka)
print(markalar)

