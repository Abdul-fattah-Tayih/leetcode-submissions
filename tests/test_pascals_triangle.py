from unittest import TestCase
from solutions.pascals_triangle import PascalsTriangle

class TestPascalsTriangle(TestCase):
    def setUp(self) -> None:
        self.solution_object = PascalsTriangle()

    def test_5_returns_a_5_level_triangle(self):
        result = self.solution_object.generate(5)
        self.assertEqual(result, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

    def test_4_returns_a_4_level_triangle(self):
        result = self.solution_object.generate(4)
        self.assertEqual(result, [[1],[1,1],[1,2,1],[1,3,3,1]])

    def test_1_returns_a_list_containing_1(self):
        result = self.solution_object.generate(1)
        self.assertEqual(result, [[1]])