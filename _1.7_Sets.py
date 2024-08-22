fruits={"orange","apple","banana"}
#normal listeden farkı vra mesela index numarasıyla ulaşamazsın bie bilgiye.ve listeyi sıralayamayız.
for x in fruits:
 print(x)

fruits.add("cherry")
fruits.update("mango","grape")  #update ile birden fazla ekleyebiliriz. var olan bi elemanı bidaha eklemek istersen bişey değişmez her eleman 1 kere gözükür

myList=[1,2,3,5,2,2,3]
print(set(myList))  #set sayesinde tekrarlanan ifadeler tekrarlanmaz bir daha
#remove methoduyla discard methodu listelerde aynı işleve yarıyor. burda da işe yarar
#pop methodu listede son elemanı silmeye yarıyodu ama burdali fruitste işe yaramaz. silinen eleman herhangş biri olabilir.
#listelerde işe yarayan clear methodu da burda işe yarar.

values=1,2,3,4,5
x,y,*z=values
#böyle dersek x e 1 ,y ye 2 geri kalanları z ye eşler
