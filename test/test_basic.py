
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


class TestCorpus(unittest.TestCase):
    def test_read_fileNotFound(self):
        myCorpus = Corpus("small redhen", "my/"+corpus_file_name_pkl, "pkl")
        self.assertRaises(FileExistsError, myCorpus.read)

    def test_read_pkl(self):
        myCorpus = Corpus("small redhen", corpus_file_name_pkl, "pkl")
        myCorpus.read()
        expected = ["wordtoken", "File", "start", "end"]
        produced = list(myCorpus.data.columns.values)
        self.assertTrue(set(expected).issubset(produced))

    def test_read_parquet(self):
        myCorpus = Corpus("small redhen", corpus_file_name_parquet, "parquet")
        myCorpus.read()
        expected = ["wordtoken", "File", "start", "end"]
        produced = list(myCorpus.data.columns.values)
        self.assertTrue(set(expected).issubset(produced))

    def test_read_csv(self):
        myCorpus = Corpus("small redhen", corpus_file_name_csv, "csv")
        myCorpus.read()
        expected = ["wordtoken", "File", "start", "end"]
        produced = list(myCorpus.data.columns.values)
        self.assertTrue(set(expected).issubset(produced))

    def test_read_excel(self):
        myCorpus = Corpus("small redhen", corpus_file_name_excel, "excel")
        myCorpus.read()
        expected = ["wordtoken", "File", "start", "end"]
        produced = list(myCorpus.data.columns.values)
        self.assertTrue(set(expected).issubset(produced))

    def test_read_unknown(self):
        myCorpus = Corpus("small redhen", corpus_file_name_pkl, "exe")
        self.assertRaises(Exception, myCorpus.read)