# Overview

This is a basic Sudoku game created with Python's pygame. I love logic games and thought it would be amazing to see the
innerworkings of building a sudoku game. To play, you simply click a square with your mouse. The square will highlight 
with a bright outline color and you can choose a number from your keyboard to enter there. If the number is not valid,
meaning that the number you selected to put in that space is either in the same row, column or 3x3 box, then the board 
will not allow you to place it there. When you have filled the board, you can either reset the board with "d" or clear
the board with "r".

[Sudoku Demo](https://www.youtube.com/watch?v=4d68XffLE9A)
# Development Environment

To create this program, I used Python's pygame. I decided to use several classes to encapsulate my project calling 
all my methods into the main function. 

# Useful Websites

* [Pygame News](https://www.pygame.org/news)
* [Geeks for Geeks](https://www.geeksforgeeks.org/python/read-json-file-using-python/)

# Future Work

* Add a way to delete individual numbers without reseting the entire board
* Add a timer and a win/lose functionality
* Add different difficulties of sudoku boards
