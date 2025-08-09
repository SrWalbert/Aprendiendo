import sounddevice as sd
import numpy as np
import aubio

# Audio config
samplerate = 44100
buffer_size = 1024

# Aubio pitch detection
pitch_detector = aubio.pitch("default", buffer_size * 4, buffer_size, samplerate)
pitch_detector.set_unit("Hz")
pitch_detector.set_silence(-40)

# Nota base para referencia
NOTE_NAMES = [
    "C",
    "C#/Db",
    "D",
    "D#/Eb",
    "E",
    "F",
    "F#/Gb",
    "G",
    "G#",
    "A",
    "A#/Bb",
    "B",
]
NOTE_NAME_ES = [
    "Do",
    "Do#/Reb",
    "Re",
    "Re#/Mib",
    "Mi",
    "Fa",
    "Fa#/Solb",
    "Sol",
    "Sol#/Lab",
    "La",
    "La#/Sib",
    "Si",
]


def hz_to_note(freq):
    if freq == 0:
        return None, 0
    A4 = 440.0
    semitones = 12 * np.log2(freq / A4)
    note_index = int(round(semitones)) + 57  # 57 = MIDI index for A4
    note_name = NOTE_NAMES[note_index % 12]
    octave = note_index // 12
    return f"{note_name}{octave}", semitones - int(semitones)


def audio_callback(indata, frames, time, status):
    samples = np.mean(indata, axis=1).astype(np.float32)
    freq = pitch_detector(samples)[0]
    note, diff = hz_to_note(freq)

    if note:
        print(f"Nota detectada: {note} ({freq:.2f} Hz) | Desviación: {diff:+.2f}")


with sd.InputStream(
    channels=1, callback=audio_callback, blocksize=buffer_size, samplerate=samplerate
):
    print("Comienza a cantar... (presiona Ctrl+C para salir)")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")
