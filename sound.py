import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


y, sr = librosa.load('schebetanie-delfina-36996.mp3')


S = librosa.stft(y)
S_db = librosa.amplitude_to_db(abs(S), ref=np.max)

plt.plot(S_db)
plt.show()