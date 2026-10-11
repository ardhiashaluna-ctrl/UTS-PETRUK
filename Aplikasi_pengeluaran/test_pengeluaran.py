
"""Pengujian otomatis aplikasi pengeluaran harian."""

import tempfile
import unittest
from pathlib import Path

from pengeluaran_app.validasi import (
    validasi_pengeluaran,
    DataPengeluaranError
)
from pengeluaran_app.fileio import (
    buat_file_awal,
    tambah_pengeluaran,
    baca_pengeluaran,
    tulis_laporan
)
from pengeluaran_app.processing import analisis_pengeluaran, format_laporan


class TestPengeluaran(unittest.TestCase):
    """Kumpulan pengujian aplikasi pengeluaran."""

    def test_validasi_data_benar(self):
        data = validasi_pengeluaran(
            "2026-10-10", "Makanan", "Makan siang", "15000"
        )
        self.assertEqual(data["nominal"], 15000.0)

    def test_nominal_negatif_ditolak(self):
        with self.assertRaises(DataPengeluaranError):
            validasi_pengeluaran(
                "2026-10-10", "Makanan", "Makan siang", "-5000"
            )

    def test_analisis_pengeluaran(self):
        data = [
            {
                "tanggal": "2026-10-10",
                "kategori": "Makanan",
                "keterangan": "Makan siang",
                "nominal": 10000.0
            },
            {
                "tanggal": "2026-10-11",
                "kategori": "Transportasi",
                "keterangan": "Ongkos",
                "nominal": 20000.0
            }
        ]

        hasil = analisis_pengeluaran(data)
        self.assertEqual(hasil["total"], 30000.0)
        self.assertEqual(hasil["rata_rata"], 15000.0)

    def test_buat_file_dan_tidak_menimpa(self):
        with tempfile.TemporaryDirectory() as folder:
            nama_file = Path(folder) / "pengeluaran.txt"

            buat_file_awal(nama_file)
            tambah_pengeluaran(
                nama_file, "2026-10-10", "Makanan",
                "Makan siang", 15000
            )

            buat_file_awal(nama_file)
            data = baca_pengeluaran(nama_file)

            self.assertEqual(len(data), 1)

    def test_tambah_dan_baca_data(self):
        with tempfile.TemporaryDirectory() as folder:
            nama_file = Path(folder) / "pengeluaran.txt"
            buat_file_awal(nama_file)

            tambah_pengeluaran(
                nama_file, "2026-10-10", "Makanan",
                "Makan siang", 15000
            )

            data = baca_pengeluaran(nama_file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["kategori"], "Makanan")

    def test_simpan_laporan(self):
        with tempfile.TemporaryDirectory() as folder:
            nama_file = Path(folder) / "laporan.txt"

            tulis_laporan(nama_file, "Laporan percobaan")
            isi = nama_file.read_text(encoding="utf-8")

            self.assertEqual(isi, "Laporan percobaan")

    def test_format_laporan_data_kosong(self):
        hasil = analisis_pengeluaran([])
        laporan = format_laporan([], hasil)

        self.assertIn("Total pengeluaran: Rp0.00", laporan)
        self.assertIn("Jumlah data: 0", laporan)


if __name__ == "__main__":
    unittest.main()
