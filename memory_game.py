import random
import tkinter as tk
from tkinter import messagebox


BOARD_SIZE = 4
HIDDEN_COLOR = "#808080"
COLORS = [
    "#D81B60",
    "#FFC107",
    "#004D40",
    "#0C960B",
    "#7C22AF",
    "#00015D",
    "#08DCC7",
    "#0691F9",
]


class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Game")
        self.master.resizable(False, False)

        self.colors = COLORS * 2
        random.shuffle(self.colors)

        self.tiles = []
        self.clicked_tiles = []
        self.matched_tiles = set()

        self.create_board()

    def create_board(self):
        board = tk.Frame(self.master, padx=12, pady=12, bg="#222222")
        board.grid(row=0, column=0)

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                index = row * BOARD_SIZE + col
                tile = tk.Frame(
                    board,
                    width=90,
                    height=70,
                    bg=HIDDEN_COLOR,
                    relief="raised",
                    borderwidth=3,
                    cursor="hand2",
                )
                tile.grid(row=row, column=col, padx=5, pady=5)
                tile.grid_propagate(False)
                tile.bind("<Button-1>", lambda event, idx=index: self.flip(idx))
                self.tiles.append(tile)

    def flip(self, index):
        if index in self.matched_tiles:
            return

        if self.tiles[index]["background"] != HIDDEN_COLOR:
            return

        if len(self.clicked_tiles) >= 2:
            return

        self.tiles[index].config(bg=self.colors[index])
        self.clicked_tiles.append(index)

        if len(self.clicked_tiles) == 2:
            self.check_match()

    def check_match(self):
        first, second = self.clicked_tiles

        if self.colors[first] == self.colors[second]:
            self.matched_tiles.update([first, second])
            self.clicked_tiles = []

            if len(self.matched_tiles) == len(self.tiles):
                messagebox.showinfo("Congratulations", "You won!")
        else:
            self.master.after(800, self.reset_tiles)

    def reset_tiles(self):
        for index in self.clicked_tiles:
            self.tiles[index].config(bg=HIDDEN_COLOR)

        self.clicked_tiles = []


def main():
    root = tk.Tk()
    MemoryGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
