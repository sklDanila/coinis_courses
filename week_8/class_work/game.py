from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()


sudoku_page = requests.get("https://west.websudoku.com/")
soup = BeautifulSoup(sudoku_page.content, "html.parser")

board = [[0 for element in range(9)] for row in range(9)]

for i in range(9):
    for j in range(9):
        cell_id = f"f{i}{j}"
        cell = soup.find("input", id=cell_id)
        if cell and "readonly" in cell.attrs:
            board[i][j] = int(cell["value"])
        else:
            board[i][j] = 0

matrix_input = []


def on_key_release(event, row, col):
    print(event.widget.winfo_name())
    print(event.widget.get())


for i in range(0, 9):
    row_of_inputs = []
    for j in range(0, 9):
        input = ttk.Entry(frame, width=4)
        input.grid(column=j, row=i)
        input.bind(
            "<KeyRelease>", lambda event, row=i, col=j: on_key_release(event, row, col)
        )
        if not board[i][j] == 0:
            input.insert(0, board[i][j])
        row_of_inputs.append(input)
    matrix_input.append(row_of_inputs)

root.mainloop()
