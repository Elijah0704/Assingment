#  Assignment-008/3 (Is it an Armstrong Number?)
#  Armstrong Sayılarını bulan Python programı
#  (Elimizdeki sayıyı rakamlara ayırıp, basamak sayısını 
#  bu rakamlara üs olarak veriyoruz ve bu sayıları topluyoruz.
#  Toplama işlemi sonucu yine aynı sayı çıkıyorsa
#  işte elimizdeki sayıya Armstrong Sayı deriz.)
while True:
    girilen_sayi=input("Sayı giriniz (Sonlandırmak 'a' ya basın.) : ")
 #  lütfen pozitif tam sayı yazınız
    if girilen_sayi=="a":
        break
    
    basamak_sayısı=len(girilen_sayi) #  basamak sayısını öğreniyorum
 
    toplam=0
    for i in range(basamak_sayısı):
        toplam = toplam + int(girilen_sayi[i])**basamak_sayısı
    
    if(toplam==int(girilen_sayi)):
        print("Girdiğiniz sayı bir Armstrong Sayı'dır!")
    else:
        print("Girdiğiniz sayı bir Armstrong Sayı değildir!")
 
