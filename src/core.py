import librosa
import os
from scipy import signal
import numpy as np


class Audio:
    def __init__(self, fullname, down_rate):
        self.filename = fullname
        self.down_rate = down_rate
        self.wave = []
        self.origin_rate = 0.0
        self.envelope = []

    def loading(self):
        if not os.path.exists(self.filename):
            raise ValueError("The audio file ", self.filename, " does not exist!")
        else:
            self.wave, self.origin_rate = librosa.load(self.filename, sr=self.down_rate)
            return self.wave

    def cutting(self, start, end):
        indices = zip((start * self.down_rate).astype(int), (end * self.down_rate).astype(int))
        return [self.wave[a:z] for a, z in indices]

    def enveloping(self, smooth_degree=800, smooth_mode='same'):
        analytic_signal = signal.hilbert(self.wave)
        amplitude_env = np.absolute(analytic_signal)
        if 0 < smooth_degree < len(amplitude_env):
            smoothing_win = signal.windows.boxcar(smooth_degree) / smooth_degree
            self.envelope = np.convolve(amplitude_env, smoothing_win, mode=smooth_mode)
        else:
            self.envelope = amplitude_env
        return self.envelope

    def rolling(self, function=np.argmin, frame=1000):
        le = frame // 2
        ri = frame - le
        i = le
        target_pos = []
        while i + ri <= len(self.envelope):
            if function(self.envelope[(i - le):(i + ri)]) == le:
                target_pos.append(i)
                i += ri
            else:
                i += 1
        return target_pos

    def chunking(self, smooth_degree=800, smooth_mode='same', frame=1000, function=np.argmin):
        self.envelope = self.enveloping(smooth_degree=smooth_degree, smooth_mode=smooth_mode)
        indices = self.rolling(function=function, frame=frame)
        return np.array(indices)
