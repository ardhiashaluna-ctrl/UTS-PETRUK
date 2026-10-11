# Dokumentasi Refactoring Aplikasi Pengeluaran Harian

## Tabel Refactoring

| No. | Bagian Sebelum Refactoring | Bagian Sesudah Refactoring | Teknik | Alasan |
|---|---|---|---|---|
| 1 | Menggunakan nama variabel yang kurang jelas, seperti `x`, untuk menyimpan nominal pengeluaran. | Menggunakan nama variabel `nominal` agar lebih mudah dipahami. | Rename Variable | Memperjelas tujuan penggunaan variabel. |
| 2 | Perhitungan total dan rata-rata ditulis langsung dalam alur program utama. | Perhitungan dipisahkan ke fungsi `analisis_pengeluaran(data)`. | Extract Function | Membuat kode lebih terstruktur dan mudah diuji. |
| 3 | Validasi data dilakukan di beberapa bagian program. | Validasi dipusatkan pada fungsi `validasi_pengeluaran()`. | Remove Duplicate Code | Mengurangi pengulangan kode dan menjaga konsistensi validasi. |


