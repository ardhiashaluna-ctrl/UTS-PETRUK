
"""Modul untuk memvalidasi data pengeluaran."""


class DataPengeluaranError(Exception):
    """Exception untuk data pengeluaran yang tidak valid."""
    pass


def validasi_pengeluaran(tanggal, kategori, keterangan, nominal):
    """Memeriksa dan mengembalikan data pengeluaran yang valid."""

    # Memastikan kolom teks tidak kosong.
    if not tanggal.strip() or not kategori.strip() or not keterangan.strip():
        raise DataPengeluaranError(
            "Tanggal, kategori, dan keterangan tidak boleh kosong."
        )

    # Mengubah nominal menjadi angka.
    try:
        nominal = float(nominal)
    except (TypeError, ValueError):
        raise DataPengeluaranError("Nominal harus berupa angka.")

    if nominal < 0:
        raise DataPengeluaranError("Nominal tidak boleh negatif.")

    # Memastikan nominal memenuhi ketentuan.
    assert nominal >= 0, "Nominal tidak boleh negatif."

    return {
        "tanggal": tanggal.strip(),
        "kategori": kategori.strip(),
        "keterangan": keterangan.strip(),
        "nominal": nominal
    }
