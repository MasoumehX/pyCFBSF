import toml
import argparse
import numpy as np
from corpus import Corpus


def main():

    # getting the arguments from user
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", type=str, default='/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/words.pkl')
    parser.add_argument("-wav", type=bool, default=False)
    parser.add_argument("-spec", type=bool, default=False)
    parser.add_argument("-resample", type=int, default=16000)
    parser.add_argument("-function", type=str, default="np.argmax", choices=["np.argmax", "np.argmin"])

    args = parser.parse_args()

    # reading the corpus which is a pandas dataframe contains the columns ['word', 'path', 'start', 'end']
    my_corpus = Corpus(fullpath=args.path)
    my_corpus.read()
    # print(my_corpus.describe())
    print(my_corpus.data.iloc[0].File)


if __name__ == '__main__':
    main()
