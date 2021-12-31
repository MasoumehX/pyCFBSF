import os
import sys
import librosa
import numpy as np
from scipy import signal
import python_speech_features


def envelope(sig):
    """
    Compute the analytic signal, using the Hilbert transform. (Amplitude envelope)
     Args:
        sig : Signal data. Must be real.
    Returns:
        Analytic signal of x, of each 1-D array along axis.
    """
    analytic_signal = signal.hilbert(sig)
    amplitude_env = np.absolute(analytic_signal)
    if 0 < 800 < len(amplitude_env):
        smoothing_win = signal.windows.boxcar(800) / 800
        return np.convolve(amplitude_env, smoothing_win, mode='same')
    else:
        return amplitude_env


def get_chunk_idx(sig, function=sys.argv["function"]):
    enveloped = envelope(sig)
    chunk_idx = []
    frame = 1000
    le = frame // 2
    ri = frame - le
    i = le
    while i + ri <= len(enveloped):
        if function(envelope[(i - le):(i + ri)]) == le:
            chunk_idx.append(i)
            i += ri
        else:
            i += 1
    return chunk_idx


class Audio:
    def __init__(self, filename, fullpath):
        self.fullpath = fullpath
        self.name = filename
        self.rate = 44100
        self.filewave = []
        self.wordwaves = []
        self.powspecwords = []
        self.words = []
        self.start = []
        self.end = []
        self.wchunks = []
        self.cduration = []
        self.features = []

    def read(self, f_rate):
        if not os.path.exists(self.fullpath):
            raise ValueError("The audio file ", self.name, " does not exist!")
        else:
            self.filewave, _ = librosa.load(self.fullpath, sr=f_rate)

    def write(self):
        raise ValueError("NOT implemented!")

    def get_word_signal(self):
        indices = zip((self.start * self.rate).astype(int), (self.end * self.rate).astype(int))
        self.wordwaves = [self.filewave[a:z] for a, z in indices]

    def get_chunks(self):
        chunk_idx = []
        chunks = []
        for wsig in self.wordwaves:
            cidx = get_chunk_idx(wsig)
            chunk_idx.append(cidx)
            if len(cidx) > 0:
                chunks.append(np.split(wsig, cidx))
            else:
                chunks.append(wsig)
        return chunks

    def get_chunks_duration(self, chunk_indices):
        """ This function returns the duration of each chunks based on the chunk indices"""
        all_chunk_duration = []
        wordwaves_len = [len(w) for w in self.wordwaves]
        for chunk_index, w_len in zip(chunk_indices, wordwaves_len):
            chunk_duration = []
            start = 0
            if len(chunk_index) < 0:
                chunk_duration.append(w_len / float(self.rate))
            else:
                for i in chunk_index:
                    end = i
                    chunk_duration.append((end - start) / float(self.rate))
                    start = end
                chunk_duration.append((w_len - start) / float(self.rate))
            all_chunk_duration.append(chunk_duration)
        return all_chunk_duration

    def compute_mfcc(self, sig):
        return python_speech_features.base.mfcc(signal=sig, samplerate=self.rate)

    def compute_logfbank(self, sig):
        return python_speech_features.logfbank(sig, samplerate=self.rate, winlen=0.005, winstep=0.005, nfilt=21,
                                               preemph=0.97)
