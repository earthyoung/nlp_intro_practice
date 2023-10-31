import pandas as pd


def series_practice():
    series = pd.Series(
        [15000, 14000, 13000, 11000], index=["pizza", "chicken", "taco", "pasta"]
    )
    print("Series: ")
    print(series)
    print("Series Values: {}".format(series.values))
    print("Series Indexes: {}".format(series.index))


series_practice()
