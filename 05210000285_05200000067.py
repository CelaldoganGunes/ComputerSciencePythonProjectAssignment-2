
# Sabitler
YATAY_CIZGI_ALT_LIMIT = 3
YATAY_CIZGI_UST_LIMIT = 7

KONUM_BOS = " "
KONUM_BEYAZ = "B"
KONUM_SIYAH = "S"

def f_tabloya_harfleri_yazdir(harf_listesi):
    print("    ", end="")
    for harf in harf_listesi[:len(harf_listesi) - 1]:
        print(f"{harf}     ", end="")
    else:
        print(f"{harf_listesi[-1]}")


def f_haritayi_yazdir(harita, harf_listesi):
    yatay_cizgi = len(harita)
    dikey_cizgi = len(harita[0])

    f_tabloya_harfleri_yazdir(harf_listesi)

    for i in range(yatay_cizgi-1):

        print(f"{i + 1}   ", end="")

        for indeks in range(dikey_cizgi - 1):
            print(f"{harita[i][indeks]} --- ", end="")
        else:
            print(f"{harita[i][dikey_cizgi -1]}   {i + 1}")

        # çizgileri yazdıracaz buraya
        print("    ", end="")
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
    f_tabloya_harfleri_yazdir(harf_listesi)


def f_haritayi_olustur(harf_listesi):
    print("Yatay çizgi sırasını girin:", end=" ")
    yatay_cizgi = f_aralik_kontrolu(YATAY_CIZGI_ALT_LIMIT, YATAY_CIZGI_UST_LIMIT)
    dikey_cizgi = yatay_cizgi + 1
    harf_listesi[:] = harf_listesi[:dikey_cizgi]

    harita = []

    for i in range(yatay_cizgi):
        liste = [KONUM_BOS] * dikey_cizgi
        harita.append(liste)

    return harita


def f_aralik_kontrolu(alt_sinir, ust_sinir):
    donguyu_bitir = False
    sayi = 0
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


def f_tas_yerlestirme(harf_listesi, harita):
    toplam_alan = len(harita) * len(harita[0])
    tas_sayisi = 0
    while tas_sayisi < toplam_alan:

        # Beyazın sırası

        beyaz = input("Beyaz oyuncu haritaya taş yerleştirmek için konum girsin: ")

        beyaz = f_konum_bosmu(beyaz, harita, harf_listesi)

        harita[int(beyaz[0]) - 1][f_harfi_sayiya_cevir(beyaz[1], harf_listesi)] = KONUM_BEYAZ
        tas_sayisi += 1
        f_haritayi_yazdir(harita, harf_listesi)

        # Siyahın sırası

        siyah = input("Siyah oyuncu haritaya taş yerleştirmek için konum girsin: ")

        siyah = f_konum_bosmu(siyah, harita, harf_listesi)

        harita[int(siyah[0]) - 1][f_harfi_sayiya_cevir(siyah[1], harf_listesi)] = KONUM_SIYAH
        tas_sayisi += 1
        f_haritayi_yazdir(harita, harf_listesi)
    else:
        print("Tüm alan doldu ve taş yerleştirme bitti.")
        f_haritayi_yazdir(harita, harf_listesi)


def f_konum_bosmu(konum, harita, harf_listesi):  # 1C 2C gibi harfli konum giriliyor
    konum = f_konum_haritada_varmi(konum, harf_listesi, harita, 1)
    konum0, konum1 = f_metni_sayi_konumuna_cevir(konum, harf_listesi)

    while harita[konum0 - 1][konum1] != KONUM_BOS:
        konum = input("Girdiğiniz konum dolu. Başka konum giriniz: ")
        konum = f_konum_haritada_varmi(konum, harf_listesi, harita, 1)
        konum0, konum1 = f_metni_sayi_konumuna_cevir(konum, harf_listesi)

    else:
        return konum


