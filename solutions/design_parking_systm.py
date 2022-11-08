"""
Question 1603
Design Parking System
"""
class ParkingSystem:
    TYPE_BIG = 1
    TYPE_MEDIUM = 2
    TYPE_SMALL = 3

    def __init__(self, big: int, medium: int, small: int):
        self.max_big = big
        self.max_medium = medium
        self.max_small = small

        self.big_count = 0
        self.medium_count = 0
        self.small_count = 0

    def addCar(self, carType: int) -> bool:
        if not self.canBeAdded(carType):
            return False
        
        self.incrementType(carType)

        return True

    def incrementType(self, carType: int):
        if carType == self.TYPE_BIG:
            self.big_count += 1
            return
        elif carType == self.TYPE_MEDIUM:
            self.medium_count += 1
            return

        self.small_count += 1
        return

    def canBeAdded(self, carType: int) -> bool:
        if carType == self.TYPE_BIG:
            return (self.big_count + 1) <= self.max_big
        elif carType == self.TYPE_MEDIUM:
            return (self.medium_count + 1) <= self.max_medium

        return (self.small_count + 1) <= self.max_small


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

if __name__ == '__main__':
    parkingSystem = ParkingSystem(1, 1, 0)
    print(parkingSystem.addCar(1)) # return true because there is 1 available slot for a big car
    print(parkingSystem.addCar(2)) # return true because there is 1 available slot for a medium car
    print(parkingSystem.addCar(3)) # return false because there is no available slot for a small car
    print(parkingSystem.addCar(1)) # return false because there is no available slot for a big car. It 