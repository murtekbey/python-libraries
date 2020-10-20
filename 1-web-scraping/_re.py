import re # Regular Expression Modülü bize bir arama sonucunda bir sonuç döndürür.

# result = dir(re)

# re module

str = "Python Programlama"

# re.findall()

# result = re.findall("Python",str) # Python ifadelerini bulur.
#result = len(result)

# re.split()

# result = re.split(" ",str) # ifadeyi bölmelere ayırır.
# result = re.split("P",str)

# re.sub()

# result = re.sub(" ","-",str) # Tüm boşluk karakterleri yerine - ekler.
# result = re.sub("\s","-",str) # \s zaten Regular expression'da boşluk karakterlerini ifade ediyor. Aynı işlemi yapar.

# re.search()

# result = re.search('Python',str) # Match objesi döner. karakteri match objesi içerisinden aratır.

# result = result.span() # kaçıncı indexde olduğunu söyler.
# result = result.start() # ilk indexini söyler.
# result = result.end() # son indexini söyler.
# result = result.group() # bulduğu ifadeyi bize gönderir.
# result = result.string # hangi string ifadede aradığını yazdırır.

# regular expression

"""

    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.

         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches

         [a-e]  => [abcde] --> a ile e arasındaki tüm karakterleri arar.
         [1-5]  => [12345] --> 1 ile 5 arasındaki tüm karakterleri arar.
         [0-39] => [01239] --> burada dikkat etmemiz gereken 0 ile 3 arasındaki tüm sayıları araması ardından 9'u arar. yani 0'dan 39 a kadar aramaz.

         [^abc] => abc dışındaki tüm karakterleri arar ^ konulduğu zaman başına.
         [^0-9] => rakam olmayan tüm karakterleri arar. 

"""

result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-e]", str)
result = re.findall("[a-z]", str) # a dan z ye tüm karakterleri arar.
result = re.findall("[0-5]", str) # 0 dan 5 e kadar tüm karakterleri arar.
result = re.findall("[^abc]", str)
result = re.findall("[^0-9]", str)

"""
    . - Her hangi bir tek karakteri belirtir.

        .. => a    : No match --> a aratılırsa eşleşme bulamaz
              ab   : 1 match --> ab aratılırsa 1 eşleşme bulur
              abc  : 1 match --> abc aratılırsa yine 1 eşleşme bulur çünkü bir sonraki aramadada 2 basamaklı daha olmasını ister fakat geriye sadece c kalıyor.
              abcd : 2 matches --> abcd aratılırsa burada 2 eşleşme bulur. ilk eşleşme ab, ikinci eşleşme cd olur.

    
"""

result = re.findall("...", str) # 3 basamaklı olan tüm karakterleri arar.
result = re.findall("Py..on", str) # Pyt..on ifadesindeki .. ifadesi değişken olduğunu tanımlar. burada önemli olan py ile başlayıp on ile bitmesi ve 6 basamaklı olması.

"""
    ^ - Belirtilen string karakterlerle başlıyor mu ? --> String ifadenin en başını ifade eder.

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""

result = re.findall("^P",str) # verilen string ifadenin en başındaki karakteri bulur. P ile başladığı için buluyor ama örneğin 'Kursu' kelimesini bulmak için K'yi aratsaydık sonuç bulamaz.


"""
    $ - Belirtilen karakterle bitiyor mu ? --> String ifadenin en sonunu ifade eder.

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""

result = re.findall("t$",str) # verilen string ifadenin en sonundaki karaterini bulur.
result = re.findall("saat$",str)
result = re.findall("saatt$",str)

"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
result = re.findall("sa*t",str) # a'dan 0 veya daha fazla olduğu sürece karakteri bulur

"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

result = re.findall("sa+t",str) # a karakterinden en az 1 tane olmasi gerekir.

"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.

        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

result = re.findall("sa?t",str) # a karakterinden 0 yada 1 kere olmasi gerekir.

"""
    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
result = re.findall("a{2}", str) # a karakterinin 2 kez tekrarlandığı yeri bize getirir. "saat" 
result = re.findall("[0-9]{2}", str) # 2 basamaklı rakamı str ifadesinde arar ve getirir. "40"

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b karakterlerini arar.

            cde =>    no match --> a ya da b ifadesi olmadığı için eşleşme yok.
            ade =>    1 match --> a ifadesi olduğu için 1 eşleşme bulur.
            acdbea => 3 match --> a, b ve tekrar a ifadeleri olduğu için 3 eşleşme bulur
"""

"""
    () - gruplamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir. a,b ya da c farketmez fakat arkasından xz gelmesi gerekiyor.
                   #  --> Örneğin : axz , bxz, cxz gibi.
"""

    # \ - Özel karakterleri aramamızı sağlar.
    #     \$a => $ karakterinin arkasına a karakterinin arar. Dolar işaretini aramamızı sağlar.
    #            $ regular exp. engine tarafından yorumlanmaz. 

    # \A - Belirtilen karakter string in başında mı ?
    #      \Athe => the string in başındamı

    # \Z - Belirtilen karakter string in sonunda mı ?
    #      the\Z => the string in sonunda mı

    # result = re.findall("\APython", str) # String ifadenin başındaki ilk ifade python mu diye ararız.
    # result = re.findall("saat\Z", str) # String ifadenin başındaki son ifade saat mi diye arama yapmış oluruz.

    # \b - Belirtilen karakter kelimenin başında ya da sonunda mı ?
    #      \bthe => the kelimenin başında mı?
    #      the\b => the kelimenin sonunda mı?

    # \B - Belirtilen karakter kelimenin başında ya da sonunda değil mı ?
    #      \Bthe => the kelimenin başında değil mi?
    #      the\B => the kelimenin sonunda değil mi?
    
    # \d - [0-9] ile aynı anlama gelir yani rakamları arar.
    #      \d => 12abc34

    # \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
    #      \D => 1ab44_50

    # \s - Boşluk karakterlerini arar.  
    # \S - Boşluk karakterleri dışındakiler.
    # \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    # \W - \w nin tam tersi


print(result)