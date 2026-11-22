# Bu program kullanıcının adını ve doğum yılını alıp yaşını hesaplar.

# datetime modülünü içe aktarıyoruz; bu yılı otomatik öğrenmek için kullanılacak
from datetime import date

# Kullanıcıdan adını metin olarak alıyoruz
ad = input("Adınız nedir? ")

# Kullanıcıdan doğum yılını alıp int() ile tam sayıya çeviriyoruz
dogum_yili = int(input("Doğum yılınız nedir? "))

# Bugünün tarihinden içinde bulunduğumuz yılı alıyoruz
bu_yil = date.today().year

# Yaşı, bu yıldan doğum yılını çıkararak hesaplıyoruz
yas = bu_yil - dogum_yili

# Kişiye özel karşılama mesajını ekrana yazdırıyoruz
print(f"Merhaba {ad}! Bu yıl {yas} yaşındasın. Kodlama dünyasına hoş geldin!")
