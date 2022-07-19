from unittest import TestCase
from solutions.maximum_points_you_can_obtain_from_cards import MaximumPointsYouCanObtainFromCards

class TestMaximumPointsYouCanObtainFromCards(TestCase):
    def setUp(self) -> None:
        self.solution_object = MaximumPointsYouCanObtainFromCards()

    def test_1(self):
        result = self.solution_object.max_score([1,2,3,4,5,6,1], 3)
        self.assertEqual(result, 12)
    
    def test_2(self):        
        result = self.solution_object.max_score([2,2,2], 2)
        self.assertEqual(result, 4)
    
    def test_3(self):
        result = self.solution_object.max_score([9,7,7,9,7,7,9], 7)
        self.assertEqual(result, 55)
    
    def test_4(self):
        result = self.solution_object.max_score([1,2,5,4,2,1], 3)
        self.assertEqual(result, 8)
    
    def test_5(self):        
        result = self.solution_object.max_score([11,49,100,20,86,29,72], 4)
        self.assertEqual(result, 232)