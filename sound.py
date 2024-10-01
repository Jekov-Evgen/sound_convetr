import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


class Sound():
    def __init__(self, path_sound) -> None:
        self.path_sound = path_sound
    
    def translation(self):
        y, sr = librosa.load(self.path_sound)


        S = librosa.stft(y)
        S_db = librosa.amplitude_to_db(abs(S), ref=np.max)

        plt.plot(S_db)
        plt.show()