x,y,z=2,5,10
numbers=1,5,7,10,6
'''
#kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z ifadelerinin toplamı arasındaki fark
a=int(input("birinci sayıyı girin:"))
b=int(input("ikinci sayıyı girin:"))
result=(a*b)-(x+y+z)
print(result)

#y nin x e kalansız bölümünü hesaplayınız
result=y//x
print(result)
'''
#x,y,z toplamının mod 3 ü nedir
result=(x+y+z)%3
print(result)

#ynin xinci kuvvetini hesaplayınız
result=y**x
#x,*y,z =numbers işlemine göre z nin küpü kaçtır?
x,*y,z=numbers
print(z**3)
#x,*y,z =numbers işlemine göre ynin değerleri toplamı nedir?
x,*y,z=numbers
print(y[0]+y[1]+y[2])