kota = {
    'jakarta': {
        'country': 'indonesia',
        'population': '10.5 juta',
        'fact': 'Merupakan pusat pemerintahan dan bisnis terbesar di Indonesia.'
    },
    'tokyo': {
        'country': 'jepang',
        'population': '14 juta',
        'fact': 'Salah satu kota metropolitan paling padat dan modern di dunia.'
    },
    'paris': {
        'country': 'perancis',
        'population': '2.1 juta',
        'fact': 'Terkenal dengan sebutan Kota Cinta dan Menara Eiffel.'
    }
}

namakota = kota.items()
for city, info in kota.items():
    print(f"\nKota: {city.capitalize()}")
    print(f"\tNegara: {info['country'].capitalize()}")
    print(f"\tPopulasi: {info['population']}")
    print(f"\tFakta: {info['fact']}")