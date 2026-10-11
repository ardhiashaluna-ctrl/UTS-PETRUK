import unittest
from analisis_suhu import analisis_suhu

class TestAnalisisSuhu(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Selasa", "suhu": 33},
            {"hari": "Rabu", "suhu": 29},
            {"hari": "Kamis", "suhu": 35},
            {"hari": "Jumat", "suhu": 32},
            {"hari": "Sabtu", "suhu": 30},
            {"hari": "Minggu", "suhu": 28}
        ]
    
    def tes_rata_rata(self):
        hasil = analisis_suhu(*self.data)
        self.assertAlmostEqual(hasil["rata-rata"], 31.14, places=2)

    def tes_suhu_tertinggi(self):
        hasil = analisis_suhu(*self.data)
        self.assertEqual(hasil["tertinggi"]["suhu"], 35)
        self.assertEqual(hasil["tertinggi"]["hari"], "Kamis")
    
    def tes_suhu_terendah(self):
        hasil = analisis_suhu(*self.data)
        self.assertEqual(hasil["terendah"]["suhu"], 28)
        self.assertEqual(hasil["terendah"]["hari"], "Minggu")

    def tes_jumlah_hari_panas(self):
        hasil = analisis_suhu(*self.data, batas_panas=32)
        self.assertEqual(hasil["jumlah_hari_panas"], 4)

    def test_data_kosong(self):
        with self.assertRaises(ValueError):
            analisis_suhu()

if __name__ == "__main__":
    unittest.main()