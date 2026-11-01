glossary = {
    'dictionary': 'Kumpulan pasangan kunci-nilai (key-value pairs) di Python.',
    'list': 'Kumpulan item yang disimpan secara berurutan dalam satu variabel.',
    'string': 'Deretan karakter yang diapit oleh tanda kutip.',
    'loop': 'Blok kode yang digunakan untuk menjalankan perintah secara berulang.',
    'boolean': 'Tipe data yang bernilai benar (True) atau salah (False).',
    'tuple': 'Kumpulan data yang mirip dengan list tetapi bersifat immutable (tidak dapat diubah).',
    'set': 'Kumpulan item unik yang tidak berurutan dan tidak memiliki duplikat.',
    'key': 'Nama pengenal unik yang digunakan untuk mengakses nilai dalam sebuah dictionary.',
    'value': 'Data atau informasi yang disimpan dan dihubungkan dengan suatu key.',
    'integer': 'Tipe data angka bulat tanpa komponen desimal.'
}

#loop
for word, meaning in glossary.items():
    print(f"\n{word.title()}:")
    print(f"\t{meaning}")