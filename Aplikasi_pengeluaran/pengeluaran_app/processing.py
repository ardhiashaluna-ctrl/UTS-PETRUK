
"""Modul untuk mengolah data pengeluaran."""


def analisis_pengeluaran(data):
    """Menghitung total, rata-rata, dan pengeluaran terbesar."""

    nominal = [item["nominal"] for item in data]

    if not nominal:
        return {
            "total": 0,
            "rata_rata": 0,
            "terbesar": None,
            "jumlah_data": 0
        }

    total = sum(nominal)
    rata_rata = total / len(nominal)
    terbesar = max(data, key=lambda item: item["nominal"])

    return {
        "total": total,
        "rata_rata": rata_rata,
        "terbesar": terbesar,
        "jumlah_data": len(data)
    }


def format_laporan(data, hasil):
    """Menyusun data dan hasil analisis menjadi teks laporan."""

    baris = [
        "LAPORAN PENGELUARAN HARIAN",
        "===========================",
        f"Jumlah data: {hasil['jumlah_data']}",
        f"Total pengeluaran: Rp{hasil['total']:.2f}",
        f"Rata-rata pengeluaran: Rp{hasil['rata_rata']:.2f}",
        "",
        "DAFTAR PENGELUARAN"
    ]

    # Mengurutkan data berdasarkan tanggal.
    data_urut = sorted(data, key=lambda item: item["tanggal"])

    for item in data_urut:
        baris.append(
            f"{item['tanggal']} | {item['kategori']} | "
            f"{item['keterangan']} | Rp{item['nominal']:.2f}"
        )

    if hasil["terbesar"] is not None:
        item = hasil["terbesar"]
        baris.extend([
            "",
            "PENGELUARAN TERBESAR",
            f"{item['kategori']} - {item['keterangan']}: "
            f"Rp{item['nominal']:.2f}"
        ])

    return "\n".join(baris) + "\n"
