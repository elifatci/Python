print("==== Emeklilik Sorgulama ====")
cinsiyet= (input("Lutfen cinsiyetinizi giriniz Kadin/K, Erkek/E: ").lower())
yas=int(input("Lutfen yasinizi giriniz: "))


if cinsiyet=="kadin" or cinsiyet=="k" and yas>=60:
    print("Emekli olabilirsiniz")
elif cinsiyet=="kadin" or cinsiyet=="k" and yas<60:
    print("Emekli olmaniz icin "+str(60-yas)+" yil daha calismalisiniz")
elif cinsiyet=="erkek" or cinsiyet=="e" and yas>=65:
    print("Emekli olabilirsiniz")
elif cinsiyet=="erkek" or cinsiyet=="k" and yas<65:
    print("Emekli olmaniz icin "+str(65-yas)+" yil daha calismalisiniz")
else:
    print("Girdiginiz degerler yanlistir ")