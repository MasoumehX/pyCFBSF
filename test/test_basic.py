
"""
Universität Tübingen - Seminar für Sprachwissenschaft
© Masoumeh Moradipour-Tari

Tests
"""
import unittest
import pandas as pd
from corpus import Corpus
from utils import path_leaf

corpus_file_name_pkl = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/test.pkl"
corpus_file_name_parquet = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/test.parquet"
corpus_file_name_csv = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/test.csv"
corpus_file_name_excel = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/test.xlsx"
sample_audio_file = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/sample.wav"


class TestCorpus(unittest.TestCase):

    def test_read_fileNotFound(self):
        myCorpus = Corpus("my/"+corpus_file_name_pkl)
        self.assertRaises(FileExistsError, myCorpus.read)

    def test_read_pkl(self):
        myCorpus = Corpus(corpus_file_name_pkl)
        myCorpus.read()
        self.assertTrue(isinstance(myCorpus.data, pd.DataFrame))

    def test_read_parquet(self):
        myCorpus = Corpus(corpus_file_name_parquet)
        myCorpus.read()
        self.assertTrue(isinstance(myCorpus.data, pd.DataFrame))

    def test_read_csv(self):
        myCorpus = Corpus(corpus_file_name_csv)
        myCorpus.read()
        self.assertTrue(isinstance(myCorpus.data, pd.DataFrame))

    def test_read_excel(self):
        myCorpus = Corpus(corpus_file_name_excel)
        myCorpus.read()
        self.assertTrue(isinstance(myCorpus.data, pd.DataFrame))

    def test_read_unknown(self):
        myCorpus = Corpus("/m"+corpus_file_name_pkl)
        self.assertRaises(Exception, myCorpus.read)

    def test_process_columns(self):
        myCorpus = Corpus(corpus_file_name_pkl)
        myCorpus.read()
        expected_cols = {"word", "file", "start", "end"}
        produced_cols = list(myCorpus.data.columns.values)
        self.assertTrue(set(expected_cols).issubset(produced_cols))


class TestUtils(unittest.TestCase):
    def test_path_leaf(self):
        expected = "sample.wav"
        produced = path_leaf(sample_audio_file)
        self.assertEqual(expected, produced)