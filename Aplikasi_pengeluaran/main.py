
"""Program utama aplikasi pengeluaran harian."""

from pathlib import Path

from pengeluaran_app.fileio import (
    buat_file_awal,
    tambah_pengeluaran,
    baca_pengeluaran,
    tulis_laporan
)
from pengeluaran_app.processing import (
    analisis_pengeluaran,
    format_laporan
)
from pengeluaran_app.validasi import DataPengeluaranError


# Lokasi file data dan laporan.
FOLDER_PROGRAM = Path(__file__).parent
FILE_DATA = FOLDER_PROGRAM / "pengeluaran.txt"
FILE_LAPORAN = FOLDER_PROGRAM / "laporan.txt"


def main():
    """Menjalankan aplikasi pengeluaran harian."""

    print("=== APLIKASI PENGELUARAN HARIAN ===")
    print(buat_file_awal(FILE_DATA))

    jawaban = input("Tambah pengeluaran? (y/n): ")

    if jawaban.lower() == "y":
        try:
            tanggal = input("Tanggal (contoh 2026-10-10): ")
            kategori = input("Kategori: ")
            keterangan = input("Keterangan: ")
            nominal = input("Nominal: ")

            tambah_pengeluaran(
                FILE_DATA,
                tanggal,
                kategori,
                keterangan,
                nominal
            )

            print("Data berhasil ditambahkan.")

        except (ValueError, OSError, DataPengeluaranError) as error:
            print(f"Data gagal ditambahkan: {error}")

    # Membaca data terbaru setelah proses penambahan.
    data = baca_pengeluaran(FILE_DATA)
    hasil = analisis_pengeluaran(data)
    laporan = format_laporan(data, hasil)

    print()
    print(laporan)
    print(tulis_laporan(FILE_LAPORAN, laporan))


if __name__ == "__main__":
    main()
