import numpy as np
import simpleaudio as sa
import time


def _make_window(sample_length):
    """
    Generate a window to prevent clicks in the audio.
    Constructed of a 10% slope on each end and a flat middle.
    """
    slope_length = 80  # int(sample_length / 10)
    slopes = np.hanning(2 * slope_length)
    ones_length = int(sample_length - 2 * slope_length)
    ones = np.ones(ones_length)
    window = slopes[0:slope_length]
    window = np.append(window, ones)
    window = np.append(window, slopes[slope_length:])
    return window


def _tone(duration, frequency=600, sampling_rate=44100):
    """
    Generates a simple audio wave object from a specified frequency and duration.
    """
    samples = np.sin(
        2 * np.pi * np.arange(sampling_rate * duration) * frequency / sampling_rate
    )
    window = _make_window(len(samples))
    samples = samples * window
    samples *= 32767 / np.max(np.abs(samples))  # Normalize to 16 bit range
    samples = samples.astype(np.int16)
    wave = sa.WaveObject(samples, 1, 2, sampling_rate)
    return wave


MORSE_CODE_MARKS = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "=": "-...-",
    ".": ".-.-.-",
    ",": "--..--",
    "/": "-..-.",
    "?": "..--..",
    "<ar>": ".-.-.",
    "<bk>": "-...-.-",
    "<bt>": "-...-",
    "<kn>": "-.--.",
    "<sk>": "...-.-",
}


def _morse_code(sign):
    return MORSE_CODE_MARKS.get(sign.lower(), "")


def _decode(word):
    """
    Decode a word into a list of letters and prosigns.
    """
    codes = []
    prosign = ""
    for char in word:
        if len(prosign) > 0:
            prosign += char
            if char == ">":
                codes.append(prosign)
                prosign = ""
        elif char == "<":
            prosign = char
        else:
            codes.append(char)
    return codes


def get_timing(wpm, fwpm):
    # time unit (secs) is the time for one dit
    # For timing, see https://morsecode.world/international/timing.html
    time_unit = 1.2 / wpm

    # Farnsworth time unit (secs) is the time for one dit at the desired speed
    # only used for spacing between letters and words
    fw_time_unit = (60 / fwpm - 31 * time_unit) / 19
    return time_unit, fw_time_unit


def send_code(message, wpm=25, fwpm=15):
    time_unit, fw_time_unit = get_timing(wpm, fwpm)
    dot_tone = _tone(time_unit)
    dash_tone = _tone(3 * time_unit)
    words = message.split()
    for word in words:
        for sign in _decode(word):
            marks = _morse_code(sign)
            for mark in marks:
                if mark == ".":
                    playback = dot_tone.play()
                    playback.wait_done()
                elif mark == "-":
                    playback = dash_tone.play()
                    playback.wait_done()
                time.sleep(time_unit)
            time.sleep(3 * fw_time_unit)
        time.sleep(7 * fw_time_unit)


if __name__ == "__main__":
    message = input("Message: ")
    send_code(message)
