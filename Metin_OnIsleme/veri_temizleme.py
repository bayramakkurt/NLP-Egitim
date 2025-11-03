
#Boşlukların Temizlenmesi
def bosluk_temizle(text):
    return " ".join(text.split()) #Önce metni kelimelerine ayırır ardından 1 boşlukla kelimeleri birleştirir.

#Büyük-Küçük Harf Dönüşümleri
def buyuk_kucuk_harf_donustur(text):
    return text.lower() #Bütün harfleri küçük harfe çevir.
#Noktalama İşaretlerinin kaldırılması
import string
def noktalama_kaldir(text):
    return text.translate(str.maketrans("", "", string.punctuation)) #From, to, delete parametreleri ile from="", to="", delete=bütün noktalama işaretleri olarak bütün noktalamaları siler.
#Özel Karakterlerin Kaldırılması
import re
def ozel_karakter_kaldir(text):
    return re.sub(r"[^A-Za-z0-9\s]", "", text) #Substract işlemi için pattern=harf sayı hariç hepsi, replacement=boş-sil, string=text işlemini uygular ve özel karakterleri siler.
#Yazım Hatalarının Düzeltilmesi
from textblob import TextBlob #Metin analizlerinde kullanılan bir kütüphane
def yazim_hata_duzelt(text):
    return TextBlob(text).correct() #Correct: Yazım hatalarını düzeltir.
#HTML ve URL Temizleme
from bs4 import BeautifulSoup
def html_url_temizleme(text):
    return BeautifulSoup(text, "html.parser").get_text() #BeautifulSoup ile HTML kısmını ayırıyoruz ve get_text() ile sadece metin kısmını alıyoruz.


#Starter
text = "Hello,      World!      2025"
print(f"Original Text: {text} \nTemizlenmiş Text: {bosluk_temizle(text)}\n--------------------------------------------------------")

text = "Hello, World! 2025"
print(f"Original Text: {text} \nTemizlenmiş Text: {buyuk_kucuk_harf_donustur(text)}\n--------------------------------------------------------")

text = "Hello, World! 2025"
print(f"Original Text: {text} \nTemizlenmiş Text: {noktalama_kaldir(text)}\n--------------------------------------------------------")

text = "Hello, World! 2025%+'^&/()=?_"
print(f"Original Text: {text} \nTemizlenmiş Text: {ozel_karakter_kaldir(text)}\n--------------------------------------------------------")

text = "Hella, W0rld! 2025"
print(f"Original Text: {text} \nTemizlenmiş Text: {yazim_hata_duzelt(text)}\n--------------------------------------------------------")

text = "<div>Hello, World! 2025</div>"
print(f"Original Text: {text} \nTemizlenmiş Text: {html_url_temizleme(text)}\n--------------------------------------------------------")