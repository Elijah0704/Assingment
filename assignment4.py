def  fibonacci(kacıncı_sayıya_kadar):
    sayi1=0
    sayi2=1
    print(sayi1)
    print(sayi2)
    i=0
    while(i<kacıncı_sayıya_kadar):
        sayi3=sayi1+sayi2
        print(sayi3)
        sayi1=sayi2
        sayi2=sayi3
        i+=1
kacıncı_sayıya_kadar=int(input("lütfen sayı giriniz"))
fibonacci(kacıncı_sayıya_kadar)
