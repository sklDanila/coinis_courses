import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("week_8\\HomeWork5\\Task_1\\salaries_dataset.csv")


def functions():
    num_column = start()

    match num_column:
        case 1:
            column = "work_year"
            print(
                f"\nMin value in {column} column is {minmax(column)[0]}, max value is {minmax(column)[1]}"
            )
            print(f"Average value in {column} column is {avg_value(column)}")
            print(
                f"Different between max and avg values: {between_max_avg(column)}%",
            )
            normalization(column)
            update_file()
        case 2:
            column = "salary"
            print(
                f"\nMin value in {column} column is {minmax(column)[0]}, max value is {minmax(column)[1]}"
            )
            print(f"Average value in {column} column is {avg_value(column)}")
            print(
                f"Different between max and avg values: {between_max_avg(column)}%",
            )
            # normalization(column)
            # update_file()
        case 3:
            column = "salary_in_usd"
            print(
                f"\nMin value in {column} column is {minmax(column)[0]}, max value is {minmax(column)[1]}"
            )
            print(f"Average value in {column} column is {avg_value(column)}")
            print(
                f"Different between max and avg values: {between_max_avg(column)}%",
            )
            normalization(column)
            update_file()
        case 4:
            column = "remote_ratio"
            print(
                f"\nMin value in {column} column is {minmax(column)[0]}, max value is {minmax(column)[1]}"
            )
            print(f"Average value in {column} column is {avg_value(column)}")
            print(
                f"Different between max and avg values: {between_max_avg(column)}%",
            )
            normalization(column)
            update_file()


def start():
    print("1.work_year\n2.salary\n3.salary_in_usd\n4.remote_ratio\n")
    num_column = int(
        input(
            "Enter the number of column in which you want to calculate the minimum and maximum: "
        )
    )
    return num_column


def minmax(column):
    global df
    min_value = df[column].min()
    max_value = df[column].max()
    return [min_value, max_value]


def avg_value(column):
    global df
    sum = 0
    count = 0
    for value in df[column]:
        sum += value
        count += 1
    avg = sum / count
    return avg


def between_max_avg(column):
    global df
    max_value = minmax(column)[1]
    avg = avg_value(column)
    max_avg = ((max_value - avg) / avg) * 100
    return max_avg


def normalization(column):
    global df
    min_value = minmax(column)[0]
    max_value = minmax(column)[1]
    df[column] = [(x - min_value) / (max_value - min_value) for x in df[column]]


def update_file():
    global df
    df.to_csv("week_8\\HomeWork5\\Task_1\\salaries_dataset.csv", index=False)


def correlation():
    global df
    numeric_data = df.select_dtypes(include="number").iloc[:, 1:]
    correlation_matrix = numeric_data.corr()
    max_positive_corr = correlation_matrix.stack().idxmax()
    max_negative_corr = correlation_matrix.stack().idxmin()
    print(
        "The two columns with the highest positive correlation are:", max_positive_corr
    )
    print(
        "The two columns with the lowest negative correlation are:", max_negative_corr
    )
