# with open("newfile.txt","r+",encoding="utf-8")as file: #r+ yerine w yazsaydı dosyanın içeriğini siler deneme yazardı ama şimdi  imleç nerdeyse oraya deneme yazar günceller
#     file.seek(20)
#     file.write("deneme")


# with open("newfile.txt","r+",encoding="utf-8")as file:
#     print(file.read())

#r+ hem okuyuo hem yazcağımız anlamına gelir bu da update dir

#**********sayfa sonunda güncelleme****************
# with open("newfile.txt","a",encoding="utf-8")as file: #append sonuna ekleyeceği için imleç sona gelir ve o şekil yazdırma işlemi yaparız
#     file.write("\nselam")


#********sayfa başında güncelleme**********
# with open("newfile.txt","r+",encoding="utf-8")as file:
#     content=file.read()
#     content="merhaba\n"+content
#     file.seek(0)
#     file.write(content)




#**sayfa ortasında güncelleme*************
with open("newfile.txt","r+",encoding="utf-8")as file:
    list=file.readlines()
    list.insert(1,"sena korkmaz\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8")as file:
    print(file.read())