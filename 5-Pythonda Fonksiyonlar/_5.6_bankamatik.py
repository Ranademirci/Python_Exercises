#BANKAMATİK UYGULAMASI

sadikHesap={
"ad":"Sadık Turan",
"hesapNo":"12345678",
"bakiye":3000,
"ekHesap":2000
}
aliHesap={
"ad":"Ali Turan",
"hesapNo":"12345678",
"bakiye":2000,
"ekHesap":1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap["ad"]}")

    if (hesap["bakiye"]>= miktar):
        hesap["bakiye"]-=miktar
        print("paraınızı alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam=hesap["bakiye"]+hesap["ekHesap"]

        if (toplam>=miktar):
            ekHesapKullanimi=input("ek hesap kullanılsın mı?(E/H)")
            if ekHesapKullanimi=="E":
                ekHesapKullanılcakMiktar=miktar-hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekHesap"]-=ekHesapKullanılcakMiktar
                print("paraınızı alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bakiye bulunmaktadır")
        else:
            print("bakiye yetersiz")
            bakiyeSorgula(hesap)
             
def bakiyeSorgula(hesap):
    print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]}tl bulunmaktadır. ek hesap limitiniz ise {hesap["ekHesap"]}tl bulunmaktadır")

paraCek(sadikHesap,3000)
print("*************************")
paraCek(sadikHesap,2000)
