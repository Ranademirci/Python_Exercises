from datetime import datetime
from datetime import timedelta #ileri bi tarihi bulmak için bunu import etmek gerekir
# from datetime import time
# from datetime import time

#datetime ile time date özelliklerini kullanabiliriz
#import datetime   result=dir(datetime.datetime)
result=datetime.now()
simdi=datetime.now()
result=simdi.month  #datetime.now().month  now yerine today da kullanılabilir.
# result=dir(datetime.time)
# result=dir(datetime.date)
result=datetime.ctime(simdi) #şuanla alakalı daha açıklayıcı veriyo
result=datetime.strftime(simdi,"%Y") #yıl bilgisi
result=datetime.strftime(simdi,"%X") #saat bilgisi
result=datetime.strftime(simdi,"%d")  #gün bilgisi
result=datetime.strftime(simdi,"%a")  #gün bilgisi string
result=datetime.strftime(simdi,"%b")  #ay bilgisi string
result=datetime.strftime(simdi,"%Y %B %A")
t="21 april 2019 hour 10:12:30"
result=datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
result=result.year

birthday=datetime(1983,5,9,12,30,10)
result=datetime.timestamp(birthday) #saniye
result=datetime.fromtimestamp(result) #saniye to datetime
result=datetime.fromtimestamp(0)#bilgisayarlar için milad bilgisi gelir
result=simdi-birthday #timedelta
# result=result.days 
# result=result.seconds
# result=result.microseconds

result=simdi+timedelta(days=10,hours=10) #10 gün sonrasını bulur 10 saat sonrasını bulur
#- ile 10 gün gerisini de bulabilirsin
print(result)

