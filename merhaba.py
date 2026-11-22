# Bu program kullanıcının adını ve doğum yılını alıp yaşını hesaplar.

# datetime modülünü içe aktarıyoruz; bu yılı otomatik öğrenmek için kullanılacak
from datetime import date

# Kullanıcıdan adını metin olarak alıyoruz
ad = input("Adınız nedir? ")

# Kullanıcıdan doğum yılını alıp int() ile tam sayıya çeviriyoruz
dogum_yili = int(input("Doğum yılınız nedir? "))

# Bugünün tarihinden içinde bulunduğumuz yılı alıyoruz
bu_yil = date.today().year

# Doğum yılı içinde bulunulan yıldan büyükse uyarı veriyoruz; değilse yaşı hesaplıyoruz
if dogum_yili > bu_yil:
    print(f"Uyarı: {dogum_yili} yılı {bu_yil} yılından büyüktür. Lütfen geçerli bir doğum yılı girin.")
else:
    yas = bu_yil - dogum_yili
    print(f"Merhaba {ad}! Bu yıl {yas} yaşındasın. Kodlama dünyasına hoş geldin!")
