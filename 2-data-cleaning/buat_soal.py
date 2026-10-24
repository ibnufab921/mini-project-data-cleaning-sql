import pandas as pd
import numpy as np

# 1. Siapkan datanya
bahan_soal = {
    'ID_Transaksi': ['T001', 'T002', 'T003', 'T004', 'T001'],
    'Tanggal': ['2026-04-01', '02/04/2026', '2026-04-03', '2026-04-04', '2026-04-01'],
    'Nama_Pelanggan': ['Budi Santoso', 'ANDI WIJAYA', np.nan, 'Rinawati', 'Budi Santoso'],
    'Total_Belanja': [1500000, -50000, 750000, 2300000, 1500000],
    'Metode_Bayar': ['Transfer Bank', 'QRIS', 'qris', 'COD', 'Transfer Bank']
}

df = pd.DataFrame(bahan_soal)

# 2. Perintah OTOMATIS menyimpan menjadi file CSV di laptop
df.to_csv('data_mentah_klatentech.csv', index=False)

print("Berhasil! File 'data_mentah_klatentech.csv' otomatis terbuat di folder Anda.")
