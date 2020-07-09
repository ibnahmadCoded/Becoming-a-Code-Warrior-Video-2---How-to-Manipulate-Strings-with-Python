def alphabet_position(text):
    import string
    alphabet = list(string.ascii_lowercase)

    positions = []
    for char in text:
        if char.lower() in alphabet:
            positions.append(str(alphabet.index(char.lower()) + 1))

    return " ".join(positions)




