def task_11():
    country = input("Enter country: ")
    total_population = 0
    with open("week_4\HomeWork4\population.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == country:
                total_population += int(data[2])
    return total_population


print(task_11())
