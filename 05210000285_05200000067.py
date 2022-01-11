import random

YATAY_CIZGI_ALT_LIMIT = 3
YATAY_CIZGI_UST_LIMIT = 7

def haritayi_Yazdir(harita):
    yatay_cizgi = len(harita)
    dikey_cizgi = len(harita[0])

    for yy in range(yatay_cizgi):
        for dd in range(dikey_cizgi):
            harita[yy][dd] = random.randint(1,10)

    print(harita)

    for satir in range(2 * yatay_cizgi - 1):
        print()
        if satir % 2 == 0:
            for i in range(yatay_cizgi):
                print(f"{harita[satir//2][i]}", end="")
                print("---", end="")
            print(f"{harita[satir//2][yatay_cizgi]}", end = "")
        else:
            for a in range(dikey_cizgi):
                print("|", end="")
                print("   ", end = "")





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
    harita = haritayi_Olustur()
    print(harita)
    haritayi_Yazdir(harita)







main()