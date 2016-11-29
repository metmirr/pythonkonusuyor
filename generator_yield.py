# -*- coding: utf-8 -*-
"""
    Generators:
    -----------
    Generators iteratörler gibidirler. Bir listenin elemenları üzerinde for ile dönmek iteratörlere
    örnek verilebilir. İteratörler ile generatörler arasındaki fark ise bir liste üzerinde bir çok kez
    dolaşabilirsiniz ve değerleri hafızada tutulurlar. Yani değerleri önceden bellidir. Ama generatörler
    de durum farklıdır; değerleri hafızada tutullmazlar, sadece değer istenildiğinde üretilip verilir ve 
    bir generatorü bir kez kullandığınızda bir daha kullanmaya kalkarsanız hata alırsınız. Çünkü bir kez
    kullanıldıklarında içleri boşalır.
    
    Yield:
    ------
    yield kelimesi aynı return gibidir ancak tek farkla, yield geriye generatör döndermek için kullanılır.
"""
# iterator oluşturma
listem = [x for x in range(5)]
for l in listem:
  print(l)
#listem burada da kullanılabilir.

# generator oluşturma
generatorum = (x for x in range(5))
for g in generatorum:
    print(g)
# generatorum daha kullanılamaz çünkü for içerisinde bütün elemanları oluşturuldu ve kullanıldı.
# her oluşturulan eleman kullanıldıktan sonra unutulur.

# yield kullanılımı
def generator_olustur():
    for i in range(5):
        yield i*i

gen = generator_olusturma() # fonksiyondan geriye generator dönderiliyor. yield ile
# gen
# <generator object gen at 0x0000000000547AF0>
for g in gen:
    print(g)
# gen daha fazla kullanılamaz.
