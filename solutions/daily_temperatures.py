from typing import List

class DailyTemperatures:
    """
        739. Daily Temperatures

        Given an array of integers temperatures represents the daily temperatures, 
        
        return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
        
        If there is no future day for which this is possible, keep answer[i] == 0 instead.
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            O(n) using a monotonically decreasing stack

            We loop over each item in the list, adding temps to the stack, and if we come across a temp that is higher

            Than the top of the stack, we keep popping while modifying the result list by adding the index difference

            between the higher and lower temp

            https://leetcode.com/submissions/detail/848817106/
        """
        result = [0 for temp in temperatures]
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp = stack.pop()
                result[stack_temp[1]] = idx - stack_temp[1]

            stack.append((temp, idx))

        return result

if __name__ == '__main__':
    obj = DailyTemperatures()

    assert obj.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert obj.dailyTemperatures([30,40,50,60]) == [1,1,1,0]