import random
import pandas as pd
from datetime import datetime

# Fungsi untuk membagi kontainer secara acak dan mengembalikan dua dictionary (ekspor dan impor)
def bagi_kontainer():
    hasil_eksport = {}
    hasil_import = {}

    jumlah_total = 10000
    persentase = [0.25, 0.15, 0.1, 0.1, 0.1, 0.25]
    list_cont = []

    for komposisi in persentase :
        container = round(komposisi*jumlah_total)
        list_cont.append(container)
    
    for i, jumlah in enumerate(list_cont, start=1):
        nama_kontainer = f"Kontainer {i}"
        # Bagi jumlah secara acak antara eksport dan import
        proporsi_eksport = random.uniform(0, 1)  # Proporsi acak
        jumlah_eksport = round(jumlah * proporsi_eksport)
        jumlah_import = jumlah - jumlah_eksport

        hasil_eksport[nama_kontainer] = jumlah_eksport
        hasil_import[nama_kontainer] = jumlah_import

    return hasil_eksport, hasil_import

# Fungsi untuk mengembalikan nilai list yang isinya jumlah per jenis 
def jumlah_kontainer_per_jenis(jenis_kontainer:dict):
    jumlah_barang = []
    for index,key in enumerate(jenis_kontainer.keys()):
        if key == f"Kontainer {index+1}":
            for i in range(jenis_kontainer[key]):
                jumlah_barang.append(index+1)
    return jumlah_barang

# Fungsi untuk generating pick up time secara random dengan selisih 15 menit
def generate_pickup_time(jumlah_kontainer):
    pickup_times = []

    for _ in range(jumlah_kontainer):
        # Generate jam dan menit secara acak
        jam = random.randint(0, 23)
        menit = random.randint(0, 59)
        waktu = datetime(2023, 1, 1, jam, menit)
        pickup_times.append(waktu.strftime('%H:%M'))

    return pickup_times

# Membuat file excel
def create_excel(jumlah_barang:list, pickup_time:list, nama_jenis_barang:str):
    data = list(zip(jumlah_barang, pickup_time))
    df = pd.DataFrame(data, columns=["Jenis Kontainer", "Pick Up Time"])
    # Nama file Excel yang akan disimpan
    nama_file_excel = f"{nama_jenis_barang}.xlsx"
    # Menulis dataframe ke dalam file Excel
    df.to_excel(nama_file_excel, index=False)

# Hasil pembagian modular kontainer dalam bentuk dua dictionary (ekspor dan impor)
hasil_eksport, hasil_import = bagi_kontainer()
print("Hasil Eksport:", hasil_eksport)
print("Hasil Import:", hasil_import)

# Data Modular Kontainer pada Bagian Eksport
jumlah_barang_eksport = jumlah_kontainer_per_jenis(hasil_eksport)
len_barang_eksport = len(jumlah_barang_eksport)
pickup_time = generate_pickup_time(len_barang_eksport)

data_eksport = create_excel(jumlah_barang_eksport,pickup_time,'Cond3_Data_Eksport')

# Data Modular Kontainer pada Bagian Import
jumlah_barang_import = jumlah_kontainer_per_jenis(hasil_import)
len_barang_import = len(jumlah_barang_import)
pickup_time = generate_pickup_time(len_barang_import)

data_import = create_excel(jumlah_barang_import,pickup_time,'Cond3_Data_Import')

list_item_eksport = []
list_item_import = []
for item in hasil_eksport.keys():
    list_item_eksport.append(hasil_eksport[item])
for item in hasil_import.keys():
    list_item_import.append(hasil_import[item])

print(f"Total Modular Kontainer Eksport: {sum(list_item_eksport)}")
print(f"Total Modular Kontainer Import: {sum(list_item_import)}")
print(f"Total Modular Kontainer: {sum(list_item_eksport) + sum(list_item_import)}")