from heapq import heapify, heappop, heappush


class LongestHappyString:
    """
        1405. Longest Happy String

        A string s is called happy if it satisfies the following conditions:
            - s only contains the letters 'a', 'b', and 'c'.
            - s does not contain any of "aaa", "bbb", or "ccc" as a substring.
            - s contains at most a occurrences of the letter 'a'.
            - s contains at most b occurrences of the letter 'b'.
            - s contains at most c occurrences of the letter 'c'.
        
        Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

        A substring is a contiguous sequence of characters within a string.
    """
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
            Greedy Max Heap solution

            - O(n log n) time complexity, where n is: a + b + c
            - O(1) storage

            In order to get the longest possible string, we need to pad the lowest occuring characters with the most occuring ones, for example:
            a: 5, b: 1, c: 1 => aabaaca

            for that we need a max heap, we always try to fill the most occuring character, which is max heap's root

            If we reach 2 occurences for a character, we switch to the next most occuring character

            Once the heap is empty or only contains a character that's already been placed twice already, we stop
        """
        heap = []
        for occurence, char in zip([a, b, c], ['a', 'b', 'c']):
            if occurence != 0:
                heappush(heap, (-occurence, char))

        window = [heap[0], 0]
        result = []

        for _ in range(a + b + c):
            if len(heap) == 0:
                break

            occurences, char = heappop(heap)
            occurences = -occurences

            if window[1] == 2 and window[0] == char:
                if not heap:
                    break
                
                second_occurences, second_char = heappop(heap)
                second_occurences += 1

                result.append(second_char)
                heappush(heap, (-occurences, char))

                if second_occurences != 0:
                    heappush(heap, (second_occurences, second_char))

                window = [second_char, 1]
                continue

            occurences -= 1
            if occurences != 0:
                heappush(heap, (-occurences, char))

            if window[0] == char:
                window[1] += 1
            else:
                window = [char, 1]

            result.append(char)

        return ''.join(result)

if __name__ == "__main__":
    obj = LongestHappyString()
    print(obj.longestDiverseString(1, 1, 7))