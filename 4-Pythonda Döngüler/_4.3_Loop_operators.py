
#RANGE
for item in range(0,10,2):
  print(item)

print(list(range(0,10,2))) #bu şekilde liste içerisinde gösterir
#burada 0 dan başlayıp 10 a kadar artış miktarı 2 olan
#range methodu aslında bi liste oluşturuyo sen başını sonunu ve artış miktarını ayarlayabilirsin 

#-----------------------------------------------------------------------------------------------------------
#ENUMERATE
#hem indeksleri hem de değerleri almayı sağlar. 
#Bu, döngü sırasında elemanların sırasını takip etmek gerektiğinde oldukça kullanışlıdır

greeting="Hello There"
for index,item in enumerate(greeting):
  print(f"index: {index} letter:{item}")

#--------------------------------------------------------------------------------------
#ZİP

list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]
print(list(zip(list1,list2,list3)))
for item in zip(list1,list2,list3):
  print(item)

for a,b,c in zip(list1,list2,list3):   # a dersek sadece 1,2,3,4,5 i alır ab dersek list 1 ile list 2 yi zipler 
  print(a,b,c)


