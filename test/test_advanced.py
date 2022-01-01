import pandas as pd
#
#
corpus_file_name_pkl = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/words.pkl"
# corpus_file_name_csv = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/words.csv"
# corpus_file_name_parq = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/words.parquet"
# corpus_file_name_excel = "/home/masoumeh/PycharmProjects/pyCFBSF/test/testfiles/words.xlsx"
df = pd.read_pickle(corpus_file_name_pkl)
print(df.shape[0])

# df = df.rename(columns={"File":"file", "wordtoken":"word"})
print(df.columns)
# df.to_pickle(corpus_file_name_pkl)
# df.to_excel(corpus_file_name_excel)
# df.to_parquet(corpus_file_name_parq, engine="pyarrow")
# df.to_csv(corpus_file_name_csv, sep=",")