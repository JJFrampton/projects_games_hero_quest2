#!/usr/bin/env python
import unittest
from Characters.Players.Elf import Elf
from Resources.Board import Board


class ElfInit(unittest.TestCase):
    def setUp(self):
        board = Board(4,4)
        self.elf = Elf("Mr. Anderson", [0,0], board)
    def tearDown(self):
        del self.elf
    # init
    def test_name(self):
        self.assertEqual(self.elf.stats_name, "Mr. Anderson")
    def test_tag(self):
        self.assertEqual(self.elf.tag, "M")
    def test_position(self):
        self.assertEqual(self.elf.position, [0,0])
    def test_board_position(self):
        self.assertEqual(self.elf.board.map[self.elf.position[0]][self.elf.position[1]], self.elf.tag)

class ElfActions(unittest.TestCase):
    def setUp(self):
        board = Board(4,4)
        self.elf = Elf("Mr. Anderson", [0,0], board)
    def tearDown(self):
        del self.elf
    # action
    def test_turn_start(self):
        self.elf.turn_start()
        self.assertEqual(self.elf.movement, 0)
    def test_movement(self):
        old_position = self.elf.position.copy()
        self.elf.movement_roll()
        self.elf.move_right(1)
        self.assertEqual(self.elf.board.map[old_position[0]][old_position[1]], 'o')
        self.assertEqual(self.elf.board.map[self.elf.position[0]][self.elf.position[1]], self.elf.tag)
    def test_movement_limit(self):
        self.elf.movement_roll()
        self.assertTrue(self.elf.move_right(1))
        self.assertFalse(self.elf.move_right(200))

if __name__ == '__main__':
    unittest.main()
