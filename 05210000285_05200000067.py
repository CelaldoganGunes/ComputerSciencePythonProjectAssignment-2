import random

YATAY_CIZGI_ALT_LIMIT = 3
YATAY_CIZGI_UST_LIMIT = 7

def haritayi_Yazdir(harita, harf_listesi):
    yatay_cizgi = len(harita)
    dikey_cizgi = len(harita[0])

    #for yy in range(yatay_cizgi):
    #    for dd in range(dikey_cizgi):
    #        harita[yy][dd] = random.randint(1,9)

    print(harita)



    for i in range(yatay_cizgi-1):

        print(f"{i + 1}   ",end="")

        for indeks in range(dikey_cizgi - 1):
            print(f"{harita[i][indeks]} --- ", end="")
        else:
            print(f"{harita[i][dikey_cizgi -1]}   {i + 1}")

        #çizgileri yazdıracaz buraya
        print("    ",end="")
        for indeks in range(dikey_cizgi - 1):
            print(f"|     ", end="")
        else:
            print(f"|")

    else:
        print(f"{yatay_cizgi}   ", end="")
        for indeks in range(dikey_cizgi - 1):
            print(f"{harita[yatay_cizgi - 1][indeks]} --- ", end="")
        else:
            print(f"{harita[yatay_cizgi - 1][dikey_cizgi -1]}   {yatay_cizgi}")



def haritayi_Olustur():
    print("Yatay çizgi sırasını girin:", end=" ")
    yatay_cizgi = aralik_Kontrolu(YATAY_CIZGI_ALT_LIMIT, YATAY_CIZGI_UST_LIMIT)
    dikey_cizgi = yatay_cizgi + 1

    harita = []

    for i in range(yatay_cizgi):
        liste = [0] * dikey_cizgi
        harita.append(liste)

    return harita




def aralik_Kontrolu(alt_sinir, ust_sinir):
    donguyu_bitir = False
    while donguyu_bitir == False:
        try:
            sayi = int(input(""))
            if alt_sinir <= sayi <= ust_sinir:
                donguyu_bitir = True
            else:
                print("Hatalı giriş, lütfen tekrar giriniz: ",end=" ")
        except ValueError:
            print("Hatalı giriş, lütfen tekrar giriniz: ",end=" ")
    return sayi

def main():
    harf_listesi = ["A", "B", "C", "D", "E", "F", "G", "H"]
    harita = haritayi_Olustur()
    print(harita)
    haritayi_Yazdir(harita, harf_listesi)








main()