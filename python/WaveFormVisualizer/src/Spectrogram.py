import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import PathManager as pm
import os

class Spectrogram:
    def __init__(self):
        self.null = None

base_path = pm.get_base_path()
print(base_path)

#load audio file 
filename = os.path.join(base_path, 'data/sound/drone/uas-drone-pass-04-71065.mp3')
y, sr = librosa.load(filename, sr=None) #sr=None, preserves sample rate

#compute mel spectogram
s = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=512, n_mels=128)
s_db = librosa.power_to_db(s, ref=np.max) #Convert to decibles

#Plot mel spectogram
plt.figure(figsize=(10, 4))
librosa.display.specshow(s_db, sr=sr, hop_length=512, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f db')
plt.title('Mel Spectogram')
plt.tight_layout()
plt.show()
