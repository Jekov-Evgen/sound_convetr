import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


class Sound():
    def __init__(self, path_sound) -> None:
        self.path_sound = path_sound
    
    def translation(self):
        download = librosa.load(self.path_sound)


        sound = librosa.stft(download)
        sound_db = librosa.amplitude_to_db(abs(sound), ref=np.max)

        plt.plot(sound_db)
        plt.show()