def f_konum_haritada_varmi(konum, harf_listesi, harita, konum_miktari):  # 1C 2C gibi harfli konum giriliyor
    konum_haritada_varmi = False
    while konum_haritada_varmi == False:
        konum = konum.upper()
        if konum_miktari == 1:
            if len(konum) == 2 and konum[1] in harf_listesi and konum[0].isdigit() \
                    and int(konum[0]) in range(1, len(harita) + 1):  # Konum haritada var
                konum_haritada_varmi = True
            else:
                konum = input("Hatalı konum girdiniz. Tekrar konumu giriniz: ")
        elif konum_miktari == 2:
            if len(konum) == 5 and konum.count(" ") == 1 and konum.index(" ") == 2:
                duble_konum_metni = konum.split(" ")
                secilen_kare = duble_konum_metni[0]
                hedef_kare = duble_konum_metni[1]

                if len(secilen_kare) == 2 and secilen_kare[1] in harf_listesi and secilen_kare[0].isdigit() \
                        and int(secilen_kare[0]) in range(1, len(harita) + 1):  # Konum haritada var
                    if len(hedef_kare) == 2 and hedef_kare[1] in harf_listesi and hedef_kare[0].isdigit() \
                            and int(hedef_kare[0]) in range(1, len(harita) + 1):  # Konum haritada var
                        return secilen_kare, hedef_kare
            if konum_haritada_varmi == False:
                konum = input("Hatalı konum girdiniz. Tekrar konumu giriniz: ")
    return konum


def f_metni_sayi_konumuna_cevir(konum, harf_listesi):  # 1C 2C gibi harfli konum giriliyor
    konum0 = int(konum[0])
    konum1 = f_harfi_sayiya_cevir(konum[1], harf_listesi)
    return konum0, konum1


def f_harfi_sayiya_cevir(harf, harf_listesi):
    indeks = harf_listesi.index(harf)
    return int(indeks)


def f_tas_eleme(harita, beyaz_kare_listesi, siyah_kare_listesi, harf_listesi):
    f_kareleri_hesaplama(harita, beyaz_kare_listesi, siyah_kare_listesi)

    if len(beyaz_kare_listesi) + len(siyah_kare_listesi) > 0:
        f_tas_sil(beyaz_kare_listesi, siyah_kare_listesi, harf_listesi, harita, "Beyaz", "Siyah")
        f_tas_sil(siyah_kare_listesi, beyaz_kare_listesi, harf_listesi, harita, "Siyah", "Beyaz")
    else:  # Hiç kare oluşmadıysa beyaz oyuncu 1 taş silecek
        tas_sil = True
        while tas_sil == True:
            silinecek_kare = input(f"Beyaz oyuncu haritadan taş silmek için konum girsin: ")
            silinecek_kare = f_konum_haritada_varmi(silinecek_kare, harf_listesi, harita, 1)

            yy, dd = f_metni_sayi_konumuna_cevir(silinecek_kare, harf_listesi)

            if harita[yy - 1][dd] != "S":
                print(f"Girdiğiniz konumda silinebilecek uygun S taş yok.")
            else:
                harita[yy - 1][dd] = " "
                f_haritayi_yazdir(harita, harf_listesi)
                tas_sil = False


def f_tas_sil(kare_listesi, rakip_kare_listesi, harf_listesi, harita, oyuncu_rengi, rakip):
    for i in range(len(kare_listesi)):
        silinecek_kare = input(f"{oyuncu_rengi} oyuncu haritadan taş silmek için konum girsin: ")
        silinecek_kare = f_konum_haritada_varmi(silinecek_kare, harf_listesi, harita, 1)

        yy, dd = f_metni_sayi_konumuna_cevir(silinecek_kare, harf_listesi)

        control = True
        while control == True:
            if harita[yy - 1][dd] != rakip[0]:
                print(f"Girdiğiniz konumda silinebilecek uygun {rakip[0]} taş yok.")
                silinecek_kare = input(f"{oyuncu_rengi} oyuncu haritadan taş silmek için konum girsin: ")
                silinecek_kare = f_konum_haritada_varmi(silinecek_kare, harf_listesi, harita, 1)
                yy, dd = f_metni_sayi_konumuna_cevir(silinecek_kare, harf_listesi)
            elif f_konum_kare_icindemi(rakip_kare_listesi, yy - 1, dd) == True:
                print(f"Girdiğiniz konumdaki taş, bir karenin üyesi olduğundan silinemez.")
                silinecek_kare = input(f"{oyuncu_rengi} oyuncu haritadan taş silmek için konum girsin: ")
                silinecek_kare = f_konum_haritada_varmi(silinecek_kare, harf_listesi, harita, 1)
                yy, dd = f_metni_sayi_konumuna_cevir(silinecek_kare, harf_listesi)
            else:
                harita[yy - 1][dd] = " "
                f_haritayi_yazdir(harita, harf_listesi)
                control = False


