# Project -> A* Maze Solver Python

# Description :

This program will take a maze in a .txt file as an input and will output a .txt file with the shortest path to solve the maze.
  
# How it works :

As mentionned above, the program takes a .txt file as an input which has to be in the following format :

1000000000

0000110002

0003110000

0000011000

 - 0 : a free case on which you can go
 - 1 : a wall, or an obstacle that blocks your way
 - 2 : the starting position
 - 3 : the ending position (your goal)

The file has to be named 'Exercise1.txt, run the program, you will then see a file named Result1.txt appear in the same directory, this file will be in the following format :

NWWWWWWSS //The path to go from start to finish

16 //The amount of steps taken to find the ending position

When in doubt, the program will choose a case using UP, LEFT, RIGHT and DOWN priority.

A folder within this project contains an example of a maze and its shortest path.

# Goal behind the app :
  
This project was a class assignment during my last semester in computer science. At first I did the whole thing in Javascript, as I usually do, but I then ran into issues. After the algorithms were coded I was unable to output the answer in a specific directory without running a server on the machine itself. 

After some research I understood that Javascript wouldn't be safe if it was possible to write files on your machine, as it is used by most websites today. As a work-around I decided to rewrite the whole thing in Python, which I really enjoyed doing.

Knowing that this is my first Python program, I suspect that it probably is far from perfect, but it sure is a good start.
 
# Developer : 
Yann Morin-Charbonneau @yannmc
