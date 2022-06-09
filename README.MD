MAZE SOLVER
-----------


Description:
------------
Maze solver finds a route through a maze given in a .txt file, or tell if there is no possible route available.

In the map file ‘#’ represents a block, ‘ ‘ (space) represents movable space
and ‘E’ means an exit. ‘^’ is the starting position.

Each step has to be either up, down, left or right. Solution is attempted with  20, 150 and 200 maximum moves.

The solution is written to a .txt file or alternatively the user is informed if no solution exists.



How to run maze solver:
-----------------------
Running the script has only been tested with python version 3.10.2

Open a command prompt to the project folder and run the script with command:

python main.py maze_file.txt

where maze_file.txt is the text file containing the maze to be solved.

You can try it with a model maze by runnin with command:

python main.py data/maze1.txt



How to run unittest cases:
--------------------------
Open a command prompt to the project folder and give a command:

python -m unittest discover test
