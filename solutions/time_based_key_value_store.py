class TimeMap:
    """
        981. Time Based Key-Value Store

        Design a time-based key-value data structure that can store multiple values for the same key at different time stamps 
        
        and retrieve the key's value at a certain timestamp.

        Implement the TimeMap class:

        TimeMap() Initializes the object of the data structure.
        
        void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
        
        String get(String key, int timestamp) Returns a value such that set was called previously, 
        
        with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
    """
    def __init__(self):
        self.dict = {} # type: dict[str, list[tuple[str, int]]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append((value, timestamp))
            return
        
        self.dict[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        """
            O(log(n))

            Do a binary search over the array
        """
        if key not in self.dict:
            return ""

        result = ""
        left = 0
        right = len(self.dict[key]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.dict[key][mid][1] <= timestamp:
                result = self.dict[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result

    def get_brute_force(self, key: str, timestamp: int) -> str:
        """
            O(n)

            This solves the question but fails due to time constraints

            In the worst case scenario, it will loop through the entire array to find the max timestamp that is < timestamp

            if it the given timestamp doesnt exist

            https://leetcode.com/problems/time-based-key-value-store/submissions/856353319/
        """
        if key not in self.dict:
            return ""

        result = ""
        for prev_element in self.dict[key]:
            if prev_element[1] <= timestamp:
                result = prev_element[0]
            else:
                break

        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == '__main__':
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)            # store the key "foo" and value "bar" along with timestamp = 1.
    assert timeMap.get("foo", 3) == 'bar'   # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    assert timeMap.get("foo", 1) == 'bar'   # return "bar"
    timeMap.set("foo", "bar2", 4)           # store the key "foo" and value "bar2" along with timestamp = 4.
    assert timeMap.get("foo", 4) == 'bar2'  # return "bar2"
    assert timeMap.get("foo", 5) == 'bar2'

    timeMap = TimeMap()
    timeMap.set("love","high",10)
    timeMap.set("love","low",20)
    timeMap.get("love",5)
    timeMap.get("love",10)
    timeMap.get("love",15)
    timeMap.get("love",20)
    timeMap.get("love",25)