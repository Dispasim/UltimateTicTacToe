This project is a ultimate tictactoe game made in python with an MinMax AI that can be player 2.

# Ultimate Tic-Tac-Toe

**Ultimate Tic-Tac-Toe** is a more complex and strategic version of the classic Tic-Tac-Toe game. It is played on a 9x9 board divided into 9 smaller 3x3 grids. Here are the rules and how to play.

## Game Rules

### 1. **Game Board**
The game board consists of **9 smaller 3x3 grids**, forming a larger 9x9 board.

### 2. **Objective of the Game**
The goal of the game is to win **3 small grids in a row** (horizontally, vertically, or diagonally) on the larger board.

### 3. **Player Turns**
- There are two players: **Player X** and **Player O**, who take turns.
- On each turn, a player places their mark (X or O) on one of the smaller 3x3 grids.

### 4. **Placement Rule in a Small Grid**
- When a player places their mark in a small 3x3 grid, the position of the mark determines which small grid the **opponent must play in on their next turn**.
  For example:
  - If Player X places their mark in position **(0, 0)** (top-left) of a small grid, the opponent (Player O) must then play in the **top-left small grid** of the large 9x9 board.

### 5. **Special Case**
- If a player is directed to play in a small grid that has already been won or is completely filled, they may play in **any available small grid**.

### 6. **Winning a Small Grid**
- A player wins a small 3x3 grid by getting **3 of their marks in a row** (horizontally, vertically, or diagonally).

### 7. **Winning the Game**
- A player wins the game by winning **3 small grids in a row** on the larger 9x9 board.

### 8. **Strategy**
Strategy is key in Ultimate Tic-Tac-Toe. Each move made not only contributes to winning the small grid but also determines where your opponent must play, which may force them into difficult positions.

## Example of Gameplay

1. **Turn 1 (Player X)**: Player X places an "X" in the center of the middle small grid. This directs Player O to play in the center of the middle small grid of the larger board.
2. **Turn 2 (Player O)**: Player O places an "O" in the center of the middle small grid. This directs Player X to play in the center small grid of the large 9x9 board.
3. **Turn 3 (Player X)**: Player X plays in the top-left grid of the large 9x9 board.

The game continues in this way, with each player trying to win their small grids while directing the opponent into undesirable positions.

## End of the Game
- The game ends when a player wins **3 small grids in a row** on the large 9x9 board.
- The game can also end in a **draw** if all the small grids are filled without either player winning 3 in a row.

## Summary of Rules

1. The game board is a **9x9 grid** made up of **9 smaller 3x3 grids**.
2. On each turn, a player places their mark in a small grid, which determines where the opponent will play next.
3. A small grid is won when a player gets **3 of their marks in a row**.
4. The winner is the first player to win **3 small grids in a row** on the larger 9x9 board.



To try to play, just execute the ultimatemorpionrapide.py file. 

!!! I recommend using spyder for that, vs code and the terminal doesn't work.

You can also play with other player using the ultimatemorpionclasse.py file and executing the Partie function.
example: Partie(True,1,False,5)
