def make_shirt(size='L', pesan='I love Python'):
    """Membuat kaos dengan ukuran default large dan pesan default."""
    print(f"Membuat kaos ukuran {size.title()} dengan pesan: '{pesan}'.")

make_shirt()

make_shirt(size='M')

make_shirt(size='S', pesan='Python sangat keren!')