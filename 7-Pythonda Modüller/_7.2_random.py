import random

result=random.random()#0.0-1.0
result=random.uniform(1,10) #1 ile 10 arasında random sayı üretir
result=int(random.uniform(1,10)) #int dersek ondalıklı olur ancak tam kısmı gözükür
result=random.randint(1,100)#1 ile 100 arasıdna bir sayı üret ve bu sayı tam sayı olsun
greeting="Hello There"
names=["ali","yağmur","deniz","cenk"]
#result=names[random.randint(0,len(names)-1)]  # 0 ile names listesinin eleman sayısının 1 eksiği kadar
result=random.choice(names)
result=random.choice(greeting)
liste = list(range(10)) #10 kadar sayıları oluşturur listede
random.shuffle(liste) #liste elemanlarını karışık bi şekilde yerleştirip liste şeklinde verir
result=liste

liste=range(100) #100e kadar sayı oluşturur
result=random.sample(liste,3)  #listenin içerisinden rastgele 3 sayı getirir.

print(result)
