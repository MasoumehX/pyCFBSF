import os
import pandas as pd
from termcolor import colored


class Corpus:
    def __init__(self, fullpath):
        self.fullpath = fullpath
        self.data = pd.DataFrame()

    def read(self):
        if not os.path.exists(self.fullpath):
            raise FileExistsError("The path does not exist!")
        _,fileformat = os.path.splitext(self.fullpath)
        if fileformat == ".pkl" or fileformat == ".pickle":
            self.data = pd.read_pickle(self.fullpath)
        elif fileformat == ".parquet":
            self.data = pd.read_parquet(self.fullpath)
        elif fileformat == ".csv":
            self.data = pd.read_csv(self.fullpath)
        elif fileformat == ".xlsx":
            self.data = pd.read_excel(self.fullpath)
        else:
            raise Exception(colored("Acceptable data format is : .pkl, .pickle, .parquet, .csv, or .excel", 'red'))

    def describe(self):
        # TODO: add more description
        print("The columns are: ", self.data.columns.values.tolist())
        print(self.data.describe())

    def process(self):
        # TODO check the dataframe is not empty
        # TODO check the dataframe does not have any null or negative values
        cols = self.data.columns.values.tolist()
        expected_cols = ["word", "file", "start", "end"]
        if not(set(cols).issubset(['word', 'file', 'start', 'end'])):
            raise Exception("Could not found these cols: ", expected_cols)