def f_hareket_etme(oyuncu, harita, harf_listesi):
    duble_konum_metni = input(f"{oyuncu} oyuncu hareket ettirmek için "
                              f"taş seçsin ve hedef konumu girsin [xx xx]: ")  # 2c 3d

    dongu_kontrol = True
    ilk_son_konum_liste = [0] * 4
    while dongu_kontrol == True:
        secilen_kare, hedef_kare = f_konum_haritada_varmi(duble_konum_metni, harf_listesi, harita, 2)
        ilk_son_konum_liste[0], ilk_son_konum_liste[1] = f_metni_sayi_konumuna_cevir(secilen_kare, harf_listesi)
        ilk_son_konum_liste[2], ilk_son_konum_liste[3] = f_metni_sayi_konumuna_cevir(hedef_kare, harf_listesi)

        ilk_son_konum_liste[0] -= 1
        ilk_son_konum_liste[2] -= 1

        # Girilen ilk konum oyuncunun kendi taşı mı?
        if harita[ilk_son_konum_liste[0]][ilk_son_konum_liste[1]] != oyuncu[0]:
            print("Girdiğiniz konumda kendi taşınız. yok")
            duble_konum_metni = input(f"{oyuncu} oyuncu hareket ettirmek için taş seçsin ve hedef konumu girsin [xx xx]: ")
            continue

        # Girilen hedef konum boş mu?
        if harita[ilk_son_konum_liste[2]][ilk_son_konum_liste[3]] != KONUM_BOS:
            print("Girdiğiniz hedef konum boş değil.")
            duble_konum_metni = input(f"{oyuncu} oyuncu hareket ettirmek için taş seçsin ve hedef konumu girsin [xx xx]: ")
            continue

        # Girilen konumların hizaları aynı mı?
        if ilk_son_konum_liste[0] == ilk_son_konum_liste[2]:
            print("Yataya kontrol", ilk_son_konum_liste[0], ilk_son_konum_liste[2])
            iki_nokta_arasi_bosluk = f_iki_nokta_arasi_bosmu(ilk_son_konum_liste[0], ilk_son_konum_liste[1], ilk_son_konum_liste[2], ilk_son_konum_liste[3], "yatay", harita)

        elif ilk_son_konum_liste[1] == ilk_son_konum_liste[3]:
            print("Dikeye kontrol", ilk_son_konum_liste[1], ilk_son_konum_liste[3])
            iki_nokta_arasi_bosluk = f_iki_nokta_arasi_bosmu(ilk_son_konum_liste[0], ilk_son_konum_liste[1], ilk_son_konum_liste[2], ilk_son_konum_liste[3], "dikey", harita)

        else:
            print("Girdiğiniz taşlar aynı hizada değil.")
            duble_konum_metni = input(f"{oyuncu} oyuncu hareket ettirmek için taş seçsin ve hedef konumu girsin [xx xx]: ")
            continue

        #Girilen konumlar arası boş mu?
        if iki_nokta_arasi_bosluk == False:
            print("Girdiğiniz konumlar arasında başka taş var.")
            duble_konum_metni = input(f"{oyuncu} oyuncu hareket ettirmek için TEKRAR taş seçsin ve hedef konumu girsin [xx xx]: ")
            continue

        dongu_kontrol = False

    #Konumu güncelle
    harita[ilk_son_konum_liste[2]][ilk_son_konum_liste[3]] = harita[ilk_son_konum_liste[0]][ilk_son_konum_liste[1]]
    harita[ilk_son_konum_liste[0]][ilk_son_konum_liste[1]] = KONUM_BOS
    f_haritayi_yazdir(harita, harf_listesi)


