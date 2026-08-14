#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI BAHANE MAKİNESİ v1.0
Resmi, ciddi, bilimsel ve tamamen saçma bir proje.
"""

import random
import time
import sys

def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def baslik():
    print("=" * 60)
    print("   █████╗ ██████╗  █████╗ ██████╗ ████████╗██╗██╗     ██╗")
    print("  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██║     ██║")
    print("  ███████║██████╔╝███████║██████╔╝   ██║   ██║██║     ██║")
    print("  ██╔══██║██╔══██╗██╔══██║██╔══██╗   ██║   ██║██║     ██║")
    print("  ██║  ██║██████╔╝██║  ██║██║  ██║   ██║   ██║███████╗██║")
    print("  ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚═╝")
    print("           B A H A N E   M A K İ N E S İ")
    print("=" * 60)
    print("  Bilimsel olarak kanıtlanmış, etik kurul onaylı,")
    print("  ve hiçbir mahkemede geçerli olmayan bahaneler.")
    print("=" * 60)
    print()

def bahane_uret(durum):
    basliklar = [
        "Kuantum Mekaniği Gerekçesi",
        "Atmosferik Anomali Raporu",
        "Zaman Dalgası Çarpışması",
        "Evrenin Yerel Yasalarının Geçici İhlali",
        "Paralel Evren Sızıntısı",
        "Kozmik Radyasyon Etkisi",
        "Gravitasyonel Dalga Rezonansı",
        "Nötrino Yağmuru Sebebiyle",
    ]
    
    aciklamalar = [
        f"{durum} sırasında yerel uzay-zaman dokusunda beklenmedik bir kırılma meydana gelmiştir. Bu durum, klasik fizik yasalarının geçici olarak askıya alınmasına yol açmıştır.",
        f"Yapılan ölçümler, {durum.lower()} anında Dünya'nın manyetik alanının 0.0003 miligauss sapma gösterdiğini ortaya koymuştur. Bu sapma, insan iradesini doğrudan etkilemektedir.",
        f"Kuantum dolanıklık prensibi gereği, sizin {durum.lower()} eyleminiz aslında 4.7 ışık yılı uzaklıktaki bir yıldızın patlamasıyla eşzamanlı gerçekleşmiştir. Bu bir tesadüf değildir.",
        f"Uluslararası Uzay İstasyonu'ndan gelen son veriler, {durum} esnasında atmosferik basıncın 0.001 milibar düştüğünü göstermektedir. Bu düşüş, tüm planları bozmaya yeterlidir.",
        f"Bilim insanları tarafından henüz tam olarak anlaşılamayan bir 'zaman köpüğü' olayı nedeniyle {durum} gerçekleşememiştir. Bu olayın tekrarlanma olasılığı %0.0000001'dir.",
        f"Sizin {durum.lower()} girişiminiz, evrenin entropi seviyesini tehlikeli bir şekilde artırmış ve sistem otomatik olarak acil durum protokolünü devreye sokmuştur.",
    ]
    
    sonuclar = [
        "Bu nedenle, ilgili eylemin gerçekleştirilmesi bilimsel olarak imkânsız hale gelmiştir.",
        "Dolayısıyla, sorumluluk tamamen kozmik güçlere aittir.",
        "Sonuç olarak, bu durum insan iradesinin ötesinde bir olaydır.",
        "Bu yüzden, herhangi bir kişisel suçlama tamamen yersizdir.",
        "Kısacası, evren buna izin vermemiştir.",
    ]
    
    baslik = random.choice(basliklar)
    aciklama = random.choice(aciklamalar)
    sonuc = random.choice(sonuclar)
    
    rapor = f"""
╔════════════════════════════════════════════════════════════╗
║          RESMİ BAHANE RAPORU - GİZLİ DEĞİL AMA ÖYLE        ║
╠════════════════════════════════════════════════════════════╣
║ Konu          : {durum.upper():<45} ║
║ Rapor Kodu    : BHM-{random.randint(10000,99999)}-{random.randint(100,999)}                           ║
║ Tarih         : {time.strftime('%d.%m.%Y %H:%M')}                              ║
║ Onay Durumu   : OTOMATİK ONAYLANDI (kimse okumadı)         ║
╠════════════════════════════════════════════════════════════╣
║ GEREKÇE BAŞLIĞI: {baslik:<42} ║
╠════════════════════════════════════════════════════════════╣
║ AÇIKLAMA:                                                  ║
║ {aciklama[:58]:<58} ║
║ {aciklama[58:116]:<58} ║
║ {aciklama[116:]:<58} ║
╠════════════════════════════════════════════════════════════╣
║ SONUÇ:                                                     ║
║ {sonuc:<58} ║
╠════════════════════════════════════════════════════════════╣
║ İmza: Bilimsel Bahane Kurulu - Otomatik İmzalama Sistemi   ║
║ Not : Bu belge hiçbir yerde geçerli değildir. Ama havalı.  ║
╚════════════════════════════════════════════════════════════╝
"""
    return rapor

def main():
    baslik()
    yavas_yaz("Hoş geldiniz. Bu makine, hayatınızın en sıradan anlarını bile")
    yavas_yaz("epik bir felakete dönüştürmek için tasarlanmıştır.")
    print()
    
    while True:
        durum = input("Ne için bahane lazım? (örnek: 'işe geç kalmak', 'ödev yapmamak')\n> ").strip()
        if not durum:
            print("Boş giremezsiniz. Evren boşluğu sevmez.")
            continue
        if durum.lower() in ["çık", "exit", "q", "quit"]:
            yavas_yaz("\nMakine kapanıyor... Evren sizi affetsin.")
            break
        
        print("\nHesaplanıyor... Kuantum fluktuasyonları taranıyor...")
        time.sleep(1.5)
        print("Paralel evrenler taranıyor...")
        time.sleep(1)
        print("Bahane formüle ediliyor...")
        time.sleep(1)
        print()
        print(bahane_uret(durum))
        print()
        devam = input("Başka bir bahane? (e/h): ").strip().lower()
        if devam not in ["e", "evet", "y", "yes"]:
            yavas_yaz("\nİyi günler. Bahaneleriniz bol olsun.")
            break

if __name__ == "__main__":
    main()
