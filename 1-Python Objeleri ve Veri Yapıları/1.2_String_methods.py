message="Hello my . name is Rana "
message=message.upper()  ##bu method sayesinde büyük harfle yazdırır.

message=message.lower() #bu method sayesinde küçük harfle yazdırılır.

message=message.title() #her kelimenin baş harfi büyük yazdırırlır.

message=message.capitalize()  #sadece ilk harf büyük harfe çevrilir.

message=message.strip() # başında ve sonunda bulunan boşluk karekterlerini siler.kullanıcının girdiği karekterlerinin baş ve sonundaki karekterleri silebilirz.
#lstrip ve rstrip soldan veya sağdan siler

message=message.split()  #kelimleri ayrıştırır.Cümleyi parçalara ayırır gibi.parantezin içinde nokta koyarsak noktaya göre ayrım yapar boşluğa göre değil.
#print(message[0]) #split ile ayırdığımız için dizindeki 0. index bize sadece hello kelimesini verir.

message=" ".join(message) # tırnak arasında boşluk olduğu için birleştirirken boşluk koyar her eleman arasına

index= message.find("is") #like kelimesini araştırsaydım cümlede olmadığı için -1 sayısı dönerdi

print(index) #bana 16 sayısını döndürür 16 sayısı ise is kelimesinin başlangıcının dizideki index numarasıdır. 

isFound=message.startswith("H") # message değişkeninin H ile başladığını sorar true döndürür. 
isFound=message.endswith("H")# message değişkeninin H ile sonlanıp sonlanmadığını sorar false döndürür döndürür. 
print(isFound)

message= message.replace(".",",")  # . ifadesini , ile yer değiştirir.
message=message.center(50,"*") #50 karekterlik bir alan oluşturur ve cümlemizi 50 karekterlik alanı ortalayack şekilde yerleştirir baştan ve sondan kalan yerlere * koyar.

message=message.ljust(50,"*")  #sola yaslar kelimeyi ve geri kalan yerlere * koyar. örneğin ************aaaaaaa gibi

message="Hello my . name is Rana "
message=message.lstrip("Hel ")  # parantez içindeki harfler çıkarılmış olarak yazılır.
print(message)

y="ranad".strip("r") #bu şekilde de yapabiliriz
print(y)

message=message.count("a",0,3) #0. indexten 3. indexe kadar kaç tane a harfi olduğunu söyler(message="Hello my . name is Rana ")
print(message)

message="Hello my . name is Rana "
message=message.isalpha() #alfabetik sıraya göre mi yazılmış kontrol eder.   isdigit() methodu da değerler rakamlardan mı oluşuyo kontrol eder.
print(message)