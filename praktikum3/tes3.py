cuaca = "mendung"

if cuaca == "menudng":
    print("diam di rumah")
else:
    print("hari ini mendung")

umur = int(input("masukkan umur anda : "))
if umur > 0:
    if umur <= 18:
        print(" umur anda termasuk kategori anak-anak")
    elif umur <= 18:
        print("umur anda termasuk kategori remaja")
    elif umur <=35:
        print("umur anda termasuk kategori dewasa")
    elif umur <=65:
        print("umur anda termasuk kategori paruh baya")
    else:
        print("umur anda termasuk kategori tua")
else:
    print("input usia harus bilangan positif")

nim = int(input("masukkan nim: "))

if nim >= 1 and nim <= 50 :
    if nim >= 1 and nim <= 25 :
        print("kelas A'1")
    else :
        print("kelas A'2")
elif nim >= 51 and nim <= 100:
    if nim >= 51 and nim <= 75 :
        print("kelas B'1")
    else :
        print("kelas B'2")
elif nim >= 101 and nim <= 121 :
    if nim >= 101 and nim <= 110 :
        print("kelas C'1")
    else :
        print("kelas C'2")
else :
    print("anda bukan mahasiswa informatika 24")

nim = int(input("mahasiswa nim: "))
hasil = "kelas A" if nim >= 1 and nim <=50 else "kelas B" if nim >= 51 and nim <=121 else "kelas C" if nim >= "mahasiswa siluman" 
print(hasil)