import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def minmax():
    df = pd.read_csv("week_8\\HomeWork5\\Task_1\\salaries_dataset.csv")
    print(
        "1.work_year\n2.salary\n3.salary_in_usd\n4.remote_ratio\n"
    )
    column = int(input("Enter the number of column in which you want to calculate the minimum and maximum: "))

    match column:
        case 1:
            

minmax()
