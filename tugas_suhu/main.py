from pathlib import Path
from analisis_suhu import baca_data, analisis_suhu, tulis_laporan

data = baca_data(Path(__file__).parent /"suhu.txt")

if data:
    hasil = analisis_suhu(*data, batas_panas=32)
    hasil["data_harian"] = data

    print("Rata-rata Suhu:", round(hasil["rata-rata_suhu"], 2))
    print("Suhu Tertinggi:", hasil["tertinggi"])
    print("Suhu Terendah:", hasil["terendah"])
    print("Jumlah Hari Panas:", hasil["jumlah_hari_panas"])

    tulis_laporan(hasil)
    print("Laporan berhasil disimpan ke laporan_suhu.txt")