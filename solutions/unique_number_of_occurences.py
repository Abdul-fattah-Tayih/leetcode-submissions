from typing import List

class UniqueNumberofOccurrences:
    """
        1207. Unique Number of Occurrences

        Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, 
        
        or false otherwise.
    """
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
            O(n)

            We create an occurences dict

            Then we loop over our occurences to and store them in a set

            If the occurence already exists in the set, then its not unique and we return false

            otherwise the occurences are unique and we return true

            https://leetcode.com/submissions/detail/852232927/
        """
        occurences_dict = {}
        occurences_set = set()
        
        for num in arr:
            occurences_dict[num] = occurences_dict.get(num, 0) + 1
            
        for occurence in occurences_dict.values():
            if occurence in occurences_set:
                return False

            occurences_set.add(occurence)
        
        return True

if __name__ == '__main__':
    obj = UniqueNumberofOccurrences()

    assert obj.uniqueOccurrences([1,2,2,1,1,3]) == True
    assert obj.uniqueOccurrences([1,2]) == False
    assert obj.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) == True