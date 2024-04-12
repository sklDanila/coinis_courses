import pandas as pd


def normalization_of_values(column):
    df = pd.read_csv("week_8\\HomeWork5\\Task_1\\salaries_dataset.csv")

    match column:
        case 1:
            min_value = df["work_year"].min()
            max_value = df["work_year"].max()
            normalized_column = [
                (x - min_value) / (max_value - min_value) for x in df["work_year"]
            ]
            print(normalized_column)
