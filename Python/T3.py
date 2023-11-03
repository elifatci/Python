print("====Artik Yil Hesabi====")
yil=int(input("Lutfen bir yil giriniz"))

if (yil%4==0 and yil/100!=0) or (yil%400==0):
    print("Artik yildir")
else:
    print("Artik yil degildir")