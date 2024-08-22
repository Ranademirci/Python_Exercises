#key - value ilişkisi
sehirler=["Kocaeli","İstanbul"]
plakalar= [41,34]
#sehirler listesinde kocaeli değerinin indexini alır plakalarda o index numarasına bakar yazdırır.
print(plakalar[sehirler.index("Kocaeli")])

# print(plakalar["Kocaeli"]) bilgisi bizi 41 e götürsün diye key value ilişkisi kurcaz
plakalar= { "Kocaeli": 41,"İstanbul": 32}
print(plakalar["Kocaeli"])

plakalar["ankara"]=6
plakalar["Kocaeli"]="new value"  #güncelleme yapabiliriz
print(plakalar)

#oluşturulan key için alt key ler de oluşturulabilir
users={
    "ranademirci" :{
        "age":20,
        "email": "rana@gmail.com"
    },
    "sedef bilgin":{
        "age":35,
        "email": "sedef@gmail.com",
        "roles" :["admin","users"]
    }
}
print(users["ranademirci"] ) #dersem o keyin valuelerini görebilirim
print(users["sedef bilgin"]["age"])
print(users["sedef bilgin"]["roles"][0])


##########dictionary_demo.py####################
'''ogrenciler={
    "120":{
      "ad": " Ali",
      "soyad" :" Yılmaz",
      "telefon" :"533 333 33 33"

    },
    "125":{
     "ad": " Can",
      "soyad" :" Korkmaz",
      "telefon" :"534 444 44 44"

    },
    "128":{
        "ad": " Volkan",
      "soyad" :" Yükselen",
      "telefon" :"535 555 55 55"
    }

}'''
#yukardaki bilgileri kullanıcıdan alıp dictionary içinde sakla

ogrenciler={}

number = input ("öğrenci no:")
name= input("öğrenci adı:")
surname=input("öğrenci soyadı:")
phone = input("öğrenci telefon:")

'''ogrenciler[number]={
    "ad": name,
    "soyad":surname,
    "telefon": phone
}'''  
#update de yukarıdaki kullanabileceğimiz bir alternatif.Ayrıdca update de , ile ayırarak başka objeler de ekleyebilriz ama bunu yukarda yapamayız.
ogrenciler.update({
    number:{
        "ad": name,
        "soyad":surname,
        "telefon": phone,
    }
})

#yukardakileri 3 kere copy paste yaparsan  3 kere sorar ve kaydeder.
print(ogrenciler)



print("*"*50)
#burası sayı girdisini alır ve o sayıyla eşleşeln bilgileri listeler.
ogrNo =input("öğrenci no:")
ogrenci=ogrenciler[ogrNo]
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci["ad"]} soyadı: {ogrenci["soyad"]} ve telefonu ise {ogrenci["telefon"]}")  