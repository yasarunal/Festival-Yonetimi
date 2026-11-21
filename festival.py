class Festival:
    def __init__(self,festivalid,ad,yil,etkinlikler,katilimcilar):
        self.festivalid = festivalid
        self.ad = ad
        self.yil = yil
        self.etkinlikler = []
        self.katilimcilar = []

    def Etkinlik_ekle(self,etkinlik):
        self.etkinlikler.append(etkinlik)
        print(f"{etkinlik.ad} etkinliği festivale eklendi.")

    def Katilimci_ekle(self,katilimci):
            self.katilimcilar.append(katilimci)
            print(f"{katilimci.ad} {katilimci.soyad} festivale katıldı.")

    def ozet(self):
            print(f"\n--- FESTİVAL ÖZETİ ---")
            print(f"Festival: {self.ad} ({self.yil})")
            print(f"Toplam Etkinlik: {len(self.etkinlikler)}")
            print(f"Toplam Katılımcı: {len(self.katilimcilar)}")

            print("\nEtkinlikler:")
            for e in self.etkinlikler:
                print(f"- {e.ad} ({e.tur}) {e.tarih} {e.saat}")

            print("\nKatılımcılar:")
            for k in self.katilimcilar:
                print(f"- {k.ad} {k.soyad} ({k.biletTipi})")

class Etkinlik:
    
    def __init__(self,etkinlikid,ad,tarih,saat,tur,sanatci):
        self.etkinlikid = etkinlikid
        self.ad = ad
        self.tarih = tarih
        self.saat = saat
        self.tur = tur
        self.sanatci = sanatci

    def etkinlikBilgi(self):

        print(f"Etkinlik: {self.ad} - Tür: {self.tur} - Tarih: {self.tarih} {self.saat}")
        if self.sanatci:
            print(f"Sanatçı: {self.sanatci.ad}")

class Kisi:
    def __init__(self,id,ad,soyad,email):
        self.id = id
        self.ad = ad
        self.soyad = soyad 
        self.email = email

    def bilgiGoster(self):
        return print(f'İsim : {self.ad} , Soyisim : {self.soyad} , Email : {self.email} , İd : {self.id}')        
    
class Katilimci(Kisi):
    def __init__(self, id, ad, soyad, email, yas, biletTipi):
        super().__init__(id, ad, soyad, email)
        self.yas = yas
        self.biletTipi = biletTipi


    def kayitOl(self):
        print(f"{self.ad} {self.soyad} festivale kaydoldu.")

    def biletGoster(self):
        return print(f"Bilet Bilgisi : {self.biletTipi}")    
    

class Sanatci(Kisi):
    def __init__(self,id,ad,soyad,email,tur,saat):
        super().__init__(id, ad, soyad, email)    
        self.tur = tur
        self.saat = saat

    def performansYap(self):
        print(f"{self.ad} {self.soyad} sahne alıyor! Tür {self.tur} , Saat {self.saat} ")

class Personel(Kisi):
    def __init__(self, id, ad, soyad, email,departman):
        super().__init__(id, ad, soyad, email)        
        self.departman = departman

    def gorev(self):
        print(f"{self.ad} {self.soyad} görevde → Departman: {self.departman}")    

class Mekan:
    def __init__(self,mekanid,ad,kapasite):
        self.mekanid = mekanid
        self.ad = ad
        self.kapasite = kapasite

    def mekanBilgi(self):
        return print(f"Mekan İD : {self.mekanid} , Mekan İsmi : {self.ad} , Kapasitesi : {self.kapasite}")
    

class Guvenlik(Personel):
    def __init__(self, id, ad, soyad, email, departman,alan):
        super().__init__(id, ad, soyad, email, departman)  
        self.alan = alan

    def devriye(self):
        print(f"{self.ad} {self.soyad} güvenlik devriyesinde → Alan: {self.alan}")

class Sahne:
    def __init__(self,sahneid,ad,sahneTuru):
        self.sahneid = sahneid
        self.ad = ad
        self.sahneTuru = sahneTuru

    def sahneBilgi(self):
        return print(f"Sahne ID : {self.sahneid} , Sahne Adı : {self.ad} , Sahne Türü : {self.sahneTuru}")

# Sanatçı oluştur
s1 = Sanatci(1, "Ahmet", "Yılmaz", "ahmet@mail.com", "Rock", "20:00")

# Etkinlik oluştur
e1 = Etkinlik(101, "Rock Konseri", "2025-07-15", "20:00", "Konser", sanatci=s1)

# Katılımcı oluştur
k1 = Katilimci(201, "Ayşe", "Demir", "ayse@mail.com", 25, "VIP")

# Festival oluştur (5 parametre girilmeli!)
f1 = Festival(1, "Malatya Festivali", 2025, [], [])

# Etkinlik ekle
f1.Etkinlik_ekle(e1)

# Katılımcı ekle
f1.Katilimci_ekle(k1)

# Özet
f1.ozet()

# Detaylı bilgiler
e1.etkinlikBilgi()
k1.biletGoster()
s1.performansYap()
