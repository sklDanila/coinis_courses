import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Загрузка файла CSV в DataFrame
df = pd.read_csv("week_7\\test_2\\Sales_table.csv")

scaler = MinMaxScaler()
selected_column = "2019"
# correlation_matrix = df.corr()
# Получение минимального и максимального значения из столбца '2020'
min_value = df["2020"].min()
max_value = df["2020"].max()

sum = 0
count = 0
for value in df["2020"]:
    sum += value
    count += 1

df[selected_column] = scaler.fit_transform(df[[selected_column]])

df.to_csv("week_7\\test_2\\Sales_table.csv", index=False)


print("Min value in collumn '2020':", min_value)
print("Max value in collumn '2020':", max_value)
print("Avg value of collumn '2020':", (sum / count))
print(
    "Different between max and avg values:",
    ((max_value - (sum / count)) / (sum / count)),
    "%",
)
