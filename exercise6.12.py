bahasafav = {
    'jeni': {
        'languages': ['python', 'c++'],
        'proficiency': 'mahir'
    },
    'sarah': {
        'languages': ['c'],
        'proficiency': 'menengah'
    },
    'rudi': {
        'languages': ['c++', 'go'],
        'proficiency': 'mahir'
    },
    'galih': {
        'languages': ['python', 'haskell'],
        'proficiency': 'pemula'
    }
}


for nama, info in bahasafav.items():
    print(f"\n{nama.capitalize()} memiliki tingkat kemahiran '{info['proficiency']}' dan menyukai bahasa:")
    for bhs in info['languages']:
        print(f"\t- {bhs.upper()}")