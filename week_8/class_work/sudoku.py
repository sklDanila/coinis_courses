from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

m = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]
# print(m)
matrix_input = []
i = 0
for i in range(0, 9):
    row_of_inputs = []
    for j in range(0, 9):
        input = ttk.Entry(frame, width=4)
        input.grid(column=j, row=i)
        input.insert(0, m[i][j])
        row_of_inputs.append(input)
    matrix_input.append(row_of_inputs)

root.mainloop()
