import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def chapter(string: str) -> str:
    print("-" * 15, string, "-" * 15)


def big_chapter(string: str) -> str:
    print("=" * 45)
    print(" " * 15, string, " " * 15)
    print("=" * 45)


class Pandas:
    def __init__(self):
        big_chapter("Pandas")
        self.series_practice()
        self.dataframe_practice()
        self.dataframe_by_list()
        self.dataframe_by_dictionary()

    @staticmethod
    def series_practice():
        chapter("1-1")
        series = pd.Series(
            [15000, 14000, 13000, 11000], index=["pizza", "chicken", "taco", "pasta"]
        )
        print("Series: ")
        print(series)
        print("Series Values: {}".format(series.values))
        print("Series Indexes: {}".format(series.index))

    @staticmethod
    def dataframe_practice():
        chapter("1-2")
        values = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
        index = ["one", "two", "three"]
        column = ["A", "B", "C"]
        df = pd.DataFrame(values, index=index, columns=column)
        print(df)
        print("Dataframe Index: {}".format(df.index))
        print("Dataframe Columns: {}".format(df.columns))
        print("Dataframe Values: \n{}".format(df.values))

    @staticmethod
    def dataframe_by_list():
        chapter("1-3-1")
        data = [
            ["1000", "Steve", 90.72],
            ["1001", "James", 78.09],
            ["1002", "Doyeon", 98.43],
            ["1003", "Jane", 64.19],
            ["1004", "Pilwoong", 81.30],
            ["1005", "Tony", 99.14],
        ]
        df = pd.DataFrame(data, columns=["학번", "이름", "점수"])
        print(df)

    @staticmethod
    def dataframe_by_dictionary():
        chapter("1-3-2")
        data = {
            "학번": ["1000", "1001", "1002", "1003", "1004", "1005"],
            "이름": ["Steve", "James", "Doyeon", "Jane", "Pilwoong", "Tony"],
            "점수": [90.72, 78.09, 98.43, 64.19, 81.30, 99.14],
        }
        df = pd.DataFrame(data)
        print(df)


class Numpy:
    def __init__(self):
        big_chapter("Numpy")
        self.ndarray()
        self.initiate_ndarray()
        self.arange()
        self.reshape()

    @staticmethod
    def ndarray():
        chapter("2-1")
        vec = np.array([1, 2, 3, 4, 5])
        print("vector: {}".format(vec))
        print("vector type: {}".format(type(vec)))
        print("vector ndim: {}".format(vec.ndim))
        print("vector shape: {}".format(vec.shape))
        mat = np.array([[1, 2, 3], [4, 5, 6]])
        print("matrix: \n{}".format(mat))
        print("matrix type: {}".format(type(mat)))
        print("matrix ndim: {}".format(mat.ndim))
        print("matrix shape: {}".format(mat.shape))

    @staticmethod
    def initiate_ndarray():
        chapter("2-2")
        zero_mat = np.zeros((2, 3))
        one_mat = np.ones((4, 2))
        same_value_mat = np.full((5, 3), 7)
        eye_mat = np.eye(3)
        random_mat = np.random.random((3, 1))
        print("zero matrix: \n{}".format(zero_mat))
        print("all 1 matrix: \n{}".format(one_mat))
        print("same value matrix: \n{}".format(same_value_mat))
        print("identity matrix: \n{}".format(eye_mat))
        print("random matrix: \n{}".format(random_mat))

    @staticmethod
    def arange():
        chapter("2-3")
        range_vec = np.arange(10)
        range_n_step_vec = np.arange(1, 10, 3)
        print("range_vec: {}".format(range_vec))
        print("range_n_step_vec: {}".format(range_n_step_vec))

    @staticmethod
    def reshape():
        chapter("2-4")
        reshape_mat = np.array(np.arange(1, 31, 1)).reshape((5, 6))
        print("reshape matrix: \n{}".format(reshape_mat))


class MatplotLib:
    def __init__(self):
        self.line_plot()

    @staticmethod
    def line_plot():
        plt.title("students")
        plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
        plt.plot([1.5, 2.5, 3.5, 4.5], [3, 5, 8, 10])
        plt.xlabel("hours")
        plt.ylabel("score")
        plt.legend(["A student", "B student"])
        plt.show()


if __name__ == "__main__":
    Pandas()
    Numpy()
    MatplotLib()
