def task_12():
    total_sum = 0
    with open("week_4\HomeWork4\\numbers.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("0x"):
                hex_number = line[2:]
                try:
                    decimal_number = int(hex_number, 16)
                    if decimal_number % 10 == 3:
                        total_sum += decimal_number
                except ValueError:
                    pass
    return total_sum


print(task_12())
