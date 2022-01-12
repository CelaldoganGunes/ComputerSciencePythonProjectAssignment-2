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

    yatay_cizgi = len(harita)
    dikey_cizgi = len(harita[0])

    for yy in range(yatay_cizgi):
        for dd in range(dikey_cizgi):
            harita[yy][dd] = random.choice(["B", "S"])

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


def Konum_Bosmu(konum, harita, harf_listesi): #1C 2C gibi harfli konum giriliyor
    konum = Konum_Haritada_Varmi(konum, harf_listesi, harita, 1)

    konum0, konum1 = Metni_Sayi_Konumuna_Cevir(konum, harf_listesi)


    while harita[konum0 - 1][konum1] != KONUM_BOS:
        konum = input("Girdiğiniz konum dolu. Başka konum giriniz: ")
        konum = Konum_Haritada_Varmi(konum, harf_listesi, harita,1)
        konum0, konum1 = Metni_Sayi_Konumuna_Cevir(konum, harf_listesi)

    else:
        return konum


def Konum_Haritada_Varmi(konum, harf_listesi, harita, konum_miktari): #1C 2C gibi harfli konum giriliyor
    konum_haritada_varmi = False
    while konum_haritada_varmi == False:
        konum = konum.upper()
        if konum_miktari == 1:
            if len(konum) == 2 and konum[1] in harf_listesi and konum[0].isdigit() and int(konum[0]) in range(1,len(harita) + 1):  # Konum haritada var
                konum_haritada_varmi = True
            else:
                konum = input("Hatalı konum girdiniz. Tekrar konumu giriniz: ")
        elif konum_miktari == 2:
            if len(konum) == 5 and konum.count(" ") == 1 and konum.index(" ") == 2:
                duble_konum_metni = konum.split(" ")
                secilen_kare = duble_konum_metni[0]
                hedef_kare = duble_konum_metni[1]

                if len(secilen_kare) == 2 and secilen_kare[1] in harf_listesi and secilen_kare[0].isdigit() and int(secilen_kare[0]) in range(1, len(harita) + 1):  # Konum haritada var
                    if len(hedef_kare) == 2 and hedef_kare[1] in harf_listesi and hedef_kare[0].isdigit() and int(hedef_kare[0]) in range(1, len(harita) + 1):  # Konum haritada var
                        return secilen_kare, hedef_kare
            if konum_haritada_varmi == False:
                konum = input("Hatalı konum girdiniz. Tekrar konumu giriniz: ")
    return konum


def Metni_Sayi_Konumuna_Cevir(konum, harf_listesi): #1C 2C gibi harfli konum giriliyor
    konum0 = int(konum[0])
    konum1 = Harfi_Sayiya_Cevir(konum[1], harf_listesi)
    return konum0, konum1


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

    if len(beyaz_kare_listesi) + len(siyah_kare_listesi) > 0:
        Tas_Sil(beyaz_kare_listesi, siyah_kare_listesi, harf_listesi, harita, "Beyaz", "Siyah")
        Tas_Sil(siyah_kare_listesi, beyaz_kare_listesi, harf_listesi, harita, "Siyah", "Beyaz")
    else:
        tas_sil = True
        while tas_sil == True:
            silinecek_kare = input(f"Beyaz oyuncu haritadan taş silmek için konum girsin: ")
            silinecek_kare = Konum_Haritada_Varmi(silinecek_kare, harf_listesi, harita,1)

            yy, dd = Metni_Sayi_Konumuna_Cevir(silinecek_kare, harf_listesi)

            if harita[yy - 1][dd] != "S":
                print(f"Girdiğiniz konumda silinebilecek uygun S taş yok.")
            else:
                harita[yy - 1][dd] = " "
                Haritayi_Yazdir(harita, harf_listesi)
                tas_sil = False


def Tas_Sil(kare_listesi, rakip_kare_listesi, harf_listesi, harita, oyuncu_rengi, rakip):
    for i in range(len(kare_listesi)):
        silinecek_kare = input(f"{oyuncu_rengi} oyuncu haritadan taş silmek için konum girsin: ")
        silinecek_kare = Konum_Haritada_Varmi(silinecek_kare, harf_listesi, harita, 1)

        yy, dd = Metni_Sayi_Konumuna_Cevir(silinecek_kare, harf_listesi)

        control = True
        while control == True:
            if harita[yy - 1][dd] != rakip[0]:
                print(f"Girdiğiniz konumda silinebilecek uygun {rakip[0]} taş yok.")
                silinecek_kare = input(f"{oyuncu_rengi} oyuncu haritadan taş silmek için konum girsin: ")
                silinecek_kare = Konum_Haritada_Varmi(silinecek_kare, harf_listesi, harita, 1)
                yy, dd = Metni_Sayi_Konumuna_Cevir(silinecek_kare, harf_listesi)
            elif Konum_Kare_Icindemi(rakip_kare_listesi, yy - 1, dd) == True:
                print(f"Girdiğiniz konumdaki taş, bir karenin üyesi olduğundan silinemez.")
                silinecek_kare = input(f"{oyuncu_rengi} oyuncu haritadan taş silmek için konum girsin: ")
                silinecek_kare = Konum_Haritada_Varmi(silinecek_kare, harf_listesi, harita, 1)
                yy, dd = Metni_Sayi_Konumuna_Cevir(silinecek_kare, harf_listesi)
            else:
                harita[yy - 1][dd] = " "
                Haritayi_Yazdir(harita, harf_listesi)
                control = False




