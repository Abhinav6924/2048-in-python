A Python implementation of the classic 2048 sliding tile puzzle game using Tkinter for the graphical user interface.
Description
2048 is a single-player sliding tile puzzle game where the objective is to combine numbered tiles by sliding them in any of the four directions (up, down, left, right) to create a tile with the number 2048. The game continues beyond 2048 for players who want to achieve higher scores.
Features

Clean and intuitive graphical interface
Smooth tile animations
Color-coded tiles
Score tracking
Win/Loss detection
Support for numbers up to 65536

Requirements

Python 3.x
Tkinter (usually comes pre-installed with Python)

Installation

Clone this repository:

clone https://github.com/Abhinav6924/2048-in-python.git
cd 2048-game

How to Play

Use WASD keys to move tiles:

'W' - Move Up
'A' - Move Left
'S' - Move Down
'D' - Move Right


When two tiles with the same number touch, they merge into one tile with the sum of their values
After each move, a new tile with a value of 2 appears in a random empty cell
The game is won when a tile with the value 2048 is created
The game is lost when no more moves are possible

Project Structure

2048.py: Main game file containing the GUI implementation
LogicsFinal.py: Game logic implementation (movement, merging, win/loss conditions)
constants.py: Game constants including colors, sizes, and keyboard configurations

Features Implementation

Grid System: 4x4 grid with colored tiles
Movement Logic: Implements compress and merge functions for tile movements
Game States:

"GAME NOT OVER": Game is in progress
"WON": Player has achieved 2048
"LOST": No more valid moves available



Color Scheme
The game features a carefully designed color scheme:

Empty cells: #9e948a
Game background: #92877d
Number tiles: Various colors based on the number value
Text colors: Optimized for readability against tile backgrounds

Contributing
Feel free to fork this project and submit pull requests. You can also open issues for bugs or feature suggestions.
