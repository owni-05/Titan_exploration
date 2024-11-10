# Titan_exploration
A Python program that simulates the movement of multiple robots on a grid based on given commands. Each robot follows a series of directional commands to move forward or rotate in place. The program outputs the final position and direction of each robot after executing all commands.

Table of Contents
Overview
Features
Installation
Usage
Input Format
Example
Code Structure
Future Enhancements
Overview
This program simulates how robots move and rotate on a grid. Each robot has an initial position and direction, and it can follow commands to turn left, turn right, or move forward. The program takes commands for multiple robots in sequence, processes their movements, and outputs their final positions and orientations.

Features
Simulate movements of multiple robots on a grid.
Robots can execute commands to turn left (L), turn right (R), or move forward (M).
Outputs the final position and direction for each robot after all commands are executed.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/robot-navigation-simulator.git
Navigate to the project directory:
bash
Copy code
cd robot-navigation-simulator
Usage
Run the program:
bash
Copy code
python robot_navigation.py
Follow the prompts to enter grid size, initial positions, and movement commands for each robot.
Input Format
Grid Size: Enter the maximum grid size (e.g., 5 5 for a grid with coordinates ranging from (0, 0) to (5, 5)). This input is not currently used for boundary checks but could be incorporated for extended functionality.

Robot Initial Position: Specify each robot’s starting position and orientation, e.g., 1 2 N, where:

1 and 2 represent the initial x and y coordinates.
N represents the initial direction (N for North, E for East, S for South, W for West).
Movement Commands: Enter a sequence of commands for each robot, such as LMLMLMLMM, where:

L means "turn left".
R means "turn right".
M means "move forward" in the current direction.
Continue entering initial positions and commands for each robot. To end the input sequence, press Ctrl + D (EOF) or Ctrl + Z on Windows.

Example
plaintext
Copy code
Enter grid size (e.g., '5 5'): 5 5
Enter initial position (e.g., '1 2 N'): 1 2 N
Enter commands (e.g., 'LMLMLMLMM'): LMLMLMLMM
Final position: (1, 3, 'N')
Enter initial position (e.g., '3 3 E'): 3 3 E
Enter commands (e.g., 'MMRMMRMRRM'): MMRMMRMRRM
Final position: (5, 1, 'E')
Code Structure
Robot Class: Handles the robot's position and direction, with methods to:
Rotate left or right.
Move forward based on the current direction.
Execute individual commands (L, R, M) and return the final position.
process_robot_commands Function: Creates a Robot instance with the initial position, executes commands, and returns the final position.
main Function: Reads input for grid size, initial positions, and commands, then processes each robot’s movement and prints the final position.
Future Enhancements
Boundary Checks: Use the grid size to restrict robot movement within specified limits.
Obstacle Detection: Add functionality to detect obstacles on the grid.
Multiple Robots on the Grid: Handle potential collisions or restrictions when robots share a grid.

