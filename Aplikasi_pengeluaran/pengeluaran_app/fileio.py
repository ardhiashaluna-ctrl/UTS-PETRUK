
"""Modul untuk operasi file pengeluaran."""

from .validasi import validasi_pengeluaran, DataPengeluaranError

HEADER = "tanggal;kategori;keterangan;nominal\n"


def buat_file_awal(nama_file):
    """Membuat file baru tanpa menimpa file yang sudah ada."""

    try:
        with open(nama_file, "x", encoding="utf-8") as file:
            file.write(HEADER)
        return "File data berhasil dibuat."

    except FileExistsError:
        return "File data sudah tersedia."


def tambah_pengeluaran(nama_file, tanggal, kategori, keterangan, nominal):
    """Memvalidasi lalu menambahkan satu data ke file."""

    data = validasi_pengeluaran(
        tanggal, kategori, keterangan, nominal
    )

    with open(nama_file, "a", encoding="utf-8") as file:
        file.write(
            f"{data['tanggal']};{data['kategori']};"
            f"{data['keterangan']};{data['nominal']}\n"
        )

    return data


def baca_pengeluaran(nama_file):
    """Membaca data file satu baris demi satu baris."""

    data_pengeluaran = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                # Lewati baris kosong.
                if not baris.strip():
                    continue

                # Lewati judul kolom.
                if nomor_baris == 1 and baris.strip() == (
                    "tanggal;kategori;keterangan;nominal"
                ):
                    continue

                try:
                    bagian = baris.strip().split(";")

                    if len(bagian) != 4:
                        raise DataPengeluaranError(
                            "Data harus memiliki empat kolom."
                        )

                    data = validasi_pengeluaran(*bagian)
                    data_pengeluaran.append(data)

                except (ValueError, DataPengeluaranError) as error:
                    # Baris rusak dilewati; pembacaan berlanjut.
                    print(
                        f"Peringatan baris {nomor_baris}: {error}"
                    )

    except FileNotFoundError:
        print("File data belum ditemukan.")

    return data_pengeluaran


def tulis_laporan(nama_file, isi_laporan):
    """Menyimpan laporan dan mengganti isi laporan sebelumnya."""

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(isi_laporan)

    return "Laporan berhasil disimpan."
