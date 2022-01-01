import random
from audio import Audio
from scipy import stats
import sys


class Features:
    def __init__(self, method="cfbsf"):
        self.method = method

    def extract_features(self, targetcorpus):
        if self.method == "cfbsf":
            # group by the files in order to extract the cues
            df = targetcorpus.data
            files = df.file.unique().tolist()
            for file in files:
                fname = file.split["/"][-1]
                afile = Audio(filename=fname, fullpath=file)
                subset = df.loc[df['file'] == file]
                afile.read(f_rate=sys.argv['resample'])
                afile.start = subset.start.values.tolist()
                afile.end = subset.end.values.tolist()
                afile.words = subset.word.values.tolist()
                afile.get_word_signal()
                afile.wchunks = afile.get_chunks()
                afile.cduration = afile.get_chunks_duration()
                afile.features = self.cfbsf(afile)
        else:
            raise ValueError("Other method than cfbsf has not implemented!")

    def cfbsf(self, afile):
        n = 20
        cfbsfs = []
        for word in afile.wchunks:
            cfbsf = []
            for index, chunk in enumerate(word, 1):
                spec = afile.compute_logfbank(chunk)
                if spec is not None:
                    if len(spec[0]) >= n:
                        for i, band in enumerate(spec, 1):
                            band_index = list(enumerate(band))
                            cfbsf.append(i)
                            n_sample = random.sample(band_index, n)
                            order_sample = sorted(n_sample, key=lambda tup: tup[0])
                            order_sample_values = [lis[1] for lis in order_sample]
                            for x in order_sample_values:
                                cfbsf.append(x)
                            for j in range(i, 21):
                                r, _ = stats.pearsonr(band, spec[j])
                                cfbsf.append(r)
                    else:
                        len_mel = len(spec[0])
                        zero_pad = n - len_mel
                        for i, band in enumerate(spec, 1):
                            cfbsf.append(i)
                            for z in band:
                                cfbsf.append(z)
                            for x in range(zero_pad):
                                cfbsf.append(0)
                            for j in range(i, 21):
                                r, _ = stats.pearsonr(band, spec[i])
                                cfbsf.append(r)
            cfbsfs.append(cfbsf)
        return cfbsfs

