# Import the necessary modules
import tkinter as tk
import random
import time

# Create the main window
window = tk.Tk()
window.title("2048 Game")

# Create the frame to hold the cells
frame = tk.Frame(window)
frame.pack()

# Create the grid
grid = []
for i in range(4):
    row = []
    for j in range(4):
        cell = tk.Label(frame, text="0", width=5, height=2, font=("Helvetica", 32, "bold"), bg="#3c3f41", fg="#ffffff")
        cell.grid(row=i, column=j, padx=5, pady=5)
        row.append(cell)
    grid.append(row)




# Define the generate_cell() method
def generate_cell():
    cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j]["text"] == "0"]
    if cells:
        i, j = random.choice(cells)
        grid[i][j]["text"] = "2" if random.random() < 0.9 else "4"
      
# Define the move_left() method
def move_left():
    for i in range(4):
        for j in range(1, 4):
            if grid[i][j]["text"] != "0":
                value = grid[i][j]["text"]
                k = j - 1
                while k >= 0 and grid[i][k]["text"] == "0":
                    grid[i][k]["text"] = value
                    grid[i][j]["text"] = "0"
                    j = k
                    k -= 1
                if k >= 0 and grid[i][k]["text"] == value:
                    new_value = str(int(value) * 2)
                    grid[i][k]["text"] = new_value
                    grid[i][j]["text"] = "0"

# Define the move_right() method
def move_right():
    for i in range(4):
        for j in range(2, -1, -1):
            if grid[i][j]["text"] != "0":
                value = grid[i][j]["text"]
                k = j + 1
                while k <= 3 and grid[i][k]["text"] == "0":
                    grid[i][k]["text"] = value
                    grid[i][j]["text"] = "0"
                    j = k
                    k += 1
                if k <= 3 and grid[i][k]["text"] == value:
                    new_value = str(int(value) * 2)
                    grid[i][k]["text"] = new_value
                    grid[i][j]["text"] = "0"

# Define the move_up() method
def move_up():
    for j in range(4):
        for i in range(1, 4):
            if grid[i][j]["text"] != "0":
                value = grid[i][j]["text"]
                k = i - 1
                while k >= 0 and grid[k][j]["text"] == "0":
                    grid[k][j]["text"] = value
                    grid[i][j]["text"] = "0"
                    i = k
                    k -= 1
                if k >= 0 and grid[k][j]["text"] == value:
                    new_value = str(int(value) * 2)
                    grid[k][j]["text"] = new_value
                    grid[i][j]["text"] = "0"

# Define the move_down() method
def move_down():
    for i in range(2, -1, -1):
        for j in range(4):
            if grid[i][j]["text"] != "0":
                value = grid[i][j]["text"]
                k = i + 1
                while k < 4 and grid[k][j]["text"] == "0":
                    grid[k][j]["text"] = value
                    grid[i][j]["text"] = "0"
                    i = k
                    k += 1
                if k < 4 and grid[k][j]["text"] == value:
                    new_value = str(int(value) * 2)
                    grid[k][j]["text"] = new_value
                    grid[i][j]["text"] = "0"

# Define the check_game_over() method
def check_game_over():
    for i in range(4):
        for j in range(4):
            if grid[i][j]["text"] == "0":
                return False
            if j < 3 and grid[i][j]["text"] == grid[i][j+1]["text"]:
                return False
            if i < 3 and grid[i][j]["text"] == grid[i+1][j]["text"]:
                return False
    return True

# Bind keys to the game
window.bind("<Left>", lambda event: move_left())
window.bind("<Right>", lambda event: move_right())
window.bind("<Up>", lambda event: move_up())
window.bind("<Down>", lambda event: move_down())

# Run the game
while True:
    generate_cell()
    if check_game_over():
        break
    window.update()

# Start the main event loop
window.mainloop()