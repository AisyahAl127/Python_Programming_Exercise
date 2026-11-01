def sandwich(*bahan):
    """Meringkas bahan-bahan sandwich yang dipesan."""
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for item in bahan:
        print(f"- {item}")

sandwich('keju', 'tomat', 'selada')
sandwich('daging sapi', 'keju')
sandwich('mentega', 'selai stroberi', 'keju', 'cokelat')