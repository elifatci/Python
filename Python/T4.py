print("---- Girilen sayinin faktoriyelini hesaplama ----")
girilenSayi= int(input("Lutfen pozitif bir tamsayi giriniz: "))
faktoriyel=1
if girilenSayi==0:
    print("0!=1")
else:
    for i in range(1,girilenSayi+1):
        faktoriyel *= i
print(f"{girilenSayi}!={faktoriyel}")