def Hareket_Etme(oyuncu, harita, beyaz_kare_listesi, siyah_kare_listesi,harf_listesi):
    duble_konum_metni = input(f"{oyuncu} oyuncu hareket ettirmek için taş seçsin ve hedef konumu girsin [xx xx]: ") #2c 3d

    dongu_kontrol = True
    Bas_Son_Liste = [0] * 4
    while dongu_kontrol == True:
        secilen_kare, hedef_kare = Konum_Haritada_Varmi(duble_konum_metni, harf_listesi, harita, 2)
        Bas_Son_Liste[0], Bas_Son_Liste[1] = Metni_Sayi_Konumuna_Cevir(secilen_kare,harf_listesi)
        Bas_Son_Liste[2], Bas_Son_Liste[3] = Metni_Sayi_Konumuna_Cevir(hedef_kare,harf_listesi)

        Bas_Son_Liste[0] -= 1
        Bas_Son_Liste[2] -= 1
        if harita[Bas_Son_Liste[0]] [Bas_Son_Liste[1]] != oyuncu[0]:
            duble_konum_metni = input(f"{oyuncu} oyuncu hareket ettirmek için TEKRAR taş seçsin ve hedef konumu girsin [xx xx]: ")
            continue

        if harita[Bas_Son_Liste[2]] [Bas_Son_Liste[3]] != KONUM_BOS:
            duble_konum_metni = input(f"{oyuncu} oyuncu hareket ettirmek için TEKRAR taş seçsin ve hedef konumu girsin [xx xx]: ")
            continue

        if Bas_Son_Liste[0] == Bas_Son_Liste[2]:
            Iki_Nokta_Arasi_Bosmu(Bas_Son_Liste[0],Bas_Son_Liste[1],Bas_Son_Liste[2],Bas_Son_Liste[3], "yatay", harita)
        elif Bas_Son_Liste[1] == Bas_Son_Liste[3]:
            Iki_Nokta_Arasi_Bosmu(Bas_Son_Liste[0],Bas_Son_Liste[1],Bas_Son_Liste[2],Bas_Son_Liste[3], "dikey", harita)
        else:
            duble_konum_metni = input(f"{oyuncu} oyuncu hareket ettirmek için TEKRAR taş seçsin ve hedef konumu girsin [xx xx]: ")
            continue

def Iki_Nokta_Arasi_Bosmu(y1,d1,y2,d2, dikey_yatay, harita):
    if dikey_yatay == "dikey":
        for yy in range(min(y1,y2) + 1, max(y1,y2) + 1):
            if harita[yy][d1] != KONUM_BOS:
                return False
    elif dikey_yatay == "yatay":
        for dd in range(min(d1,d2) + 1, max(d1,d2) + 1):
            if harita[y1][dd] != KONUM_BOS:
                return False
    return True

def Oyunun_Govdesi(harita, beyaz_kare_listesi, siyah_kare_listesi):
    beyaz_tas_sayisi = 0
    siyah_tas_sayisi = 0

    for yy in range(len(harita)):
        for dd in range(len(harita[0])):
            if harita[yy][dd] == "S":
                siyah_tas_sayisi += 1
            elif harita[yy][dd] == "B":
                beyaz_tas_sayisi += 1

    while siyah_tas_sayisi > 3 or beyaz_tas_sayisi > 3:
        Hareket_Etme("Beyaz", harita, beyaz_kare_listesi, siyah_kare_listesi)






def Konum_Kare_Icindemi(kare_listesi, yy, dd):
    for kare in kare_listesi:
        if [yy, dd] in kare:
            return True
    else:
        return False


def main():
    #print(random.seed())
    harf_listesi = ["A", "B", "C", "D", "E", "F", "G", "H"]
    beyaz_kare_listesi = []
    siyah_kare_listesi = []
    harita = Haritayi_Olustur(harf_listesi)
    print(harita)
    Haritayi_Yazdir(harita, harf_listesi)
    #Tas_Yerlestirme(harf_listesi, harita)
    Tas_Eleme(harita, beyaz_kare_listesi, siyah_kare_listesi, harf_listesi)









main()