"""
def calcualte(initial, commands):
    left_order = ['N', 'W', 'S', 'E']
    right_order = ['N', 'E', 'S', 'W']

    res_list = []

    res_list.append(initial)

    for each in commands:
        prev_x, prev_y, prev_direction = res_list[-1]
        if each == 'L':
            index = left_order.index(prev_direction)
            if index < 3:
                next_direction = left_order[index + 1]
            else:
                next_direction = left_order[0]

            next_x, next_y = prev_x, prev_y
            

        elif each == 'R':
            index = right_order.index(prev_direction)
            if index < 3:
                next_direction = right_order[index + 1]
            else:
                next_direction = right_order[0]

            next_x, next_y = prev_x, prev_y

        
        elif each == 'M':
            if prev_direction == 'N':
                next_y = prev_y + 1
                next_x = prev_x

            if prev_direction == 'E':
                next_x = prev_x + 1
                next_y = prev_y

            if prev_direction == 'S':
                next_y = prev_y - 1
                next_x = prev_x

            if prev_direction == 'W':
                next_x = prev_x - 1
                next_y = prev_y

            next_direction = prev_direction
        res_list.append((next_x, next_y, next_direction))

    return res_list[-1]


initial = (3, 3, 'E')
commands = ['M', 'M', 'R', 'M', 'M','R','M','R','R','M']
print(calcualte(initial, commands))
"""

class Robot:
    def __init__(self, initial_position):
        # Initialize robot's position and direction
        self.x, self.y, self.direction = initial_position
        # Define order of directions for left and right rotations
        self.left_order = ['N', 'W', 'S', 'E']
        self.right_order = ['N', 'E', 'S', 'W']

    def turn_left(self):
        # Rotate the robot 90 degrees to the left
        index = self.left_order.index(self.direction)
        self.direction = self.left_order[(index + 1) % 4]

    def turn_right(self):
        # Rotate the robot 90 degrees to the right
        index = self.right_order.index(self.direction)
        self.direction = self.right_order[(index + 1) % 4]

    def move_forward(self):
        # Move the robot forward in the current direction
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'W':
            self.x -= 1

    def execute_command(self, command):
        # Execute a single command (L, R, or M)
        if command == 'L':
            self.turn_left()
        elif command == 'R':
            self.turn_right()
        elif command == 'M':
            self.move_forward()

    def get_position(self):
        # Return the robot's current position and direction
        return (self.x, self.y, self.direction)


def process_robot_commands(initial, commands):
    # Create a new robot instance with the given initial position
    robot = Robot(initial)
    # Execute each command in the sequence
    for command in commands:
        robot.execute_command(command)
    # Return the robot's final position after all commands are executed
    return robot.get_position()


def main():
    # Input grid size (currently unused, but could be used for boundary checks)
    grid_size = input("Enter grid size (e.g., '5 5'): ")
    max_x, max_y = map(int, grid_size.split())
    
    # Read each robot's initial position and commands in a loop
    while True:
        try:
            # Input initial position in the format 'x y D'
            initial_input = input("Enter initial position (e.g., '1 2 N'): ")
            x, y, direction = initial_input.split()
            initial_position = (int(x), int(y), direction)
            
            # Input movement commands (e.g., 'LMLMLMLMM')
            commands = input("Enter commands (e.g., 'LMLMLMLMM'): ").strip()
            
            # Process commands and get final position of the robot
            final_position = process_robot_commands(initial_position, commands)
            
            # Print the final position and direction of the robot
            print("Final position:", final_position)
            
        except EOFError:
            # Stop reading input if end of file (EOF) is reached
            break

# Run the main function to start the program
main()