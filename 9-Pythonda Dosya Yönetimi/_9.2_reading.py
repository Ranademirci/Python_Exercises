# try:
#     file=open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#    print("dosya okuma hata")
# finally:
#     print("dosya kapadnı")
#     file.close()

file=open("newfile.txt","r",encoding="utf-8")
# #for döngüsü
# # for i in file:
# #     print(i,end="")

# *********#read() fonksiyonu**********
# content1=file.read() #dosyadaki tüm her şeyi okur
# print("içerik1")
# print(content1) #ve yazdırır
# content2=file.read() #dosya daha kapanmadığı için imleç yazının sonunda
# print("içerik2")
# print(content2) # bu yüzden bişey yazılmaz 
# content=file.read(5) #ilk 5 karekteri alır
# content=file.read(3)

# print(content)

#************readline() fonksiyonu*******
# content=file.readline() #kaldığı konumdan itibaren 1 satır okur
# print(content)
# print(file.readline(),end="") #print(content) ile aynı işlevi yapar.end sonuna boşluk bırakır.

#*******readlines()************
liste=file.readlines()
print(liste[0]) #liste şeklinde verir
print(liste[1])

file.close()