from bs4 import BeautifulSoup
import requests
import aiohttp
import asyncio


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
