import os # işletim sistemiyle alakalı bir bilgi talebinde bulunabilirsiniz ve işlem yapabilirsiniz.
import datetime

result = dir(os) # os içerisinde bir sürü class ve method bulunur.
result = os.name # hangi işletim sistemi olduğunu söyler.

######################################################################################################################################################
## Dizin Değiştirme ##
# os.chdir('C:\\') # belirttiğimiz dizine gider.
# os.chdir('..') # bir üst dizine geçer.
# os.chdir('../..') # iki üst dizine geçer.

######################################################################################################################################################
## Klasör Oluşturma ##
# os.mkdir('newdirectory') # aynı dizin içerisinde bir klasör oluşturur. chdir metodunda sonra çalıştırılırsa chdir dizininde belirtilen yerde klasör oluşur.
# os.makedirs("newdirectory/yeniklasör") # istediğimiz dizine alt alta klasörler oluşturabiliriz.
# os.rename("newdirectory","yeniklasör") # klasörün ismini değiştirme.
# os.rmdir("newdirectory") # klasörü siler.
# os.removedirs("newdirectory/yeniklasör") # gidip dizindeki son gösterdiğimiz klasörü siler.

######################################################################################################################################################
## Etkin Dizini Öğrenme ##
# result = os.getcwd() # dosyanın dizinini gösterir.

######################################################################################################################################################
## Listeleme ##
# result = os.listdir() # Şu anda etkin olan dizin içerisindeki klasörleri gösterir.
# result = os.listdir('C:\\') # istediğimiz konumdaki dizini listeleme.

# for dosya in os.listdir(): # mevcut konumdaki .py uzantıyla biten tüm dosyaları listelemiş oluruz.
#     if dosya.endswith('.py'):
#         print(dosya)

# result = os.stat("_datetime.py")
# result = result.st_size/1024 # dosyanın KB cinsinden değerini buluruz.
# result = datetime.datetime.fromtimestamp(result.st_ctime) # Dosyanın oluşturulma zamanını bize anlıyacağımız dile çevirerek söyler.
# result = datetime.datetime.fromtimestamp(result.st_atime) # Bu dosyaya son erişilme zamanı. 
# result = datetime.datetime.fromtimestamp(result.st_mtime) # Son değiştirilme tarihi.

# os.system("notepad.exe") # işletim sistemi üzerinden istediğimiz bi programı çalıştırabiliriz.

######################################################################################################################################################
## Path Özellikleri ##
result = os.path.abspath("_os.py") # aradığımız dosyanın tam konumunu bize söyler.
result = os.path.dirname("c:/Users/murte/Desktop/python_kütüphaneler/1-web-scraping/_os.py") # tam konumu verilen bir dosyanın dizin ismini alıyoruz.
result = os.path.dirname(os.path.abspath("_os.py")) # 2 metodu aynı anda kullanıyoruz. Önce bize dosyanın tam konumunu buluyo daha sonra dosyanın dizin ismini bize gönderiyor.
result = os.path.exists("c:/Users/murte/Desktop/python_kütüphaneler/1-web-scraping/_os.py") # dosyanın var olup olmadığını sorgular. varsa True değeri verir.
result = os.path.isdir("c:/Users/murte/Desktop/python_kütüphaneler/1-web-scraping/_os.py") # klasör modülü True değerini verir fakat _os.py bir dosya olduğu için false değeri verir.
result = os.path.isfile("c:/Users/murte/Desktop/python_kütüphaneler/1-web-scraping/_os.py") # dosya modülü true bilgisi verir.
result = os.path.join("C:\\","deneme","deneme1") # klasörleri oluşturmaz ancak bize bir path oluşturur.
result = os.path.split("C:\\deneme") # dizinleri ayırır. listeler.
result = os.path.splitext("_os.py") # dosyanın ismi ile uzantısını ayırır. ayırdıktan sonra uzantısını yada ismini değiştirebilirsiniz.
result = result[0] # dosyanın ismini bize verir.
result = result[1] # dosyanın uzantısını bize verir.

######################################################################################################################################################

print(result)