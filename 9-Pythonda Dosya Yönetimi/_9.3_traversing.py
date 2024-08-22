with open("newfile.txt","r",encoding="utf-8") as file:
   content=file.read()
   print(content)
   file.seek(0) #imlecin konumunu belirleyebiliriz.
   print(file.tell())#imleçin nerde olduğunu gösterir
   content2=file.read()
#with operatörü kodun sonunda sonlanacağı için dosya kapatma methodunu yazmamıza gerek kalmaz.
