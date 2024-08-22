# Liste oluştur
list = ["bmw", "mercedes", "mazda", "opel"]

# Listenin kaç elemanlı olduğunu yazdır
print(len(list))

# Listenin ilk ve son elemanını yazdır
print(list[0])
print(list[-1])

# "mazda" değerini "toyota" ile değiştir
list[2] = "toyota"
print(list)

# "mercedes" listenin bir elemanı mı?
result = "mercedes" in list
print(result)

#listenin -2 indeksindeki değer nedir?
print(list[-2])

#listenin ilk 3 elemanını alın
print(list[0:3])

#listenin son 2 elemanı yerine toyata ve renault değerlerşni ekle
list[-2:]=["toyata","renault"]
print(list)

#listenin üstüne nissan ve audi değerlerini ekle
list=list+["nissan","audi"]
print(list)

#listenin son elemanını silin
#list=list[:-1]  alternatif
del list[-1] 
print(list)

#liste elemanlarını tersten yazdır
list=list[-1::-1]
print(list)

#studentA= Yiğit,Turan,2003 (70,60,70) 
studentA=["Yiğit","Turan",2003,[70,60,70]]
print(f"{studentA[0]} { studentA[1]} {2024-studentA[2]} yasindadir ve not ortalaması: { ( studentA[3][0]+studentA[3][1]+studentA[3][2])/3}")


