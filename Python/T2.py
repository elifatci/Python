print("---- NOT - HARF DÖNÜŞÜM UYGULAMASI ----")
girilenNot= int(input("Notunuzu tamsayı olarak giriniz: "))

if girilenNot>=85 and girilenNot<100:
    harf_notu="AA"
elif girilenNot>=80 and girilenNot<85:
    harf_notu="BA"
elif girilenNot>=75 and girilenNot<80:
    harf_notu="BB"
elif girilenNot>=65 and girilenNot<75:
    harf_notu="CB"
elif girilenNot>=50 and girilenNot<65:
    harf_notu="CC"
else:
    harf_notu="FF"
print(f"Girdiğiniz notun Karşılığı olan harf notu: :{harf_notu}")