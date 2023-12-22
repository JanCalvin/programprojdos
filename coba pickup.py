from datetime import datetime, timedelta
import pandas as pd
import random

# Jumlah kontainer untuk ekspor dan impor
ekspor = {'Kontainer 1': 794, 'Kontainer 2': 824, 'Kontainer 3': 834, 'Kontainer 4': 851, 'Kontainer 5': 798, 'Kontainer 6': 835}
impor = {'Kontainer 1': 853, 'Kontainer 2': 857, 'Kontainer 3': 863, 'Kontainer 4': 852, 'Kontainer 5': 787, 'Kontainer 6': 852}

# jumlah_ekspor = []
# for index,key in enumerate(ekspor.keys()):
#     if key == f"Kontainer {index+1}":
#         for i in range(ekspor[key]):
#             jumlah_ekspor.append(index+1)

def jumlah_kontainer_per_jenis(jenis_kontainer:dict):
    jumlah_barang = []
    for index,key in enumerate(jenis_kontainer.keys()):
        if key == f"Kontainer {index+1}":
            for i in range(jenis_kontainer[key]):
                jumlah_barang.append(index+1)
    return jumlah_barang

def generate_pickup_time(jumlah_kontainer):
    start_time = datetime(2023, 1, 1, 0, 0)  # Tanggal dan waktu awal
    end_time = datetime(2023, 1, 1, 0, 0)  # Tanggal dan waktu akhir (sama dengan awal)

    pickup_times = []

    for _ in range(jumlah_kontainer):
        end_time += timedelta(minutes=15)
        pickup_time = random.uniform(start_time.timestamp(), end_time.timestamp())
        pickup_times.append(datetime.fromtimestamp(pickup_time).strftime('%H:%M'))

    return pickup_times

def create_excel(jumlah_barang:list, pickup_time:list, nama_jenis_barang:str):
    data = list(zip(jumlah_barang, pickup_time))
    df = pd.DataFrame(data, columns=["Jenis Kontainer", "Pick Up Time"])
    # Nama file Excel yang akan disimpan
    nama_file_excel = f"{nama_jenis_barang}.xlsx"
    # Menulis dataframe ke dalam file Excel
    df.to_excel(nama_file_excel, index=False)


## Coba
jumlah_barang_eksport = jumlah_kontainer_per_jenis(ekspor)
len_barang_eksport = len(jumlah_barang_eksport)
pickup_time = generate_pickup_time(len_barang_eksport)

## buat excel
data_eksport = create_excel(jumlah_barang_eksport,pickup_time,'Data_Eksport_Cond1')

