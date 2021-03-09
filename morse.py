#!/usr/bin/env python3

# Spacing:
# character: 3
# word: 7

# Rec. ITU-R M.1677-1
CHARS = {
    # 1.1.1
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',

    # 1.1.2
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',

    # 1.1.3
    '.': '.-.-.-',
    ',': '--..--',
    ':': '---...',
    '?': '..--..',
    "'": '.----.',
    '-': '-...-',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '"': '.-..-.',
    '=': '-...-',
    '+': '.-.-.',
    '@': '.--.-.',

    # Other conventions
    '!': '-.-.--',
    '&': '.-...',
    ';': '-.-.-.',
    '_': '..--.-',
    '$': '...-..-',

    # Extensions
    'å': '.--.-',
    'ä': '.-.-',
    'ö': '---.',

    # Spacing
    ' ': '  ',
}

PATS = {
    '.': '10',
    '-': '1110',
    ' ': '00',
}


def enc_chars(s):
    return ''.join([CHARS[c] + ' ' for c in s.lower()])


def enc_pats(s):
    return ''.join([PATS[c] for c in s])


if __name__ == '__main__':
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument('msg')
    ap.add_argument('-a', nargs='?', const='msg.wav')
    ap.add_argument('-p', action='store_true')
    args = ap.parse_args()

    chars = enc_chars(args.msg)
    pats = enc_pats(chars)

    print(chars)
    print(pats)

    if args.a or args.p:
        import cw
        w = cw.frames(pats)
        if args.a:
            print("Saving audio to %s" % args.a)
            cw.save(w, args.a)
        if args.p:
            print("Playing...")
            cw.play(w)
