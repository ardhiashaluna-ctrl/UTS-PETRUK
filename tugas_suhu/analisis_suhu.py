def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                try:
                    hari, suhu = baris.strip().split(';')
                    data.append({
                        "hari": hari,
                        "suhu": int(suhu)
                    })
                except ValueError:
                    continue  
    except FileNotFoundError:
        print("Error: File", nama_file, "tidak ditemukan.")
    return data

def analisis_suhu(*data_suhu, batas_panas=32):
    if len(data_suhu) == 0:
        raise ValueError("Data suhu tidak boleh kosong.")

    suhu_tertinggi = max(data_suhu, key=lambda data: data['suhu'])
    suhu_terendah = min(data_suhu, key=lambda data: data['suhu'])
    total_suhu = sum(data['suhu'] for data in data_suhu)
    rata_rata = total_suhu / len(data_suhu)
    jumlah_hari_panas = sum(1 for data in data_suhu if data['suhu'] >= batas_panas)

    hasil = {
        "rata-rata_suhu": rata_rata,
        "tertinggi": suhu_tertinggi,
        "terendah": suhu_terendah,
        "jumlah_hari_panas": jumlah_hari_panas,
        "data_harian": list(data_suhu)
    }

    return hasil

def tulis_laporan(hasil, nama_file="laporan_suhu.txt"):
        with open(nama_file, 'w') as file:
            file.write("LAPORAN ANALISIS SUHU HARIAN\n")
            file.write("====================\n")
            file.write(f"Rata-rata Suhu: {hasil['rata-rata_suhu']:.2f} derajat\n")
            file.write(f"Suhu Tertinggi: {hasil['tertinggi']['suhu']} derajat" f"({hasil['tertinggi']['hari']}\n")
            file.write(f"Suhu Terendah: {hasil['terendah']['suhu']} derajat" f"({hasil['terendah']['hari']})\n")
            file.write(f"Jumlah Hari Panas: {hasil['jumlah_hari_panas']} hari\n")
            file.write("\nKategori Suhu Setia:\n")
            for data in hasil['data_harian']:
                kategori = "Panas" if data['suhu'] >= 32 else "Normal"
                file.write(f"{data['hari']}: {data['suhu']} - {kategori}\n")
