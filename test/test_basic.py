
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

    def test_getExtension_file(self, filename="sample.pkl"):
        extension = filename.split(".")[-1]
        self.assertTrue(extension in ['pkl', 'pickle', 'parquet', 'csv', 'xlsx'])

    def test_read_fileNotFound(self):
        myCorpus = Corpus("my/"+corpus_file_name_pkl)
        self.assertRaises(FileExistsError, myCorpus.read)

    def test_read_pkl(self):
        myCorpus = Corpus(corpus_file_name_pkl)
        myCorpus.read()
        expected = ["wordtoken", "File", "start", "end"]
        produced = list(myCorpus.data.columns.values)
        self.assertTrue(set(expected).issubset(produced))

    def test_read_parquet(self):
        myCorpus = Corpus(corpus_file_name_parquet)
        myCorpus.read()
        expected = ["wordtoken", "File", "start", "end"]
        produced = list(myCorpus.data.columns.values)
        self.assertTrue(set(expected).issubset(produced))

    def test_read_csv(self):
        myCorpus = Corpus(corpus_file_name_csv)
        myCorpus.read()
        expected = ["wordtoken", "File", "start", "end"]
        produced = list(myCorpus.data.columns.values)
        self.assertTrue(set(expected).issubset(produced))

    def test_read_excel(self):
        myCorpus = Corpus(corpus_file_name_excel)
        myCorpus.read()
        expected = ["wordtoken", "File", "start", "end"]
        produced = list(myCorpus.data.columns.values)
        self.assertTrue(set(expected).issubset(produced))

    def test_read_unknown(self):
        myCorpus = Corpus("/m"+corpus_file_name_pkl)
        self.assertRaises(Exception, myCorpus.read)

    def test_process_columns(self):
        cols = {"word": "wordtoken", "file": "File", "start": "start", "end": "end"}
        myCorpus = Corpus(corpus_file_name_pkl)
        myCorpus.read()
        produced = list(myCorpus.data.columns.values)
        self.assertTrue(set(cols.values()).issubset(produced))

    def test_prepare_filename(self):
        expectedfname = audio_file.split("/")[-1]
        self.assertTrue(expectedfname, "sample.wav")