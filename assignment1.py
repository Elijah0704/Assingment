#Assignment_3
#Yapmaya çalıştığım şey yaşı 75 üstü ve sigara içiyor mu diye bakmak, ikisinden biri varsa risk var.
#Kronik hastalığı varsa risk var. Bağışıklığı yoksa risk var. Bunlar üzreinde bool cebri kullanımı ayarladım.
#Bağışıklığı varsa her türlü riski yoktur.
age = int(input("Yaşınızı giriniz;"))
if age >=75 :
    print(True) 
else :
    print(False)
cigarette = int(input("Sigara kullanıyor musunuz?,Kullanıyorsanız 1 kullanmıyorsanız 0 yazınız "))
if cigarette ==0 :
    print(False) 
else :
    print(True)
chronic = int(input("Kronik hastalığınız var mı? Varsa 1 yoksa 0 yazınız. "))
if chronic ==0 :
    print(False) 
else :
    print(True)
immune = int(input("Bağışıklığınız var mı? Varsa ^^^^0^^^^ yoksa ^^^^1^^^ yazınız. "))
if immune ==0 :
    print(False) 
else :
        print(True)
risk = int(((age and cigarette) or chronic) and immune)
if risk ==0 :
    print("Risk yoktur:(---", False , "---)") 
else :
    print("Risk vardır:(---", True ,"---)")
