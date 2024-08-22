#error handling=> hata yönetimi
#alabilecek olduğumuz hataları tahmin edip hataya göre error handling kodu yazmamız gerek
#print(a) =>name error tanımlanmamış a
#int("1a2")=> value error
#print(10/0)=> zero division error
#print("denem"e)#syntax error yazım yanlışı

# try:
#     x=int(input("x :"))
#     y=int(input("y :"))
#     print(x/y)
# #except ZeroDivisionError:
#     print("y için 0 girilemez")
# #except ValueError:
#     print("x ve y için sayısal değer girmelisiniz")

# except (ZeroDivisionError,ValueError) as e:
#     print("yanlış bilgi girdiniz ")
#     print(e)  #hatanın ne olduğunu yazar


# try:
#     x=int(input("x :"))
#     y=int(input("y :"))
#     print(x/y)

# except :
#     print("yanlış bilgi girdiniz ")

while True:
    try:
        x=int(input("x :"))
        y=int(input("y :"))
        print(x/y)

    except Exception as ex:
        print("yanlış bilgi girdiniz ",ex)
    else:
        break
    finally: #her zaman çalışır except veya else bloğu çalışmasına rağmen
        print("try except sonlandı.")