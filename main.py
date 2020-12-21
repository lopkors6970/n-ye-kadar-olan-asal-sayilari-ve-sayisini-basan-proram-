sayi = int(input("Bir tam sayi degeri giriniz:"))
sayac = 0 
sayac2 = 0 

for i in range (2,sayi+1):
    sayac = 0 
    for j in range (2,i):
        if (i%j==0):
            sayac +=1
            break
    if (sayac==0):
        print(i)
        sayac2+=1
print("Toplam {} adet asal sayi vardir.".format(sayac2))
