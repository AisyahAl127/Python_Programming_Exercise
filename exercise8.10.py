def kirim(messages, terkirim):
    """Mencetak setiap pesan dan memindahkannya ke daftar terkirim."""
    while messages:
        pesankini = messages.pop(0)
        print(f"Mengirim pesan: {pesankini}")
        terkirim.append(pesankini)

text_messages = [
    "Halo, apa kabar?",
    "Jangan lupa kerjakan tugas Python ya.",
    "Sampai jumpa besok di sekolah!"
]
terkirim = []

kirim(text_messages, terkirim)

# Mencetak kedua daftar untuk verifikasi
print("\nDaftar Pesan Asli:")
print(text_messages)

print("\nDaftar Pesan Terkirim:")
print(terkirim)