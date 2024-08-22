#kendimiz koşula bağlı exception fırlatıyoruz.


# x=10

# if x>5 :
#     raise Exception("x 5 ten büyük değer alamaz")


def check_password(psw):
    import re #regular expression modülü import edip bunun aracılığıyla kontrol işlemi yapıcaz
    if len(psw)<8:
        raise Exception("parola en az 7 karekter olmalı")
    
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harf içermeli")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf içermeli")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam içermeli")
    elif not re.search("[_@$]",psw):
        raise Exception("parola alpha numeric karakter içermeli")
    elif  re.search("\s",psw):
        raise Exception("parola boşluk içermemelidir.")
    else:
        print("geçerli parola")
password="1234567A_a"
try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("geçerli parola : else")
finally:
    print("validation tamamladnı")