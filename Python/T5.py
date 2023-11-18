sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tekSayilar=[]
ciftSayilar=[]
for sayi in sayilar:
    if sayi%2==0:
        ciftSayilar.append(sayi)
    else:
        tekSayilar.append(sayi)



print(ciftSayilar)
print(tekSayilar)