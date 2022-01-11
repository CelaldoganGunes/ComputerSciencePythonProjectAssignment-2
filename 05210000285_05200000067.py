import random

YATAY_CIZGI_ALT_LIMIT = 3
YATAY_CIZGI_UST_LIMIT = 7


def Tabloya_Harfleri_Yazdir(harf_listesi):
    print("    ", end="")
    for harf in harf_listesi[:len(harf_listesi) - 1]:
        print(f"{harf}     ", end="")
    else:
        print(f"{harf_listesi[-1]}")


def Haritayi_Yazdir(harita, harf_listesi):
    yatay_cizgi = len(harita)
    dikey_cizgi = len(harita[0])

    #for yy in range(yatay_cizgi):
    #    for dd in range(dikey_cizgi):
    #        harita[yy][dd] = random.randint(1,9)

    print(harita)

    Tabloya_Harfleri_Yazdir(harf_listesi)

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
    Tabloya_Harfleri_Yazdir(harf_listesi)



def Haritayi_Olustur(harf_listesi):
    print("Yatay çizgi sırasını girin:", end=" ")
    yatay_cizgi = Aralik_Kontrolu(YATAY_CIZGI_ALT_LIMIT, YATAY_CIZGI_UST_LIMIT)
    dikey_cizgi = yatay_cizgi + 1
    harf_listesi[:] = harf_listesi[:dikey_cizgi]
    print(harf_listesi)

    harita = []

    for i in range(yatay_cizgi):
        liste = [0] * dikey_cizgi
        harita.append(liste)

    return harita




def Aralik_Kontrolu(alt_sinir, ust_sinir):
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
    harita = Haritayi_Olustur(harf_listesi)
    print(harita)
    Haritayi_Yazdir(harita, harf_listesi)








main()