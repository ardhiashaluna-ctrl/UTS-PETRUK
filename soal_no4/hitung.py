def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0

    total = 0 
    for angka in nilai:
        total += angka
    return total / len(nilai)

def tampilkan_hasil(nama, nilai, batas_lulus=70):
    rata_rata = hitung_rata_rata(nilai)

    print("Nama: ", nama)
    print("Rata-rata: ", round(rata_rata, 2))

    status = "Lulus" if rata_rata >= batas_lulus else "Tidak Lulus"
    print("Status: ", status)

if __name__ == '__main__':
    nilai_budi = [80, 75, 90]
    nilai_sari = [60, 65, 55, 70]

    tampilkan_hasil("Budi", nilai_budi)
    print()
    tampilkan_hasil("Sari", nilai_sari)