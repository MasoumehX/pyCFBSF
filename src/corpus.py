import os
import sys
import pandas as pd
from termcolor import colored
from audio import Audio


class Corpus:
    def __init__(self, fullpath):
        self.fullpath = fullpath
        self.data = pd.DataFrame()

    def read(self):
        if not os.path.exists(self.fullpath):
            raise FileExistsError("The path does not exist!")

        fileformat = self.fullpath.split(".")[-1]
        if fileformat == "pkl" or fileformat == "pickle":
            self.data = pd.read_pickle(self.fullpath)
        elif fileformat == "parquet":
            self.data = pd.read_parquet(self.fullpath)
        elif fileformat == "csv":
            self.data = pd.read_csv(self.fullpath)
        elif fileformat == "xlsx":
            self.data = pd.read_excel(self.fullpath)
        else:
            raise Exception(colored("Acceptable data format is : .pkl, .pickle, .parquet, .csv, or .excel", 'red'))
        self.process()

    def describe(self):
        # TODO: add more description
        print("The columns are: ", self.data.columns.values.tolist())
        print(self.data.describe())

    def process(self):
        # TODO check the dataframe is not empty
        # TODO check the dataframe does not have any null or negative values
        cols = self.data.columns.values.tolist()
        if not set(cols).issubset(['word', 'file', 'start', 'end']):
            raise Exception("The dataframe must contain columns: word, file, start, end! Please check the name of cols!")

    def save(self):
        raise NotImplementedError()

