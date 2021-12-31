import os
import pandas as pd
from termcolor import colored


class Corpus:
    def __init__(self, name, fullpath, dformat="pkl"):
        self.fullpath = fullpath
        self.name = name
        self.fileformat = dformat
        self.data = pd.DataFrame()

    def read(self):
        if not os.path.exists(self.fullpath):
            raise FileExistsError("The corpus file ", self.name, " does not exist!")
        if self.fileformat == "pkl" or self.fileformat == "pickle":
            self.data = pd.read_pickle(self.fullpath)
        elif self.fileformat == "parquet":
            self.data = pd.read_parquet(self.fullpath)
        elif self.fileformat == "csv":
            self.data = pd.read_csv(self.fullpath)
        elif self.fileformat == "excel":
            self.data = pd.read_excel(self.fullpath)
        else:
            raise Exception(colored("Acceptable data format is : .pkl, .pickle, .parquet, .csv, or .excel", 'red'))

    def save(self):
        raise NotImplementedError()

