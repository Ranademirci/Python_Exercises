import re
result=dir(re)
 
#re module
str="python kursu: python programlama rehberiniz | 40 saat"
#re.findall()
##result=re.findall("python",str)
##result=len(result) #kaç tane olduğunu bulmak için

#re.split()
##result=re.split(" ",str)

#re.sub()
##result=re.sub(" ","-",str)  #değiştirme işlemi

#re.search()
result=re.search("python",str)
#result=result.span()#konumunu öğrenebilirsin
#result=result.start() #kaçıncı indexten başladığını
#result=result.end() #ka.ıncı indeksten bittiğini
#result=result.group()
#result=result.string #arama işleminde hangi string ifadede aradığı


#regular expresiion modülü

result=re.findall("[abc]",str)
result=re.findall("[a-e]",str) #abcde karekterlerini arar
result=re.findall("[1-35]]",str) #1235 şeklinde çübnkü tekrarlanan alan 1 3 arasıdır 5 aynen kalır
result=re.findall("[^abc]",str) #abc dışındaki bütün karekterler

result=re.findall("...",str)  #3 erli string halinde gruplar
result=re.findall("^p") # belirtilen string p ile başlıyor mu
result=re.findall("^a") #belirtilen string ifade a ile bitiyor mu
result=re.findall("sa*t")#bir karekterin sıfır ya da daha fazla sayıda olmasını kontrol eder
result=re.findall("sa+t") #bir karekterin bir ya da daha fazla sayıda olmasını kontrol eder
result=re.findall("sa?t") #bir karekterin sıfır ya da bir kere olmasını kontrol eder
result=re.findall("a{2}",str) #a kerakteri 2 kez arka arkaya tekrarlanan
result=re.findall("[0-9]{2}",str) #2 basamaklı rakamı arıyoruz
result=re.findall("a|b",str) #a veya b seçeneklerden birinin gerçekleşmesi gerekir
result=re.findall("(a|b)x",str) #gruplama yapmak için kullanılır a,b karekterleirnin arkasından x gelmelidir.
result=re.findall("\Apython",str)
result=re.findall("saat\Z",str)

#\ özel karekterleri aramamızı sağlar
#\Athe   the string in başında mı
#\Zthe   the string in sonunda mı
# \s boşluk karakterlerini arar
# \S boşluk karekterleri dışındakiker.
# \w alfabetik karekterler,rakamlar ve alt çizgi karekteri
# \W  \w nin tam tersi
print(result)