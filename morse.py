#!/usr/bin/env python3

# Spacing:
# character: 3
# word: 7

CHARS = {
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

    ' ': '  ',
}

PATS = {
    '.': '10',
    '-': '1110',
    ' ': '00',
}


def enc_chars(s):
    return ''.join([CHARS[c] + ' ' for c in s])


def enc_pats(s):
    return ''.join([PATS[c] for c in s])


if __name__ == '__main__':
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument('msg')
    ap.add_argument('-a', nargs='?', const='msg.wav')
    args = ap.parse_args()

    chars = enc_chars(args.msg)
    pats = enc_pats(chars)

    print(chars)
    print(pats)

    if args.a:
        import cw
        print("Saving audio to %s" % args.a)
        w = cw.frames(pats)
        # cw.play(w)
        cw.save(w, args.a)
