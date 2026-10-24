import pandas as pd
import numpy as np

# Langkah 1: Membaca file soal yang sudah dibuat sebelumnya
print("--- MEMBACA DATA MENTAH ---")
df = pd.read_csv('data_mentah_klatentech.csv')
print(df)
print("\n" + "="*50 + "\n")

# Langkah 2: Menghapus Data Ganda (Duplicate)
df = df.drop_duplicates()

# Langkah 3: Menyeragamkan Format Tanggal menjadi YYYY-MM-DD
df['Tanggal'] = pd.to_datetime(df['Tanggal'], errors='coerce').dt.strftime('%Y-%m-%d')

# Langkah 4: Menghapus data jika Total Belanja minus (di bawah 0)
df = df[df['Total_Belanja'] >= 0]

# Langkah 5: Mengisi Nama Pelanggan yang kosong dengan kata "Anonim"
df['Nama_Pelanggan'] = df['Nama_Pelanggan'].fillna('Anonim')

# Langkah 6: Menyeragamkan Teks (Format Judul dan Huruf Kapital)
df['Nama_Pelanggan'] = df['Nama_Pelanggan'].str.title()
df['Metode_Bayar'] = df['Metode_Bayar'].str.upper()

print("--- DATA SETELAH DIBERSIHKAN (SIAP MASUK DATABASE) ---")
print(df)

# Langkah 7: Menyimpan hasil data bersih menjadi file baru
df.to_csv('data_bersih_klatentech.csv', index=False)
print("\nSukses! File 'data_bersih_klatentech.csv' telah berhasil disimpan.")
