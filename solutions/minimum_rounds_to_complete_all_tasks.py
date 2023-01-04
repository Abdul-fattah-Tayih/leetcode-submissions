from typing import List

class MinimumRoundsToCompleteAllTasks:
    """
        2244. Minimum Rounds to Complete All Tasks

        You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. 
        
        In each round, you can complete either 2 or 3 tasks of the same difficulty level.

        Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.
    """
    def minimumRounds(self, tasks: List[int]) -> int:
        """
            Time: O(n)

            Space: O(n)

            We create a frequency dict for all the numbers, keys being the task level, and the value is the count
            
            Then we loop over the dict, in each iteration we check the count:

                1. if its == 1, we return -1 because we cant remove 2 or 3 from it and end up with 0
                2. if its divisible by 3, we add the count / 3 to the total rounds, because the least amount of rounds is acheived using 3s
                3. else we get the 3s in the number by doing an integer division (count // 3), then we check the remainder
                    a. if remainder == 1, then that means we need to remove a 3 and instead use 2s
                    b. else we add the count // 2 to the rounds because we always end up with a number that is divisble by 2 only in this case

            https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/submissions/871469371/
        """
        total_rounds = 0
        frequency_dict = {}
        for task in tasks:
            frequency_dict[task] = frequency_dict.get(task, 0) + 1

        for level, count in frequency_dict.items():
            if count < 2:
                return -1

            if count % 3 == 0:
                total_rounds += (count // 3)
            else:
                threes_in_number = count // 3
                remainder = count - (threes_in_number * 3)
                
                if remainder == 1:
                    total_rounds += threes_in_number - 1 + ((remainder + 3) // 2)
                elif remainder > 1:
                    total_rounds += threes_in_number + (remainder // 2)
                
        return total_rounds

if __name__ == '__main__':
    obj = MinimumRoundsToCompleteAllTasks()

    assert obj.minimumRounds([2,2,3,3,2,4,4,4,4,4]) == 4
    assert obj.minimumRounds([2,3,3]) == -1
    assert obj.minimumRounds([5, 5, 5, 5]) == 2
