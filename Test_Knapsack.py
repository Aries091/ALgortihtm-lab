import unittest
from Knapsack_Greedy import fractional_knapsack_greedy
from Knapsack_Dynamic import zero_one_knapsack_dp
from Kanpsack_Bruteforce import fractional_knapsack_brute_force, zero_one_knapsack_brute_force

class TestKnapsackGreedy(unittest.TestCase):
    def test_fractional_knapsack(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        
        expected_value = 240
        value = fractional_knapsack_greedy(weights, values, capacity)
        
        self.assertAlmostEqual(value, expected_value)
    

class TestKnapsackDP(unittest.TestCase):
    def test_zero_one_knapsack(self):
        weights = [2, 4, 6,9]
        values = [10,10,12,18]
        capacity = 15
        
        expected_value = 38
        expected_tuple = (1,1,0,1)
        value, items = zero_one_knapsack_dp(weights, values, capacity)
             
        self.assertEqual(value, expected_value)
        self.assertEqual(items, expected_tuple)
        self.assertTrue(all(weights[i] <= capacity for i in items))
    
    def test_another_scenario(self):
        weights = [1, 3, 4, 5]
        values = [10, 40, 50, 70]
        capacity = 10
        
        value, items = zero_one_knapsack_dp(weights, values, capacity)
        self.assertTrue(value > 0)
        self.assertTrue(sum(weights[i] for i in items) <= capacity)


class TestKnapsackBruteForce(unittest.TestCase):
    def test_fractional_knapsack(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        
        expected_value = 240.0 
        
        
        value = fractional_knapsack_brute_force(weights, values, capacity)
        
        self.assertAlmostEqual(value, expected_value)
       
    
    def test_zero_one_knapsack(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        
        expected_value = 220 
        expected_combination = (0, 1, 1)
        
        value, combination = zero_one_knapsack_brute_force(weights, values, capacity)
        
        self.assertEqual(value, expected_value)
        self.assertEqual(combination, expected_combination)


if __name__ == '__main__':
    unittest.main()