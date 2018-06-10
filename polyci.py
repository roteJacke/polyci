

# 0-255 ASCII some numbers missing, alternative needed
code_book = [  # 189 letters and symbols
    "\t", " ", "!", "#", "$", "%", "&", "'", "(", ")",
    "*", "+", ",", "-", ".", "/", "0", "1", "2", "3",
    "4", "5", "6", "7", "8", "9", ":", ";", "<", "=",
    ">", "?", "@", "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[",
    "]", "^", "_", "`", "a", "b", "c", "d", "e", "f",
    "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "{", "|", "}", "~", "¡", "¢", "£", "¤", "¥", "¦",
    "§", "¨", "©", "ª", "«", "¬", "®", "¯", "°", "±",
    "²", "³", "´", "µ", "¶", "·", "¸", "¹", "º", "»",
    "¼", "½", "¾", "¿", "À", "Á", "Â", "Ã", "Ä", "Å",
    "Æ", "Ç", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï",
    "Ð", "Ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "×", "Ø", "Ù",
    "Ú", "Û", "Ü", "Ý", "Þ", "ß", "à", "á", "â", "ã",
    "ä", "å", "æ", "ç", "è", "é", "ê", "ë", "ì", "í",
    "î", "ï", "ð", "ñ", "ò", "ó", "ô", "õ", "ö", "÷",
    "ø", "ù", "ú", "û", "ü", "ý", "þ", " ", "\n"
]
about = "Module for basic symmetrical encryption."
f = {
    "decrypt(txt, key)": "Decrypts most ASCII chars with given key.",
    "encrypt(txt, key)": "Encrypts most ASCII chars with given key.",
}


def decrypt(txt, key):
    return _modify_txt(txt, str(key), -1)


def encrypt(txt, key):
    return _modify_txt(txt, str(key), 1)


def _modify_txt(txt, key, mode):
    txt, key, k_order = str(txt), str(key), 0
    modified_txt, cb = "", code_book
    for letter in txt:
        if key[k_order] not in cb:
            print("Error: Unknown key symbol.")
            return None
        if letter in cb:
            # Shift letter position based on key
            shift = cb.index(letter) + (cb.index(key[k_order]) * mode)
            shift = shift % len(cb)  # avoid overflow
            modified_txt += cb[shift]
        else:
            modified_txt += "?"  # unknown symbol
        k_order += 1
        if k_order >= len(key): k_order = 0
    return modified_txt


def _modnum(n, shiftn, multiplier):
    # encrypts a number and returns it
    n = n + (shiftn * multiplier)  # encrypt n
    n = n % 256  # 256 colors in gif
    return n


def help():
    print("Functions:")
    for x in f.items():
        print("{} :: {}".format(x[0], x[1]))
    print()
