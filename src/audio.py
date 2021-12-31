import os
import librosa
import numpy as np
from scipy import signal
import python_speech_features


class Audio:
    def __init__(self, filename, fullpath):
        self.fullpath = fullpath
        self.name = filename
        self.wave = []
        self.audio_file = os.path.join(self.fullpath, self.name)
        self.rate = 0.0

    def read(self, f_rate):
        if not os.path.exists(self.audio_file):
            raise ValueError("The audio file ", self.name, " does not exist!")
        else:
            self.wave, _ = librosa.load(self.audio_file, sr=f_rate)

    def write(self):
        raise ValueError("NOT implemented!")

    def get_raw_idx(self, start, end):
        indices = zip((start * self.rate).astype(int), (end * self.rate).astype(int))
        return [self.wave[a:z] for a, z in indices]

    def envelope(self, smooth_degree=800, smooth_mode='same'):
        analytic_signal = signal.hilbert(self.wave)
        amplitude_env = np.absolute(analytic_signal)
        if 0 < smooth_degree < len(amplitude_env):
            smoothing_win = signal.windows.boxcar(smooth_degree) / smooth_degree
            return np.convolve(amplitude_env, smoothing_win, mode=smooth_mode)
        else:
            return amplitude_env

    def get_real_idx(self, function=np.argmin, frame=1000):
        enveloped = self.envelope()
        chunk_idx = []
        le = frame // 2
        ri = frame - le
        i = le
        while i + ri <= len(enveloped):
            if function(self.envelope[(i - le):(i + ri)]) == le:
                chunk_idx.append(i)
                i += ri
            else:
                i += 1
        return chunk_idx

    def get_chunks(self):
        idx = self.get_real_idx()
        chunks = []
        if len(idx) > 0:
            chunks.append(np.split(self.wave, idx))
        else:
            chunks.append(self.wave)
        return chunks

    def compute_mfcc(self, sig):
        return python_speech_features.base.mfcc(signal=sig, samplerate=self.rate)

    def compute_logfbank(self, sig):
        return python_speech_features.logfbank(sig, samplerate=self.rate, winlen=0.005, winstep=0.005, nfilt=21,
                                               preemph=0.97)
