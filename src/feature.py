import random
from audio import Audio
from scipy import stats


class Features:
    def __init__(self, method="cfbsf"):
        self.features = []
        self.method = method

    def extract_features(self):
        if self.method == "cfbsf":
            self.cfbsf()
        else:
            raise ValueError("Other method than cfbsf has not implemented!")

    def cfbsf(self):
        audio = Audio(filename="", fullpath="")
        audio.read(f_rate=16000)
        chunks = audio.get_chunks()
        n = 20  # sample size
        for chunk in chunks:
            cfbf = []
            spec = audio.compute_logfbank(chunk)
            if spec is not None:
                if len(spec[0]) >= n:
                    for i, band in enumerate(spec, 1):
                        band_index = list(enumerate(band))
                        cfbf.append(i)
                        n_sample = random.sample(band_index, n)
                        order_sample = sorted(n_sample, key=lambda tup: tup[0])
                        order_sample_values = [lis[1] for lis in order_sample]
                        for x in order_sample_values:
                            cfbf.append(x)
                        for j in range(i, 21):
                            r, _ = stats.pearsonr(band, spec[j])
                            cfbf.append(r)
                else:
                    len_mel = len(spec[0])
                    zero_pad = n - len_mel
                    for i, band in enumerate(spec, 1):
                        cfbf.append(i)
                        for z in band:
                            cfbf.append(z)
                        for x in range(zero_pad):
                            cfbf.append(0)
                        for j in range(i, 21):
                            r, _ = stats.pearsonr(band, spec[i])
                            cfbf.append(r)

            self.features.append(cfbf)
