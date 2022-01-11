import random

YATAY_CIZGI_ALT_LIMIT = 3
YATAY_CIZGI_UST_LIMIT = 7

KONUM_BOS = " "
KONUM_BEYAZ = "B"
KONUM_SIYAH = "S"


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
    #s        harita[yy][dd] = random.choice(["B", "S"])
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
        liste = [KONUM_BOS] * dikey_cizgi
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
                print("Hatalı giriş, lütfen tekrar giriniz: ", end=" ")
        except ValueError:
            print("Hatalı giriş, lütfen tekrar giriniz: ", end=" ")
    return sayi


def Tas_Yerlestirme(harf_listesi, harita):
    toplam_alan = len(harita) * len(harita[0])
    tas_sayisi = 0
    while tas_sayisi < toplam_alan:
        beyaz = input("Beyaz oyuncu haritaya taş yerleştirmek için konum girsin: ")

        beyaz = Konum_Bosmu(beyaz, harita, harf_listesi)

        harita [int(beyaz[0]) - 1] [Harfi_Sayiya_Cevir(beyaz[1], harf_listesi)] = KONUM_BEYAZ
        tas_sayisi += 1
        Haritayi_Yazdir(harita, harf_listesi)

        siyah = input("Siyah oyuncu haritaya taş yerleştirmek için konum girsin: ")

        siyah = Konum_Bosmu(siyah, harita, harf_listesi)

        harita [int(siyah[0]) - 1] [Harfi_Sayiya_Cevir(siyah[1], harf_listesi)] = KONUM_SIYAH
        tas_sayisi += 1
        Haritayi_Yazdir(harita, harf_listesi)
    else:
        print("Tüm alan doldu ve taş yerleştirme bitti.")
        Haritayi_Yazdir(harita, harf_listesi)


def Konum_Bosmu(konum, harita, harf_listesi):
    konum = Konum_Haritada_Varmi(konum, harf_listesi, harita)

    konum0 = int(konum[0])
    konum1 = Harfi_Sayiya_Cevir(konum[1], harf_listesi)

    while harita[konum0 - 1][konum1] != KONUM_BOS:
        konum = input("Girdiğiniz konum dolu. Başka konum giriniz: ")
        konum = Konum_Haritada_Varmi(konum, harf_listesi, harita)
        konum0 = int(konum[0])
        konum1 = Harfi_Sayiya_Cevir(konum[1], harf_listesi)

    else:
        return konum




def Konum_Haritada_Varmi(konum, harf_listesi, harita):
    konum_haritada_varmi = False
    while konum_haritada_varmi == False:

        konum = konum.upper()

        if len(konum) == 2 and konum[1] in harf_listesi and konum[0].isdigit() and int(konum[0]) in range(1, len(harita)+1): #Konum haritada var
            konum_haritada_varmi = True
        else:
            konum = input("Hatalı konum girdiniz. Tekrar konumu giriniz: ")
    return konum



def Harfi_Sayiya_Cevir(harf, harf_listesi):
    indeks = harf_listesi.index(harf)
    return int(indeks)


def Tas_Eleme(harita,beyaz_kare_listesi,siyah_kare_listesi, harf_listesi):
    yatay_cizgi = len(harita)
    dikey_cizgi = len(harita[0])

    for yy in range(yatay_cizgi-1):
        for dd in range(dikey_cizgi-1):
            pos1 = harita[yy][dd]
            pos2 = harita[yy+1][dd]
            pos3 = harita[yy+1][dd+1]
            pos4 = harita[yy][dd+1]

            kare = pos1 + pos2 + pos3 + pos4

            if kare == "BBBB":
                print(kare)
                beyaz_kare_listesi.append([ [yy, dd], [yy+1, dd], [yy+1, dd+1], [yy, dd+1] ])
            elif kare == "SSSS":
                print(kare)
                siyah_kare_listesi.append([ [yy, dd], [yy+1, dd], [yy+1, dd+1], [yy, dd+1] ])

    print(f"beyaz kare sayısı: {len(beyaz_kare_listesi)} {beyaz_kare_listesi}")
    print(f"siyah kare sayısı: {len(siyah_kare_listesi)} {siyah_kare_listesi}")

    for i in range(len(beyaz_kare_listesi)):
        silinecek_kare = input("Beyaz oyuncu haritadan taş silmek için konum girsin: ")
        silinecek_kare = Konum_Haritada_Varmi(silinecek_kare, harf_listesi, harita)


def main():
    harf_listesi = ["A", "B", "C", "D", "E", "F", "G", "H"]
    beyaz_kare_listesi = []
    siyah_kare_listesi = []
    harita = Haritayi_Olustur(harf_listesi)
    print(harita)
    Haritayi_Yazdir(harita, harf_listesi)
    Tas_Yerlestirme(harf_listesi, harita)
    Tas_Eleme(harita, beyaz_kare_listesi, siyah_kare_listesi, harf_listesi)









main()