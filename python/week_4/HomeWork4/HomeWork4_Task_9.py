def task_9():
    input_city = input("Enter city: ")
    max_members = 0
    result_state = ""
    with open("week_4\HomeWork4\cities.txt", "r") as f:
        for line in f:
            city, state, count_members = line.strip().split(",")
            if city == input_city:
                if int(count_members) > max_members:
                    max_members = int(count_members)
                    result_state = state
    print(f"The biggest population of {input_city} is in {result_state}.")


task_9()
