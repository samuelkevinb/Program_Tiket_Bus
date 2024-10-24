# Data tujuan dan harga
daftar_tujuan = {
    "SBY": ("Surabaya", 300000),
    "BL": ("Bali", 350000),
    "LMP": ("Lampung", 50000)
}

# Menampilkan daftar tujuan dan harga
print("Daftar Tujuan dan Harga Perjalanan:")
print("=" * 40)
for kode, (nama, harga) in daftar_tujuan.items():
    print(f"{kode}: {nama} - Rp {harga}")
print("=" * 40)

# Input dari pengguna
pembeli = input("Nama Pembeli: ")
no_hp = input("No. Handphone: ")
tujuan = input("Pilih tujuan [SBY/BL/LMP]: ")

# Validasi tujuan dan mendapatkan harga serta nama tujuan
if tujuan in daftar_tujuan:
    nama_tujuan, harga = daftar_tujuan[tujuan]
else:
    print("Pilihan tidak ada di daftar.")
    exit()  # Keluar dari program jika tujuan tidak valid

jumlah = int(input("Jumlah Beli: "))

# Menghitung potongan
if jumlah >= 3:
    potongan = (jumlah * harga) * 0.05  # 5% potongan
    alasan_diskon = "Anda mendapatkan diskon 5% karena membeli 3 tiket atau lebih."
else:
    potongan = 0
    alasan_diskon = "Tidak ada diskon yang diberikan."

# Menghitung total
subtotal = jumlah * harga  # Subtotal sebelum potongan
total = subtotal - potongan

# Menampilkan detail transaksi
print("=======================")
print("  PENJUALAN TIKET BUS  ")
print("=======================")
print("Nama Pembeli: " + str(pembeli))
print("No. Handphone: " + str(no_hp))
print("Tujuan yang dipilih: " + str(tujuan))
print("Kota Tujuan: " + str(nama_tujuan))
print("Harga per tiket: Rp " + str(harga))
print("Jumlah Beli: " + str(jumlah))
print("Subtotal: Rp " + str(subtotal))
print("=======================")
print(alasan_diskon)
print("Potongan yang didapat: Rp " + str(potongan))
print("Total yang harus dibayar: Rp " + str(total))

# Menampilkan penjumlahan subtotal dan potongan
total_setelah_potongan = subtotal - potongan
print(f"Total setelah potongan (Subtotal - Potongan): Rp {subtotal} - Rp {potongan} = Rp {total_setelah_potongan}")

# Menghitung dan menampilkan uang kembali
ubay = int(input("Uang Bayar: "))
ukem = ubay - total
print("Uang Kembali: Rp " + str(ukem))

# Menampilkan penjumlahan uang bayar dan total
total_bayar = ubay
print(f"Total bayar (Uang Bayar): Rp {total_bayar} - Rp {total} = Uang Kembali: Rp {ukem}")
