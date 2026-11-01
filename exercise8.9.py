def show_pesan(messages):
    """Mencetak setiap pesan teks di dalam daftar."""
    for pesan in messages:
        print(pesan)

pesansingkat = [
    "Halo, apa kabar?",
    "Jangan lupa kerjakan tugas Python ya.",
    "Sampai jumpa besok di sekolah!"
]

show_pesan(pesansingkat)