from typing import List

class MostBeautifulItemForEachQuery:
    """
        2070. Most Beautiful Item for Each Query

        You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

        You are also given a 0-indexed integer array queries.
        
        For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j].
        
        If no such item exists, then the answer to this query is 0.

        Return an array answer of the same length as queries where answer[j] is the answer to the jth query.
    """
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        """
            N: length of items
            M: length of queries

            O(n log(n) + m log(n)) solution

            The idea for this solution is to:
            1. Sort the items by the price (index 0 of each pair)
            2. Create a list that will store pairs, each pair is the price, and the maximum beauty up until that pair
            3. Go over the queries, in each query we use binary search to find the appropriate pair, and add the beauty of that pair if found
            4. if no pair is found, then if the price is <= query, then we use it, in case the exact price does not exist
        """

        prefix = []
        items.sort(key=lambda x: x[0])

        for price, beauty in items:
            if not prefix:
                prefix.append([price, beauty])
                continue

            if prefix[-1][0] == price:
                prefix[-1][1] = max(beauty, prefix[-1][1])
                continue

            prefix.append([price, max(beauty, prefix[-1][1])])

        result = []
        for query in queries:
            val = 0
            left = 0
            right = len(prefix) - 1

            while left <= right:
                mid = left + (right - left) // 2
                
                if prefix[mid][0] == query:
                    val = prefix[mid][1]
                    break

                if prefix[mid][0] > query:
                    right = mid - 1
                else:
                    val = max(val, prefix[mid][1])
                    left = mid + 1

            result.append(val)

        return result

if __name__ == "__main__":
    obj = MostBeautifulItemForEachQuery()
    
    result = obj.maximumBeauty(
        [[1,2],[3,2],[2,4],[5,6],[3,5]], 
        [1,2,3,4,5,6]
    )

    print(result)