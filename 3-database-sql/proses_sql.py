import pandas as pd
import sqlite3

# Langkah 1: Membaca file data yang sudah bersih
df_bersih = pd.read_csv('data_bersih_klatentech.csv')

# Langkah 2: Membuat Database Tiruan di Memori Laptop (SQLite)
# Menggunakan koneksi database relasional langsung dari Python
koneksi = sqlite3.connect('database_klatentech.db')
cursor = koneksi.cursor()

# Langkah 3: Eksekusi DDL (Membuat Tabel Penjualan di Database)
cursor.execute('''
CREATE TABLE IF NOT EXISTS penjualan (
    id_transaksi TEXT PRIMARY KEY,
    tanggal TEXT,
    nama_pelanggan TEXT,
    total_belanja INTEGER,
    metode_bayar TEXT
)
''')

# Langkah 4: Eksekusi DML (Memasukkan Data Bersih dari Pandas ke Tabel SQL)
df_bersih.to_sql('penjualan', koneksi, if_exists='replace', index=False)
koneksi.commit()
print("-> Data bersih berhasil dimigrasikan ke database SQL!\n")

# ========================================================
# LANGKAH 5: TAHAP QUERY SQL (PENCARIAN DATA)
# ========================================================
print("--- MENJALANKAN QUERY SQL: TOTAL PENDAPATAN QRIS ---")

# Tulis query SQL asli di dalam string Python
query_qris = '''
SELECT 
    metode_bayar,
    SUM(total_belanja) AS total_pendapatan
FROM 
    penjualan
WHERE 
    metode_bayar = 'QRIS'
GROUP BY 
    metode_bayar;
'''

# Eksekusi query ke database dan tampilkan hasilnya berbentuk tabel
hasil_query = pd.read_sql_query(query_qris, koneksi)
print(hasil_query)

# Tutup koneksi database jika sudah selesai
koneksi.close()
