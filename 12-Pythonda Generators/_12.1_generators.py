def cube():
    
    for i in range(5):
       yield i**3
       
 
for i in cube() :
    print(i)

#oluşturduğumuz bir değeri br liste içerisinde saklamak gerekmiyosa
#o elemanı sadece o anda kullanıyosak ve daha sonra o elemana ulaşmak istediğimizde
#bulamicaksak bize o anda üretilen değer gelir. yieldden her seferinde talep edilcek.bellekte boşune yer tahsis etmiyz

liste=[i**3 for i in range(5)] #bunu generator şeklinde yapmak istersek köşeli parantezleri () bunlara çevirmemiz yeterli olcak
print(liste)

generator=(i**3 for i in range(5)) 
for i in generator:
    print(i)
# print(next(generator))
# print(next(generator))
# print(next(generator))