print("Selamat datang di Absen Otomatis")
print("Masukkan Nomor Mata Kuliah Hari Ini")
print("HARI SENIN")
print("1. SISTEM MULTIMEDIA")
print("HARI SELASA")
print("2. ROUTING & SWITCHING ESSENTIAL")
print("3. MANAJEMEN JARINGAN")
print("HARI RABU")
print("4. INTERAKSI MANUSIA KOMPUTER")
print("5. PEMBELAJARAN MESIN")
print("HARI KAMIS")
print("6. MOBILE COMMERCE")
print("7. KECERDASAN BUATAN")

a=int(input("Masukkan NO Mata Kuliah :"))
if a ==1:
    import Sistem_mult
elif a==2:
    import ROUTING_d_SWITCHING_ESSENTIAL
elif a==3:
    import MANAJEMEN_JARINGAN
elif a==4:
    import imk
elif a==5:
    import Pembelajaran_mesin
elif a==6:
    import Mobile_commerce
elif a==7:
    import ai
else:
    print("Maaf input anda Salah ")