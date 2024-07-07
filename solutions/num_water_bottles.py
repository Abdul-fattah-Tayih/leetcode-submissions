class NumWaterBottles:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        empty_bottles = numBottles
        full_bottles = 0

        while empty_bottles >= numExchange:
            full_bottles = empty_bottles // numExchange
            result += full_bottles
            empty_bottles = empty_bottles % numExchange
            empty_bottles += full_bottles

        return result
    
if __name__ ==  "__main__":
    obj = NumWaterBottles()

    print(obj.numWaterBottles(15, 4))