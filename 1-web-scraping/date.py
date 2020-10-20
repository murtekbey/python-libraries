from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

simdi = datetime.now()
simdi = datetime.today()

result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')  # Sadece yıl bilgisi.
result = datetime.strftime(simdi,'%X')  # Sadece saat bilgisi.
result = datetime.strftime(simdi,'%d')  # Sadece gün bilgisi.
result = datetime.strftime(simdi,'%A')  # Sadece gün bilgisini string olarak verir.
result = datetime.strftime(simdi,'%B')  # Sadece ay bilgisini string olarak verir.
                                        # İstediğimiz bilgiyi spesifik bir şekilde istediğimiz gibi alabiliriz.
result = datetime.strftime(simdi,'%Y %B %A') # Yıl, Ay, Gün şeklinde.

t = '15 April 2019 hour 10:12:30' # datetime objesine çeviricez.

result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S') # bu şekilde önceden girdiğimiz string bilgiyi, tarih bilgisine dönüştürebiliriz.
result = result.year

birthday = datetime(1983,5,9,12,30,10) # (yıl,ay,gün,saat,dakika,saniye)

result = datetime.timestamp(birthday) # yazdığımız tarihin saniye cinsinden değeri
result = datetime.fromtimestamp(result) # saniye cinsinden yazılan değerin tarih cinsinden değeri.
result = datetime.fromtimestamp(0) # 1970-01-01 - Bilgisayarlar için kullanılan milad bilgisi. Tarih 1970'den itibaren başlar.

result = simdi - birthday # timedelta 

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)

result = simdi + timedelta(days=10) # Şimdinin tarihi üzerine timedelta() komutu ile 10 gün ekledik.
result = simdi + timedelta(days=730, minutes = 10) # Şimdinin tarihi üzerine timedelta() komutu ile 730 gün + 10 dakika ekledik.

result = simdi - timedelta(days=10) # şimdinin tarihinden 10 gün çıkardık.
result = datetime.strftime(simdi,'%d/%m/%Y %X')
print(result)