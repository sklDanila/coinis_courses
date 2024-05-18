def task_10():
    input_country = input("Enter country: ")
    with open("week_4\HomeWork4\population.txt", "r") as f:
        min_population = float("inf")
        city_with_min_population = None
        for line in f:
            data = line.strip().split(",")
            if data[0] == input_country:
                population = int(data[2])
                if population < min_population:
                    min_population = population
                    city_with_min_population = data[1]
    return city_with_min_population


print(task_10())
