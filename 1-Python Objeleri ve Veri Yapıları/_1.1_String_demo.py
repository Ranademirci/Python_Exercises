course="abcçdefgğhıijklmnoöprsştuüvyz"
website="www.rana.com"
lenght=len(website)
y=len(course)
#course karekter dizisinde kaç karekter bulunur?
print(len(course))

#webiste içinden www karekterlerini alın
print(website[0:3])

#webiste içinden com karekterlerini alın
print(website[-3:lenght])

#course içinden ilk 15 ve son 16 karekteri alın
print(course[:15])
print(course[-15:])

#course dizisindeki karekterleri tersten yazdıralım
print(course[y:0:-1])

###############################################
name,surname,age="rana","d","20"
#bunları birleştirerek 1 cümlede yaz
print(f"my name is {name} {surname} and {age} yasindayim.")

################################################
#Hello word ifadesindeki w harfini W ya çevir
x="Hello world"
length=len(x)
print(x[:6]+"W"+x[-4:])
print(x.replace("w","W"))

#####################################
#abc ifadesini 3 kere yanyana yazdır
x="abc"*3
print(x)