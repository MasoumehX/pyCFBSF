
"""
Universität Tübingen - Seminar für Sprachwissenschaft
© Masoumeh Moradipour-Tari

Tests
"""

import unittest
from corpus import Corpus

corpus_file_name_pkl = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/words.pkl"
corpus_file_name_parquet = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/words.parquet"
corpus_file_name_csv = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/words.csv"
corpus_file_name_excel = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/words.xlsx"
audio_file = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/sample.wav"


class TestCorpus(unittest.TestCase):

    def test_read_fileNotFound(self):
        myCorpus = Corpus("my/"+corpus_file_name_pkl)
        self.assertRaises(FileExistsError, myCorpus.read)

    def test_read_pkl(self):
        myCorpus = Corpus(corpus_file_name_pkl)
        myCorpus.read()
        expected_n_row = 131372
        produced = myCorpus.data.shape[0]
        self.assertEqual(expected_n_row, produced)

    def test_read_parquet(self):
        myCorpus = Corpus(corpus_file_name_parquet)
        myCorpus.read()
        expected_n_row = 131372
        produced = myCorpus.data.shape[0]
        self.assertEqual(expected_n_row, produced)

    def test_read_csv(self):
        myCorpus = Corpus(corpus_file_name_csv)
        myCorpus.read()
        expected_n_row = 131372
        produced = myCorpus.data.shape[0]
        self.assertEqual(expected_n_row, produced)

    def test_read_excel(self):
        myCorpus = Corpus(corpus_file_name_excel)
        myCorpus.read()
        expected_n_row = 131372
        produced = myCorpus.data.shape[0]
        self.assertEqual(expected_n_row, produced)

    def test_read_unknown(self):
        myCorpus = Corpus("/m"+corpus_file_name_pkl)
        self.assertRaises(Exception, myCorpus.read)

    def test_process_columns(self):
        myCorpus = Corpus(corpus_file_name_pkl)
        myCorpus.read()
        expected_cols = {"word", "file", "start", "end"}
        produced_cols = list(myCorpus.data.columns.values)
        self.assertTrue(set(expected_cols).issubset(produced_cols))

    def test_prepare_getfilename(self):
        expectedfname = audio_file.split("/")[-1]
        self.assertTrue(expectedfname, "sample.wav")