import argparse
from corpus import Corpus
from feature import Features


def main():

    # getting the arguments from user
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", type=str, help="a full path to the dataframe contains words.",
                        default='/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/train.pkl')
    parser.add_argument("-wav", type=bool, help="Ture if the audio signals should be stored in output.", default=False)
    parser.add_argument("-spec", type=bool, help="True if the power spectrum should be stored in output.", default=False)
    parser.add_argument("-resample", type=int, help="downsampling or upsampling rate", default=16000)
    parser.add_argument("-function", type=str, help="a function to find the chunk boundaries.", default="np.argmax",
                        choices=["np.argmax", "np.argmin"])

    args = parser.parse_args()

    # reading the corpus which is a pandas dataframe contains the columns ['word', 'file', 'start', 'end']
    corpus = Corpus(fullpath=args.path)
    corpus.read()
    print(corpus.data.iloc[0].file)
    features = Features()
    features.extract_features(targetcorpus=corpus)


if __name__ == '__main__':
    main()
