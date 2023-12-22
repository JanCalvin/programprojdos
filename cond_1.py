import random
import pandas as pd
from datetime import datetime

# Tetapkan seed untuk generator nomor acak
random.seed(50)

# Jumlah kontainer yang akan dibagi
jumlah_modular_kontainer = 10000

# Jumlah jenis kontainer
jenis_modular_kontainer = 6

# Fungsi untuk membagi kontainer secara acak dan mengembalikan dua dictionary (ekspor dan impor)
def bagi_kontainer(jumlah_modular_kontainer, jenis_modular_kontainer):
    hasil_ekspor = {f'Kontainer {i+1}': 0 for i in range(jenis_modular_kontainer)}
    hasil_impor = {f'Kontainer {i+1}': 0 for i in range(jenis_modular_kontainer)}
    
    for _ in range(jumlah_modular_kontainer):
        jenis = random.randint(0, jenis_modular_kontainer - 1)
        jenis_kontainer = f'Kontainer {jenis + 1}'
        
        # Menggunakan random.choice() untuk memutuskan apakah ekspor atau impor
        tipe = random.choice(["Ekspor", "Impor"])
        
        if tipe == "Ekspor":
            hasil_ekspor[jenis_kontainer] += 1
        else:
            hasil_impor[jenis_kontainer] += 1

    return hasil_ekspor, hasil_impor

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
hasil_eksport, hasil_import = bagi_kontainer(jumlah_modular_kontainer, jenis_modular_kontainer)
print("Ekspor:", hasil_eksport)
print("Impor:", hasil_import)

# Data Modular Kontainer pada Bagian Eksport
jumlah_barang_eksport = jumlah_kontainer_per_jenis(hasil_eksport)
len_barang_eksport = len(jumlah_barang_eksport)
pickup_time = generate_pickup_time(len_barang_eksport)

data_eksport = create_excel(jumlah_barang_eksport,pickup_time,'Cond1_Data_Eksport')

# Data Modular Kontainer pada Bagian Import
jumlah_barang_import = jumlah_kontainer_per_jenis(hasil_import)
len_barang_import = len(jumlah_barang_import)
pickup_time = generate_pickup_time(len_barang_import)

data_import = create_excel(jumlah_barang_import,pickup_time,'Cond1_Data_Import')

list_item_eksport = []
list_item_import = []
for item in hasil_eksport.keys():
    list_item_eksport.append(hasil_eksport[item])
for item in hasil_import.keys():
    list_item_import.append(hasil_import[item])

print(f"Total Modular Kontainer Eksport: {sum(list_item_eksport)}")
print(f"Total Modular Kontainer Import: {sum(list_item_import)}")
print(f"Total Modular Kontainer: {sum(list_item_eksport) + sum(list_item_import)}")