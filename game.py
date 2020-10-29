from tkinter import Frame, Label, CENTER
import game_ai
import game_functions

EDGE_LENGTH = 100
# game size
CELL_COUNT = 4
# cell border width
CELL_PAD = 6

UP_KEY = "'w'"
DOWN_KEY = "'s'"
LEFT_KEY = "'a'"
RIGHT_KEY = "'d'"
AI_KEY = "'/'"
AI_PLAY_KEY = "'='"

LABEL_FONT = ("Helvetica", 50, "bold")

# border color
GAME_COLOR = "#bbada0"
# empty cell color
EMPTY_COLOR = "#cec0b5"
# cell number label colors
LABEL_COLORS = {2: "#695c57",
                4: "#695c57",
                8: "#ffffff",
                16: "#ffffff",
                32: "#ffffff",
                64: "#ffffff",
                128: "#ffffff",
                256: "#ffffff",
                512: "#ffffff",
                1024: "#ffffff",
                2048: "#ffffff",
                4096: "#ffffff",
                8192: "#ffffff"}
# cell number background colors
TILE_COLORS = {2: "#eee4da",
               4: "#ede0c8",
               8: "#f2b179",
               16: "#f59563",
               32: "#f67d5f",
               64: "#e64c2e",
               128: "#ede291",
               256: "#fce130",
               512: "#ffdb4a",
               1024: "#f0b922",
               2048: "#edc22e",
               4096: "#edc22e",
               8192: "#edc22e"}


class Display(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048 AI')
        self.master.bind("<Key>", self.key_press)

        self.commands = {UP_KEY: game_functions.move_up,
                         DOWN_KEY: game_functions.move_down,
                         LEFT_KEY: game_functions.move_left,
                         RIGHT_KEY: game_functions.move_right,
                         AI_KEY: game_ai.ai_move,
                         }

        self.grid_cells = []
        self.build_grid()
        self.init_matrix()
        self.draw_grid_cells()

        self.mainloop()

    def build_grid(self):
        background = Frame(self, bg=GAME_COLOR, width=EDGE_LENGTH, height=EDGE_LENGTH)
        background.grid()

        for row in range(CELL_COUNT):
            grid_row = []
            for col in range(CELL_COUNT):
                cell = Frame(background, bg=EMPTY_COLOR,
                             width=EDGE_LENGTH / CELL_COUNT,
                             height=EDGE_LENGTH / CELL_COUNT)
                cell.grid(row=row, column=col, padx=CELL_PAD, pady=CELL_PAD)
                t = Label(master=cell, text="",
                          bg=EMPTY_COLOR,
                          justify=CENTER, font=LABEL_FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = game_functions.initialize_game()

    def draw_grid_cells(self):
        for row in range(CELL_COUNT):
            for col in range(CELL_COUNT):
                tile_value = self.matrix[row][col]
                if not tile_value:
                    self.grid_cells[row][col].configure(
                        text="", bg=EMPTY_COLOR)
                else:
                    self.grid_cells[row][col].configure(text=str(
                        tile_value), bg=TILE_COLORS[tile_value],
                        fg=LABEL_COLORS[tile_value])
        self.update_idletasks()

    def key_press(self, event):
        valid_game = True
        key = repr(event.char)
        if key == AI_PLAY_KEY:
            move_count = 0
            while valid_game:
                self.matrix, valid_game = game_ai.ai_move(self.matrix, 40, 30)
                if valid_game:
                    self.matrix = game_functions.add_new_tile(self.matrix)
                    self.draw_grid_cells()
                move_count += 1
        if key == AI_KEY:
            self.matrix, move_made = game_ai.ai_move(self.matrix, 20, 30)
            if move_made:
                self.matrix = game_functions.add_new_tile(self.matrix)
                self.draw_grid_cells()
                move_made = False

        elif key in self.commands:
            self.matrix, move_made, _ = self.commands[repr(event.char)](self.matrix)
            if move_made:
                self.matrix = game_functions.add_new_tile(self.matrix)
                self.draw_grid_cells()
                move_made = False


gamegrid = Display()
