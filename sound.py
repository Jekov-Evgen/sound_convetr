import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


class Sound:
    def __init__(self, path_sound) -> None:
        self.path_sound = path_sound
    
    def translation(self):
        y, sr = librosa.load(self.path_sound)

        sound = librosa.stft(y)
        sound_db = librosa.amplitude_to_db(abs(sound), ref=np.max)

        mean_db = np.mean(sound_db, axis=1)

        frequencies = librosa.fft_frequencies(sr=sr)

        plt.figure(figsize=(10, 6))
        plt.plot(frequencies, mean_db)
        plt.title('Средний частотный спектр')
        plt.xlabel('Частота (Гц)')
        plt.ylabel('Амплитуда (дБ)')
        plt.grid(True)
        plt.show()