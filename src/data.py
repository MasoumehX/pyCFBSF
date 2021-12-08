from termcolor import colored
import pandas as pd


def data_pre_processing(database):
    """
        This function is responsible to make sure the input database contains three important columns,
        start, end, path, moreover a quality insurance of the quality of the data such as detecting the
        null, negative or

        :param database:
        :return: None
    """

    if not isinstance(database, pd.DataFrame):
        raise ValueError("The input must be a Pandas Dataframe.")
    else:
        print(colored("#####################", 'yellow'), " Analyzing the database ", colored("#####################", 'yellow'))
        # print(database.describe())


if __name__ == '__main__':
    df = pd.DataFrame([])
    data_pre_processing(df)