def f_iki_nokta_arasi_bosmu(y1, d1, y2, d2, dikey_yatay, harita):
    if dikey_yatay == "dikey":
        for yy in range(min(y1, y2) + 1, max(y1, y2) + 1):
            if yy != y1 and harita[yy][d1] != KONUM_BOS:  # Kendi konumu değilse ve konum boş değilse false gönder
                return False
    elif dikey_yatay == "yatay":
        for dd in range(min(d1, d2) + 1, max(d1, d2) + 1):
            if dd != d1 and harita[y1][dd] != KONUM_BOS:  # Kendi konumu değilse ve konum boş değilse false gönder
                return False
    return True


def f_kareleri_hesaplama(harita, beyaz_kare_listesi, siyah_kare_listesi):
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
                beyaz_kare_listesi.append([[yy, dd], [yy+1, dd], [yy+1, dd+1], [yy, dd+1]])
            elif kare == "SSSS":
                siyah_kare_listesi.append([[yy, dd], [yy+1, dd], [yy+1, dd+1], [yy, dd+1]])


def f_yeni_kare_olustumu(yeni_liste, eski_liste):
    yeni_kare = False
    for kare in yeni_liste:
        if kare not in eski_liste:
            yeni_kare = True
            break
    eski_liste[:] = yeni_liste
    return yeni_kare


def f_oyunun_govdesi(harita, beyaz_kare_listesi, siyah_kare_listesi, harf_listesi):
    beyaz_tas_sayisi = 0
    siyah_tas_sayisi = 0
    kazanan = ""

    for yy in range(len(harita)):
        for dd in range(len(harita[0])):
            if harita[yy][dd] == "S":
                siyah_tas_sayisi += 1
            elif harita[yy][dd] == "B":
                beyaz_tas_sayisi += 1

    while siyah_tas_sayisi > 3 and beyaz_tas_sayisi > 3:

        # Beyazın Sırası
        yeni_beyaz_kare_listesi = []
        yeni_siyah_kare_listesi = []

        f_hareket_etme("Beyaz", harita, harf_listesi)
        f_kareleri_hesaplama(harita, yeni_beyaz_kare_listesi, yeni_siyah_kare_listesi)

        if f_yeni_kare_olustumu(yeni_beyaz_kare_listesi, beyaz_kare_listesi) == True:
            f_tas_sil([1], siyah_kare_listesi, harf_listesi, harita, "Beyaz", "Siyah")
            siyah_tas_sayisi -= 1
            if siyah_tas_sayisi < 4:
                kazanan = "Beyaz"
                break

        # Siyahın Sırası
        yeni_beyaz_kare_listesi = []
        yeni_siyah_kare_listesi = []

        f_hareket_etme("Siyah", harita, harf_listesi)
        f_kareleri_hesaplama(harita, yeni_beyaz_kare_listesi, yeni_siyah_kare_listesi)

        if f_yeni_kare_olustumu(yeni_siyah_kare_listesi, siyah_kare_listesi) == True:
            f_tas_sil([1], beyaz_kare_listesi, harf_listesi, harita, "Siyah", "Beyaz")
            beyaz_tas_sayisi -= 1
            if beyaz_tas_sayisi < 4:
                kazanan = "Siyah"
                break

    print("")
    print("")
    print("")
    print(f"Oyun Bitti!")
    print(f"Kazanan Oyuncu: {kazanan}")
    print("")
    print("")
    f_haritayi_yazdir(harita, harf_listesi)


def f_konum_kare_icindemi(kare_listesi, yy, dd):
    for kare in kare_listesi:
        if [yy, dd] in kare:
            return True
    else:
        return False


def main():
    harf_listesi = ["A", "B", "C", "D", "E", "F", "G", "H"]
    beyaz_kare_listesi = []
    siyah_kare_listesi = []
    harita = f_haritayi_olustur(harf_listesi)
    f_haritayi_yazdir(harita, harf_listesi)
    f_tas_yerlestirme(harf_listesi, harita)
    f_tas_eleme(harita, beyaz_kare_listesi, siyah_kare_listesi, harf_listesi)
    f_oyunun_govdesi(harita, beyaz_kare_listesi, siyah_kare_listesi, harf_listesi)

main()