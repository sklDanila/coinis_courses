def task_9(file):
    input_city = input("Enter city: ")
    max_members = 0
    result_state = ""
    with open("week_4\class_work\HomeWork4\cities.txt", "r") as f:
        for line in f:
            city, state, count_members = line.strip.split("")


task_9()
