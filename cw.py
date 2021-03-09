import pyaudio
import struct
import math
import wave

RATE = 44100
FORMAT = pyaudio.paInt16
FREQ = 600
WPM = 10  # [effective]
UNIT = 60.0 / (50 * WPM)  # length of a dit, [s]

p = pyaudio.PyAudio()


def frames(s):
    dat = []
    for ch in s:
        n_frames = int(RATE * UNIT)
        a_frame = FREQ / RATE
        for i in range(n_frames):
            if ch == '1':
                f = int(math.sin((i * a_frame) * 2 * math.pi) * 32767)
            elif ch == '0':
                f = 0
            else:
                raise ValueError(f'Invalid character: {ch}')
            dat.append(f)
    return struct.pack(f'{len(dat)}h', *dat)


def play(b):
    stream = p.open(format=FORMAT, channels=2, rate=RATE, output=True)
    stream.write(b)
    stream.stop_stream()
    stream.close()


def save(b, path):
    wf = wave.open(path, 'wb')
    wf.setnchannels(2)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b)
