# mini-project-data-cleaning-sql
Simulasi pembersihan data menggunakan Python Pandas dan analisis database dengan SQLite - Kasus KlatenTech

# Proyek Backend Terintegrasi: Simulasi Data Cleaning & SQL Querying
Halo! Saya Ibnu Fabian Putra Pamungkas, siswa SMK Jurusan PPLG. Proyek ini merupakan portofolio backend pertama saya yang mensimulasikan alur kerja penanganan data berantakan di industri (Studi Kasus: Toko Elektronik "KlatenTech").

Melalui proyek ini, saya belajar konsep ETL (Extract, Transform, Load) secara mandiri dari nol sebelum saya terjun ke dunia PKL yang sesungguhnya.

## Mengapa Proyek Ini Dibuat?
Di dunia nyata, data yang ditarik dari aplikasi kasir sering kali berantakan karena sistem validasi yang belum sempurna. Proyek ini dibuat untuk membuktikan bagaimana logika pemrograman Python dan database SQL dapat menyelesaikan masalah tersebut secara otomatis.

## Langkah-Langkah yang Saya Lakukan

### Langkah 1: Eksperimen Membuat Masalah (Extract & Data Simulation)
Menggunakan skrip `buat_soal.py`, saya sengaja membuat tiruan data kotor dalam format `.csv` menggunakan bantuan library **Pandas**. Data kotor ini memiliki 4 masalah utama:
* Data transaksi ganda (duplikat).
* Format tanggal campuran yang berantakan.
* Anomali angka nominal yang minus.
* Teks kapitalisasi yang tidak konsisten serta nama pelanggan yang kosong (`NaN`).

*Pelajaran baru bagi saya:* Di sini saya baru memahami bahwa file `.csv` sebenarnya hanyalah teks polos yang dipisahkan oleh tanda koma, itulah mengapa file ini sangat ringan dan disukai oleh backend developer dibandingkan Excel.

### Langkah 2: Pembersihan Otomatis (Transform / Data Cleaning)
Menggunakan skrip `bersihkan_data.py`, saya menerapkan logika koding Python Pandas untuk menyaring data:
* Menghapus duplikat secara instan dengan `.drop_duplicates()`.
* Membuang baris transaksi anomali (minus).
* Mengisi kolom nama yang kosong menjadi "Anonim".
* Menyeragamkan teks metode bayar menjadi huruf kapital semua (`QRIS`).

### Langkah 3: Migrasi Database & Pelaporan (Load & SQL Query)
Melalui skrip `proses_sql.py`, data yang sudah bersih disimpan secara permanen ke dalam database **SQLite**. Saya kemudian menulis query SQL untuk menghitung total pendapatan khusus metode pembayaran **QRIS**:
```sql
SELECT metode_bayar, SUM(total_belanja) AS total_pendapatan
FROM penjualan
WHERE metode_bayar = 'QRIS'
GROUP BY metode_bayar;
```
Hasil akhirnya, database sukses menyajikan data omset akurat sebesar **750.000** tanpa terganggu oleh data rusak di awal.

## Apa yang Saya Pelajari?
1. Paham alur kerja pemrosesan data (ETL).
2. Tahu perbedaan mendasar antara file CSV dan Excel.
3. Mengerti pentingnya database relasional untuk menyimpan data secara permanen dibandingkan hanya mengolahnya di memori Python.
