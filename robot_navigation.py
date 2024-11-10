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
        self.x, self.y, self.direction = initial_position
        self.left_order = ['N', 'W', 'S', 'E']
        self.right_order = ['N', 'E', 'S', 'W']

    def turn_left(self):
        index = self.left_order.index(self.direction)
        self.direction = self.left_order[(index + 1) % 4]  # Rotate left

    def turn_right(self):
        index = self.right_order.index(self.direction)
        self.direction = self.right_order[(index + 1) % 4]  # Rotate right

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'W':
            self.x -= 1

    def execute_command(self, command):
        if command == 'L':
            self.turn_left()
        elif command == 'R':
            self.turn_right()
        elif command == 'M':
            self.move_forward()

    def get_position(self):
        return (self.x, self.y, self.direction)


def process_robot_commands(initial, commands):
    robot = Robot(initial)
    for command in commands:
        robot.execute_command(command)
    return robot.get_position()


def main():
    # Input grid size
    grid_size = input("Enter grid size (e.g., '5 5'): ")
    max_x, max_y = map(int, grid_size.split())
    
    # Read each robot's initial position and commands
    while True:
        try:
            # Input initial position
            initial_input = input("Enter initial position (e.g., '1 2 N'): ")
            x, y, direction = initial_input.split()
            initial_position = (int(x), int(y), direction)
            
            # Input movement commands
            commands = input("Enter commands (e.g., 'LMLMLMLMM'): ").strip()
            
            # Process commands and get final position
            final_position = process_robot_commands(initial_position, commands)
            print("Final position:", final_position)
            
        except EOFError:
            # Stop reading input if end of file is reached
            break

# Run the main function
main()
