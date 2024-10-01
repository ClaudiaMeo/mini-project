print("------------------------------")
print("Nama : Maria Claudia Meo")
print("Kelas: Sistem Informasi-C 2024")
print("Nim  : 2409116108       ")
print("Tugas Mini Project (1) DDP")

# Masukkan Nama & Nim

while True:
    print("Halo Semua, Selamat Datang Di Mini Project DDP")
    username = input("Masukkan Username: ")
    password = input("masukkan password: ")
    if username =="admin" and password =="123":
        print("Anda Berhasil Login")
        break
    else:
        print("Anda Tidak Bisa Login")

# Masukkan Harga Barang Dan Jumlah Barang

while True:
    harga = int(input("Masukkan harga barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))

    total_harga = harga * jumlah

    if harga > 250000:
        diskon = harga * 25/100
        total = harga - diskon
        print("=== Anda berhasil mendapatkan diskon sebesar 25% ===")
    elif harga < 250000:
        total = harga
        print("==== Anda tidak mendapatkan diskon ====")
    else:
        print("Anda tidak mendapatkan diskon")

    print("Total harga yang harus anda bayar: ")
 
    lanjut = input("Apakah anda ingin menghitung total harga lagi? (y/n): ")
    
    if lanjut.lower() != "y":
        print("Terimakasih Telah Berbelanja di Toko Kami!!!")
        break