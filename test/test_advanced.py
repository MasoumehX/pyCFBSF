import pandas as pd
from utils import get_file_path

#
#
corpus_file_name_pkl = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/test.pkl"
corpus_file_name_csv = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/test.csv"
corpus_file_name_parq = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/test.parquet"
corpus_file_name_excel = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/test.xlsx"
df = pd.read_pickle(corpus_file_name_pkl)
# print(df.shape[0])
# print(df.columns)
source_files = [get_file_path(file, "") for file in df.file.to_list()]
df["file"] = source_files
print(df.file.iloc[0])

# df = df.rename(columns={"File":"file", "wordtoken":"word"})
df.to_pickle(corpus_file_name_pkl)
df.to_excel(corpus_file_name_excel)
df.to_parquet(corpus_file_name_parq, engine="pyarrow")
df.to_csv(corpus_file_name_csv, sep=",")

print("Finished!")