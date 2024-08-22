#dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
#kullanımı: open(dosya_adi,dosya_erişme_modu)
#dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w" (Write) yazma modu. 
# Dosyayı konumda oluşturur.
# dosya içeriğini siler ve yeniden ekleme yapar

# file= open("newfile.txt","w")
# file.close()
# file=open("C:/Users/ranad/OneDrive/Masaüstü/newfile.txt","w")
# encoding="utf-8"  bu okunamayan karekterleri okunur hale getirir
file= open("newfile.txt","w",encoding="utf-8")
file.write("hellö")
file.close()


# "a" (append) ekleme. dosya konumda yoksa oluşturur.
file= open("newfile.txt","a",encoding="utf-8")
file.write("\nhello")
file.close()

# "x" (create) oluşturma. dosya zaten varsa hata verir.
file= open("newfile2.txt","x",encoding="utf-8")

# "r" (read) okuma varsayılan. dosya konumda yoksa hata verir