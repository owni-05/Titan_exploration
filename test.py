import unittest
from robot_navigation import process_robot_commands
class TestRobotMovement(unittest.TestCase):
    def test_single_move_forward(self):
        # Test moving forward in all directions
        self.assertEqual(process_robot_commands((1, 1, 'N'), 'M'), (1, 2, 'N'))
        self.assertEqual(process_robot_commands((1, 1, 'E'), 'M'), (2, 1, 'E'))
        self.assertEqual(process_robot_commands((1, 1, 'S'), 'M'), (1, 0, 'S'))
        self.assertEqual(process_robot_commands((1, 1, 'W'), 'M'), (0, 1, 'W'))

    def test_turn_left(self):
        # Test turning left from all directions
        self.assertEqual(process_robot_commands((1, 1, 'N'), 'L'), (1, 1, 'W'))
        self.assertEqual(process_robot_commands((1, 1, 'W'), 'L'), (1, 1, 'S'))
        self.assertEqual(process_robot_commands((1, 1, 'S'), 'L'), (1, 1, 'E'))
        self.assertEqual(process_robot_commands((1, 1, 'E'), 'L'), (1, 1, 'N'))

    def test_turn_right(self):
        # Test turning right from all directions
        self.assertEqual(process_robot_commands((1, 1, 'N'), 'R'), (1, 1, 'E'))
        self.assertEqual(process_robot_commands((1, 1, 'E'), 'R'), (1, 1, 'S'))
        self.assertEqual(process_robot_commands((1, 1, 'S'), 'R'), (1, 1, 'W'))
        self.assertEqual(process_robot_commands((1, 1, 'W'), 'R'), (1, 1, 'N'))

    def test_combined_commands(self):
        # Test a combination of moves and turns
        self.assertEqual(process_robot_commands((1, 2, 'N'), 'LMLMLMLMM'), (1, 3, 'N'))
        self.assertEqual(process_robot_commands((3, 3, 'E'), 'MMRMMRMRRM'), (5, 1, 'E'))

    def test_no_movement(self):
        # Test no movement commands (empty string)
        self.assertEqual(process_robot_commands((2, 3, 'N'), ''), (2, 3, 'N'))

    def test_repeated_turns(self):
        # Test repeated left and right turns to return to original direction
        self.assertEqual(process_robot_commands((1, 1, 'N'), 'LLLL'), (1, 1, 'N'))
        self.assertEqual(process_robot_commands((1, 1, 'N'), 'RRRR'), (1, 1, 'N'))

    def test_complex_path(self):
        # Test a complex sequence of moves and turns
        self.assertEqual(process_robot_commands((0, 0, 'N'), 'MRMLMRM'), (2, 1, 'N'))
        self.assertEqual(process_robot_commands((2, 2, 'S'), 'MLMLMLM'), (2, 2, 'W'))

if __name__ == '__main__':
    unittest.main()
